def _legacy_mergeOrderings(orderings):
    # Collect the first occurrence of each element
    first_occurrence = {}
    for order_idx, ordering in enumerate(orderings):
        for elem_idx, elem in enumerate(ordering):
            if elem not in first_occurrence:
                first_occurrence[elem] = (order_idx, elem_idx)
    
    # Build the graph and in-degree dictionary
    graph = {}
    in_degree = {}
    # Initialize all elements in the graph and in_degree
    for ordering in orderings:
        for elem in ordering:
            if elem not in graph:
                graph[elem] = []
            if elem not in in_degree:
                in_degree[elem] = 0
    # Add edges for consecutive elements in each ordering
    for ordering in orderings:
        for i in range(len(ordering) - 1):
            u = ordering[i]
            v = ordering[i + 1]
            if v not in graph[u]:
                graph[u].append(v)
                in_degree[v] += 1
    
    # Use a priority queue to select the next node based on first_occurrence
    import heapq
    heap = []
    for elem in in_degree:
        if in_degree[elem] == 0:
            heapq.heappush(heap, (first_occurrence[elem], elem))
    
    merged = []
    while heap:
        prio, u = heapq.heappop(heap)
        merged.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, (first_occurrence[v], v))
    
    return merged
