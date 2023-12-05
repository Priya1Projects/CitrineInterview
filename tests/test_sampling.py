# test_sampling.py
import unittest

import sys

from  LHSampling.sampling import sample
from  LHSampling.constraints import Constraint
from unittest.mock import Mock

class TestSampling(unittest.TestCase):
    
    # Create a mock constraint file for testing
        with open("test_example.txt", "w") as f:
            f.write("2\n")  # Replace with actual constraint data
            f.write("0.0 0.0\n")  # Replace with actual constraint data
            f.write("# Simple 3-component mixture\n")  # Replace with actual constraint data
            f.write("1.0 - x[0] - x[1] >= 0.0\n")  # Replace with actual constraint data
        instance = Constraint("test_example.txt")
        result = sample(n=5) 
        print(result)
        # bounds= Constraint("test_example.txt")
        # result = sample(n=5)  # Assuming the second parameter is the path to the constraint file

        # Add your assertions based on the expected behavior of the sample function
        #self.assertIsInstance(result, list)
        # Add more assertions based on the specific behavior you expect

if __name__ == '__main__':
    unittest.main()
