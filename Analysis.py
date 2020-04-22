
#Student name: Ainara Ruiz
#This is my final project for the module Programing & Scripting 
#With this program I want to perform an analysis of the iris data set using Python.

#The next comments explain a little bit about my process to develop this code and instructions in how to run it. 
#You can also find more information related to this code and the iris dataset in my README.md which is  available in this repository.

#The first task that this programs performs is to to output a summary of each variable (Sepal Length, Sepal Width, Petal Length and Petal Width)
#  to a single text file.
# I took this approach as reference:[Iris dataset analysis approach] (https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)  
#Took as reference in how to work with CSV files: https://realpython.com/python-csv/

import pandas as pd #Imported pandas to load the data and add analysis tools
import matplotlib.pyplot as plt #Imported this libary for plotting
import seaborn as sns #Imported Seaborn for extra dimension in my graphic.

df = pd.read_csv('irisdataset.csv') #We load our iris data set file to work with it.

# Then took some of the commands from my reference and chose to use command describe() in order to get a summary of the main points that can be observed
#in the data and then output this summary to a text file as requested in project's brief.
# I am using Pandas library describe function in order to do this and assigning a variable to the result of this function:

Summary = df.describe()


with open('Summary1.txt', 'w') as outfile: #Then the program created a text file and outputs results of this describe command 
    #to the new created text file.
    print >>outfile, 'Summary of variables from iris dataset: \n'  ,Summary                                                                                                                  , Summary

#For the second part of the exercise I am creating a histogram for each variable and save to png file.
#As it looks cleaner I decided to make a histogram that contains all variables in a single graph, so it wil be saved into a single
#file:


f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot( df["SepalLength"] , color="darkgreen", ax=axes[0, 0])#Plotting sepal length 
sns.distplot( df["SepalWidth"] , color="purple", ax=axes[0, 1]) #Plotting sepal width 
sns.distplot( df["PetalLength"] , color="limegreen", ax=axes[1, 0]) #Plotting petal length graph
sns.distplot( df["PetalWidth"] , color="orchid", ax=axes[1, 1]) #Plotting petal width graph
plt.savefig("Histogram.png") #This command saves the graphic as a png file which is available in repository /images/Histogram.png


#As an addition I am adding also histograms for the variables within every species of iris flower, using Facetgrid function:
#This way is easier to see the differences in every variable size range plus how it differs between the 3 types of iris flowers.

sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"SepalLength").add_legend()
plt.savefig("Histsepallength.png")# running this command we save every graph into a png file/ files available in repository /images.
sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"SepalWidth").add_legend()
plt.savefig("Histsepalwidth.png")
sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"PetalLength").add_legend()
plt.savefig("Histpetallength.png")
sns.FacetGrid(df,hue="Species",size=3).map(sns.distplot,"PetalWidth").add_legend()
plt.savefig("Histpetalwidth.png")


#For the third section of this program, we create scatter plots that will be printed in our screen
#we can then save them if we wish. I have added this scatter plots to my README.md file in repository.

#Scatterplot 1 - *Sepal Lenght vs Sepal Width*

#First I separate the species to be used as categories in scatter plots.

setosa=df.loc[df["Species"]=="Iris-setosa"]
virginica=df.loc[df["Species"]=="Iris-virginica"]
versicolor=df.loc[df["Species"]=="Iris-versicolor"]


#Then I specify my x and y axis contents which will be two variables for each scatter plot. I separate species using color so it is easy to see
#the differences between them. 
sns.relplot(x="SepalLength", y="SepalWidth",hue="Species", data=df) #Here we adjust the features of the scatter plot.
plt.title("Sepal length & sepal width (cm)",y=0.95)# Adding title and placement of the title.

plt.show() #running the scatter plot

#Scatterplot 2 - *Petal Lenght vs Petal Width*

sns.relplot(x="PetalLength", y="PetalWidth",hue="Species", data=df)
plt.title("Petal length & petal width (cm)", y=0.95)

plt.show()



print( "Thanks for using my code, please find some extra information and extra machine learning prediction model in README file here : https://github.com/Ainara12/Pands-project")

