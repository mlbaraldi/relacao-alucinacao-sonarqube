def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == "pep440":
        version_parts = []
        
        # Handle epoch
        epoch = pieces.get("epoch")
        if epoch is not None:
            version_parts.append(f"{epoch}!")
        
        # Main version components: major.minor.patch
        main_version = []
        for part in ["major", "minor", "patch"]:
            if part in pieces:
                main_version.append(str(pieces[part]))
            else:
                break
        version_parts.append(".".join(main_version))
        
        # Pre-release (a, b, rc)
        pre_release = pieces.get("pre_release")
        if pre_release:
            pre_mapping = {"alpha": "a", "beta": "b", "rc": "rc"}
            pre_char = pre_mapping.get(pre_release, "")
            pre_number = pieces.get("pre_release_num", 0)
            version_parts.append(f"{pre_char}{pre_number}")
        
        # Post-release
        post_number = pieces.get("post_release_num")
        if post_number is not None:
            version_parts.append(f".post{post_number}")
        
        # Development release
        dev_number = pieces.get("dev_num")
        if dev_number is not None:
            version_parts.append(f".dev{dev_number}")
        
        # Local version identifier
        local = pieces.get("local")
        if local:
            version_parts.append(f"+{local}")
        
        return "".join(version_parts)
    
    elif style == "semver":
        version_parts = []
        
        # Main version components: major.minor.patch
        main_version = []
        for part in ["major", "minor", "patch"]:
            if part in pieces:
                main_version.append(str(pieces[part]))
            else:
                break
        version_parts.append(".".join(main_version))
        
        # Pre-release identifiers
        pre_components = []
        pre_release = pieces.get("pre_release")
        if pre_release:
            pre_number = pieces.get("pre_release_num", 0)
            pre_components.append(f"{pre_release}.{pre_number}")
        
        # Additional pre-release components can be added here if needed
        
        if pre_components:
            version_parts.append(f"-{'.'.join(pre_components)}")
        
        # Build metadata
        build_components = []
        dev_number = pieces.get("dev_num")
        if dev_number is not None:
            build_components.append(f"dev{dev_number}")
        
        post_number = pieces.get("post_release_num")
        if post_number is not None:
            build_components.append(f"post{post_number}")
        
        local = pieces.get("local")
        if local:
            build_components.append(local)
        
        if build_components:
            version_parts.append(f"+{'.'.join(build_components)}")
        
        return "".join(version_parts)
    
    else:
        raise ValueError(f"Unknown style: {style}")
