"""EX07 - Dictionary."""

__author__ = "730578942"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Function will invert keys and values."""
    dic: dict[str, str] = {}

    for key, value in x.items():
        if value in dic:
            raise KeyError("Duplicate keys exist.") 
        else:
            dic[value] = key
    return dic


def favorite_color(x: dict[str, str]) -> str:
    """Function will return the most common value in a dictionary."""
    v: list[str] = list(x.values())
    largest: dict[str, int] = {}
    for i in v:
        if v.count(i) > largest.get(i, 0):
            largest[i] = v.count(i)
            
    return max(largest, key=largest.get)
        

def count(x: list[str]) -> dict[str, int]:
    """Function will return a dictionary where the keys are the elements of the input list and the values are the counts."""
    dic: dict[str, int] = {}

    for i in x:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic