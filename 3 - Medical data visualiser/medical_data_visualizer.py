import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Computing BMI - We calculate their BMI by dividing their weight in kilograms by the square of their height in meters.  
height_squared = (df['height'] / 100) ** 2
bmi_values = df['weight'] / height_squared

# create a list to populate values
bmi = []

# loop through the tuple and add 0s or 1s to bmi list accordingly
for row, bmi_val in bmi_values.items():
  if bmi_val > 25:
    bmi.append(1)
  else:
    bmi.append(0)

# Add 'overweight' column
df['overweight'] = pd.Series(bmi)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

# We now create 2 new lists to hold new normalised values. Then loop through each row and append values accordingly.
cholesterol_new, gluc_new = [], []

# loop through the dataframe and add 0s or 1s to new lists accordingly
for index, data in df[['cholesterol', 'gluc']].iterrows():
  cholesterol_new.append(0) if data['cholesterol'] == 1 else cholesterol_new.append(1)
  gluc_new.append(0) if data['gluc'] == 1 else gluc_new.append(1)

# Assign new list for cholesterol and gluc as a series to dataframe
df['cholesterol'] = pd.Series(cholesterol_new)
df['gluc'] = pd.Series(gluc_new)
  

# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = df[['cardio', 'active', 'alco', 'cholesterol', 'gluc','overweight', 'smoke']]

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.melt(id_vars='cardio')

  # Draw the catplot with 'sns.catplot()'
  
  sns.set(style='white')
  plt1 = sns.catplot(data=df_cat, kind='count', x='variable', y=None, hue='value', col='cardio', errorbar=None)

  # set axis labels
  plt1.set_axis_labels(x_var='variable', y_var='total')

  # Get the figure for the output
  fig = plt1.figure

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # data cleaning
  # Select rows to discard if diastolic pressure is MORE THAN systolic.
  to_discard1 = df[df['ap_lo'] > df['ap_hi']]['id']
  
  # Select rows to discard if height is (LOWER THAN 2.5th percentile) or (MORE THAN 97.5th percentile).
  to_discard2 = df[ (df['height'] < df['height'].quantile(0.025)) | (df['height'] > df['height'].quantile(0.975)) ]['id']
  
  # Select rows to discard if weight is (LOWER THAN 2.5th percentile) or (MORE THAN 97.5th percentile)
  to_discard3  = df[ (df['weight'] < df['weight'].quantile(0.025)) | (df['weight'] > df['weight'].quantile(0.975)) ]['id']

  # Concat the dfs to discard
  id_set_to_discard = pd.concat([to_discard1, to_discard2, to_discard3])
  
  # Drop duplicate rows
  id_set_to_discard.drop_duplicates(inplace=True)

  
  # Assign cleaned data
  df_heat = df[~(df['id'].isin(id_set_to_discard))]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr))


  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(10, 10))
  
  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr, cmap='magma', annot=True, fmt=".1f", mask=mask, cbar_kws={"shrink": .6})

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
