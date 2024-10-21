#!/usr/bin/env python3
'''Module for computing lengths of sequences.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence from the input and its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
