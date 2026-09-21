

def process_text_links(text):
    # Split the text into individual words
    words = text.split()

    # Iterate over each word and check if it's a link
    for i, word in enumerate(words):
        # Check if the word is a link
        if word.startswith("http"):
            # Add the "href" attribute to the link
            words[i] = f"<a href='{word}'>{word}</a>"

    # Join the words back into a string
    processed_text = " ".join(words)

    return processed_text
