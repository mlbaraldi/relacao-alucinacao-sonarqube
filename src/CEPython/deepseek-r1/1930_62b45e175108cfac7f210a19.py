def validate_fixity(self, fixity, manifest_files):
    errors = []
    if not isinstance(fixity, dict):
        errors.append("Fixity block is not a dictionary")
    else:
        for algorithm, entries in fixity.items():
            if not isinstance(entries, dict):
                errors.append(f"Fixity algorithm '{algorithm}' has invalid entries (not a dictionary)")
            else:
                for file_path in entries:
                    if file_path not in manifest_files:
                        errors.append(f"File '{file_path}' in fixity block is not present in the manifest")
    if errors:
        raise ValueError("Fixity validation errors:\n" + "\n".join(errors))
