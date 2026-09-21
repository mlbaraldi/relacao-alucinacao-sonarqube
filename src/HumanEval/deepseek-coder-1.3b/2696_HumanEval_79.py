
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary = 'db' + binary + 'db'
    return binary
