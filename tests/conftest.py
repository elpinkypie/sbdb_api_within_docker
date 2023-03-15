import pytest
from controller.file_operation import read_json


@pytest.fixture(scope="session", autouse=True)
def setup_base_url():
    base_url = 'https://ssd-api.jpl.nasa.gov/cad.api'
    yield base_url


# this function can be used in future to load test data from test file for parametrised tests
@pytest.fixture(scope="session")
def load_test_data():
    load_file = read_json(path="")
    return load_file


@pytest.fixture(scope="session")
def data_gen():
    print("Create random data generation object...")
    # here would be methods for generating random data for tests
