

# Programming and Scripting Project 2020 

This document contains a summary of my efforts to complete the final project for the Programming and Scripting module, along with observations  about the dataset and the references used to complete it. 

## Project Abstract 

My goal with this project is to analyze the Fisher’s Iris data set and reach to a set of conclusions using Python. 
One of the main conclusions I want to reach is to confirm if it is  possible to identify the three different species of iris flower just by the size of their features using the plotting tools that Python offers along with a little experimentation at the end of this assignment in which I tried this using *sklearn library*.

[Iris Data set in CSV format downloaded from this link](https://gist.github.com/netj/8836201)  

## Summary of dataset  

**1.History:**

This dataset was created in 1936 by the British statistician and biologist Ronald Fisher.
The set is composed of a total of 150 instances, 50 for each of the 3 species which refer to a type of iris plant (iris setosa, iris versicolor & iris virginica). 

![](images/irissetosa.jpg)  
![](images/irisversicolor.jpg)  
![](images/irisvirginica.jpg)  



For those who are not familiar with the two main concepts of this dataset, see definitions below:

*Sepal: This is one of the parts of the flower which forms the outer part surrounding the petals.*
*Petal: This part of the flower consists of the brightly coloured parts that together will form most of the flower.* 

**2.Data set variables:** 

The way the data is organised is as follows:  
There are four columns with the different flower parts measures in centimetres and the fifth column is the species of the flower observed.
 
*Variables:*  

SepalLength (This is the length of the sepal of flower in cm)
SepalWidth (This is the width of the sepal of the flower in cm)
PetalLength (This is the length of the petal of the flower in cm)
PetalWidth (This is the width of the petal of the flower in cm)
Species (Species name)

## Project ##  

**1. Project process:**    

In order to create this project I have divided my work into smaller separate tasks until I was ready to join all and create the final version of ["Analysis.py"](https://github.com/Ainara12/Pands-project/blob/master/Analysis.py). I have also planned my tasks using Github planning and Milestone tools as you can see in this repository.
My approach was to split these small tasks into different stages with a date to be completed, and to then proceed with the next phase or stage. I created 3 phases with 3 specific milestones. See details of these phases below for reference:  

1.	Phase 1. Documentation  
2.	Phase 2. I created separate programs to achieve the 3 main tasks and I observe other author’s analysis of this dataset as documented in references section.    
3.	Phase 3. I put together the tasks to create Analysis.py and added my observations and information to this document.  

**2.Summary statistics table:**  

The first task was to organise the data and have a look at its distribution. I used command df.describe() to see a Summary statistics table to show what is the mean, std dev, minimum and maximum values within the different variables etc. The generated document containing this summary can be found in this repository as ["Summary.txt"](https://github.com/Ainara12/Pands-project/blob/master/Summary.txt). I have also included here an image for reference:  

![](images/statisticstable.JPG)  
 
Looking at these values, we can see that there is an extensive range of sepal and petal sizes. Our goal with this analysis is to determine if is possible to classify the three iris species by their components measurements.


**3.Histograms:**  

Following the procedure and guidelines provided, the second part of the tasks that Analysis.py performs is saving a histogram of every variable into a png file.  
A histogram is a type of graph used to represent the data distribution by using bins along the range of the data and then drawing bars to show the number of observations that fall in each bin. For the creation of these histograms I have used *matplotlib* , *pandas* and *seaborn* libraries. I have selected *seaborn* libraries to give some more dimension and colour to my plots.  

In order to move along within the Analysis you just need to get to the histogram section and create the file, for this I used command savefig and add name of the png file. The png file is added to this repository in the images folder [(histogram)](https://github.com/Ainara12/Pands-project/blob/master/images/Histogram.png) as reference.  
Instead of creating a individual file for every histogram I have added the four histograms to a single graphic which will be saved as a single png by the program.

*4 variables histogram*

![](images/Histogram.png)  

 
With the histogram we can see the range of species-secific values for each of the four variables ( sepal length, sepal width, petal length and petal width).  

I have also added a histogram that shows the variables and species category in the same plot , as a reference to see the difference in distribution within the three types of iris flowers.  

![](images/Histsepallength.png)  
![](images/Histsepalwidth.png)  
![](images/Histpetallength.png)  
![](images/Histpetalwidth.png)  


Observing these histograms we can already see at first glance how some of the species have very different ranges of values in some of their attributes, for example setosa in relation to the other two types of iris flowers, seems to have smaller petals.  

**4.Scatter plots:**  

After the histogram section we move down to the scatter plot representation of this data. I have created two scatter plots combining two variables ( sepal length & sepal width) and (petal length & petal width) and separating by species using color. Scatter plots are a useful type of graphic when we want to see the relation between two variables.(You can access scatter plots through these links:[ Scatter plot 1 ](https://github.com/Ainara12/Pands-project/blob/master/images/scatterplot1.png)[Scatter plot 2](https://github.com/Ainara12/Pands-project/blob/master/images/scatterplot2.png)).
 
Observing the first scatter plot, there seems to be a clear difference between the setosa species and the other two. Setosa iris flowers seem to have wider sepals than the versicolor and virginica species, while the other two species seem to have longer sepals.  

![](images/scatterplot1.png)  

On the other hand the second scatter plot we can spot that setosa species seem to have shorter and narrower petals than the other two species.  
![](images/scatterplot2.png)  

 
**5.Conclusions from plots:** 

Observing these graphic representations above we can reach the following conclusions in relation to this data set:  

- Versicolor and virginica species of iris flower seem to be generally bigger in terms of petal size, with virginica having the widest and longest petal sizes, while setosa is clearly smaller and narrower.  

- In sepal size terms, we have wider and shorter sepals in setosa species. For versicolor and virginica , sepals size seems to be similar.  

-	We can determine if an iris flower belongs to setosa species looking at its parts measurements, particularly petal length.

**6. Machine learning approach:**

Following this tutorial : https://www.youtube.com/watch?v=Y17Y_8RK6pc 
I experimented with machine learning using the *sklearn* module available in Python to make a prediction of which one would be the iris species depending on their features size.I have added this analysis as a separate program which I named "machinelearning.py" as a different approach to analyse this data set and use it to predict results. The code is available in this repository as [machinelearning.py](https://github.com/Ainara12/Pands-project/blob/master/machinelearning.py).

See below the process I followed to apply this model to the dataset.  

1.	First I imported *sklearn library* and loaded *iris dataset* which is included in this library.  

2.	I printed its keys which are (['target', 'DESCR', 'target_names', 'feature_names', 'data', 'filename'] they are stored as a dictionary.   

3.	I printed the dataset to see how it's stored; we can see that we have a target array which shows a value given to every species of flower ( 0= Setosa, 1=Versicolor and 2= Virginica):

4. I organised data to create first a pair of scatter plots to see the data and if it is right:
```
#I set the variable for the function iris.data.T included in sklearn:

features = iris.data.T

#Then I specify the flower parts as features

sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
petal_width = features[3]

sepal_length_label = iris.feature_names[0]
sepal_width_label =iris.feature_names[1]
petal_length_label = iris.feature_names[2]
petal_width_label = iris.feature_names[3]  

```

Then I created two scatter plots for each set of variables using *matplotlib* as done in the previous section (you can ccess to scatter plot in this repository using these links:[Scatter plot 1](https://github.com/Ainara12/Pands-project/blob/master/images/scatterplot1ml.png)[Scatter plot 2](https://github.com/Ainara12/Pands-project/blob/master/images/scatterplot2ml.png)):  

![](images/scatterplot1ml.png)  
![](images/scatterplot2ml.png)  

Again we can spot the big diference that setosa has in terms of petal size with the other two types. Taking this into account, Could we predict which type of iris flower we have just having its measurements?
For the creation of this model I follow the K Nearest Neighbors algorithm. This algorithm is based storing all available cases and classifies new cases based on a similarity measure. In this case we have chosen  1 as the closest neighbor to be considered. In order to see if this is possible to predict with Python I followed the next steps to create a model using *sklearn* functionalities:  


1. We divided our data in two , as I want to have a portion for testing the model accuracy and another part to make the predictions. In this case I follow the split 25% for test, and 75% for the rest as the tutorial did.  

```
X_train, X_test, y_train, y_test = train_test_split(iris["data"],iris["target"])
knn= KNeighborsClassifier(n_neighbors=1)
```
2.Then I add to my *fit* function training data and training data from our target( the information we want to predict). 
 ```
knn.fit(X_train, y_train)
``` 
3. We create a variable then for a new set of measurements from a new flower that we want to test. 
Lets try entering this array of number ( using *numpy* library) and see if the model can predict which species this new flower belongs to by using the prediction function:

``` 
X_new = np.array([[0.3,1.0,3.5,6.0]]) #enter an array of float values for each flower part
prediction = knn.predict(X_new)
print(prediction) 
``` 
4. We get this result which indicates that these particular flower with these array of values corresponding to its features belongs to the iris virginica species.  

![](images/predictionresult.png)  


![](images/irisvirginica.jpg)  

To be able to confirm that this example is accurate, I have also added the option to test the model and see what is the accuracy. To do so I followed these steps to analyse the testing data we have split in the previous step:  

1. We use for this operation the functionality *knn.score* which shows a score between 0 and 1 that evaluates the accuracy of the data:

``` 
print(knn.score(X_test, y_test))
``` 
In this case we get a pretty high score ( score goes from 0 to 1) which means that we have 0.97 accuracy that for the value set we have being given in this example the new flower belongs to iris virginica species, based on the data we have provided to the model. 

![](images/accuracyexample.png)  

**7. General conclusion:**  

From this study I have done and based on the data we have at the moment (150 instances), we can say that iris setosa have wider sepals and smaller petals than the other two species while generally iris versicolor and virginica have wider and longer petals and also longer sepals than setosa. 
Taking this into account, we can predict with high accuracy  to which species an iris flower belongs to just adding its measurements to our model. 



**References:**  
[Dataset history and details](https://archive.ics.uci.edu/ml/datasets/Iris)    
[Dataset analysis](https://www.kaggle.com/uciml/iris)   
[Flower parts definitions](https://dictionary.cambridge.org/dictionary/english/)    
[Dataset extracted from this resource](https://gist.github.com/netj/8836201)   
[Analysis of iris dataset taken as reference for some parts of the project](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)  
[How to work with CSV files in Python](https://realpython.com/python-csv/)  
[Histogram tutorial in Seaborn](https://www.tutorialspoint.com/seaborn/seaborn_histogram.htm)  
[Seaborn color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)    
[Several variables histogram with Seaborn](https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn/)  
[K nearest neighborg algorithm](https://www.saedsayad.com/k_nearest_neighbors.htm)  
[Machine learning approach using sklearn]( https://www.youtube.com/watch?v=Y17Y_8RK6pc )   










