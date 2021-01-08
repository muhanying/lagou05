import pytest
import yaml

from pythoncode.calculator import Calculator


@pytest.fixture()
def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        add_data = datas["add"]
        sub_data = datas["sub"]
        mul_data = datas["mul"]
        div_data = datas["div"]
        div_ids = datas["divids"]
    return [add_data, sub_data, mul_data, div_data, div_ids]


@pytest.fixture(scope="module")
def print_mark():
    print("开始计算了")
    yield
    print("结束计算了")


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.parametrize("a, b, excepted", get_datas()[1])
    def test_add(self, a, b, excepted):
        assert self.cal.add(a, b) == excepted
