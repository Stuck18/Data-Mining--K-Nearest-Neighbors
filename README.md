# Datamining-K-Nearest-Neighbors
## KNN implementation as part of CSC 535 Datamining

## Instructions
This KNN implementation will use weighted voting. In weighted voting, the vote of a neighbor is inversely proportional to its distance to the test sample. 

The provided MNIST_train.cvs will be used as the training data and the MNIST_test.csv will be used as the test data set.

There are 10 classes, labeled 0, 1, 2, ..., 9 for this data set. The first attribute/column is the class label. Also note taht the first line/row in both data sets is the headers line. A description of teh MNIST data is available at [](https://www.kaggle.com/c/digit-recognizer/data)

The program output will display the following
* The value of K
* For each test sample, print both the desired class and the computed class, where desired class, is the class label as given in teh data set, and computed class, is what the code produces as the output for the sample.
* The accuracy rate
* The number of misclassified test samples
* The total number of test samples

## Remarks
* Use Euclidean distance measure to computed distances.
* May use a random sample of the training data to decide on the value of K to use for the algorithm.
