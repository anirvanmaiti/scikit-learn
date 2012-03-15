#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Linear Regression Example
=========================================================
This example uses the only the first feature of the
`diabetes` dataset, in order to illustrate a two-dimensional
plot of this regression technique. The straight line can be seen
in the plot, showing how linear regression attempts to draw a
straight line that will best minimize the residual sum of squares 
between the observed responses in the dataset, and the responses 
predicted by the linear approximation.
 
The coefficients, the residual sum of squares and 
the variance score are also calculated.

"""
from __future__ import print_function
print(__doc__)


# Code source: Jaques Grobler
# License: BSD



import pylab as pl
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:,np.newaxis]
diabetes_X_temp = diabetes_X[:,:,2] 

# Split the data into training/testing sets
diabetes_X_train = diabetes_X_temp[:-20]
diabetes_X_test  = diabetes_X_temp[-20:] 

from sklearn import linear_model
from sklearn.datasets.samples_generator import make_regression

# this is our test set, it's just a straight line with some
# gaussian noise
X, Y = make_regression(n_samples=100, n_features=1, n_informative=1,\
                        random_state=0, noise=35)


# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit (diabetes_X_train, diabetes_y_train)

# The coefficients
print 'Coefficients: \n', regr.coef_
# The mean square error
print ("Residual sum of squares: %.2f" % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test)**2))
# Explained variance score: 1 is perfect prediction
print ('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs 
pl.scatter(diabetes_X_test, diabetes_y_test,  color='black')
pl.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue', linewidth=3)

pl.xticks(())
pl.yticks(())

pl.show()
