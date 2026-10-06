
def closest_integer(value):
    try:
        num = float(value)
        if num == int(num):
            return num
        else:
            return int(num + 0.5)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")
