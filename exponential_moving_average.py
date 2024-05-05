def ema (array, period ):

    ema = np.empty_like(array)
    ema = np.full( ema.shape , np.nan)
    ema[0] = np.mean(array[0] , dtype=np.float16)
    alpha = 2 / (period + 1)
    # Calculate the EMA for each window of 14 values
    for i in range(1 , len(array) ):
          ema[i] = np.array( (array[i] * alpha +  ema[i-1]  * (1-alpha) ) , dtype=np.float16 )
    
    return ema 


def ema(price, period):

        price = np.array(price)
        alpha = 2 / (period + 1.0)
        alpha_reverse = 1 - alpha
        data_length = len(price)

        power_factors = alpha_reverse ** (np.arange(data_length + 1))
        initial_offset = price[0] * power_factors[1:]

        scale_factors = 1 / power_factors[:-1]

        weight_factor = alpha * alpha_reverse ** (data_length - 1)

        weighted_price_data = price * weight_factor * scale_factors
        cumulative_sums = weighted_price_data.cumsum()
        ema_values = initial_offset + cumulative_sums * scale_factors[::-1]

        return ema_values
