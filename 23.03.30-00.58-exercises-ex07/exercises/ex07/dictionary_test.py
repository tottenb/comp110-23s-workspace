"""EX07 - Dictionary-Tests."""

__author__ = "730578942"


def invert(x: dict[str, str]) -> dict[str,str]:
    """Function will invert keys and values."""
    v: list[str] = [x.values()]
    k: list[str] = [x.keys()]
    dic: dict[str, str] = {}

    for i in v:
        if v.count(i) > 1:
            raise KeyError("Duplicate keys exist.") 
        
    for i in range(len(v)):
        dic[v[i]] = k[i]
    return dic



def  favorite_colors(x: dict[str, str]) -> str:
    v: list[str] = x.values()
    largest: dict[str,int] = {}
    for i in v:
        if v.count(i) > largest.values()[0]:
            largest.pop(0)
            largest[i] = v.count(i)
    
    return largest.key(0)
        


def count(x: list[str]) -> dict[str, int]:
    dic: dict[str, int] = {}

    for i in x:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic