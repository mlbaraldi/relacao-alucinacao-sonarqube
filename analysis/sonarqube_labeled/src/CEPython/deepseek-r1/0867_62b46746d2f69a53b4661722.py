def absorb(self, args):
    if isinstance(self, And):
        composite_type = Or
    elif isinstance(self, Or):
        composite_type = And
    else:
        return list(args)

    base_terms = []
    composite_terms = []
    for term in args:
        if isinstance(term, composite_type):
            composite_terms.append(term)
        else:
            base_terms.append(term)

    # Apply absorption
    remaining_composite = []
    for ct in composite_terms:
        if any(subterm in base_terms for subterm in ct.args):
            continue
        remaining_composite.append(ct)

    # Apply negative absorption
    new_composite = []
    for ct in remaining_composite:
        new_subterms = []
        for subterm in ct.args:
            if isinstance(subterm, Not):
                x = subterm.args[0]
                if x in base_terms:
                    continue  # Skip this Not(x)
                else:
                    new_subterms.append(subterm)
            else:
                new_subterms.append(subterm)
        # Build new composite term
        if not new_subterms:
            # Handle empty composite term
            if composite_type is Or:
                new_ct = Boolean(False)
            else:
                new_ct = Boolean(True)
        elif len(new_subterms) == 1:
            new_ct = new_subterms[0]
        else:
            new_ct = composite_type(*new_subterms)
        new_composite.append(new_ct)

    return base_terms + new_composite
