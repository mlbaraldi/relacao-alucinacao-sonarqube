def paging(response, max_results):
    for start in range(0, len(response), max_results):
        yield response[start:start + max_results]
