

def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_list = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib_list.append(fibfib_list[-1] + fibfib_list[-2] + fibfib_list[-3])
        return fibfib_list[-1]
