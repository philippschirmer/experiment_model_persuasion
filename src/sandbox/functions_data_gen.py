# TODO: function that based on model space and model prior on that space, draws a realized model
# could be just a random choice function?

import numpy as np

obs = 80

model_space = np.arange(1,obs,dtype=int)

model_space.shape

model_prior = np.full(model_space.shape,1/obs)

def gen_random_model(model_space, model_prior):
    '''
    Input: Model_space 1D array
        model prior: 1D array, probability distribution w/ standard attributes.


    Output: trend_shift: scalar, realized model choice.
    '''

    trend_shift = np.random.choice(model_space, size=None, replace=True, p=model_prior)

    trend_shift

    # generate trend vector including shift

    # trend_with_shift = np.full(100,c)
    # for i in range(0,100):
    #     if i <= trend_shift:
    #         trend_with_shift[i] = trend[0]
    #     elif i > trend_shift:
    #         trend_with_shift[i] = trend[1]

    # trend_with_shift

    return trend_shift


gen_random_model(model_space, model_prior)