# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

#print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

num_list = [0,1,2,3,4,5,6,7,8]
num_set = mean_var_std.calculate(num_list)

for key, val in num_set.items():
  print (key, val)

# Run unit tests automatically
main(module='test_module', exit=False)