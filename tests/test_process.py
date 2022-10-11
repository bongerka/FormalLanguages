import pytest
from src.modules.RegularExpressionHandling import RegularExpressionHandling

alphabet: set = {"a", "b", "c", "1"}
operations: set = {".", '+', '*'}


def test_answer_1():
    instance = RegularExpressionHandling('ab+c.aba.*.bac.+.+*', 3, 2, alphabet, operations)
    result = instance.are_exist_necessary_words()
    assert result is True


def test_answer_2():
    instance = RegularExpressionHandling('a1+1.aba.*.bac.+.+*', 3, 2, alphabet, operations)
    result = instance.are_exist_necessary_words()
    assert result is True


def test_answer_3():
    instance = RegularExpressionHandling('acb..bab.c.*.ab.ba.+.+*a.', 3, 0, alphabet, operations)
    result = instance.are_exist_necessary_words()
    assert result is False


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
    expr1 = [1, 1, 1]
    expr2 = [0, 1, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__sum
    res = my_func(expr1, expr2)
    assert res == [1, 1, 1]


def test_sum_2():
    expr1 = [0, 1, 0, 0, 0]
    expr2 = [1, 1, 1, 1, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__sum
    res = my_func(expr1, expr2)
    assert res == expr2


def test_concat_1():
    expr1 = [1, 1, 1]
    expr2 = [0, 1, 0]
    my_func = RegularExpressionHandling._RegularExpressionHandling__concatenation
    res = my_func(expr1, expr2)
    assert res == [1, 1, 1]


def test_concat_2():
    expr1 = [1, 1, 1, 0, 1]
    expr2 = [1, 0, 1, 1, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__concatenation
    res = my_func(expr1, expr2)
    assert res == [1, 1, 1, 1, 1]


def test_kleene_star_1():
    expr = [0, 1, 1, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__kleene_star
    res = my_func(expr)
    assert res == [1, 1, 1, 1]


def test_kleene_star_2():
    expr = [1, 1]
    my_func = RegularExpressionHandling._RegularExpressionHandling__kleene_star
    res = my_func(expr)
    assert res == [1, 1]


def test_kleene_star_3():
    expr = [0, 1, 0]
    my_func = RegularExpressionHandling._RegularExpressionHandling__kleene_star
    res = my_func(expr)
    assert res == [1, 1, 1]


if __name__ == "__main__":
    pytest.main()
