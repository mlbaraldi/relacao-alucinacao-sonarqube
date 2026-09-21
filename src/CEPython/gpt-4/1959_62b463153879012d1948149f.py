

def _eval_file(prefix, file_path):
    """
    Identifica o tipo de arquivo do pacote: `asset` ou `rendition`.

    Identifica o tipo de arquivo do pacote e atualiza `packages` com o tipo e
    o endereço do arquivo em análise.

    Parameters
    ----------
    prefix : str
        nome do arquivo XML sem extensão
    filename : str
        filename
    file_folder : str
        file folder

    Returns
    -------
    dict
    """
    packages = {'asset': [], 'rendition': []}
    file_path = file_folder + '/' + filename
    file_type = 'asset' if filename.endswith('.asset') else 'rendition'
    packages[file_type].append(file_path)
    return packages
