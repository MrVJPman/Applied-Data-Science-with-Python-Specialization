import pandas as pd
import numpy as np

np.random.binomial(1, 0.5)
#Roll once with probability of 0.5 times

np.random.binomial(1000, 0.5)/1000
#Roll 1000 times with probability of 0.5 times


#Use np.random.binomial(n, p, size) to do 
#10000 simulations of flipping a fair coin 20 times, then see what proportion of the simulations are 15 or greater.
x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())

#Tornado have 0.01% chance 
#perform 100000 
chance_of_tornado = 0.01/100
np.random.binomial(100000, chance_of_tornado)
#Array of 1

#Perform 1 million simulations of a fair coin 1 times, with 0.01% chance
chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1
print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))

np.random.uniform(0, 1) #Generates a random number from [0, 1)
np.random.normal(0.75) #Generates a random number from a normal distribution with an expected number of 0.75


#Generates 1000 random number from a normal distribution with an expected number of 0.75
distribution = np.random.normal(0.75,size=1000)
#Calculate the standard deviation
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))
np.std(distribution)


import scipy.stats as stats
stats.kurtosis(distribution) #performs kurtosis on a distribution
stats.skew(distribution) #performs skew on a distribution


#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
#Array of 10,000 sizes
chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)
chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)

output = plt.hist([chi_squared_df2,chi_squared_df5], bins=50, histtype='step', 
                  label=['2 degrees of freedom','5 degrees of freedom'])
plt.legend(loc='upper right')



#=======================================Hypothesis Testing=======================================

df = pd.read_csv('grades.csv')

#assignments submited before/after Dec 31
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']

from scipy import stats

#Perform t-test : compare means of population

stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
#Ttest_indResult(statistic=1.3239868220912567, pvalue=0.18563824610067967)
#p value need to be 0.05
#We're saying there's a positive result every 20 tests
#P hacking if when we run too many tests