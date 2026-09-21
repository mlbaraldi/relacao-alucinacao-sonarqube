def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    cfg = VersioneerConfig()
    # Populate the configuration settings
    cfg.VCS = 'git'                # Version control system (git, hg, etc.)
    cfg.style = 'pep440'           # Version style (pep440, semver, etc.)
    cfg.tag_prefix = 'v'           # Tag prefix (e.g., 'v' for tags like v1.0.0)
    cfg.parentdir_prefix = ''      # Parent directory prefix (if any)
    cfg.versionfile_source = 'src/myproject/_version.py'  # Path to version file
    cfg.verbose = False            # Verbosity flag
    cfg.lookupfile = '.versioneer-lookup'  # Lookup file for version data
    return cfg
