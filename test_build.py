from datetime import datetime
import pytest
from requests import session

# from csvdata import read_csv

def add(a, b):
    return a + b



class TestAdd:


    # @pytest.mark.skip
    @pytest.mark.api
    def test_int(self):
        res = add(1, 3)
        assert res == 4

    #
    # @pytest.mark.skipif(1==1,reason='我不想干')
    # @pytest.mark.usefixtures("fixt")
    @pytest.mark.web
    def test_str(self,fixt):
        res = add('1', '3')
        assert res == '13'

    @pytest.mark.web
    def test_str(self,fixt):
        res = add('1', '3')
        assert res == '13'