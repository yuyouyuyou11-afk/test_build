from datetime import datetime
import pytest
from requests import session
import logging
import allure

logger = logging.getLogger(__name__)
# from csvdata import read_csv

# def add(a, b):
#     return a + b



# class TestAdd:


#     # @pytest.mark.skip
#     @pytest.mark.api
#     def test_int(self):
#         res = add(1, 3)
#         assert res == 4

#     #
#     # @pytest.mark.skipif(1==1,reason='我不想干')
#     # @pytest.mark.usefixtures("fixt")
#     @pytest.mark.web
#     def test_str(self,fixt):
#         res = add('1', '3')
#         assert res == '13'

#     @pytest.mark.web
#     def test_str(self,fixt):
#         res = add('1', '3')
#         assert res == '13'






@allure.feature("加法功能")
class TestAdd:

        @allure.story("整数相加")
        def test_int(self):
            logger.info("开始执行整数相加用例")
            a, b = 3, 5
            result = a + b
            logger.info(f"计算结果: {result}")
            assert result == 8

        @allure.story("字符串相加")
        def test_str(self):
            logger.info("开始执行字符串拼接用例")
            a, b = "Hello", "World"
            result = a + b
            logger.info(f"拼接结果: {result}")
            assert result == "HelloWorld"
