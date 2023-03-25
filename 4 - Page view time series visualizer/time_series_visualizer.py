import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[ (df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975)) ]


def draw_line_plot():
  # Draw line plot using matplotlib (change figure size)
  fig, ax = plt.subplots(figsize=(9, 4))
  
  # plot x axis, y axis
  ax.plot(df.index, df['value'], color='r', linewidth=0.6)
  
  # set title, x and y labels
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')  

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  
  # We first create a variable to hold datetime (from index)
  datetime = pd.DataFrame(df_bar.index)

  # Populate data
  df_bar['year'] = list(datetime['date'].dt.year)
  df_bar['month'] = list(datetime['date'].dt.month)

  # pivot the table data
  df_pivot = df_bar.pivot_table(values='value', index='year', columns='month', aggfunc=np.mean)

  # Draw bar plot
  # setting legend labels
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  
  # plot and return an axis object as 'ax_bar'
  ax_bar = df_pivot.plot.bar(figsize=(9, 5))
  ax_bar.set(title='Months', xlabel='Years', ylabel='Average Page Views')
  ax_bar.legend(months)

  fig = ax_bar.figure
  
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  # create a figure with 2 sub plots
  fig, [ax1, ax2] = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
  
  # Plotting first axis (left chart)
  sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
  ax1.set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
  
  
  # Plotting second axis (right chart)
  months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
  
  sns.boxplot(data=df_box, x='month', y='value', order=months_order, ax=ax2)
  ax2.set(title='Month-wise Box Plot (Seasonality)',  xlabel='Month', ylabel = 'Page Views')
  
  fig.tight_layout()

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
