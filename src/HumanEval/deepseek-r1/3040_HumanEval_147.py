
def get_max_triples(n):
    count0 = (n + 1) // 3
    count1 = n - count0
    
    def comb3(x):
        if x < 3:
            return 0
        return x * (x - 1) * (x - 2) // 6
    
    return comb3(count0) + comb3(count1)
