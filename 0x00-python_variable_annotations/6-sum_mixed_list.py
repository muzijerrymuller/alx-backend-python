#!/usr/bin/env python3
"""Convert the sum of the mixed list to a float and return it"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats as a float."""
    return float(sum(mxd_lst))
