import numpy as np

def shift(array , place):

    array =  array.astype(np.float16)

    shifted = np.roll(array, place)

    shifted[0:place] = np.nan
    return shifted
