#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits = pd.read_table('fruit_data_with_colors.txt')
# create a mapping from fruit label value to fruit name to make results easier to interpret
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))   
#{1: 'apple', 2: 'mandarin', 3: 'orange', 4: 'lemon'}

#==============================Examining the data=================================

# plotting a scatter matrix
from matplotlib import cm

X = fruits[['height', 'width', 'mass', 'color_score']]
y = fruits['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) 
#random_state creates a seed

cmap = cm.get_cmap('gnuplot')
scatter = pd.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap=cmap)
#creates 9 diagrams, 6 scatter and 3 histograms


# plotting a 3D scatter plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c = y_train, marker = 'o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()


#==============================KNN =================================
from sklearn.neighbors import KNeighborsClassifier
from adspy_shared_utilities import plot_fruit_knn

# For this example, we use the mass, width, and height features of each fruit instance
X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) # default is 75% / 25% train-test split

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train) #train the classifier
knn.score(X_test, y_test) #estimate accuracy using test data

# first example: a small fruit with mass 20g, width 4.3 cm, height 5.5 cm
# second example: a larger, elongated fruit with mass 100g, width 6.3 cm, height 8.5 cm
fruit_prediction = knn.predict([[20, 4.3, 5.5]])
#fruit_prediction = knn.predict([[100, 6.3, 8.5]])
lookup_fruit_name[fruit_prediction[0]]

plot_fruit_knn(X_train, y_train, 5, 'uniform')   # we choose 5 nearest neighbors



#=====================checking accuracy of different values of K=================================

k_range = range(1,20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0,5,10,15,20]); #k=6 is best

#=====================checking accuracy for different test/train split=================================

knn = KNeighborsClassifier(n_neighbors = 5)
plt.figure()
for s in [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]:

    scores = []
    for i in range(1,1000):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1-s)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_test, y_test))
    plt.plot(s, np.mean(scores), 'bo')

plt.xlabel('Training set proportion (%)')
plt.ylabel('accuracy');
#===============

#A low value of �k� (close to 1) is more likely to overfit the training data 
#and lead to worse accuracy on the test data, compared to higher values of �k�

#Setting �k� to the number of points in the training set will result 
#in a classifier that always predicts the majority class

#The k-nearest neighbors classification algorithm has to 
#memorize all of the training examples to make a prediction