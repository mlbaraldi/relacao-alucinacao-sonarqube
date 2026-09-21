def data(self, *keys):
    result = {}
    if not keys:
        for field, value in zip(self.fields, self.values):
            result[field] = value
    else:
        for key in keys:
            if isinstance(key, int):
                if key < 0 or key >= len(self.fields):
                    raise IndexError("Index out of bounds")
                field_name = self.fields[key]
                result[field_name] = self.values[key]
            else:
                try:
                    idx = self.fields.index(key)
                    result[key] = self.values[idx]
                except ValueError:
                    result[key] = None
    return result
