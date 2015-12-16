'''
Created on Dec 17, 2015

@author: alexander ostrikov
'''

from numpy.testing import *
import pymc as pm
from pymc.pandas_utils import mcmc_traces_to_dataframe
import pandas as pd

# test extract mcmc traces to dataframe

class test_pandas_utils(TestCase):

    def get_model(self, n=1):
        u = pm.Uniform('u1', 0, 1, size=n)
        b = pm.Bernoulli("b1", u, size=n)

        model = pm.Model([u, b])
        mcmc = pm.MCMC(model)
        mcmc.sample(100)
        return mcmc


    def test_size1(self):
        mcmc = self.get_model(1)
        assert type(mcmc_traces_to_dataframe(mcmc)) is pd.DataFrame

    def test_size2(self):
        mcmc = self.get_model(2)
        assert type(mcmc_traces_to_dataframe(mcmc)) is pd.DataFrame





