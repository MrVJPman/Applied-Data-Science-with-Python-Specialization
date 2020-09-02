import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib notebook

# see the pre-defined COLOUR styles provided.
print(plt.style.available)
# use the 'seaborn-colorblind' style
plt.style.use('seaborn-colorblind')



np.random.seed(123)
df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20}, 
                  index=pd.date_range('1/1/2017', periods=365))
#df.plot()
df.plot('A','B', kind = 'scatter');

# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')

df.plot.box(); #box plot
df.plot.hist(alpha=0.7); #df.plot.hist(alpha=0.7);
df.plot.kde(); #Kernel density estimation plots are useful for deriving a smooth continuous function from a given sample.





#Uses iris flower data set to plot a scatter matrix 
#scatter matrix: a way to compare multiples variable
iris = pd.read_csv('iris.csv')
pd.tools.plotting.scatter_matrix(iris);
plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');




#=========================Seaborn=================================  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib notebook


np.random.seed(1234)
#1000 numbers, with standard deviation of 10
v1 = pd.Series(np.random.normal(0,10,1000), name='v1')
#1000 numbers, mean of 60 standard deviation of 15
v2 = pd.Series(2*v1 + np.random.normal(60,15,1000), name='v2')

plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50,150,5), label='v1');
plt.hist(v2, alpha=0.7, bins=np.arange(-50,150,5), label='v2');
plt.legend();

# plot a kernel density estimation over a stacked barchart
plt.figure()
plt.hist([v1, v2], histtype='barstacked', normed=True);
v3 = np.concatenate((v1,v2)) #combine v1 and v2 together
sns.kdeplot(v3); #kernel density plot


plt.figure() #graph for v1 and v2 only, v3 as a red line
# we can pass keyword arguments for each individual component of the plot
sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'});



#creates a joint plot where there are two additional plots showing v1/v2 distribution
grid = sns.jointplot(v1, v2, alpha=0.4);
grid.ax_joint.set_aspect('equal')

sns.jointplot(v1, v2, kind='hex'); #hex is better for larger data sets
sns.jointplot(v1, v2, kind='kde', space=0); 
 
sns.set_style('white') # set the seaborn style for all the following plots




#Categorical datas
iris = pd.read_csv('iris.csv')
sns.pairplot(iris, hue='Name', diag_kind='kde', size=2);
plt.figure(figsize=(8,6))
plt.subplot(121)
sns.swarmplot('Name', 'PetalLength', data=iris);
plt.subplot(122)
sns.violinplot('Name', 'PetalLength', data=iris);