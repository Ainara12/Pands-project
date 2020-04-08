
#To create histogram I followed these steps from seaborn mainpage: https://seaborn.pydata.org/examples/faceted_histogram.html
#I import the libraries we are going to use to do so. 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#First I think which question i want to answer. I want to group here the measurements of the flower parts separated by species 
# and see the ranges they move along. 

#First I extract data from the dataset and definded df

df=pd.read_csv("irisdataset.csv")
#Second I create the histogram settings: style and context and the format data.
sns.set(style='darkgrid', context='paper')
g = sns.FacetGrid(df, col='Species', col_wrap=3, hue='Species', height=9)
# I created map for Sepal length separated by the 3 species being also differentiated by color.
g.map(sns.barplot, 'Species', 'SepalLength');

plt.show()


