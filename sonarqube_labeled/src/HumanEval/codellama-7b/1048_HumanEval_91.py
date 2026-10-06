
def is_bored(S):
    # Initialize a counter for the number of boredoms
    boredoms = 0

    # Iterate over the words in the input string
    for word in S.split():
        # Check if the current word is "I"
        if word == "I":
            # If it is, increment the boredoms counter
            boredoms += 1

    # Return the number of boredoms
    return boredoms
