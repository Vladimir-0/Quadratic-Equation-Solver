from typing import Tuple, Union
from decimal import Decimal


def solve(a: Decimal, b: Decimal, c: Decimal) -> Union[Tuple[Decimal, Decimal], None]:
    """
    Calculate the quadratic equation roots.
    :param a: First coefficient.
    :param b: Second coefficient.
    :param c: Third coefficient.
    :return: The calculation result or None if D < 0.
    """
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    else:
        x1 = (-b + (d ** 1 / 2)) / (2 * a)
        x2 = (-b - (d ** 1 / 2)) / (2 * a)
    return x1, x2
