import numpy as np
"""
SMA function in numpy just like pandas one
"""
def sma(array, period):
  weights = np.ones(period) / period
  arr     =  np.convolve(array, weights, mode='valid')

  window = period - 1
  sma = np.empty(window + len(arr), dtype=arr.dtype)
  sma[:window] = np.nan * window
  sma[window:] = arr
  # fill missing values by taking mean of first values upto chosen period 
  sma[np.isnan(sma)] = np.nanmean(arr[:period])
  
  return sma

def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array) ):
          sma[i] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 

def sd (array, sma, period ):

    sd = np.empty_like(array)
    sd = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array) ):
          diff = np.array(array[i-period:i] - sma[i] , dtype=np.float32)
          sqr_diff = diff ** 2 
          var = np.sum(sqr_diff) / period 
          sd[i] = np.sqrt( var ) 
    return sd


