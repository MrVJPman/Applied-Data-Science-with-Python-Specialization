#%matplotlib notebook

import matplotlib as mpl
mpl.get_backend()

import matplotlib.pyplot as plt
plt.plot(3, 2, '.') #Draws a dot at (3, 2)





# First let's set the backend without using mpl.use() from the scripting layer
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

# create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the fig
ax = fig.add_subplot(111)

# plot the point (3,2)
ax.plot(3, 2, '.')

# save the figure to test.png
# you can see this figure in your Jupyter workspace afterwards by going to
# https://hub.coursera-notebooks.org/
canvas.print_png('test.png')
#%%html
#<img src='test.png' />




# create a new figure
plt.figure()
# plot the point (3,2) using the circle marker
plt.plot(3, 2, 'o')
# get the current axes
ax = plt.gca()
# Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])


# create a new figure
plt.figure()
# plot the point (1.5, 1.5) using the circle marker
plt.plot(1.5, 1.5, 'o')
# plot the point (2, 2) using the circle marker
plt.plot(2, 2, 'o')
# plot the point (2.5, 2.5) using the circle marker
plt.plot(2.5, 2.5, 'o')



# get current axes
ax = plt.gca() 
# get all the child objects the axes contains
ax.get_children()



#=========================================Scatterplots=========================================

import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.figure()
plt.scatter(x, y) # similar to plt.plot(x, y, '.'), but the underlying child objects in the axes are not Line2D




x = np.array([1,2,3,4,5,6,7,8])
y = x
# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green']*(len(x)-1)
colors.append('red')
plt.figure()
# plot the point with size (radius) 100 and chosen colors
plt.scatter(x, y, s=100, c=colors)




# convert the two lists into a list of pairwise tuples
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
print(list(zip_generator)) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
# The single star * unpacks a collection into positional arguments
print(*zip_generator) # (1, 6) (2, 7) (3, 8) (4, 9) (5, 10)
plt.figure()
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students') # plot a data series 'Tall students' in red using the first two elements of x and y
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students') # plot a second data series 'Short students' in blue using the last three elements of x and y 
plt.xlabel('The number of times the child kicked a ball') # add a label to the x axis
plt.ylabel('The grade of the student') # add a label to the y axis
plt.title('Relationship between ball kicking and grades') # add a title
plt.legend() # add a legend (uses the labels from plt.scatter)
plt.legend(loc=4, frameon=False, title='Legend') # add the legend to loc=4 (the lower right hand corner), also gets rid of the frame and adds a title

plt.gca().get_children() # get children from current axes (the legend is the second to last item in this list)
legend = plt.gca().get_children()[-2] # get the legend from the current axes
legend.get_children()[0].get_children()[1].get_children()[0].get_children() # you can use get_children to navigate through the child artists

# import the artist class from matplotlib
from matplotlib.artist import Artist

def rec_gc(art, depth=0):
    if isinstance(art, Artist):
        # increase the depth for pretty printing
        print("  " * depth + str(art))
        for child in art.get_children():
            rec_gc(child, depth+2)
# Call this function on the legend artist to see what the legend is made up of
rec_gc(plt.legend())
 
#=========================================Line Plots=========================================

import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure()
plt.plot(linear_data, '-o', exponential_data, '-o') # plot the linear data and the exponential data
plt.plot([22,44,55], '--r') # plot another series with a dashed red line
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline', 'Competition', 'Us']) # add a legend with legend entries (because we didn't have labels when we plotted the data series)
plt.gca().fill_between(range(len(linear_data)),  # fill the area between the linear data and exponential data
                       linear_data, exponential_data, 
                       facecolor='blue', 
                       alpha=0.25)



plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')
plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates)) # convert the map to a list to get rid of the error
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')
x = plt.gca().xaxis

# rotate the tick labels for the x axis
for item in x.get_ticklabels():
    item.set_rotation(45)
# adjust the subplot so the text doesn't run off the image
plt.subplots_adjust(bottom=0.25)
ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title("Exponential ($x^2$) vs. Linear ($x$) performance") # you can add mathematical expressions in any text element


#=========================================Bar Charts=========================================

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

new_xvals = []
# plot another set of bars, adjusting the new xvals to make up for the first set of bars plotted
for item in xvals:
    new_xvals.append(item+0.3)
plt.bar(new_xvals, exponential_data, width = 0.3 ,color='red')

from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))] 

# This will plot a new set of bars with errorbars using the list of random error values
plt.bar(xvals, linear_data, width = 0.3, yerr=linear_err)




# stacked bar charts are also possible
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, exponential_data, width = 0.3, bottom=linear_data, color='r')
#plt.barh(xvals, exponential_data, height = 0.3, left=linear_data, color='r') Move it to the left 




#=========================================Dejunkifying a Plot Exercise=========================================


import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

# TODO: change the bar colors to be less bright blue
# TODO: make one bar, the python bar, a contrasting color
plt.bar(pos, popularity, align='center', color=['blue', 'lightslategrey', 'lightslategrey', 'lightslategrey', 'lightslategrey'])

# TODO: remove the Y label since bars are directly labeled
plt.xticks(pos, languages, color="grey")
plt.ylabel('% Popularity', color="grey")
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', color="grey")

#TODO: remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(bottom='off', left='off', labelleft='off')

# remove the frame of the chart
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
    
# direct label each bar with Y axis values
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)
plt.show()

#=========================Solution for Michigan

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

# change the bar colors to be less bright blue
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
# make one bar, the python bar, a contrasting color
bars[0].set_color('#1F77B4')

# soften all labels by turning grey
plt.xticks(pos, languages, alpha=0.8)

# TODO: remove the Y label since bars are directly labeled
#plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)
    
# TODO: direct label each bar with Y axis values
plt.show()