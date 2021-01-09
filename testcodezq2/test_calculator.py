import allure
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


@allure.feature("测试计算器功能")
class TestCalculator:
    # def __init__(self):
    #     pass

    def setup_class(self):
        self.cal = Calculator()

    def test_o(self, get_data):
        print(f"{get_data[1]}")

    @allure.story("测试加法功能")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, excepted", get_data()[0])
    def test_add(self, a, b, excepted, print_mark):
        assert self.cal.add(a, b) == excepted

    @allure.story("测试减法功能")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, excepted", get_data()[1])
    def test_sub(self, a, b, excepted, print_mark):
        res = self.cal.sub(a, b)
        if isinstance(res, float):
            res = round(res, 2)
        assert res == excepted

    @allure.story("测试乘法功能")
    @allure.link("http://www.baidu.com", name="testcase")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, excepted", get_data()[2])
    def test_mul(self, a, b, excepted, print_mark):
        assert self.cal.mul(a, b) == excepted

    @allure.story("测试除法功能")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, excepted", get_data()[3])
    def test_div(self, a, b, excepted, print_mark):
        with allure.step("step1:第一步"):
            print("测试allurestep")
        assert self.cal.div(a, b) == excepted
