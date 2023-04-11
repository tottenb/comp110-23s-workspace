"""EX07 - Dictionary-Tests."""

__author__ = "730578942"


from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests the invert function on an dictionary that is empty."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_use_case_one() -> None:
    """Tests the invert function on a dictionary of states and cities."""
    test_dict: dict[str, str] = {'illinois': 'chicago', 'idaho': 'boise'}
    assert invert(test_dict) == {'chicago': 'illinois', 'boise': 'idaho'}


def test_invert_use_case_two() -> None:
    """Tests the invert function on a dictionary of classifications and animals."""
    test_dict: dict[str, str] = {'mammal': 'dog', 'reptile': 'gecko'}
    assert invert(test_dict) == {'dog': 'mammal', 'gecko': 'reptile'}


def test_favorite_color_empty() -> None:
    """Tests the favorite_color function on an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == {}


def test_favorite_color_use_case_one() -> None:
    """Tests the favorite_color function on a dictionary where everyone likes blue."""
    test_dict: dict[str, str] = {'kris': 'blue', 'jordan': 'blue'}
    assert favorite_color(test_dict) == 'blue'


def test_favorite_color_use_case_two() -> None:
    """Tests the favorite_color function on a dictionary where red and blue are liked equally."""
    test_dict: dict[str, str] = {'kris': 'red', 'jordan': 'blue'}
    assert favorite_color(test_dict) == 'red'


def test_count_empty() -> None:
    """Tests the count function on an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_use_case_one() -> None:
    """Tests the count function on a list of favorite colors."""
    test_list: list[str] = ['blue', 'blue', 'blue', 'red', 'yellow']
    assert count(test_list) == {'blue': 3, 'red': 1, 'yellow': 1}


def test_count_use_case_two() -> None:
    """Tests the count function on a list of favorite baseball teams."""
    test_list: list[str] = ['cubs', 'cubs', 'cubs', 'guardians', 'guardians', 'pirates']
    assert count(test_list) == {'cubs': 3, 'guardians': 2, 'pirates': 1}