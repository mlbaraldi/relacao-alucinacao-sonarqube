def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    num_objects = 0
    good_objects = 0
    for obj in self._iter_objects():
        num_objects += 1
        valid = True
        
        # Check hierarchy structure validity
        if not self._is_object_in_valid_hierarchy(obj):
            valid = False
            if show_warnings:
                print(f"Warning: Object {obj} has an invalid hierarchy placement.")
        
        # Check object validity if required
        if valid and validate_objects:
            if not obj.validate(check_digests=check_digests):
                valid = False
                if show_warnings:
                    print(f"Warning: Object {obj} failed content validation.")
        
        if valid:
            good_objects += 1
    
    return num_objects, good_objects
