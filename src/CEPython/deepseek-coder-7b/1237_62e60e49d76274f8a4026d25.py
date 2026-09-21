from neo4j import GraphDatabase


def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Connect to the Neo4j database
            driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
            
            # Define the transaction function
            def tx_func(tx):
                # Execute the original function within the transaction
                result = func(tx, *args, **kwargs)
                # Apply metadata if provided
                if metadata:
                    for key, value in metadata.items():
                        tx.run(f"CALL db.setTXMetaData('{key}', {value})")
                return result
            
            # Execute the transaction with the specified timeout
            with driver.session() as session:
                if timeout is not None:
                    session.write_transaction(tx_func, timeout=timeout)
                else:
                    session.write_transaction(tx_func)
        
        return wrapper
    return decorator

# Example usage
