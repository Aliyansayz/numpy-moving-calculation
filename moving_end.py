def moving_end (array, period ):

    moving_end = np.empty_like(array)
    moving_end = np.full( moving_end.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_end[i-1] = np.array(array[i-1:i] , dtype=np.float16 )
    return moving_end     
