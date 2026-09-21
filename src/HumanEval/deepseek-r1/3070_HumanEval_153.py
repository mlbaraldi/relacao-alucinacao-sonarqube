
def Strongest_Extension(class_name, extensions):
    max_strength = None
    strongest_ext = None
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if max_strength is None or strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
