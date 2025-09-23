# from pathlib import Path

# #alll the paths
# CONFIG_FILE_PATH=Path("config/config.yaml")
# PARAMS_FILE_PATH=Path("params.yaml")
# SCHEMA_FILE_PATH=Path("schema.yaml")

from pathlib import Path

# Automatically get the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

# Paths
CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
SCHEMA_FILE_PATH = PROJECT_ROOT / "schema.yaml"
