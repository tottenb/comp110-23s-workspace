"""EX05 - Utils_Tests."""

__author__ = "730578942"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests the only_evens function with positive integers."""
    assert only_evens([]) == []


def test_only_evens_many() -> None:
    """Tests the only_evens function with positive integers."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]


def test_only_evens_with_neg() -> None:
    """Tests the only_evens function with positive and negative integers."""
    test_list: list[int] = [1, 2, -3, -4, 5, 6]
    assert only_evens(test_list) == [2, -4, 6]


def test_concat_empty() -> None:
    """Tests the concat function with two empty lists."""
    assert concat([], []) == []


def test_concat_positive() -> None:
    """Tests the concat function with two lists of positive integers."""
    test_list_1: list[int] = [1, 2, 3, 4]
    test_list_2: list[int] = [5, 6, 7, 8]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_negative() -> None:
    """Tests the concat function with two lists of negative integers."""
    test_list_1: list[int] = [-10, -20, -30]
    test_list_2: list[int] = [-500, -600, -700]
    assert concat(test_list_1, test_list_2) == [-10, -20, -30, -500, -600, -700]


def test_sub_one_item() -> None:
    """Tests the sub function when the input is a list with only one element."""
    assert sub([1], 0, 1) == [1]


def test_sub_many() -> None:
    """Tests the sub function with a list of positive integers."""
    test_list = [0, 1, 2, 3, 4, 5]
    assert sub(test_list, 2, 4) == [2, 3]


def test_sub_many_with_neg() -> None:
    """Tests the sub function with a list of negative integers."""
    test_list = [-10, -20, -30, -40]
    assert sub(test_list, 0, 3) == [-10, -20, -30]