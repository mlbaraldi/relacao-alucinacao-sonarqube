
def tri(n):
    # Initialize the first three numbers of the sequence
    sequence = [1, 3, 2]
    
    # Calculate the rest of the sequence
    for i in range(3, n+1):
        if i % 2 == 0:
            sequence.append(1 + i / 2)
        else:
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])
    
    return sequence
