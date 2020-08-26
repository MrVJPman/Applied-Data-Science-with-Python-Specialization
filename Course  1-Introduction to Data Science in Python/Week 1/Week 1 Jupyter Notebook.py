def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2)) #3
print(add_numbers(1, 2, 3)) #6

#=====================================================================

def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True)) 
#Flag is true!
#3

#=====================================================================

def add_numbers(x,y):
    return x+y

a = add_numbers
a(1,2)


#=====================================================================

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Kevyn Collins-Thompson'] = None

for name, email in x.items():
    print(name)
    print(email)
    
#Christopher Brooks
#brooksch@umich.edu
#Bill Gates
#billg@microsoft.com
#Kevyn Collins-Thompson
#None



#=====================================================================

import csv

#%precision 2 
#floating decimal is 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # The first three dictionaries in our list.


mpg[0].keys() #column names
sum(float(d['cty']) for d in mpg) / len(mpg) #Average cty fuel economy
sum(float(d['hwy']) for d in mpg) / len(mpg) #Average highway fuel economy
cylinders = set(d['cyl'] for d in mpg) #All the unique values for cyl

#=====================================================================

#average cty mpg for each group.
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # go through every row
        if d['cyl'] == c: # if the cylinder level of this type matches the current cylinder
            summpg += float(d['cty']) # increment the mpg to get the total mpg
            cyltypecount += 1 # increment the count of cars that has this cylider
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])

#All the unique values for class
vehicleclass = set(d['class'] for d in mpg) 

#=====================================================================

import datetime as dt
import time as tm

tm.time() #seconds since jan 1, 1970

#creates the current time
dtnow = dt.datetime.fromtimestamp(tm.time()) 
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second 

today = dt.date.today()#today's date
delta = dt.timedelta(days = 100) # create a timedelta of 100 days, this will be used against the variable today
today - delta # the date 100 days ago

today > today-delta # compare dates, return a boolean

#=============================MAP()=====================================

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2) #calls the function [min] on from each of the values from [store1] and [store 2]
#min(10.00, 9.00)
#min(11.00, 11.10)
#min(12.34, 12.34)
#min(2.34, 2.01)

#cheapest is an iteratable object we must iterate through
for item in cheapest:
    print(item)
    
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
    
def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))


#=============================lambda=====================================
#lamba a, b, c are the INPUTS
#: a + b are the OUTPUTS
my_function = lambda a, b, c : a + b #function definition

#calling the function
my_function(1, 2, 3) #3 
#calling the function
(lambda a, b, c : a + b)(1, 2, 3)


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda input_person : input_person.split()[0] + ' ' + input_person.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map((lambda input_person : input_person.split()[0] + ' ' + input_person.split()[-1]),  people))


#=============================list comprehension=====================================

#same list
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)        
my_list = [number for number in range(0,1000) if number % 2 == 0]
           #number : the value
           #for number in range(0,1000) : the list of chosen values
           #if number % 2 == 0 : conditionals

#example 2           
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst
times_tables() == [i * j for i in range(10) for j in range(10)]           

#example 3
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = ["{}{}{}{}".format(letter1, letter2, digit1, digit2) for letter1 in lowercase 
          for letter2 in lowercase for digit1 in digits for digit2 in digits]
correct_answer == answer

#example 4
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [letter1 + letter2 + digit1 + digit2 
          for letter1 in lowercase 
          for letter2 in lowercase
          for digit1 in digits
          for digit2 in digits]
correct_answer == answer

#=============================numpy=====================================

import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist) #convert into an np array
y = np.array([4, 5, 6]) #direct creation
m = np.array([[7, 8, 9], [10, 11, 12]]) #Multidimension array
m.shape #(2, 3) two rows, three values

n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
#array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
n = n.reshape(3, 5) # creates a new array to be 3x5
#array([[ 0,  2,  4,  6,  8],
       #[10, 12, 14, 16, 18],
       #[20, 22, 24, 26, 28]])

o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
#array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ])

#resize changes the shape and size of array in-place.
o.resize(3, 3)
#array([[ 0. ,  0.5,  1. ],
#       [ 1.5,  2. ,  2.5],
#       [ 3. ,  3.5,  4. ]])


np.ones((3, 2))
#array([[ 1.,  1.],
#       [ 1.,  1.],
#       [ 1.,  1.]])

np.zeros((2, 3))
#array([[ 0.,  0.,  0.],
#       [ 0.,  0.,  0.]])

np.eye(3)  #1 on the diagonals, 0 everywhere else
#array([[ 1.,  0.,  0.],
 #      [ 0.,  1.,  0.],
  #     [ 0.,  0.,  1.]])


#Recall : y = np.array([4, 5, 6]) 
np.diag(y)
#array([[4, 0, 0],
#       [0, 5, 0],
#       [0, 0, 6]])

np.array([1, 2, 3] * 3)
np.repeat([1, 2, 3], 3)
#array([1, 2, 3, 1, 2, 3, 1, 2, 3])


p = np.ones([2, 3], int)
#array([[1, 1, 1],
#       [1, 1, 1]])

np.vstack([p, 2*p])
#array([[1, 1, 1],
#       [1, 1, 1],
#       [2, 2, 2],
#       [2, 2, 2]])

np.vstack([p, 3*p, 5*p]) #stack vertically
#array([[1, 1, 1],
#       [1, 1, 1],
#       [3, 3, 3],
#       [3, 3, 3],
#       [5, 5, 5],
#       [5, 5, 5]])

np.hstack([p, 3*p, 5*p]) #stack horizontally
#array([[1, 1, 1, 3, 3, 3, 5, 5, 5],
#       [1, 1, 1, 3, 3, 3, 5, 5, 5]])



print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]
print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]
print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]
x.dot(y) # dot product  1*4 + 2*5 + 3*6


z = np.array([y, y**2])
print(len(z)) # number of rows of array, 2
#array([[ 4,  5,  6],
#       [16, 25, 36]])

z.shape
#(2, 3)

z.T
#array([[ 4, 16],
#       [ 5, 25],
#       [ 6, 36]])

z.T.shape
#(3, 2)

z.dtype
#dtype('int64')

z = z.astype('f')
z.dtype
#dtype('float32')

a = np.array([-4, -2, 1, 3, 5])
a.sum() #-3
a.max() #5
a.min() #-4
a.mean() #-0.6
a.std() #3.26

a.argmax() #index of max value, @4
a.argmin() #index of min value, @0

s = np.arange(13)**2
#array([ 0,  1,  4,  9,  16,  25,  36,  49,  64,  81, 100, 121, 144])

s[-5::-2] 
#array([64, 36, 16,  4,  0])
#start from -5, and count back backwards twice

r = np.arange(36)
r.resize((6, 6))
#array([[ 0,  1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10, 11],
#       [12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23],
#       [24, 25, 26, 27, 28, 29],
#       [30, 31, 32, 33, 34, 35]])

r[-1, ::2] #This is a slice of the last row, and only every other element.

r[r > 30] #only values greater than 30
r[r > 30] = 30 #set all values greater than 30 to 30

r2[:] = 0 #zeroes out the whole array

r2 = r[:3,:3] #creates a shallow copy of r
r_copy = r.copy()  #creates a deep copy of r


test = np.random.randint(0, 10, (4,3)) #creates a 4 by 3 array with values from 0 to 9
for i, row in enumerate(test): #loops data structure with index
    print('row', i, 'is', row)
#row 0 is [6 0 6]
#row 1 is [6 7 3]
#row 2 is [7 4 4]
#row 3 is [9 2 9]


test2 = test**2
#array([[36,  0, 36],
#       [36, 49,  9],
#       [49, 16, 16],
#       [81,  4, 81]])
for i, j in zip(test, test2): #loops two data structures at the same time
    print(i,'+',j,'=',i+j)

# [6 0 6] + [36  0 36] = [42  0 42]
# [6 7 3] + [36 49  9] = [42 56 12]
# [7 4 4] + [49 16 16] = [56 20 20]
# [9 2 9] + [81  4 81] = [90  6 90]  