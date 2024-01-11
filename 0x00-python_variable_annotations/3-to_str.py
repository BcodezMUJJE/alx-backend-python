#!/usr/bin/env python3

'''Amodule that takes a float as argument and returns a string'''


def to_str(n: float) -> str:
    '''Afunction that returns the string quivalent of any float argument'''
    return str(n)


if __name__ == '__main__':
    print(f'to_str(3.142)')
    print(to_str(0.00))

    print(to_str.__annotations__)
