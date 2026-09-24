
def tri(n):
    if n < 0:
        return []
    elif n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    else:
        tri_seq = [1, 3]
        for i in range(2, n + 1):
            if i % 2 == 0:
                tri_seq.append(1 + i / 2)
            else:
                tri_seq.append(tri_seq[i - 1] + tri_seq[i - 2] + tri_seq[i - 3])
        return tri_seq
