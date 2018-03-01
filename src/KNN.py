'''
Seth Tucker
2/9/2018

Input:
	T = training data
	K = number of neighbors
	t = input tuple to classify
	
Output:
	c = class to which t is assigned
	
KNN Algorithm
N = empty set
for each d in T do
	if |N| <= K, then
		N = N union {d};
	else
		if there exists a u in N such that sim(t, u) <= sim(t, d), then
			begin
				N = N - {u};
				N = N union {d};
			end
c = class to which the most u in N are classified

'''

import csv # For loading the training and testing data
import math # For finding Euclidean distance

#Read data from csv file
def getData(inputFile):
	data = []
	
	with open(inputFile, 'r') as csvInput:
		lines = csv.reader(csvInput)
		next(lines) # Skip over header line
		for row in lines:
			data.append(row)
	
	return data
	
def euclideanDist(
	
def KNN(data):
	#stuff and magic
	
def main():
	# File locations of testing and training csv files
	trainCSVFile = '../MNIST_train.csv'
	testCSVFile = '../MNIST_test.csv'
	
	# Get data from csv files
	trainingData = getData(trainCSVFile)
	testingData = getData(testCSVFile)
	
	
			
main()