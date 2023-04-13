import numpy as np

def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
