

def add_rendition(self, lang, file_path):
    # Check if the language is valid
    if lang not in ["en", "es", "fr", "de"]:
        raise ValueError("Invalid language")

    # Check if the file path is valid
    if not os.path.isfile(file_path):
        raise ValueError("Invalid file path")

    # Add the rendition to the dictionary
    self.renditions[lang] = file_path
