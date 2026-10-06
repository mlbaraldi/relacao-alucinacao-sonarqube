

def namesAndDescriptions(self, all=False):
    names = []
    descriptions = []
    for name, value in self.__dict__.items():
        if all or value.description:
            names.append(name)
            descriptions.append(value.description)
    return names, descriptions
