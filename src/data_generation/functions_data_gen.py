# TODO: function that based on model space and model prior on that space, draws a realized model
# could be just a random choice function?

import numpy as np
import pandas as pd

obs = 100

model_space = np.arange(1,obs,dtype=int)

model_space.shape

model_prior = np.full(model_space.shape,1/obs)

# TODO: Make model prior "complete"; include switching prob and trend sign?

def gen_random_model(model_space, model_prior):
    '''
    Input: Model_space 1D array
        model prior: 1D array, probability distribution w/ standard attributes.


    Output: trend_shift: scalar, realized model choice.
    '''

    # trend_shift = np.random.choice(model_space, size=None, replace=True, p=model_prior)

    # trend_shift

    # generate trend vector including shift

    # trend_with_shift = np.full(100,c)
    # for i in range(0,100):
    #     if i <= trend_shift:
    #         trend_with_shift[i] = trend[0]
    #     elif i > trend_shift:
    #         trend_with_shift[i] = trend[1]

    # trend_with_shift

    # return trend_shift
    pass

# TODO: Write function that generates the data based on model, parameter, observations.

# TODO: Make sure to have correct definition of model.

def generate_data(model_switching_point, model_change_sign, trend_abs, var_errors, obs, seed):
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

    #Generate timeline
    t = np.arange(0,obs,1,dtype=int)

    # Generate (stochastic) trend:
    # Either first increasing, then decreasing, or vice versa.

    # Generate (normally distributed) errors
    rng = np.random.default_rng(seed)
  
    errors = rng.normal(0, var_errors, obs)



    # Set the shifting point.
    trend_shift = model_switching_point


    trend = np.array([0,0])

    # TODO: To be outsourced into model generation process. (?)
    #draw_rand_bin = rng.binomial(1, p, size=None)

    # TODO: Make 
    if model_change_sign == "pos_to_neg":
        trend = np.array([trend_abs,-trend_abs])
    elif model_change_sign == "neg_to_pos":
        trend = np.array([trend_abs,-trend_abs]) 


    # generate trend vector including shift

    trend_with_shift = np.full(100,trend_abs)
    for i in range(0,100):
        if i <= trend_shift:
            trend_with_shift[i] = trend[0]
        elif i > trend_shift:
            trend_with_shift[i] = trend[1]

    # generate cumulative trend, errors

    cum_sum_trend = np.cumsum(trend_with_shift)

    cum_sum_errors = np.cumsum(errors)

    # shift y upwards by 100 to "normalize" stock
    y = cum_sum_trend + cum_sum_errors
    y = y + 100 - min(y[0:80])
    # TODO: Better upwards shift by 100 + minimal value observed?

    stacked_array= np.stack((t, y), axis=-1)
    data = pd.DataFrame(stacked_array).rename(columns={0: "Time", 1: "Stock price"})



    return data