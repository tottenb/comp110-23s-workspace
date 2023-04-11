"""Example Function for Unit Tests"""

def sum(xs: list[float]) -> float:
    """will return the sum of all elements in list xs"""
    sum_total: float = 0.0
    for item in range(len(xs)):
        sum_total += xs[item]
    return sum_total