#%matplotlib notebook

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(1, 2, 1) # subplot with 1 row, 2 columns, and current axis is 1st subplot axes
linear_data = np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data, '-o')

exponential_data = linear_data**2 
plt.subplot(1, 2, 2) # subplot with 1 row, 2 columns, and current axis is 2nd subplot axes
plt.plot(exponential_data, '-o')

plt.subplot(1, 2, 1) # plot exponential data on 1st subplot axes
plt.plot(exponential_data, '-x')




plt.figure()
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2, sharey=ax1) # pass sharey=ax1 to ensure the two subplots share the same y axis
plt.plot(linear_data, '-o')
plt.plot(exponential_data, '-x')



plt.figure()
plt.subplot(1,2,1) == plt.subplot(121) # the right hand side is equivalent shorthand syntax



fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True) # create a 3x3 grid of subplots
ax5.plot(linear_data, '-') # plot the linear_data on the 5th subplot axes [Row 2, Column 2]
# set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)
# necessary on some systems to update the plot
plt.gcf().canvas.draw()




#=========================Histograms=================================

# create 2x2 grid of axis subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

# draw n = 10, 100, 1000, and 10000 samples from the normal distribution and plot corresponding histograms
for n in range(0,len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample, bins=100) #axs[n].hist(sample)
    #change the bins so the graph looks more continous than discrete
    axs[n].set_title('n={}'.format(sample_size))
    
    
plt.figure()
Y = np.random.normal(loc=0.0, scale=1.0, size=10000) #normal distribution
X = np.random.random(size=10000) #return a float between 0 to 0.1
plt.scatter(X,Y)    



# use gridspec to partition the figure into subplots
import matplotlib.gridspec as gridspec

plt.figure()
gspec = gridspec.GridSpec(3, 3)

top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
s = side_histogram.hist(Y, bins=100, orientation='horizontal')

# clear the histograms and plot normed(0 to 1) histograms
top_histogram.clear()
top_histogram.hist(X, bins=100, normed=True)
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal', normed=True)
side_histogram.invert_xaxis() # flip the side histogram's x axis

# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)
    
    
    
#=========================Box Plots=================================    

import pandas as pd
normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample, 
                   'random': random_sample, 
                   'gamma': gamma_sample})
df.describe()

        #gamma	        normal	        random
#count	10000.000000	10000.000000	10000.000000
#mean	2.001463	-0.008420	0.502343
#std	1.406765	0.999909	0.288900
#min	0.009941	-3.787779	0.000053
#25%	0.966549	-0.692355	0.248944
#50%	1.699038	-0.012142	0.503586
#75%	2.703818	0.659787	0.756367
#max	11.201966	3.896508	0.999966



plt.figure()
# if `whis` argument isn't passed, boxplot defaults to showing 1.5*interquartile (IQR) whiskers with outliers
_ = plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis='range') # plot boxplots for all three of df's columns
#plt.clf() # clear the current figure
plt.figure()
_ = plt.hist(df['gamma'], bins=100)


import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis='range')
# overlay axis on top of another 
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)
ax2.yaxis.tick_right() # switch the y axis ticks for ax2 to the right side



#=========================Heatmaps=================================  

#Perfect for longitutde, latitude, and a third property

plt.figure()

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
_ = plt.hist2d(X, Y, bins=100)
# add a colorbar legend
plt.colorbar()

#=========================Animations=================================  

import matplotlib.animation as animation

x = np.random.randn(100)
# create the function that will do the plotting, where curr is the current frame
def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == n: 
        a.event_source.stop()
    plt.cla()
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x[:curr], bins=bins)
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr), [3,27])
fig = plt.figure()
a = animation.FuncAnimation(fig, update, interval=100) #100 milliseconds


#=========================Interactivity=================================  

plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {},{} \nand data {},{}'.format(event.x, event.y, event.xdata, event.ydata))

# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
#Displays a message every time we click on something



from random import shuffle
origins = ['China', 'Brazil', 'India', 'USA', 'Canada', 'UK', 'Germany', 'Iraq', 'Chile', 'Mexico']
shuffle(origins)
df = pd.DataFrame({'height': np.random.rand(10),
                   'weight': np.random.rand(10),
                   'origin': origins})
plt.figure()
# picker=5 means the mouse doesn't have to click directly on an event, but can be up to 5 pixels away
plt.scatter(df['height'], df['weight'], picker=5)
plt.gca().set_ylabel('Weight')
plt.gca().set_xlabel('Height')
def onpick(event):
    origin = df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('Selected item came from {}'.format(origin))
    #every time we click somewhere, it reveals the country it is from

# tell mpl_connect we want to pass a 'pick_event' into onpick when the event is detected
plt.gcf().canvas.mpl_connect('pick_event', onpick)
