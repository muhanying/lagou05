from decimal import Decimal

import pytest
import yaml

from pythoncode.calculator import Calculator


class TestCalculator:
    def setup_class(self):
        print("start")
        self.cal = Calculator()

    @pytest.mark.parametrize("a, b, excepted", [(1, 2, 3), (-1, 1, 0), (1.03, 1.23, 2.26)])
    def test_add(self, a, b, excepted):
        print("add")
        assert self.cal.add(a, b) == excepted

    @pytest.mark.parametrize("a, b, excepted", yaml.safe_load(open("./data.yml"))["data"])
    def test_sub(self, a, b, excepted):
        print("sub")
        print(yaml.safe_load(open("./data.yml"))["data"])
        assert self.cal.sub(Decimal(a), Decimal(b)) == Decimal(excepted)

    @pytest.mark.parametrize("a, b, excepted", yaml.safe_load(open("./data.yml"))["mul"])
    def test_sub(self, a, b, excepted):
        print("mul")
        print(yaml.safe_load(open("./data.yml"))["mul"])
        assert self.cal.mul(a, b) == excepted

    @pytest.mark.parametrize("a, b, excepted", yaml.safe_load(open("./data.yml"))["div"], ids=yaml.safe_load(open("./data.yml"))["divids"])
    def test_dev(self, a, b, excepted):
        print("div")
        print(yaml.safe_load(open("./data.yml"))["div"])
        assert self.cal.div(a, b) == excepted


