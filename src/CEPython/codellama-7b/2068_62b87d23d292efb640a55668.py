from versioneer import VersioneerConfig


def get_config():
    config = VersioneerConfig()
    config.version = "1.0.0"
    config.name = "my_package"
    config.description = "This is a sample package"
    config.authors = ["John Doe", "Jane Smith"]
    config.maintainers = ["John Doe", "Jane Smith"]
    config.license = "MIT"
    config.url = "https://github.com/johndoe/my_package"
    config.keywords = ["sample", "package"]
    config.classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
    return config
