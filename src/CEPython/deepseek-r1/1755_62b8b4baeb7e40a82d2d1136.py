def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface import Method
    import inspect
    errors = []

    # Step 1: Verify the candidate claims to provide the interface unless tentative
    if not tentative and not iface.providedBy(candidate):
        errors.append(Invalid(f"{candidate} does not claim to provide {iface}."))

    # Collect all names (methods and attributes) from the interface
    for name in iface.names():
        attr = iface[name]
        if isinstance(attr, Method):
            # Handle method checks
            if not hasattr(candidate, name):
                errors.append(Invalid(f"Method '{name}' not found on {candidate}."))
                continue

            candidate_method = getattr(candidate, name)
            interface_method_func = attr.interface

            # Attempt to get the expected signature from the interface's method
            try:
                expected_sig = inspect.signature(interface_method_func)
            except ValueError:
                # Skip signature check if it can't be obtained (e.g., built-in functions)
                continue

            # Adjust expected signature if verifying a class (vtype indicates class)
            if vtype == 'class':
                params = list(expected_sig.parameters.values())
                if params and params[0].name in ('self', 'cls'):
                    expected_sig = expected_sig.replace(parameters=params[1:])

            # Get the actual signature from the candidate's method
            try:
                actual_sig = inspect.signature(candidate_method)
            except ValueError:
                errors.append(Invalid(f"Method '{name}' has a signature that cannot be inspected."))
                continue

            # Compare signatures
            if expected_sig != actual_sig:
                errors.append(Invalid(
                    f"Method '{name}' has incorrect signature. Expected {expected_sig}, got {actual_sig}."
                ))
        else:
            # Handle attribute checks
            if not hasattr(candidate, name):
                errors.append(Invalid(f"Attribute '{name}' not found on {candidate}."))

    # Handle collected errors
    if errors:
        if len(errors) == 1:
            raise errors[0]
        else:
            error_messages = [str(e) for e in errors]
            raise Invalid("Multiple validation errors occurred:\n" + "\n".join(error_messages))
    
    return True
