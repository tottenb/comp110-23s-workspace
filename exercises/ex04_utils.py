"""EX04 - Utils."""

__author__ = "730578942"


def all(xs: list[int], integer: int) -> bool:
    """Evaluates if all integer elements in a list are the same."""
    idx: int = 0
    if len(xs) == 0:
        return False
    else:
        while idx < len(xs):
            if xs[idx] == integer:
                idx = idx + 1
            else:
                return False
        return True


def max(input: list[int]) -> int:
    """Returns the maximum value integer from a list."""
    idx: int = 0
    max: int = input[0]

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while idx < len(input):
            if input[idx] > max:
                max = input[idx]
                idx = idx + 1
            else:
                idx = idx + 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Evaluates if two lists are identical."""
    idx_1: int = 0
    idx_2: int = 0
    if len(list_1) != len(list_2):
        return False
    else:
        while idx_1 < len(list_1):
            if list_1[idx_1] == list_2[idx_2]:
                idx_1 = idx_1 + 1
                idx_2 = idx_2 + 1
            else:
                return False
        return True