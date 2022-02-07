# First code attempt to generate the data we later on use in the experiment on model persuasion


from scipy import randn


# February 7, 2022: At this stage only pseudo-code to save ideas of how this might look like

# Set-up:
# model_space = list with all possible models
# model_prior = probability distribution over the model space
# 

# Example:
# Consider venture capital investment game from Schwartzstein Sunderam (2021):
# Entrepreneur has success probability p in (0,1) that can be redrawn up to once in t in {1,...,9}
# periods. 
# model of the game: When was probability redrawn.
# model prior (e.g.): uniform over 1, ..., 9.
# parameter prior (required?): uniform over (0,1).
# 1. Generation
# Draw (or specify) model. 
# draw parameter's of the model 
# generate data for successes and failures
# 2. Analytics and estimation
# 
# estimate likelihood about observing model, given parameter prior (?) - check again here.
# -> this corresponds to the naive solution for responders in Schwartzstein Sunderam (2021)
# 


# generate inputs function.



def generate_data():
    shocks = zeros(0,1)