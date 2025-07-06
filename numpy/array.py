import numpy as np

# 1D array
arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))


# tuple truns turn into array
arr2 = np.array((1,2,3,4,5))
# print(arr2)
# print(type(arr2)) #ndarray


# 0D array
arr3 = np.array(32)
# print(arr3)
# print("0D array",type(arr3))

# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D array",arr)


# 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print("3D array",arr)
# print('Shape',arr.shape)


# Dimension
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)



arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

arr = np.array([1, 2, 3, 4])

# print(arr[1])


# 2d array index
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 2nd row: ', arr[1, 1])

# 3d array index

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

