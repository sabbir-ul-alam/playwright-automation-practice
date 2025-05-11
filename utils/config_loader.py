import json
import os


def load_config(env: str):
    with open(f"config/{env}.json") as file:
        return json.loads(file)