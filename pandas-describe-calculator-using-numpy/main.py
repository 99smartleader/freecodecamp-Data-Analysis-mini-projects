# This main function is for compiling both function of what to test and with which application for compatibility.
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)
