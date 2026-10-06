import functools
from neo4j import GraphDatabase


def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
            with driver.session() as session:
                if timeout is not None:
                    session.run("CALL dbms.setTXMetaData({})", metadata)
                    session.run("CALL dbms.setTXTimeout({}, 'SECONDS')", timeout)
                result = session.write_transaction(func, *args, **kwargs)
            driver.close()
            return result
        return wrapper
    return decorator
