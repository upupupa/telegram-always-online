import pytest


@pytest.fixture
def sample_fixture():
    yield True
