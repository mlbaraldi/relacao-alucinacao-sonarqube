

def _eval_file(prefix, file_path):
    """
    Identifica o tipo de arquivo do pacote: `asset` ou `rendition`.

    Identifica o tipo de arquivo do pacote e atualiza `packages` com o tipo e
    o endereço do arquivo em análise.

    Parameters
    ----------
    prefix : str
        nome do arquivo XML sem extensão
    file_path : str
        path to the file

    Returns
    -------
    dict
    """
    global packages

    file_type = None
    if file_path.endswith('.asset'):
        file_type = 'asset'
    elif file_path.endswith('.rendition'):
        file_type = 'rendition'

    if file_type is not None:
        packages[prefix] = {'type': file_type, 'path': file_path}

    return packages
