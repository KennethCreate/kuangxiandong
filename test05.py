import pytest


@pytest.mark.demo
@pytest.mark.smoke
def test_add_02():
    b = 1 + 2
    assert 0 == b
