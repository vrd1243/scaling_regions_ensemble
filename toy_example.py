#!/bin/python 
import numpy as np
import pylab as pl
from random import randint
import numpy as np
from pytisean import tiseanio
from matplotlib import pyplot as plt
from curvature import *
from subprocess import call
import pandas as pd
import os
from scipy.stats import gaussian_kde
print(os.getcwd())
from scipy import constants 
import scipy
from scipy.stats import powerlaw as scipypowerlaw

output_dir = 'toy/'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

k = 10
m = 5

x = np.arange(0,10,0.05)
y = np.zeros(x.shape)
print(x.shape)

print(x[10])
print(x[-10])
y[:20] = 0
y[20:-20] = m*(x[20:-20] - x[20])
y[-20:] = y[-21]

#y[x.shape[0]//clip:] = m*x[x.shape[0]//clip:] + (y[x.shape[0]//clip] - m*x[x.shape[0]//clip])
#y += k*np.exp(-0.5*x)*np.sin(5*x)
y += k*np.exp(-0.5*x)*np.sin(5*x)
#y += k*np.exp(-0.8*x)*np.sin(5*x)

#yhat = 1 / (x) + .1*500*np.cos(500*x)

region = np.zeros((x.shape[0],2))
region[:,0] = x
region[:,1] = y

region = region[::2,:]
np.savetxt('toy_example.txt', region)
print(region.shape)

plt.figure(figsize=(8,6), dpi=300)
plt.plot(region[:,0],region[:,1],'.', ms=3)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(output_dir + '/toy_scaling_region.png')