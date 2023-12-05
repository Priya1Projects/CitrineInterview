import numpy as np
import sys
from  LHSampling.sampling import sample
# ['example.py', 'input', 'output', 'n_res']
cliargs= sys.argv
print(cliargs)
# valid_points = sample(5,  "tests\\mixture.txt") # 
valid_points = sample(int(cliargs[3]), cliargs[1])
# with open("sampler\\output.txt", "w") as f:
with open( cliargs[2], "w") as f:
    for p in valid_points:
        strop= ""
        strop =strop + " ".join(map(str, p.flatten()))
        f.write(strop+"\n")  
            
