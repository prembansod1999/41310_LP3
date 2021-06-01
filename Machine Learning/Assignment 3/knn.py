
import numpy as np

x = np.array([2, 4, 4, 4, 6, 6])
y = np.array([4, 2, 4, 6, 2, 4])
classlist = np.array([1, 1, 2, 1, 2, 1])
test_tuple = [6, 6]

k = 3
knn_array = []

dict = {}

for i in range(np.size(x)):
	dict[i] = np.sqrt(((x[i] - test_tuple[0])**2) + ((y[i] - test_tuple[1])**2))

dict = sorted(dict.items(), key = lambda kv : (kv[1], kv[0]))

for i in range(k):
	knn_array.append(dict[i][0])

my_class = []

for i in range(k):
	my_class.append(classlist[knn_array[i]])

my_class = {i: my_class.count(i) for i in range(k)}

max = 0

for key, value in my_class.items():
	if value > max:
		max = value
		maxclass = key

if maxclass == 1:
	print ("The Predicted class for [6, 6] is: Blue")
elif maxclass == 2:
	print ("The predicted class for [6, 6] is: Orange")