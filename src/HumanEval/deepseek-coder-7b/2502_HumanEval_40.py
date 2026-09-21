

def triples_sum_to_zero(l: list):
    l = list(set(l))  # Remove duplicates
    n = len(l)
    for i in range(n):
        target = -l[i]
        left = i + 1
        right = n - 1
        while left < right:
            if l[left] + l[right] == target:
                return True
            elif l[left] + l[right] < target:
                left += 1
            else:
                right -= 1
    return False
