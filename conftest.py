import pytest
from utils.config_loader import load_config


@pytest.fixture(scope="session")
def config():
    return load_config()
