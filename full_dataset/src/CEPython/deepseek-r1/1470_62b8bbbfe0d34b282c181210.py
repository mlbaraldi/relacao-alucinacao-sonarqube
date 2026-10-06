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
    try:
        data = text_buffer.encode(encoding)
    except Exception:
        return -1

    mode = 'wb' if overwrite else 'ab'
    try:
        with open(file_name, mode) as f:
            bytes_written = f.write(data)
            return bytes_written
    except Exception:
        return -1
