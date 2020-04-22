
#I created this file to try to predict which is the iris flower species by taking into account its features measurements

#I first import sklearn library which has stored our iris dataset and has the functionalities to make this work

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split#I imported the model from library
from sklearn.neighbors import KNeighborsClassifier#This model is going to allow us to use K nearest neighbors algorithm 
import numpy as np #I also import numpy for our arrays of values
import matplotlib.pyplot as plt #And I import matplotlib for the scatter plots

iris= load_iris()

print( iris.keys()) #Whis this option I am showing the keys stored as dictionary in this libary


#Then in order to separate the 4 features ( sepal length, sepal width, petal length and petal width )I create variables for each of them

features = iris.data.T

sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
petal_width = features[3]

sepal_length_label = iris.feature_names[0]
sepal_width_label =iris.feature_names[1]
petal_length_label = iris.feature_names[2]
petal_width_label = iris.feature_names[3]

#In order to display the scatter plots, run command plt.show()
#Scatter plot 1:

plt.scatter(sepal_length, sepal_width, c=iris.target)
plt.xlabel(sepal_length_label)
plt.ylabel(sepal_width_label)
plt.title("Sepal length & sepal width correlation")
plt.show()

#Scatter plot 2 :

plt.scatter(petal_length, petal_width, c=iris.target)
plt.xlabel(petal_length_label)
plt.ylabel(petal_width_label)
plt.title("Petal length & petal width correlation")
plt.show()

#Prediction model: 

#The first step is to split the data.
# In order to split the data into 25% ( for test)and 75% we use the following
#functionality that sklearn provides:
#here we select data as we want to split data to perform tests and also target to
#predict which species the flower belongs to ( specified as target in this library).

X_train, X_test, y_train, y_test = train_test_split(iris["data"],iris["target"])
knn= KNeighborsClassifier(n_neighbors=1) #we created variable for Kneighbors classifier function and in this case 1 as the closest neighbor to be considered

knn.fit(X_train, y_train)#Then we add to our fit function training data and training data from our target

#Now we are ready to run this model, lets enter a sample for a new specimen and 
#see in which species it will fit according to this model:

X_new = np.array([[5.0,3.0,0.2,0.3]]) #enter an array of float values for each flower part

#To predict considering this array we define a variable for the prediction and
#use function predict: 

prediction = knn.predict(X_new)
print( prediction) 

#The prediction function returns one of the three values 
#  assigned to each of the three iris species:

#[0] for setosa
#[1]for versicolor
#[2]for virginica

#I also added option to test the accuracy of the predictions, I use knn.score function an indicate
# to use the portion of data that we kept for testing. 

print(knn.score(X_test, y_test))

print ('Thanks for using my first attemp of machine learning !')

