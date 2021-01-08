import pytest
import yaml

from pythoncode.calculator import Calculator


def get_data():
    with open("./data.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        add_data = data["add"]
        sub_data = data["sub"]
        mul_data = data["mul"]
        div_data = data["div"]
        div_ids = data["divids"]
    return [add_data, sub_data, mul_data, div_data, div_ids]


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.parametrize("a, b, excepted", get_data()[0])
    def test_add(self, a, b, excepted, print_mark):
        assert self.cal.add(a, b) == excepted

    @pytest.mark.parametrize("a, b, excepted", get_data()[1])
    def test_sub(self, a, b, excepted, print_mark):
        res = self.cal.sub(a, b)
        if isinstance(res, float):
            res = round(res, 2)
        assert res == excepted

    @pytest.mark.parametrize("a, b, excepted", get_data()[2])
    def test_mul(self, a, b, excepted, print_mark):
        assert self.cal.mul(a, b) == excepted

    @pytest.mark.parametrize("a, b, excepted", get_data()[3])
    def test_div(self, a, b, excepted, print_mark):
        assert self.cal.div(a, b) == excepted
