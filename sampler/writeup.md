### Problem
Efficient generation of valid spaces in N-dimensional space within non-linear constraints

### Approach
A Latin hypercube (Quasi- Monte Carlo) is a commonly used safe approach used for large samples of high dimensional spaces.

Randomise vector generation using qmc.LatinHypercube() optimization with the given dimensions.
Apply different constraints and append only the satisfactory vectors to the list of vectors.
Repeat steps 1 and 2 until you get the number of results needed.

The advantage is each univariate marginal distribution is stratified.

Performance: The execution time is 5 seconds for 2 dimensions

### Instructions & Installations
The project is written purely in python following the commonly used structure. 
Modules LHSampling contains the main code 
Modules tests contain the example input files
Modules sampler contains the output text file
setup.py should be installed for cross referencing modules
Install the packages in requirements.txt
Run the below script to get the results written into .\sampler\output.txt
### This is example format
    python <samplingscipt> <input file>  <output file> <n_reults> 
### This is example command line 
    python LHSampling\\output.py "tests\\mixture.txt" "sampler\\output.txt" 1000  

