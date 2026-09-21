

def _explore_folder(folder):
    packages = {}
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            basename = os.path.splitext(filename)[0]
            if basename not in packages:
                packages[basename] = []
            packages[basename].append(filename)
    return packages
