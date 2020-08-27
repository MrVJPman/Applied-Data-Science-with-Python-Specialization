import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])

#creating new columns
df['Date'] = ['December 1', 'January 1', 'mid-May']
df['Delivered'] = True #all the values set to True
df['Feedback'] = ['Positive', None, 'Negative'] #set a row with None

adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
adf['Date']
#0    December 1
#1           NaN
#2       mid-May
#Name: Date, dtype: object





staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')


#Join on the indexes
pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True) #all rows froms staff/student
pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True) #intersected rows froms staff/student
pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)  #all rows froms staff 
pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True) #all rows froms student


#Join on the column 
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
#same as pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True



staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
#Creates new column location_x and location_y 



staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
#Multi Merges from two joining 


    #Price	Product
#Product ID		
#4109	5.0	Sushi Roll
#1412	0.5	Egg
#8931	1.5	Bagel

    #Customer	Product ID	Quantity
#0	Ali	        4109	        1
#1	Eric	        1412	        12
#2	Ande	        8931	        6
#3	Sam	        4109	        2


answer = pd.merge(products, invoices, how = "outer", left_index=True, right_on='Product ID')

#=========================================Idiomatic Pandas: Making Code Pandorable=========================================

print(df.head())

#idiom 1 : Avoid ][

#idiom 2: method chaining 

(df.where(df['SUMLEV']==50)
 .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

#same as below
#df = df[df['SUMLEV']==50]
#df.set_index(['STNAME','CTYNAME'], inplace=True)
#df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})


#method chaining to modify the DataFrame df in one statement to drop any entries where 'Quantity' is 0 
#rename the column 'Weight' to 'Weight (oz.)'?
print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))



import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                    'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
#        This method also creates a new dataframe with max/min
#        row['max'] = np.max(data)
#        row['min'] = np.min(data)
#        return row
    return pd.Series({'min': np.min(data), 'max': np.max(data)})


df.apply(min_max, axis=1)
#applies min_max on df,
#obtains the min and max from the six years

#lambda method
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)

#=========================================Group by=========================================
import pandas as pd
import numpy as np


for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))


#Use groupby to group the dataframe, and apply a function to calculate the total weight (Weight x Quantity) by category.        
print(df.groupby('Category').apply(lambda dataframe,a,b: sum(dataframe[a] * dataframe[b]), 'Weight (oz.)', 'Quantity'))

# def totalweight(dataframe, w, q):
#        return sum(df[w] * df[q])
#        
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))    

df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')
#There are 1177 records in group 0 for processing.
#There are 1134 records in group 1 for processing.
#There are 831 records in group 2 for processing.

#fun is called with df ass item
#frame is # of rows
#group is the output 

#For each set of rows grouped by STNAME, find the average population in 2010
df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

#For each set of rows grouped by STNAME, find the average and total population in 2010
#'2010 average' and "'2010 total' are the column names
#level =0 specify the level of index we're using. In this case STNAME is the only level that exists
#https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.groupby.html
(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
    .agg({'2010 average': np.average, '2010 total': np.sum}))

#For each set of rows grouped by STNAME, find both the average and total population in 2010, 2011
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'averages': np.average, 'totals': np.sum}))
#4 columns total

#For each set of rows grouped by STNAME, find both the average population in 2010
#and the total population in 2011
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))
#2 columns total

#=========================================Scales=========================================

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)

#               Grades
#excellent	A+
#excellent	A
#excellent	A-
#good	B+
#good	B
#good	B-
#ok	C+
#ok	C
#ok	C-
#poor	D+
#poor	D

#Changes the type to category, present in ascending order
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)

grades > 'C'
#excellent     True
#excellent     True
#excellent     True
#good          True
#good          True
#good          True
#ok            True
#ok           False
#ok           False
#poor         False
#poor         False
#Name: Grades, dtype: bool


s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

# Your code here
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
#Try casting this series to categorical with the ordering Low < Medium < High.
s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)




#Suppose we have a series that holds height data for jacket wearers. Use pd.cut to bin this data into 3 bins.
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
# Your code here
pd.cut(s,3)
# You can also add labels for the sizes [Small < Medium < Large].
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])


df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10) 
#Create 10 ranges of values from the minimum/maximum 
#and then place the average values in these ranges

#=========================================Pivot Tables=========================================

#The rows are for each of the YEAR within the column YEAR
#The columns are each of the labels within the column Make
#The values at the row/column is the average (kW)
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)

#margins=True : Value for all of them 
#df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)


#Create a pivot table that shows the mean price and mean rating for every 'Manufacturer' / 'Bike Type' combination.
print(Bikes)

# Your code here
Bikes.pivot_table(values=["Price", "Rating"], index='Bike Type', columns='Manufacturer', aggfunc=np.mean)
#IBM solution
print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))


#=========================================Date Functionality in Pandas=========================================

pd.Timestamp('9/1/2016 10:05AM') #Creates a timestamp

#Creates a Period
pd.Period('1/2016')
pd.Period('3/5/2016')

t1 = pd.Series(['a', 'b', 'c'], [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
#2016-09-01    a
#2016-09-02    b
#2016-09-03    c
#dtype: object

type(t1.index)
#pandas.tseries.index.DatetimeIndex

t2 = pd.Series(['d', 'e', 'f'], [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
#2016-09    d
#2016-10    e
#2016-11    f
#Freq: M, dtype: object

type(t2.index)
#pandas.tseries.period.PeriodIndex


d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
                #a	b
#2 June 2013	18	52
#Aug 29, 2014	68	44
#2015-06-26	66	33
#7/12/16	54	85

ts3.index = pd.to_datetime(ts3.index) #Converts the data indexes to a different format
                #a	b
#2013-06-02	18	52
#2014-08-29	68	44
#2015-06-26	66	33
#2016-07-12	54	85

pd.to_datetime('4.7.12', dayfirst=True)
#Timestamp('2012-07-04 00:00:00')

pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')
#Timedelta('2 days 00:00:00') --> This is a difference

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')
#Timestamp('2016-09-14 11:10:00') --> This is a particular time

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
#DatetimeIndex(['2016-10-02', '2016-10-16', '2016-10-30', '2016-11-13',
#               '2016-11-27', '2016-12-11', '2016-12-25', '2017-01-08',
#               '2017-01-22'],
#              dtype='datetime64[ns]', freq='2W-SUN')

df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
              #Count 1	Count 2
#2016-10-02	104	125
#2016-10-16	109	122
#2016-10-30	111	127
#2016-11-13	117	126
#2016-11-27	114	126
#2016-12-11	109	121
#2016-12-25	105	126
#2017-01-08	105	125
#2017-01-22	101	123

df.index.weekday_name
#array(['Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday', 'Sunday',
#       'Sunday', 'Sunday', 'Sunday'], dtype=object)
 
df.diff()

           #Count 1	Count 2
#2016-10-02	NaN	NaN
#2016-10-16	5.0	-3.0
#2016-10-30	2.0	5.0
#2016-11-13	6.0	-1.0
#2016-11-27	-3.0	0.0
#2016-12-11	-5.0	-5.0
#2016-12-25	-4.0	5.0
#2017-01-08	0.0	-1.0
#2017-01-22	-4.0	-2.0

df.resample('M').mean() #Every month
              #Count 1	Count 2
#2016-10-31	108.0	124.666667
#2016-11-30	115.5	126.000000
#2016-12-31	107.0	123.500000
#2017-01-31	103.0	124.000000
       
df['2017'] 
            #Count 1	Count 2
#2017-01-08	105	125
#2017-01-22	101	123
df['2016-12']
            #Count 1	Count 2
#2016-12-11	109	121
#2016-12-25	105	126
df['2016-12':]
            #Count 1	Count 2
#2016-12-11	109	121
#2016-12-25	105	126
#2017-01-08	105	125
#2017-01-22	101	123

df.asfreq('W', method='ffill') 
#change the weeks
#also forward fill the missing Count Values

              #Count 1	Count 2
#2016-10-02	97	120
#2016-10-09	97	120
#2016-10-16	104	123
#2016-10-23	104	123
#2016-10-30	101	120
#2016-11-06	101	120
#2016-11-13	107	126
#2016-11-20	107	126
#2016-11-27	107	120
#2016-12-04	107	120
#2016-12-11	110	125
#2016-12-18	110	125
#2016-12-25	115	124
#2017-01-01	115	124
#2017-01-08	115	125
#2017-01-15	115	125
#2017-01-22	122	129

import matplotlib.pyplot as plt
#%matplotlib inline

df.plot()