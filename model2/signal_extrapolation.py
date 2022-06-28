import numpy as np

def extrapolate_index_return(param, t, n, signals):
    if param['type'] == 'Expert Model':
        signals["index_return"] = param["lambda"] * signals["basket_return"] +\
        (1 - param["lambda"]) * np.random.normal(param["mu"], param["std"], (t,n))
    elif param['type'] == 'Normal Fitted':
        signals["index_return"] = np.random.normal(param["mu"], param["std"], (t,n))
    else:
        raise NotImplementedError
    
def extrapolate_basket_return(param, t, n, signals):
    if param['type'] == 'Expert Model':
        signals["basket_return"] = np.random.normal(param["mu"], param["std"], (t,n))
    elif param['type'] == 'Normal Fitted':
        signals["basket_return"] = np.random.normal(param["mu"], param["std"], (t,n))
    else:
        raise NotImplementedError