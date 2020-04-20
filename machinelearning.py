
#I created this file to try to predict which is the iris flower species by taking into account its features mesaurements

#I first import sklearn library

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split#I imported the model from library
from sklearn.neighbors import KNeighborsClassifier#This model is going to allow us to use K nearest neighbors algorithm 
import numpy as np 

#import matplotlib.pyplot as plt 

iris= load_iris()

#print( iris.keys())#Whis this option I am showing the keys stored as dictionary 

#print(iris)

#Then in order to separate the 4 features ( sepal length, sepal width, petal length and petal width )we create variables for each of them

features = iris.data.T

sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
petal_width = features[3]

sepal_length_label = iris.feature_names[0]
sepal_width_label =iris.feature_names[1]
petal_length_label = iris.feature_names[2]
petal_width_label = iris.feature_names[3]

#Scatter plot 1 creation:

#plt.scatter(sepal_length, sepal_width, c=iris.target)
#plt.xlabel(sepal_length_label)
#plt.ylabel(sepal_width_label)
#plt.title("Sepal length & sepal width correlation")
#plt.show()

#Scatter plot 2 creation:

#plt.scatter(petal_length, petal_width, c=iris.target)
#plt.xlabel(petal_length_label)
#plt.ylabel(petal_width_label)
#plt.title("Petal length & petal width correlation")
#plt.legend()
#plt.show()

#In order to split the data into 25% ( for test)and 75% we use the following
#functionality that sklearn provides:
#here we select data as we want to split the data and also target as we want
#predict which species the flower belongs to ( specified as target in this library).

X_train, X_test, y_train, y_test = train_test_split(iris["data"],iris["target"])
knn= KNeighborsClassifier(n_neighbors=1) #we created variable for Kneighbors classifier function and in this case 1 as the closest neighbor to be considered

knn.fit(X_train, y_train)#Then we add to our fit function training data and training data from our target

#Now we are ready to run this model, lets enter a sample for a new specimen and 
#see in which species will fir according to this model:

X_new = np.array([[0.3,1.0,3.5,6.0]]) #enter an array of float values for each flower part

#To predict considering this array we define a variable for the prediction and
#use function predict: 

#prediction = knn.predict(X_new)
#print( prediction) 

#The prediction function returns one of the three values 
#  assigned to each of the three iris species:

#[0] for setosa
#[1]for versicolor
#[2]for virginica

print(knn.score(X_test, y_test))