
def Strongest_Extension(class_name, extensions):
    # Initialize a dictionary to store the strength of each extension
    strengths = {}

    # Loop through each extension and calculate its strength
    for extension in extensions:
        # Calculate the number of uppercase letters in the extension's name
        cap = len([c for c in extension if c.isupper()])

        # Calculate the number of lowercase letters in the extension's name
        sm = len([c for c in extension if c.islower()])

        # Calculate the strength of the extension
        strength = cap - sm

        # Add the strength to the dictionary
        strengths[extension] = strength

    # Find the strongest extension
    strongest_extension = max(strengths, key=strengths.get)

    # Return the strongest extension in the format "ClassName.StrongestExtensionName"
    return f"{class_name}.{strongest_extension}"
