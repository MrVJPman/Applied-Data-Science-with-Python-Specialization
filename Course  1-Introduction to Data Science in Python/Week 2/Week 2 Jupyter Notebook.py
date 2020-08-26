import pandas as pd

#==========================================The Series Data Structure========================================

animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)
#0    Tiger
#1     Bear
#2    Moose
#dtype: object <-- Notice this is an object

numbers = [1, 2, 3]
pd.Series(numbers)
#0    1
#1    2
#2    3
#dtype: int64 <-- Notice int64

animals = ['Tiger', 'Bear', None]
pd.Series(animals)
#0    Tiger
#1     Bear
#2    None
#dtype: object <-- Notice this is an object

numbers = [1, 2, None]
pd.Series(numbers)
#0    1.0
#1    2.0
#2    NaN
#dtype: float64 <-- Notice float64 despite integers

import numpy as np
np.nan == None #False
np.nan == np.nan #also False
np.isnan(np.nan) #True


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
#Archery           Bhutan
#Golf            Scotland
#Sumo               Japan
#Taekwondo    South Korea
#dtype: object

s.index
#Index(['Archery', 'Golf', 'Sumo', 'Taekwondo'], dtype='object')

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
#India      Tiger
#America     Bear
#Canada     Moose
#dtype: object

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
#Golf      Scotland
#Sumo         Japan
#Hockey         NaN
#dtype: object

#Notice that all indexes are created, but all values are left ignored

#==========================================Querying a Series========================================

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)

s.iloc[3] #same thing as s[3]
s.loc['Golf'] #same thing as s['Golf']


sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
#s[0] #error
s.iloc[0]


s = pd.Series([100.00, 120.00, 101.00, 3.00])
import numpy as np
print(np.sum(s))  #way faster than a for loop

#this creates a big series of 10000 random numbers from 0 to 9999
s = pd.Series(np.random.randint(0,1000,10000))
s+=2 #adds two to each item in s using broadcasting

for label, value in s.iteritems():
    s.set_value(label, value+2) #change every value in s by two
#    s.loc[label] = value+2 #does the same thing

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
#0             1
#1             2
#2             3
#Animal    Bears
#dtype: object

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
#Archery           Bhutan
#Golf            Scotland
#Sumo               Japan
#Taekwondo    South Korea
#dtype: object

cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
#Cricket    Australia
#Cricket     Barbados
#Cricket     Pakistan
#Cricket      England
#dtype: object

all_countries
#Archery           Bhutan
#Golf            Scotland
#Sumo               Japan
#Taekwondo    South Korea
#Cricket        Australia
#Cricket         Barbados
#Cricket         Pakistan
#Cricket          England
#dtype: object

all_countries.loc['Cricket']
#Cricket        Australia
#Cricket         Barbados
#Cricket         Pakistan
#Cricket          England
#dtype: object

#==========================================The DataFrame Data Structure========================================

import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

#Getting all the item purchased
df['Item Purchased']

df.loc['Store 2']
#Cost                      5
#Item Purchased    Bird Seed
#Name                  Vinod
#Name: Store 2, dtype: object

type(df.loc['Store 2'])
#pandas.core.series.Series

df.loc['Store 1']
#               Cost	Item Purchased	Name
#Store 1	22.5	Dog Food	Chris
#Store 1	2.5	Kitty Litter	Kevyn

df.loc['Store 1', 'Cost']
#Store 1    22.5
#Store 1     2.5
#Name: Cost, dtype: float64

df.loc['Store 1']['Cost'] #Avoid this chaining approach. This creates a copy, not a view.
#Store 1    22.5
#Store 1     2.5
#Name: Cost, dtype: float64

df.loc[:,['Name', 'Cost']] #All rows, only "name" and "cost" columns
#    Name	Cost
#Store 1	Chris	22.5
#Store 1	Kevyn	2.5
#Store 2	Vinod	5.0

copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df
#    Cost	Item Purchased	Name
#Store 2	5.0	Bird Seed	Vinod


#CREATE a new column
df['Location'] = None 

#UPDATE :applying a discount of 20% across all the values in the 'Cost' column?
df["Cost"] *= 0.8

#DELETE a column
del copy_df['Name'] 

#Tranpose
df.T

#==========================================Dataframe Indexing and Loading========================================

costs = df['Cost']
costs+=2
df
#    Cost	Item Purchased	Name	Location
#Store 1	24.5	Dog Food	Chris	None
#Store 1	4.5	Kitty Litter	Kevyn	None
#Store 2	7.0	Bird Seed	Vinod	None

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1) 
#make the index as the first column
#skip the first row 

#all the columns 
df.columns 

#renaming the column names
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
#    if col[:1]=='':
#        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

#==========================================Querying a DataFrame========================================

#creates a SERIES with (True/False) of all indexes for this condition
df['Gold'] > 0

#creates a new dataframe where the rows of indexs with False are all set to NaN
only_gold = df.where(df['Gold'] > 0)

#count the number of rows for this column, ignoring all rows with NaN
only_gold['Gold'].count()
df['Gold'].count()

#remove all NaN
only_gold = only_gold.dropna()

#Creates a new DATAFRAME where the for the column gold, the rows are greater than 0
only_gold = df[df['Gold'] > 0]

#Get the total length of rows 
len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])

#Creates a VIEW on DATAFRAME where a country won 0 gold in the summer, but more tan 0 in the winter
df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


# Names of people who bought products worth more than $3.00.
#solution 1 : 
df["Name"][df["Cost"] > 3]
#solution 2 : 
df[df["Cost"] > 3]["Name"]



#==========================================Indexing Dataframes========================================

#creates a new column from the index
df['country'] = df.index

#sets the index values as the values from column "Gold"
df = df.set_index('Gold')

#resets the index to be just integers starting from 0
df = df.reset_index()

#Creates an array of all the unique values of the column SUMLEV
df['SUMLEV'].unique()

#sets the index to STNAME then CTYNAME
df = df.set_index(['STNAME', 'CTYNAME'])

#retrieve the rows from the combined index. This is a SERIES.
df.loc['Michigan', 'Washtenaw County']

#retrieve the rows from the combined index. This is a DATAFRAME
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]




purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

#Reindex the purchase records DataFrame to be indexed hierarchically, first by store, then by person. 
#Name these indexes 'Location' and 'Name'.
df['Location'] = df.index
df = df.set_index(['Location', 'Name'])
#Then add a new entry to it with the value of:
#Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.

data = {'Cost': 3.00, 'Item Purchased': 'Kitty Food'}
purchase_4 = pd.Series(data, name=('Store 2', 'Kevyn'))
df.append(purchase_4)

#df = df.set_index([df.index, 'Name'])
#df.index.names = ['Location', 'Name']
#df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))


#==========================================Missing values========================================

#sort the index in ascending order
df = df.sort_index()  

#Forward Filling : replace all NaN values with the last non-NaN value
df = df.fillna(method='ffill')