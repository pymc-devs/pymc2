"""
This example uses Markov chain Monte Carlo to sample from the posterior of the PyMC probability model declared in salmon_sampler.py, and visualizes the output as maps.

============================================================
= WARNING: This example is very computationally demanding! =
============================================================
I have set the map resolutions to give nice-looking results, but I am using
an 8-core, 3.0GHz Apple Mac Pro with 8GB of RAM and with environment variable 
OMP_NUM_THREADS set to 8. If you are using a less powerful machine, you may 
want to change the 'm' parameters
below.

The MCMC takes several hours on my machine. To make it run faster, thin the dataset.
"""

from salmon_sampler import *
from pylab import *

# salmon = SalmonSampler('chum')
# salmon = SalmonSampler('sockeye')
salmon = SalmonSampler('pink')


# Really takes 100k
iter=100000
thin=iter/2000
burn=50000
# salmon.sample(iter=iter,burn=burn,thin=thin)
salmon.isample(iter=iter,burn=burn,thin=thin)


close('all')
salmon.plot_SR()
salmon.plot_traces()
