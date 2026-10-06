
def is_bored(S):
    # Split the string into sentences
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    
    # Initialize the count of boredoms
    boredom_count = 0
    
    # Iterate over each sentence
    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()
        
        # If the sentence starts with "I", increment the boredom count
        if words and words[0] == "I":
            boredom_count += 1
            
    # Return the count of boredoms
    return boredom_count
