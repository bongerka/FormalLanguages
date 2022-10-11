import pytest
from src.modules.RegularExpressionHandling import RegularExpressionHandling

alphabet: set = {"a", "b", "c", "1"}
operations: set = {".", '+', '*'}


def test_initiation_1():
    with pytest.raises(AttributeError) as e:
        RegularExpressionHandling("ad.b+)", 2, 1, alphabet, operations)
    assert e.value.args[0] == "Unacceptable symbols"


def test_initiation_2():
    with pytest.raises(AttributeError) as e:
        instance = RegularExpressionHandling("ac.a+*a", 2, 1, alphabet, operations)
        instance.are_exist_necessary_words()
    assert e.value.args[0] == "Incorrect expression"


def test_sum_1():
    expr1 = [1, 0, 3]
    expr2 = [-1, 2, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__sum
    res = my_func(expr1, expr2)
    assert res == [1, 0, 1]


def test_sum_2():
    expr1 = [-1, 0, -1, -1, -1]
    expr2 = [1, 0, 1, 0, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__sum
    res = my_func(expr1, expr2)
    assert res == expr2


def test_concat_1():
    expr1 = [0, 0, 0]
    expr2 = [-1, 0, -1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__concatenation
    res = my_func(expr1, expr2)
    assert res == [1, 0, 0]


def test_concat_2():
    expr1 = [4, 7, 3, -1, 1]
    expr2 = [3, -1, 2, 1, 5]
    my_func = RegularExpressionHandling._RegularExpressionHandling__concatenation
    res = my_func(expr1, expr2)
    assert res == [5, 4, 3, 5, 4]


def test_clini_star_1():
    expr = [-1, 0, 3, 2]
    my_func = RegularExpressionHandling._RegularExpressionHandling__kleene_star
    res = my_func(expr)
    assert res == [0, 0, 0, 0]


def test_clini_star_2():
    expr = [2, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__kleene_star
    res = my_func(expr)
    assert res == [0, 1]


def test_clini_star_3():
    expr = [-1, 0, -1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__kleene_star
    res = my_func(expr)
    assert res == [0, 0, 0]


def test_clni_star_3():
    instance = RegularExpressionHandling('ab+c.aba.*.bac.+.+*', 3, 2, alphabet, operations)
    result = instance.are_exist_necessary_words()
    assert result is True


def test_clini_str_3():
    instance = RegularExpressionHandling('a1+1.aba.*.bac.+.+*', 3, 2, alphabet, operations)
    result = instance.are_exist_necessary_words()
    assert result is True


def test_ini_star_3():
    instance = RegularExpressionHandling('acb..bab.c.*.ab.ba.+.+*a.', 3, 0, alphabet, operations)
    result = instance.are_exist_necessary_words()
    assert result is False


if __name__ == "__main__":
    pytest.main()
