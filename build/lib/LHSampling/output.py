import numpy as np
import sys
from  LHSampling.sampling import sample
# ['example.py', 'input', 'output', 'n_res']
cliargs= sys.argv
valid_points = sample(5,  "tests\\mixture.txt") # sample(cliargs[3], cliargs[1])
for p in valid_points:
    strop = " ".join(map(str, p))
    with open(cliargs[2], "w") as f:
            f.write(strop+"\n")  
            
