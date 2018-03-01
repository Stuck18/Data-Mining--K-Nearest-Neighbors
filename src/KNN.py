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
	
# T = Training Data, K = number of neighbors, t = input tuple to classify
def KNN(T, K, t):
	N = []
	for d in T:
		if (len(N) <= K):
			N.append(d)
		else:
			if #there exists u in N such that sim(t, u) <= sim(t, d):
				for elem in N:
					if (N[elem] == u):
						N.remove(u)
						N.append(d)
	c = #class to which the most u in N are classified
	return c
			
	file.close()
	
# Determine the accuracy of the algorithm
def calcAccuracy(CCList, DCList):
	accuracy = 0
	misClassified
	for elem in DCList:
		if (DCList[elem] == CCList[elem]):
			accuracy += 1
		else:
			misClassified += 1
	accuracy = (accuracy / float(len(DCList))) * 100.0
	return accuracy, misClassified
	
def main():
	# File locations of testing and training csv files
	trainCSVFile = '../MNIST_train.csv'
	testCSVFile = '../MNIST_test.csv'
	
	# Get data from csv files
	trainingData = getData(trainCSVFile)
	testingData = getData(testCSVFile)
	
	neighbors = 4 # Hardcoded value for testing, remove later
	
	# These will be used to determine accuracy
	computedClassList = []
	desiredClassList = []
	
	print("K = ", neighbors)
	
	for elem in testingdata:
		computedClass = KNN(trainingData, neighbors, testingData[elem])
		desiredClass = testingData[elem][0]
		computedClassList.append(computedClass)
		desiredClassList.append(desiredClass)
		print("Desired class: ", testingData[elem][0], ", Computed class: ", computedClass)
	
	accuracy, misClassified = calcAccuracy(computedClassList, desiredClassList)
	
	print("Accuracy rate: ", accuracy, "%")
	print("Number of misclassified test samples: ", numMissclassified)
	print("Total number of test samples: ", len(testingData))
	
main()