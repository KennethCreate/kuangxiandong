import yaml
import pytest

yaml.safe_load(open("./data.yml"))


def add_function(a, b):
    return a + +b


@pytest.mark.parametrize("a,b,expected",
                         yaml.safe_load(open("./data.yml"))["datas"],
                         ids=yaml.safe_load(open("./data.yml"))["myid"])
def test_add(a, b, expected):
    assert add_function(a, b) == expected
