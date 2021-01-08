import pytest
import yaml


@pytest.fixture(scope="module")
def print_mark():
    print("开始计算了")
    yield
    print("结束计算了")


