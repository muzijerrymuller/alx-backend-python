#!/usr/bin/env python3
"""
this function takes floats from a list and return th sum
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Calculates the sum of a list of floating-point numbers.

    This function takes a list of floating-point numbers as input and
    computes their sum using the built-in `sum()` function. The result
    is returned as a floating-point number.

    Args:
        input_list (List[float]): A list of floating-point numbers to be sumed
                                   The list can contain zero or more float val

    Returns:
        float: The sum of the floating-point numbers in the input list. If the
               input list is empty, the function will return 0.0.

    Example:
        >>> result = sum_list([1.5, 2.5, 3.0])
        >>> print(result)
        7.0

        >>> empty_result = sum_list([])
        >>> print(empty_result)
        0.0
    '''
    return float(sum(input_list))
