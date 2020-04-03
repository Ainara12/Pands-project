
#Ainara Ruiz Castillo
#First I am investigating ways to start the first small task related to this project and this code.
# The final program is to be called analysis.py - I am explorating here the first piece of code .
#The purpose of this piece of code is to output a summary of each variable to a single text file.
# Took this approach as reference: https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#Took as reference in how to work with CSV files: https://realpython.com/python-csv/
import pandas #Imported pandas to load the data and then to orgaise the data I loaded it using panda library


dataset = pandas.read_csv('irisdataset.csv')

print (dataset.describe()) #and we print our data to see how it looks

# Then took some of the commands from my reference and schose to use dataset.describe() in order to get a summary of the main points that can be observed
#in the data. 
#Using this I am creating a Function that we can use to see this data in general for the set.









    


