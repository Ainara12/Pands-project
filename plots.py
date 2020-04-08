#In this document I am creating  a plot with the goal to find correlation between different features from iris flowers and 
#the species they belong to
#First I import the libraries: numpy to organise the data, matplotlib ,seaborn and pandas to organise data and create plots.
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


col=['SepalLength','SepalWidth','PetalLength','PetalWidth','Species']#I define columns and names
df=pd.read_csv("irisdataset.csv",names=col,skiprows=1) #I open the csv file with pandas and add the variables above for names
#Now I can print different 
#print("number of samples from each type") 
#print(df["Species"].value_counts())

#To visualise the data using histograms we do the following:
#divide data into the 3 species of iris flower:

setosa=df.loc[df["Species"]=="Iris-setosa"]
virginica=df.loc[df["Species"]=="Iris-virginica"]
versicolor=df.loc[df["Species"]=="Iris-versicolor"]

sns.relplot(x="SepalLength", y="SepalWidth",hue="Species", data=df)
plt.show()

sns.relplot(x="PetalLength", y= "PetalWidth", hue="Species", data= df)
plt.show()


 