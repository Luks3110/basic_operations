import numpy as np
def sum(*args):
    """
    Sums all the arguments.
    """
    if len(args == 0):
        raise ValueError("No arguments given")
    return np.sum(args)
    