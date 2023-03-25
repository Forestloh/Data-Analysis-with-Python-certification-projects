import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  fig, ax = plt.subplots(figsize=(9, 4))
  
  ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], label = 'data')

  # Calc regression 1
  reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], alternative='two-sided')
  
  # Find earliest year value in df
  yr_min = df['Year'].min()
  
  # create to store year values up till 2050
  years = pd.Series([yr for yr in range(yr_min, 2051)])
  
  # Create first line of best fit
  ax.plot(years, reg.intercept + reg.slope*years,color='red', label = 'reg line: yr 1880 to 2050')
    

  
  # Get data from year 2000
  df2 = df[df['Year']>= 2000]

  # Calc regression 2
  reg2 = linregress(x=df2['Year'], y=df2['CSIRO Adjusted Sea Level'], alternative='two-sided')

  # Create list to store year values up till 2050
  years2 = pd.Series([yr for yr in range(2000, 2051)])

  # Create second line of best fit
  ax.plot(years2, reg2.intercept + reg2.slope*years2,color='purple', label = 'reg line: yr 2000 to 2050')


  # Add labels and title, and show legend
  ax.set(title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)')
  ax.legend()

  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()