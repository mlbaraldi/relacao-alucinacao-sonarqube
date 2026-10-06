

def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    num_objects = 0
    good_objects = 0

    # Iterate over all objects in the storage root
    for obj in self.storage_root.objects:
        num_objects += 1

        # Check if the object is valid
        if validate_objects:
            if not obj.is_valid():
                if show_warnings:
                    print(f"Warning: Object {obj.name} is not valid")
                continue

        # Check if the object's digest is valid
        if check_digests:
            if not obj.digest_valid():
                if show_warnings:
                    print(f"Warning: Object {obj.name} has an invalid digest")
                continue

        # If the object is valid, increment the number of good objects
        if obj.is_valid() and obj.digest_valid():
            good_objects += 1

    return num_objects, good_objects
