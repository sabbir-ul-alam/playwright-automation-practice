import json
import os
from dotenv import load_dotenv

load_dotenv()

def load_env_config():
    env = os.getenv("ENV", "stg")
    with open(f"config/{env}.json") as f:
        return json.load(f)

def load_user_credentials():
    env = os.getenv("ENV", "stg")
    with open(f"config/data/{env}_credentials.json") as f:
        return json.load(f)["user_credentials"]
