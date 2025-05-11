# utils/config_loader.py
import json
import os
from dotenv import load_dotenv

load_dotenv()


def load_config():
    env = os.getenv("ENV", "stg")
    # Load environment config
    with open(f"config/{env}.json") as f:
        env_config = json.load(f)

    # Load credentials
    cred_path = f"config/data/{env}_credentials.json"
    if os.path.exists(cred_path):
        with open(cred_path) as f:
            env_config["user_credentials"] = json.load(f)["user_credentials"]

    return env_config
