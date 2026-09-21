

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")

    def convert_to_base(n, b):
        convert_string = "0123456789"
        if n < b:
            return convert_string[n]
        else:
            return convert_to_base(n // b, b) + convert_string[n % b]

    return convert_to_base(x, base)

# Test cases
