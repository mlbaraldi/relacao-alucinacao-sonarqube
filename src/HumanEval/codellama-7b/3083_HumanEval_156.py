
def int_to_mini_roman(number):
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_numerals = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m"
    }

    result = ""
    while number > 0:
        for key, value in roman_numerals.items():
            if number >= key:
                result += value
                number -= key
                break

    return result
