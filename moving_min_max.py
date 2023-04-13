def moving_min (array, period ):

    moving_min = np.empty_like(array)
    moving_min = np.full( moving_min.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_min[i-1] = np.min(array[i-period:i] , dtype=np.float16 )
    return moving_min

def moving_max (array, period ):

    moving_max = np.empty_like(array)
    moving_max = np.full( moving_max.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_max[i-1] = np.max(array[i-period:i] , dtype=np.float16 )
    return moving_max     
