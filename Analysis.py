
#Ainara Ruiz Castillo
#First I am investigating ways to start the first small task related to this project and this code.
# The final program is to be called analysis.py - I am explorating here the first piece of code .
#The purpose of this piece of code is to output a summary of each variable to a single text file.
# Took this approach as reference: https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#Took as reference in how to work with CSV files: https://realpython.com/python-csv/

import pandas as pd #Imported pandas to load the data and then to orgaise the data I loaded it using panda library
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('irisdataset.csv')

# Then took some of the commands from my reference and chose to use command describe() in order to get a summary of the main points that can be observed
#in the data and then output this summary to a text file as requested in project's brief.
# I am using Pandas library
#Describe fucntion in order to do this and assigning a variable to the result of this function:

Summary = df.describe()


with open('Summary1.txt', 'w') as outfile: #Then the program created a text file and outputs results of this describe command 
    #to the new created text file.
    print >>outfile, 'Summary of variables from iris dataset: \n'  ,Summary                                                                                                                  , Summary

#For the second part of the exercise I am creating a histogram for each variable and save to png file.
#As it looks cleaner I decided to make a histogram that contains all variables in a single graph, so it wil be saved into a single
#file:


f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot( df["SepalLength"] , color="darkgreen", ax=axes[0, 0])
sns.distplot( df["SepalWidth"] , color="purple", ax=axes[0, 1])
sns.distplot( df["PetalLength"] , color="limegreen", ax=axes[1, 0])
sns.distplot( df["PetalWidth"] , color="orchid", ax=axes[1, 1])
plt.savefig("Histogram.png")

#As an addition I am adding also histograms for the variables within every species of iris flower, using pairplot option:


sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"SepalLength").add_legend()
plt.savefig("Histsepallength.png")
sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"SepalWidth").add_legend()
plt.savefig("Histsepalwidth.png")
sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"PetalLength").add_legend()
plt.savefig("Histpetallength.png")
sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"PetalWidth").add_legend()
plt.savefig("Histpetalwidth.png")


#Third part , scatterplots need to be output:

#Scatterplot 1 - Sepal Lenght vs Sepal Width
#First I separate the species to be used as categories in scatter plots.

setosa=df.loc[df["Species"]=="Iris-setosa"]
virginica=df.loc[df["Species"]=="Iris-virginica"]
versicolor=df.loc[df["Species"]=="Iris-versicolor"]


sns.relplot(x="SepalLength", y="SepalWidth",hue="Species", data=df) #Here we adjust the features of the scatter plot.
plt.title("Sepal length & sepal width (cm)",y=0.95)# Adding title.

plt.show()

#Scatterplot 2 - Petal Lenght vs Petal Width

sns.relplot(x="PetalLength", y="PetalWidth",hue="Species", data=df)
plt.title("Petal length & petal width (cm)", y=0.95)

plt.show()





