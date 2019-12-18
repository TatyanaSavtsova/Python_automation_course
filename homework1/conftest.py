import pytest


@pytest.fixture()
def function_fixture():
    print("\n This is a function fixture!")
    yield
    print("\n I'm here to say 'Bye' after the test.")


@pytest.fixture(scope="module")
def module_fixture():
    print("\n This is a module fixture!")


@pytest.fixture(scope="session")
def session_fixture():
    print("\n This is a session fixture!")