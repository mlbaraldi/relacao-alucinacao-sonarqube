

def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    num_objects = 0
    good_objects = 0

    for obj in self.objects:
        num_objects += 1
        if validate_objects and check_digests and self.validate_object(obj):
            good_objects += 1
        elif show_warnings:
            print(f"Warning: Object {obj['name']} is invalid.")

    return num_objects, good_objects
