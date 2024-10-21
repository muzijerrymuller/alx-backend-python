#!/usr/bin/env python3
'''
Module to provide a function for
calculating the floor of a float number.
'''


import math


def floor(n: float) -> int:
    """
    Returns the floor of the float number n.
    Args:
    n (float): The float number to get the floor value of.
    Returns:
    int: The largest integer less than or equal to n.
    """
    return math.floor(n)
