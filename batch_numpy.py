import numpy as np

a = np.array(([1,2,3,4,5,6],[2,5,8,4,6,6]))
b = np.array(([1,2,3,4,5,6]))
c = np.arange(1,5)
d = np.array(([1,2,3,4,5,6],[1,2,3,4,5,6]))

"""
print(c)
print(a.size)
print(a.shape)
print(a.reshape(2,6))
print(a.size)
print(a.max())
print(a.min())

print (np.zeros((2,3)))
print(np.ones((4,5)))

print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.ravel())

print(np.linspace(1,100,num=20))

print(a.sum())
print(a.sum(axis=0)) # 0 for columns
print(a.sum(axis=1)) # 1 for rows
print(a.sum(axis=1, keepdims=True)) # 1 for rows
print(a+b)
print(a*b)
print(a/b)
print(a.dot(d))
print(np.sqrt(a))
print(np.square(a))
print(a.std())
print(a.mean())
print(a[:,2])
print(a[0,2:4])
print(a[:,2:4])
"""
"""
Statistics methods

Median is defined as the value separating the higher half of a data sample from the lower half.
The numpy.median() function is used as shown in the following program.

Arithmetic mean is the sum of elements along an axis divided by the number of elements. The numpy.mean() function returns the arithmetic mean of elements in the array.
If the axis is mentioned, it is calculated along it.

Standard deviation is the square root of the average of squared deviations from mean. The formula for standard deviation is as follows −
std = sqrt(mean(abs(x - x.mean())**2))

If the array is [1, 2, 3, 4], then its mean is 2.5. Hence the squared deviations are [2.25, 0.25, 0.25, 2.25] and the square root of its mean divided by 4, i.e., sqrt (5/4) is 1.1180339887498949


Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2). In other words, the standard deviation is the square root of variance.
"""
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))

for i in a:
    print(i) # print rows
# print(a.flat)

for cell in a.flat:
    print(cell)


print(np.vstack((a,b)))
print(np.hstack((a,d))) # i/p must have same dimensions

# find out vsplit and hsplit

print(a>5)
print(d[a>5]) # filtering
d[a>5] = -1
print(d) # replacing


"""
# # # Pure iterative Python # # #
points = [[9,2,8],[4,7,2],[3,4,4],[5,6,9],[5,0,7],[8,2,7],[0,3,2],[7,3,0],[6,1,1],[2,9,6]]
qPoint = [4,5,3]
minIdx = -1
minDist = -1
for idx, point in enumerate(points):  # iterate over all points
        dist = sum([(dp-dq)**2 for dp,dq in zip(point,qPoint)])**0.5  # compute the euclidean distance for each point to q
        if dist < minDist or minDist < 0:  # if necessary, update minimum distance and index of the corresponding point
            minDist = dist
            minIdx = idx

print('Nearest point to q: ', points[minIdx])
# Nearest point to q:  [3, 4, 4]

# # # Equivalent NumPy vectorization # # #
import numpy as np
points = np.array([[9,2,8],[4,7,2],[3,4,4],[5,6,9],[5,0,7],[8,2,7],[0,3,2],[7,3,0],[6,1,1],[2,9,6]])
qPoint = np.array([4,5,3])
minIdx = np.argmin(np.linalg.norm(points-qPoint,axis=1))  # compute all euclidean distances at once and return the index of the smallest one
print('Nearest point to q: ', points[minIdx])
# Nearest point to q:  [3 4 4]

"""