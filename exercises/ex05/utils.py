"""EX05 - Utils."""

__author__ = "730578942"


def only_evens(input: list[int]) -> list:
    """Takes a list of integers as input as returns all even integers from input list."""
    idx: int = 0
    output_list: list() = []
    while idx < len(input):
        if input[idx] % 2 == 0:
            output_list.append(input[idx])
            idx = idx + 1
        else:
            idx = idx + 1
    return output_list


def concat(list1: list[int], list2: list[int]) -> list:
    """Combines elements from two lists into one."""
    idx1: int = 0
    idx2: int = 0
    output_list: list() = []
    if len(list1) == 0 and len(list2) == 0:
        return []
    else:
        while idx1 < len(list1):
            output_list.append(list1[idx1])
            idx1 = idx1 + 1
        while idx2 < len(list2):
            output_list.append(list2[idx2])
            idx2 = idx2 + 1
        return output_list


def sub(list: list[int], int1: int, int2: int) -> list:
    """From the given list a subset is created between the given index values."""
    start_idx: int = int1
    end_idx: int = int2
    output_list: list() = []
    if int1 < 0:
        start_idx = 0
    if int2 > len(list):
        end_idx = len(list)
    i: int = start_idx
    while (i < end_idx):
        output_list.append(list[i])
        i = i + 1
    return output_list