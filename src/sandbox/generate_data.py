# TODO: Write function that generates the data based on model, parameter, observations.


def generate_data(model, params, obs, seed):
    ''' Generates the data for a specified model, specified parameters and hyperparameters
        
        Inputs:
        model: String, determines which data generating process class to use
        params: np-array (1D) TODO: Could also be list?, determines the parametrization
        for the chosen model (e.g. betas, trend, variance )
        obs: pos. Integer, determines how many data points to generate. 
        seed: integer, to replicate certain data generations.
        Outputs: 
        data_generated - np-array ((1+K) D ) of dependent and independent variables of data.
    
    '''
    # Set parameters

    #Generate timeline

    t = np.arange(0,obs,1,dtype=int)

    # Set std and switching probability

    var_errors = params[0]
    p = params[1]

    # Generate (stochastic) trend:
    # Either first increasing, then decreasing, or vice versa.


    rng = np.random.default_rng(seed)
    draw_rand_bin = rng.binomial(1, p, size=None)

    errors = rng.normal(0, var_errors, obs)


    # Set the trend component
    c = .5

    # Generate trend shift (first up, then down, or vice versa)

    trend = np.array([0,0])

    if draw_rand_bin == 0:
        trend = np.array([c,-c])
    elif draw_rand_bin == 1:
        trend = np.array([c,-c])    


    # Determine whether there is a trend shift
    # For shift at t=0, this is equivalent to no shift (i.e., second part of trend is used throughout).

    # Set up shifting probabilities
    p_shift_at_0 = 0.5

    equal_prob_t80= (1-  p_shift_at_0) / (79)

    p_shift_at_t = np.full(80, equal_prob_t80)


    p_shift_at_t[0] = p_shift_at_0

    p_shift_at_t

    check_sum = np.sum(p_shift_at_t)
    # check_sum

    trend_shift = np.random.choice(80, size=None, replace=True, p=p_shift_at_t.tolist())

    trend_shift = np.random.choice(80, size=None, replace=True)

    trend_shift

    # generate trend vector including shift

    trend_with_shift = np.full(100,c)
    for i in range(0,100):
        if i <= trend_shift:
            trend_with_shift[i] = trend[0]
        elif i > trend_shift:
            trend_with_shift[i] = trend[1]

    trend_with_shift


    # run cumulative trend, errors

    cum_sum_trend = np.cumsum(trend_with_shift)

    cum_sum_errors = np.cumsum(errors)

    # shift y upwards by 100 to "normalize" stock
    y = cum_sum_trend + cum_sum_errors + 100

    return None