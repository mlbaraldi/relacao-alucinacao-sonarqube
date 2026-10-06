def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    from typing import List, Optional
    base = len(alphabet)
    if base == 0:
        raise ValueError("Alphabet must not be empty.")
    
    if number < 0:
        raise ValueError("Negative numbers are not supported.")
    
    # Handle the case where the number is zero
    if number == 0:
        digits = [0]
    else:
        digits = []
        n = number
        while n > 0:
            n, rem = divmod(n, base)
            digits.append(rem)
        # Reverse to get the most significant digit first
        digits = digits[::-1]
    
    # Convert digits to corresponding characters
    chars = [alphabet[d] for d in digits]
    
    # Apply padding if necessary
    if padding is not None:
        current_length = len(chars)
        if current_length < padding:
            # Prepend the necessary number of alphabet[0] characters
            chars = [alphabet[0]] * (padding - current_length) + chars
    
    return ''.join(chars)
