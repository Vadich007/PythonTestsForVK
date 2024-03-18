import pytest
from contextlib import nullcontext as no_exception

class TestsTuple:        
    def test_tuple_positive(self):
        a = (1,2,3)
        assert a.count(1) == 1

    def test_tuple_negative(self): 
        a = (1,2,3)
        try:
            a[0] = 9
        except TypeError:
            pass

    @pytest.mark.parametrize('data', [
            (((1,2,3,4)), 3, 2, no_exception),
            (((1,1,1,1)), 1, 0, no_exception),
            (((1,2,1,0)), 3, 0, ValueError),
        ]
    )
    def test_tuple_parametrize(self, data):
        t, x, res, exception = data
        try:
            t.index(x) == res
        except exception:
            pass
        

class TestsDict:
    def test_dict_positive(self):
        countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
        assert countries_and_capitals["Россия"] == "Москва"

    def test_dict_negative(self):
        countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
        try:
            del countries_and_capitals["Иран"]
        except KeyError:
            pass

    @pytest.mark.parametrize(
        "data",
        [
            ({"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж"}, "Россия","Москва", "Ключа нет в словаре" ),
            ({"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж"}, "Рим","Ключа нет в словаре", "Ключа нет в словаре" )
        ]
    )       
    def test_dict_parametrize(self, data):
        d, x, res, default = data
        assert d.get(x, default) == res