
def tri(n):
    # Initialize the list with the first three numbers of the sequence
    tri_list = [1, 3, 2]

    # Calculate the rest of the numbers
    for i in range(3, n + 1):
        if i % 2 == 0:
            tri_list.append(1 + i / 2)
        else:
            tri_list.append(tri_list[i - 1] + tri_list[i - 2] + tri_list[i - 3])

    return tri_list[:n + 1]
