import numpy as np

x = np.array([[0, 0]
			 ,[0, 1]
			 ,[1, 1]
			 ,[1, 0]])
y = np.array([[1]
			 ,[0]
			 ,[1]
			 ,[0]])

k = 0.01

def sigmoid(x, deriv):
	if (deriv == False):
		return 1/(1+np.exp(-x))
	if (deriv == True):
		return x*(1-x)

l0 = x
w1 = np.random.rand(2, 3)
l1 = sigmoid(np.dot(l0, w1), False)
w2 = np.random.rand(3, 1)
h = sigmoid(np.dot(l1, w2), False)
j = 0.5*(y-h)**2

for i in range(10):
	dJ = y-h
	print(dJ)
	w2 = w2 - np.dot(l1.T, dJ*sigmoid(h, True))
	dJ = np.dot(l1.T, dJ*sigmoid(h, True))
	w1 = w1 - np.dot(l0.T, dJ*sigmoid(l1, True))
	print(dJ)
	print(np.sum(j))
	print("-----------------------------------------")
