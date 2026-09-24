

def inject_config(self):
    # Check if the environment variable for config path is defined
    if "CONFIG_PATH" not in os.environ:
        # If not, set it to the default value
        os.environ["CONFIG_PATH"] = "config.json"
