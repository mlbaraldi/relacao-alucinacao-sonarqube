
def generate_integers(a, b):
    # Ensure a is smaller than b
    if a > b:
        a, b = b, a

    # Generate the list of even numbers between a and b
    return [i for i in range(a, b + 1) if i % 2 == 0 and '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i)]
