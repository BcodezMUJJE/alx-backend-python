#!/usr/bin/env python3

''' Duck typing - the first element of a sequence
'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Augment the following code with the correct
    duck-typed annotation
    '''
    if lst:
        return lst[0]
    else:
        return None
