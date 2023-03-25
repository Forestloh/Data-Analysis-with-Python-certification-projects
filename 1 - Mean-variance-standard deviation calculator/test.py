import numpy as np
import statistics as stats

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

calc = np.array([float(x) for x in list]).reshape(3, 3)

print(calc[0])
print(stats.variance(calc[0]))