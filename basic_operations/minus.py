import numpy as np


def minus(*args):
    """
    Subtracts all the arguments.
    """
    if len(args) == 0:
        raise ValueError("No arguments given")
    return np.subtract(*args)
