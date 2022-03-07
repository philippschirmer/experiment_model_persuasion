import numpy as np
import pandas as pd
import pytask
from src.config import BLD

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
    ''' Generates the data for a specified model, specified parameters, observations and seed.
        In the current form, the function draws normally distibuted shocks that add noise to the
        true trend. Trend component is generated according to model and parameter, before being
        summed with generated noise.
        
        Inputs:
        model_switching point: integer - determines switching point of trend component
        model_change_sign: string - determines whether trend is first positive then negative, or vice versa.
        trend_abs: float - absolute strength of the trend.
        var_errors: float - variance of the normal noise / error term.
        obs: integer, determines how many data points to generate. 
        seed: integer, to replicate certain data generations.

        Outputs: 
        data_generated - pd.DataFrame: 2xobs DataFrame with variables "Time" and "Stock price" saved in columns.
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

def save_data(sample, path):
    sample.to_csv(path, sep=",", index=False)


@pytask.mark.produces({
                    "first": BLD / "data/data_1.csv", 
                    "second": BLD / "data/data_2.csv", 
                    "third": BLD / "data/data_3.csv",
                    "fourth": BLD / "data/data_4.csv",
                    "fifth" : BLD / "data/data_5.csv"
})
def task_get_simulated_data(produces):
    sample_1 = generate_data(model_switching_point=40, model_change_sign="neg_to_pos", trend_abs=1, var_errors=10, obs=100, seed=12345)
    save_data(sample_1, produces["first"])
    sample_2 =  generate_data(model_switching_point=20, model_change_sign="pos_to_neg", trend_abs=1, var_errors=10, obs=100, seed=23456)
    save_data(sample_2, produces["second"])
    sample_3 = generate_data(model_switching_point=60, model_change_sign="neg_to_pos", trend_abs=1, var_errors=10, obs=100, seed=34567)
    save_data(sample_3, produces["third"])
    sample_4 = generate_data(model_switching_point=30, model_change_sign="neg_to_pos", trend_abs=5, var_errors=20, obs=100, seed=45678)
    save_data(sample_4, produces["fourth"])
    sample_5 = generate_data(model_switching_point=50, model_change_sign="neg_to_pos", trend_abs=1, var_errors=30, obs=100, seed=56789)
    save_data(sample_5, produces["fifth"])
