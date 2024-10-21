#!/usr/bin/env python3
"""multiplyer"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The value by which to multiply the input.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The product of value and the multiplier.
        """
        return value * multiplier
    
    return multiplier_function
