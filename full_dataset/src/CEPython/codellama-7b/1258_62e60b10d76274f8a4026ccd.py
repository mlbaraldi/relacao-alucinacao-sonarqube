

def data(self, *keys):
    # Create a dictionary to store the data
    data_dict = {}

    # If no keys are provided, include all values
    if not keys:
        for key, value in self.items():
            data_dict[key] = value
    # Otherwise, include only the specified keys
    else:
        for key in keys:
            # Check if the key is in the record
            if key in self:
                data_dict[key] = self[key]
            # If the key is not in the record, insert a None value
            else:
                data_dict[key] = None

    return data_dict
