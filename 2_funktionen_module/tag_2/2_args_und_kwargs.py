"""
*args und **kwargs
"""


def values(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


values(2, 3, 4, a=1, b=2, c=3)