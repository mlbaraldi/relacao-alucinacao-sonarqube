
def Strongest_Extension(class_name, extensions):
    # Calculate strength for each extension
    strengths = [(ext, sum(c.isupper() - c.islower() for c in ext)) for ext in extensions]
    # Find the strongest extension
    strongest_ext = max(strengths, key=lambda x: x[1])
    # Return the class name and the strongest extension
    return f'{class_name}.{strongest_ext[0]}'

# Test the function
