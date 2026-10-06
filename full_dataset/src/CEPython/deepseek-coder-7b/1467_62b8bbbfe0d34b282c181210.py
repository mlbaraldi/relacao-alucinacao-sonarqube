

def append_text_to_file(file_name, text_buffer, encoding, overwrite=False):
    """
    Write to the specified filename, the provided binary buffer
    Create the file if required.
    :param file_name:  File name.
    :type file_name: str
    :param text_buffer: Text buffer to write.
    :type text_buffer: str
    :param encoding: The encoding to use.
    :type encoding: str
    :param overwrite: If true, file is overwritten.
    :type overwrite: bool
    :return: The number of bytes written or lt 0 if error.
    :rtype int
    """
    if overwrite:
        mode = 'w'
    else:
        mode = 'a'

    try:
        with open(file_name, mode, encoding=encoding) as file:
            return file.write(text_buffer)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e.strerror}")
        return -1
