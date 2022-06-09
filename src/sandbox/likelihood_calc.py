# Work in progress, Code to calculate likelihoods for the given models
# Goal is to map the model messages into likelihoods and assess which model is the best
# from a "Bayesian" perspective (with uniform prior), as well as which models are better "fitting"
# than the baseline model. 

from sklearn.covariance import log_likelihood
from src.config import BLD, EXP

import pandas as pd
import pytask
import plotly.express as px

import math


def calc_likelihood():
    ''' Inputs:
        Data
        Model class
        Model spec - Int - 

        fitted_params

        Outputs:

        likelihood


    '''

    pass


# Sandbox; Work with existing data

#

def fit_model():
    '''
    Calculate optimal parameters for a given model, e.g. switching point.

    Makes sense to calc params separately from likelihood, as they are also relevant to assess e.g. the prediction of the model.
    
    Inputs:
    data
    model
    variance

    Outputs

    fitted_params

    '''
    pass


# For e.g. model_choice=50, fit two sub models; linear regression optimal? -> yes

# Better: Look at first differences, estimate average increase -- optimal trend estimate?
# 


data= pd.read_csv(BLD / "data/data_1.csv") 



# TODO: Remove set variance, make part of the function
variance = 30

# TODO: Make model choice dynamic, so we can loop over it.
model_choice = 50 

data_1 = data[0:model_choice]
data_2 = data[model_choice : data["Stock price"].size]


# Differentiate series

data_1_diff = data_1

data_1_shifted = data_1
data_1_shifted["Time"] = data_1["Time"] + 1 

# data_1_diff["Stock price change"]= data_1["Stock price"] - data_1_shifted["Stock price"]


for i in range(0,10,1):
    data_1_diff["Stock price change"].iloc[[i]]= data_1["Stock price"].iloc[[i+1]] - data_1["Stock price"].iloc[[i]]

data_test = data_1


data_test["Stock price change"] = data_1["Stock price"].diff()

data_test.drop(0)

mean_test = data_test["Stock price change"].mean()


# TODO: To be adjusted
n=50

n_1 = model_choice

n_2= data_test.len() - model_choice


data_diff_sq = (data_test["Stock price change"] - mean_test) ** 2

# calculating log likelihood

lg_likelihood = - n / 2 * math.log(2 * math.pi) - n/2 * math.log(variance) - 1 / (2 * variance) * data_diff_sq.sum()


# Look at pre-built likelihood calcs


# Formula for calculating the likelihood
# likelihood = (2 * math.pi * variance) ** (- n / 2) 

#* math.exp( - 1 / (2 * variance) * sum(data_test["Stock price change"] - mean_test))

