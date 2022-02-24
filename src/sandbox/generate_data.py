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
    pass