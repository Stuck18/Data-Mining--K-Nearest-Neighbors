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
import operator

#Read data from csv file
def getData(inputFile):
	data = []
	with open(inputFile, 'r') as csvInput:
		lines = csv.reader(csvInput)
		next(lines) # Skip over header line
		for row in lines:
			data.append(row)
	return data
	
# Compute the euclidean distance between 2 tuples
def euclideanDist(tuple1, tuple2):
	sum = 0
	distance = 0 
	for i in range(0, len(tuple1)):
		sum += math.pow((int(tuple1[i]) - int(tuple2[i])), 2)
	distance = math.sqrt(sum)
	return distance
	
# T = Training Data, K = number of neighbors, t = input tuple to classify
def KNN(T, K, t):
	N = []
	for d in range(0, len(T)):
		TUDist = euclideanDist(t[1:], T[d][1:])
		if (len(N) <= K):
			N.append((T[d][0], TUDist))
		else:
			for i in range(0, len(N)):
				if (TUDist <= N[i][1]):
					N.remove(N[i])
					N.append((T[d][0], TUDist))
					break
	
	votes = {}
	for i in range(len(N)):
		vote = N[i][0]
		if vote in votes:
			votes[vote] += 1
		else:
			votes[vote] = 1
	votes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
	c = votes[0][0]
	return c
	
# Determine the accuracy of the algorithm
def calcAccuracy(CCList, DCList):
	accuracy = 0
	misClassified = 0
	for i in range(0, len(DCList)):
		if (DCList[i] == CCList[i]):
			accuracy += 1
		else:
			misClassified += 1
	accuracy = (accuracy / float(len(DCList))) * 100.0
	return accuracy, misClassified
	
def main():
	# File locations of testing and training csv files
	trainCSVFile = 'MNIST_train.csv'
	testCSVFile = 'MNIST_test.csv'
	
	# Get data from csv files
	trainingData = getData(trainCSVFile)
	testingData = getData(testCSVFile)
	
	K = 4 # Hardcoded value for testing, remove later
	
	# These will be used to determine accuracy
	computedClassList = []
	desiredClassList = []
	
	print("K = " + str(K))
	
	for i in range(0, len(testingData)):
		computedClass = KNN(trainingData, K, testingData[i])
		desiredClass = testingData[i][0]
		computedClassList.append(computedClass)
		desiredClassList.append(desiredClass)
		print("Desired class: " + str(testingData[i][0]) + ", Computed class: " + str(computedClass))
	
	accuracy, misClassified = calcAccuracy(computedClassList, desiredClassList)
	
	print("Accuracy rate: " + str(accuracy) + "%")
	print("Number of misclassified test samples: " + str(misClassified))
	print("Total number of test samples: " + str(len(testingData)))
	
main()
