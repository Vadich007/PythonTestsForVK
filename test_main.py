import pytest
from contextlib import nullcontext as no_exception

class TestsTuple:        
    def test_tuple_positive():
        a = (1,2,3)
        assert a.count() == 3

    def test_tuple_negative(): 
        a = (1,2,3)
        try:
            a[0] = 9
        except TypeError:
            pass
    
    @pytest.mark.parametrize(
        "t, x, res, exception",
        [
            ((1,2,3,4), 3, 2, no_exception),
            ((1,1,1,1), 1, 0, no_exception),
            ((1,2,1,0), 3, 0, pytest.raises(ValueError)),
        ]
    )
    def test_tuple_parametrize(t, x,res, exception):
        with exception:
            assert t.index(x) == res
        

class TestsDict:

    def test_dict_positive():
        countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
        assert countries_and_capitals["Россия"] == "Москва"

    def test_dict_negative():
        countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
        try:
            del countries_and_capitals["Иран"]
        except KeyError:
            pass
        
    @pytest.mark.parametrize(
            "d, x,res, default",
            [
                ({"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж"}, "Москва","Россия", "Ключа нет в словаре" ),
                ({"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж"}, "Рим","Ключа нет в словаре", "Ключа нет в словаре" )
            ]
    )    
    def test_dict_parametrize(d, x, res, default):
         assert d.get(x, default) == res