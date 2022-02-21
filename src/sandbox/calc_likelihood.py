# TODO / Tentative: write function that for a specified model and parametrization, calculates
# the likelihood of observing the respective data.

# Open question: How to structure this function, can it be kept flexible to allow for different 
# models? Issue there: different models require vastly different likelihood functions that need
# to be worked out first. 
# Maybe better to write indiv likelihood function for each model class (or have this fct.)
# call different subfunctions. 

def calc_likelihood(data, model, params):
    ''' Function that calculates the likelihood of observing the given data, under the specified model.
    
    Inputs: data (1+K)D np.array    - contains dependent variable Y and K features.
            model: string           - prespecified model of which to calc. the likelihood.
            params: 1D np.array     - parameters of model.

     ''' 
    pass