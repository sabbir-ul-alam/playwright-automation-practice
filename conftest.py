import os

import pytest
from utils.config_loader import load_env_config, load_user_credentials

def pytest_addoption(parser):
    parser.addoption("--env", action = 'store', default = 'stg', help= "Enrionment to run tests against" )


@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    os.environ['ENV'] = request.config.getoption("--env")


@pytest.fixture(scope="session")
def config():
    return load_env_config()


@pytest.fixture(params=load_user_credentials())
def user(request):
    return request.param


# # Hook to dynamically parameterize test function with user credentials
# def pytest_generate_tests(metafunc):
#     if "user" in metafunc.fixturenames:
#         credentials = load_user_credentials()
#         metafunc.parametrize("user", credentials)