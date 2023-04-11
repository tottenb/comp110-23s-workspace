"""CQ04 - Dictionaries."""

__author__ = "730578942"

def zip(list1: list[str], list2: list[int]) -> dict[str,int]:
    zipped_dict: dict[str,int] = {}
    idx: int = 0
    if len(list1) != len(list2) or len(list1) == 0:
        return zipped_dict
    else: 
        while idx < len(list1):
            zipped_dict[list1[idx]] = list2[idx]
            idx = idx + 1
    return zipped_dict