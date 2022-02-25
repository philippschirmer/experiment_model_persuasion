# TODO: function that based on model space and model prior on that space, draws a realized model
# could be just a random choice function?

def gen_random_model(model_space, model_prior):
    '''
    Input: Model_space 1D array
        model prior: 1D array, probability distribution w/ standard attributes.


    Output: realized model choice (scalar?)
    '''

    # Generate trend shift (first up, then down, or vice versa)

    trend = np.array([0,0])

    draw_rand_bin = rng.binomial(1, p, size=None)

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





    pass