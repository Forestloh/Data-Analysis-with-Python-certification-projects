import numpy as np

def calculate(list):
  # check that list contains exactly 9 elements.
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    # Check all numbers are int / float type 
    for ele in list:
      if type(ele) not in [int, float]:
        raise ValueError('List must contain nine numbers.')

  # convert list input to floats. Then shape to 3 x 3 Numpy array
  np_array = np.array(list).reshape(3, 3)

  # functions
  def get_mean(array):    
    y_axis, x_axis = [], []
    for i in range (3):
      y_axis.append(array[:, i].mean())
      x_axis.append(array[i].mean())
    flattened = array.flatten().mean()
    return [y_axis, x_axis, flattened]

  def get_var(array):
    y_axis, x_axis = [], []
    for i in range (3):
      y_axis.append(np.var(array[:, i]))
      x_axis.append(np.var(array[i]))
    flattened = np.var(array.flatten())
    return [y_axis, x_axis, flattened]

  def get_sd(array):
    y_axis, x_axis = [], []
    for i in range (3):
      y_axis.append(np.std(array[:, i]))
      x_axis.append(np.std(array[i]))
    flattened = np.std(array.flatten())
    return [y_axis, x_axis, flattened]

  def get_max(array):
    y_axis, x_axis = [], []
    for i in range (3):
      y_axis.append(array[:, i].max())
      x_axis.append(array[i].max())
    flattened = array.flatten().max()
    return [y_axis, x_axis, flattened]

  def get_min(array):
    y_axis, x_axis = [], []
    for i in range (3):
      y_axis.append(array[:, i].min())
      x_axis.append(array[i].min())
    flattened = array.flatten().min()
    return [y_axis, x_axis, flattened]


  def get_sum(array):
    y_axis, x_axis = [], []
    for i in range (3):
      y_axis.append(array[:, i].sum())
      x_axis.append(array[i].sum())
    flattened = array.flatten().sum()
    return [y_axis, x_axis, flattened]

  # Create dictionary
  calculations = dict()
  calculations['mean'] = get_mean(np_array)
  calculations['variance'] = get_var(np_array)
  calculations['standard deviation'] = get_sd(np_array)
  calculations['max'] = get_max(np_array)
  calculations['min'] = get_min(np_array)
  calculations['sum'] = get_sum(np_array)
  
  return calculations
