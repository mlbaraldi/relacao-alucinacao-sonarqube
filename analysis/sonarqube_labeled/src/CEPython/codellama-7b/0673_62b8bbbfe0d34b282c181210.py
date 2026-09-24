

def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    # Open the file in binary mode
    with open(file_name, "ab" if overwrite else "a", encoding=encoding) as f:
        # Write the text buffer to the file
        f.write(text_buffer.encode(encoding))

    # Return the number of bytes written
    return len(text_buffer.encode(encoding))
