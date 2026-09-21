
def solve(N):
    sum_digits = sum(int(d) for d in str(N))
    return bin(sum_digits)[2:]
