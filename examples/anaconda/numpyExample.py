# dealing with images

import cv2
import numpy as np

# bgr = 1 3x5  grey = 0 2D
im_g = cv2.imread('data.png', 0)

# im_g = 2D array
im_g[0:2,2:4]
im_g.shape()

# iterate by column
for itr in im_g.T:
	

# one by one data access 
for itr in im_g.flat


cv2.imwrite('newDat.png', im_g)

# stacking horiz
numpy.hstack(im_g, im_g)
# veritical stacking
numpy.vstack(im_g,im_g)

# Numpy is a Linear Algebra Library for Python

# array operations + * - / **
npArray = np.arange(0,10)

np.sqrt(npArray)
np.exp(npArray)
np.max(npArray)
np.sin(npArray)
np.log(npArray)


#python list and list of list can be converted into np objects.
np.zeros(4,4)
np.ones(4,4)
np.linspace(0,20,4) # returns evenly spaced numbers
np.eye(3) # for an identity matrix ( diag 1 left top to right bottom)


# <random.rand> random samples
npArray = np.random.rand(2,3)

# <randn> standard normal distribution 

# <randint> 

# <reshape> same data new structure
npArray.reshape(4,4)

# <min>

# <max>

# <argmax>

# <min>

# <argmin>

# <sin>

# <log>

# <shape> indicates the shape of the array

# <dtype> data type of the array


npArray[0:5] = 33
# fills 0 - 4 with 33

# <copy>
npArrayCopy = npArray.copy()

# conditionals produce an array of boolean
boolArray = npArray > 25

# retrieve the contents by passing it back in the orig arra
resultsArray = npArray[boolArray]




dataset = np.array([[2, 4, 6, 8, 3, 2, 5],
					[7, 5, 3, 1, 6, 8, 0],
					[1, 3, 2, 1, 0, 0, 8]])
print (np.max(dataset, axis=1) ‐ np.min(dataset, axis=1))

npArray = np.array([15.0, 20.0, 22.0, 75.0, 40.0, 35.0]) 
npArray = npArray*.01


array1 = np.array([2, 0, 0, 2]) 

array2 = np.array([ [1, 2, 3, 4],
					[2, 3, 4, 5],
					[3, 4, 5, 6],
					[4, 5, 6, 7]])

array3 = np.dot(array1, array2)










