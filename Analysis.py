
#Ainara Ruiz Castillo
#First I am investigating ways to start the first small task related to this project and this code.
# The final program is to be called analysis.py - I am explorating here the first piece of code .
#The purpose of this piece of code is to output a summary of each variable to a single text file.
# Took this approach as reference: https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#Took as reference in how to work with CSV files: https://realpython.com/python-csv/
import pandas as pd #Imported pandas to load the data and then to orgaise the data I loaded it using panda library
import matplotlib.pyplot as plt
import numpy as numpy
import seaborn as sns

df = pd.read_csv('irisdataset.csv')



# Then took some of the commands from my reference and chose to use command describe() in order to get a summary of the main points that can be observed
#in the data and then output this summary to a text file as requested in project's brief.
# I am using Pandas library
#Describe fucntion in order to do this and assigning a variable to the result of this function:

Summary = df.describe()


print( Summary)


with open('Summary.txt', 'w') as outfile: #Then the program created a text file and outputs results of this describe command 
    #to the new created text file.
    print >>outfile, 'Summary of variables from iris dataset: \n'  ,Summary                                                                                                                        , Summary

#For the second part of the exercise I am creating a histogram for each variable and save to png file.

#I define dimensions of the plot grid:
plt.subplots(figsize=None)
fig_dims = (6, 4)

#Histogram 1 - Sepal Length and iris species:

sns.barplot(x="Species", y= "SepalLength" ,data=df) #Asign data to axis
plt.title("Sepal length within iris flower species ", fontsize =15)# I add title and legend 
plt.ylabel ("Sepal length", fontsize= 10)
plt.xlabel ("Species")
plt.legend(loc="lower left")

plt.show()#Use this command to populate the graph
plt.savefig("SepalLength.png")

#Histogram 2 - Sepal Width and iris species:

fig_dims = (6, 4)
sns.barplot(x="Species", y= "SepalWidth" ,data=df) #Asign data to axis
plt.title("Sepal width within iris flower species ", fontsize =15)# I add title and legend 
plt.ylabel ("Sepal width", fontsize= 10)
plt.xlabel ("Species")
plt.legend(loc="lower left")

plt.show()#Use this command to populate the graph

#Histogram 3 - Petal Length and iris species:

fig_dims = (6, 4)
sns.barplot(x="Species", y= "PetalLength" ,data=df) #Asign data to axis
plt.title("Petal Length within iris flower species ", fontsize =15)# I add title and legend 
plt.ylabel ("Petal length", fontsize= 10)
plt.xlabel ("Species")
plt.legend(loc="lower left")
plt.show()


#Histogram 4 - Petal Width and iris species:

fig_dims = (6, 4)
sns.barplot(x="Species", y= "PetalWidth" ,data=df) #Asign data to axis
plt.title("Petal Width within iris flower species ", fontsize =15)# I add title and legend 
plt.ylabel ("Petal width", fontsize= 10)
plt.xlabel ("Species")
plt.legend(loc="lower left")
plt.show()

#Third part , scatterplots need to be output:

#Scatterplot 1 - Sepal Lenght vs Sepal Width

setosa=df.loc[df["Species"]=="Iris-setosa"]
virginica=df.loc[df["Species"]=="Iris-virginica"]
versicolor=df.loc[df["Species"]=="Iris-versicolor"]

sns.relplot(x="SepalLength", y="SepalWidth",hue="Species", data=df)
plt.show()

#Scatterplot 2 - Petal Lenght vs Petal Width

setosa=df.loc[df["Species"]=="Iris-setosa"]
virginica=df.loc[df["Species"]=="Iris-virginica"]
versicolor=df.loc[df["Species"]=="Iris-versicolor"]

sns.relplot(x="PetalLength", y="PetalWidth",hue="Species", data=df)
plt.show()


    


