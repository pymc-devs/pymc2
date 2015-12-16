'''
Created on Dec 16, 2015

@author: alexander ostrikov
'''

import pandas as pd
import numpy as np

def mcmc_traces_to_dataframe(mcmc):
    def get_data(trace):
        shape = trace.shape
        if len(shape) == 1:
            return trace
        elif len(shape) == 2 and shape[1] == 1:
            return trace[:, 0]
        elif len(shape) == 2:
            return trace.tolist()
        else:
            return np.NaN

    df1 = pd.DataFrame(data=[get_data(s.trace.gettrace()) for s in mcmc.variables])
    df2 = df1.T
    df2.columns = [s.trace.name for s in mcmc.variables]
    return df2