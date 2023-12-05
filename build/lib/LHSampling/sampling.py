from scipy.stats import qmc

import os
import sys
import numpy as np
from  LHSampling.constraints import Constraint

def sample(n, fname):
    bounds = Constraint(fname=fname)
    dim = bounds.get_ndim()
    example =bounds.get_example() 
    sample=[]
    valid_points=[]
    # use LHS to randomly choose random vectors and reject if doesnt fall under a valid space by the constraints
    sampler = qmc.LatinHypercube(d=dim)
    while len(valid_points) < n:   
        sample = sampler.random()
        if is_valid_points(sample, bounds):
            valid_points.append(sample)   
    return  valid_points
# bound by constraint 
def get_valid_points(points, constraints):
# Check if the point satisfies all non-linear constraints 
    finalvector=[]    
    points =points.flatten()
    if constraints.apply(x=points):
        finalvector.append(points)  
    return finalvector
def is_valid_points(point, constraints):
# Check if the point satisfies all non-linear constraints 
    point =point.flatten()
    for p in point:
        if constraints.apply(x=point):
            return True
        return False

