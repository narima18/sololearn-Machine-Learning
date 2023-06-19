# sololearn-Machine-Learning
This repository contains projects contributing towards the earning of the Machine Learning certificate from sololearn.

## Project 1: What's in a Column?

Getting a column from a numpy array.

**Task**

Given a csv file and a column name, print the elements in the given column.

**Input Format**

First line: filename of a csv file

Second line: column name

**Output Format**

Numpy array

**Sample Input**

https://sololearn.com/uploads/files/one.csv

File one.csv contents:

a,b

1,3

2,4

**Sample Output**

[1 2]

## Project 2: Bob the Builder

Building a Logistic Regression model.

**Task**

You are given a feature matrix and a single datapoint to predict. Your job will be to build a Logistic Regression model with the feature matrix and make a prediction (1 or 0) of the single datapoint.

**Input Format**

First line: Number of data points in the feature matrix (n)

Next n lines: Values of the row in the feature matrix, separated by spaces

Next line: Target values separated by spaces

Final line: Values (separated by spaces) of a single datapoint without a target value

**Output Format**

Either 1 or 0

**Sample Input**

6

1 3

3 5

5 7

3 1

5 3

7 5

1 1 1 0 0 0

2 4

**Sample Output**

1

 ## Project 3: Welcome to the Matrix

Calculating Evaluation Metrics using the Confusion Matrix.

**Task**

You will be given the values of the confusion matrix (true positives, false positives, false negatives, and true negatives). Your job is to compute the accuracy, precision, recall and f1 score and print the values rounded to 4 decimal places. To round, you can use round(x, 4).

**Input Format**

The values of tp, fp, fn, tn, in that order separated by spaces

**Output Format**

Each value on its own line, rounded to 4 decimal places, in this order:

accuracy, precision, recall, f1 score

**Sample Input**

233 65 109 480

**Sample Output**

0.8038

0.7819

0.6813

0.7281

## Project 4: Split to Achieve Gain

Calculate Information Gain.

**Task**

Given a dataset and a split of the dataset, calculate the information gain using the gini impurity.

The first line of the input is a list of the target values in the initial dataset. The second line is the target values of the left split and the third line is 
the target values of the right split.

Round your result to 5 decimal places. You can use round(x, 5).

**Input Format**

Three lines of 1's and 0's separated by spaces

**Output Format**

Float (rounded to 5 decimal places)

**Sample Input**

1 0 1 0 1 0

1 1 1

0 0 0

**Sample Output**

0.5

## Project 5: A Forest of Trees

Build a Random Forest model.

**Task**

You will be given a feature matrix X and target array y. Your task is to split the data into training and test sets, build a Random Forest model with the training set, and make predictions for the test set. Give the random forest 5 trees.

You will be given an integer to be used as the random state. Make sure to use it in both the train test split and the Random Forest model.

**Input Format**

First line: integer (random state to use)

Second line: integer (number of datapoints)

Next n lines: Values of the row in the feature matrix, separated by spaces

Last line: Target values separated by spaces

**Output Format**

Numpy array of 1's and 0's

**Sample Input**

1

10

-1.53 -2.86

-4.42 0.71

-1.55 1.04

-0.6 -2.01

-3.43 1.5

1.45 -1.15

-1.6 -1.52

0.79 0.55

1.37 -0.23

1.23 1.72

0 1 1 0 1 0 0 1 0 1

**Sample Output**

[1 0 0]
