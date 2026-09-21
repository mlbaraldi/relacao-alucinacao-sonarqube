

def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Validate storage root hierarchy.

    Parameters:
    validate_objects : bool, optional
        If True, validate objects. Default is True.
    check_digests : bool, optional
        If True, check digests. Default is True.
    show_warnings : bool, optional
        If True, show warnings. Default is False.

    Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
    """

    # Assuming self.storage_root is a StorageRoot object
    # and self.storage_root.objects is a list of Objects
    # and each Object has a method is_valid() that returns True if the object is valid

    num_objects_checked = 0
    good_objects = 0

    for obj in self.storage_root.objects:
        num_objects_checked += 1
        if validate_objects and not obj.is_valid():
            if show_warnings:
                print(f"Warning: Object {obj.name} is not valid")
            else:
                print(f"Object {obj.name} is not valid")
        if check_digests and obj.digest != obj.calculate_digest():
            if show_warnings:
                print(f"Warning: Digest of Object {obj.name} does not match")
            else:
                print(f"Digest of Object {obj.name} does not match")

    return num_objects_checked, good_objects
