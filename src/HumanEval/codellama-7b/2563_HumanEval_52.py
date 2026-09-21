

def below_threshold(l: list, t: int):
    for i in range(len(l)):
        if l[i] >= t:
            return False
    return True
