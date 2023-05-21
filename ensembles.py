import numpy as np
from pytisean import tiseanio
from matplotlib import pyplot as plt
from curvature import *
from subprocess import call
import pandas as pd
import os

    
def plot_d2(d2,dims, filename, limits, start_dim=1):
    
    data_per_dim = int(d2.shape[0] / dims)
    plt.figure(figsize=(12,8), dpi=300)
    for dim in range(start_dim,dims+1):
        
        idx = (np.where(np.logical_and(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0] >= limits[0],
                            d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0] < limits[1])))
        
        [p, COV] = np.polyfit(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0][idx], 
                 d2[(dim-1)* data_per_dim:(dim * data_per_dim),1][idx], deg=1, cov=True)
        
        plt.plot(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0], 
                 d2[(dim-1)* data_per_dim:(dim * data_per_dim),1], '.', 
                 #label=r'm=%d, d2=%.2f $\pm$ %.2f' % (dim, p[0], np.sqrt(COV[0][0])))
                 label=r'm=%d, d2=%.2f' % (dim, p[0]))

        #x_coord = np.arange(limits[0],limits[1],0.1)
        #y_coord = x_coord * p[0] + p[1]
        
        #plt.plot(x_coord, y_coord, color='black')
    plt.axvline(x=limits[0], color='black')
    plt.axvline(x=limits[1], color='black')
    
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(r'log ($\epsilon$)', fontsize=20)
    plt.ylabel(r'log (C($\epsilon$))', fontsize=20)    
    plt.legend(prop={'size': 16})
    plt.savefig(filename)
    print("Saving as ", filename)
    plt.show()
    
    
def fit_slopes(d2, dims, limits):
    data_per_dim = int(d2.shape[0] / dims)
    print(limits)
    for dim in range(1,dims+1):
        
        idx = (np.where(np.logical_and(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0] >= limits[0],
                            d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0] < limits[1])))
        
        [p, COV] = np.polyfit(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0][idx], 
                 d2[(dim-1)* data_per_dim:(dim * data_per_dim),1][idx], deg=1, cov=True)
        print(r'embedding dim={}, correlation dimension={}+/-{}'.format(dim, p[0], np.sqrt(COV[0][0])))
        

def generate_individual_ensembles_ordered_fixed(d2, limits, lpower = 0, epower = 1, min_points = 10):
    
    idx = np.where(np.logical_and(d2[:,0] >= limits[0], d2[:,0] < limits[1]))[0]
    
    lhs_arr = []
    rhs_arr = []
    slope = []
    error = []
    weights = []
    
    count = 0
    for lhs_idx in range(idx.shape[0] - min_points):
        for rhs_idx in range(lhs_idx+min_points, idx.shape[0]):
            
            lhs = idx[lhs_idx]
            rhs = idx[rhs_idx]

            [p, e, _, _, _] = np.polyfit(d2[:,0][lhs:rhs], 
                     d2[:,1][lhs:rhs], deg=1, full=True)
            
            # The 1e-10 is an epsilon to avoid divide by 0.
            fit_error = 1e-10 + np.sqrt((e[0]) / (rhs_idx - lhs_idx - 1))
            fit_length = np.sqrt((d2[:,0][rhs] - d2[:,0][lhs]) ** 2 + (p[0]*(d2[:,0][rhs] - d2[:,0][lhs])) ** 2) 
            
            lhs_arr.append(lhs)
            rhs_arr.append(rhs)        
            slope.append(p[0])
            error.append(fit_error)
            weights.append((fit_length ** lpower)/(fit_error ** epower))
            count += 1
    #print(len(lhs_arr))
        
    return [np.array(lhs_arr), np.array(rhs_arr), np.array(slope), np.array(error), np.array(weights)] 

def plot_d2_with_slopes(d2,dims, filename, limits, start_dim=1):
    
    data_per_dim = int(d2.shape[0] / dims)
    plt.figure(figsize=(12,8), dpi=300)
    for dim in range(start_dim,dims+1):
        
        idx = (np.where(np.logical_and(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0] >= limits[0],
                            d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0] < limits[1])))
        
        [p, COV] = np.polyfit(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0][idx], 
                 d2[(dim-1)* data_per_dim:(dim * data_per_dim),1][idx], deg=1, cov=True)
        
        plt.plot(d2[(dim-1)* (data_per_dim):(dim * data_per_dim),0], 
                 d2[(dim-1)* data_per_dim:(dim * data_per_dim),1], '.', 
                 label=r'm=%d, d2=%.2f' % (dim, p[0]))
                 #label=r'm=%d, d2=%.2f $\pm$ %.2f' % (dim, p[0], np.sqrt(COV[0][0])))
       
        x_coord = np.arange(limits[0],limits[1],0.1)
        y_coord = x_coord * p[0] + p[1]
        print(dim, p[0])
        
        #plt.plot(x_coord, y_coord, color='black')

    plt.axvline(x=limits[0], color='black', markersize=.01)
    plt.axvline(x=limits[1], color='black', markersize=.01)
        
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(r'log ($\epsilon$)', fontsize=20)
    plt.ylabel(r'log (C($\epsilon$))', fontsize=20)    
    plt.legend(prop={'size': 16})
    plt.savefig(filename)
    plt.show()
