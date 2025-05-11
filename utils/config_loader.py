# utils/config_loader.py
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load ENV variable from .env


def load_config():
    env = os.getenv("ENV", "stg")
    with open(f"config/{env}.json") as f:
        return json.load(f)
