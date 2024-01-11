#!/usr/bin/env python3


from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

# Note: The following line has been modified to pass an integer factor
zoom_3x = zoom_array(array, 3)

print(zoom_array.__annotations__)
