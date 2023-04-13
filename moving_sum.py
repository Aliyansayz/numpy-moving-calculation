import numpy as np

def moving_sum (array, period ):

    moving_sum = np.empty_like(array)
    moving_sum = np.full( moving_sum.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_sum[i-1] = np.sum(array[i-period:i] , dtype=np.float16 )
    return moving_sum 
