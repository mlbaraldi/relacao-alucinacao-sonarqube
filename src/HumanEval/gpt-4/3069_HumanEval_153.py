
def Strongest_Extension(class_name, extensions):
    # Initialize the strongest extension and its strength
    strongest_extension = None
    strongest_strength = None

    # Iterate over each extension
    for extension in extensions:
        # Calculate the strength of the extension
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM

        # If this is the first extension or it's stronger than the current strongest
        if strongest_extension is None or strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    # Return the class name and the strongest extension in the required format
    return f'{class_name}.{strongest_extension}'
