import numpy as np

def shift(array , place): """ array_shift  """

    array =  array.astype(np.float16)

    shifted = np.roll(array, place)

    shifted[0:place] = np.nan
    return shifted
  
def moving_end (array, period ): """ moving_end """

    moving_end = np.empty_like(array)
    moving_end = np.full( moving_end.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_end[i-1] = np.array(array[i-1:i] , dtype=np.float16 )
    return moving_end     
  
def moving_min (array, period ):  """ moving_min """

    moving_min = np.empty_like(array)
    moving_min = np.full( moving_min.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_min[i-1] = np.min(array[i-period:i] , dtype=np.float16 )
    return moving_min

def moving_max (array, period ):  """ moving_max  """

    moving_max = np.empty_like(array)
    moving_max = np.full( moving_max.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_max[i-1] = np.max(array[i-period:i] , dtype=np.float16 )
    return moving_max     
  
def moving_sum (array, period ):  """ moving_sum """

    moving_sum = np.empty_like(array)
    moving_sum = np.full( moving_sum.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_sum[i-1] = np.sum(array[i-period:i] , dtype=np.float16 )
    return moving_sum 
  
def sma (array, period ): """Simple Moving Average   """

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
