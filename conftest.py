import pytest


@pytest.fixture(scope="session")
def browser_config():
    return {
        "implicit_wait": 10,
        "explicit_wait": 10,
    }
