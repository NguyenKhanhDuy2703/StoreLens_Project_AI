import yaml
file_path = "src/configs/tracking_config.yaml"
def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r' , encoding="UTF-8") as file:
        config = yaml.safe_load(file)
    return config