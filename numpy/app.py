import os
import json
import numpy as np
print("NumPy version:", np.__version__)

import matplotlib
import matplotlib.pyplot as plt
print("Matplotlib version:", matplotlib.__version__)

import sklearn
from sklearn import preprocessing, neighbors
print("scikit-learn version:", sklearn.__version__)

from sklearn import preprocessing, neighbors

training_set = {'Dog':[[1,2],[2,3],[3,1]], 'Cat':[[11,20],[14,15],[12,15]]}
testing_set = [15,20]

#ploting all data
c = 'x'
for data in training_set:
	print(data)
	
	#print(training_set[data])
	for i in training_set[data]:
		plt.plot(i[0], i[1], c, color='c')
	
	c = 'o'
plt.show()

#prepare X and Y
x = []
y = []
for group in training_set:
	
	for features in training_set[group]:
		x.append(features)
		y.append(group)

#import model builing
#initialize and fit
clf = neighbors.KNeighborsClassifier()
clf.fit(x, y)


#preprocess testing data
import numpy as np
testing_set = np.array(testing_set)
testing_set = testing_set.reshape(1,-1)

#predition 
prediction = clf.predict(testing_set)
print(prediction)

# Write only the final accuracy to result.txt
output_directory = os.environ["IEXEC_OUT"]
output_path = os.path.join(output_directory, "result.txt")

with open(output_path, "w") as f:
    f.write(f"Prediction: {prediction}\n")

with open(os.path.join(output_directory, 'computed.json'), 'w') as f:
        json.dump({"deterministic-output-path": output_path}, f)
