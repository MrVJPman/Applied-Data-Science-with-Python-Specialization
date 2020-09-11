#Working with Text Data in pandas

import pandas as pd

time_sentences = ["Monday: The doctor's appointment is at 2:45pm.", 
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]

df = pd.DataFrame(time_sentences, columns=['text'])

#-----------------------------------------------------------------
df['text'].str.len() #length of of each text
#0    46
#1    50
#2    49
#3    49
#4    54
#Name: text, dtype: int64





#-----------------------------------------------------------------
df['text'].str.split().str.len() #number of tokens
#0    7
#1    8
#2    8
#3    10
#4    10
#Name: text, dtype: int64


#-----------------------------------------------------------------
df['text'].str.contains('appointment') #whether each text contains the word 'appointment'
#0    True
#1    True
#2    False
#3    False
#4    False
#Name: text, dtype: bool


#-----------------------------------------------------------------
df['text'].str.count(r'\d') #count number of digits
#0    3
#1    4
#2    3
#3    4
#4    8
#Name: text, dtype: int64




#-----------------------------------------------------------------
df['text'].str.findall(r'\d') #displays all numbers in order of their appearance
#0                   [2, 4, 5]
#1                [1, 1, 3, 0]
#2                   [7, 0, 0]
#3                [1, 1, 1, 5]
#4    [0, 8, 1, 0, 0, 9, 0, 0]
#Name: text, dtype: object




#-----------------------------------------------------------------
df['text'].str.findall(r'\d') #displays all numbers in order of their appearance
#0                   [2, 4, 5]
#1                [1, 1, 3, 0]
#2                   [7, 0, 0]
#3                [1, 1, 1, 5]
#4    [0, 8, 1, 0, 0, 9, 0, 0]
#Name: text, dtype: object




#-----------------------------------------------------------------
df['text'].str.findall(r'(\d?\d):(\d\d)') # retrieve hour followed by times
#0               [(2, 45)]
#1              [(11, 30)]
#2               [(7, 00)]
#3              [(11, 15)]
#4    [(08, 10), (09, 00)]
#Name: text, dtype: object



#-----------------------------------------------------------------
df['text'].str.replace(r'\w+day\b', '???') # replace weekdays with '???'
#0          ???: The doctor's appointment is at 2:45pm.
#1       ???: The dentist's appointment is at 11:30 am.
#2          ???: At 7:00pm, there is a basketball game!
#3         ???: Be back home by 11:15 pm at the latest.
#4    ???: Take the train at 08:10 am, arrive at 09:...
#Name: text, dtype: object




#-----------------------------------------------------------------
df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3])# replace weekdays with 3 letter abbrevations
#0          Mon: The doctor's appointment is at 2:45pm.
#1       Tue: The dentist's appointment is at 11:30 am.
#2          Wed: At 7:00pm, there is a basketball game!
#3         Thu: Be back home by 11:15 pm at the latest.
#4    Fri: Take the train at 08:10 am, arrive at 09:...
#Name: text, dtype: object



#-----------------------------------------------------------------
# create two new columns from hour and minutes
df['text'].str.extract(r'(\d?\d):(\d\d)')
#       0	1
#0	2	45
#1	11	30
#2	7	00
#3	11	15
#4	08	10


#-----------------------------------------------------------------
df['text'].str.extractall(r'((\d?\d):(\d\d) ?([ap]m))') # extract the entire time, the hours, the minutes, and the period
#               0	         1	 2	3
#       match				
#0	0	2:45pm	         2	45	pm
#1	0	11:30 am	11	30	am
#2	0	7:00pm	         7	00	pm
#3	0	11:15 pm	11	15	pm
#4	0	08:10 am	08	10	am
#       1	09:00am	        09	00	am



#-----------------------------------------------------------------
# Do the same as above but name the columns
df['text'].str.extractall(r'(?P<time>(?P<hour>\d?\d):(?P<minute>\d\d) ?(?P<period>[ap]m))')
#               time	         hour	 minute	period
#       match				
#0	0	2:45pm	         2	45	pm
#1	0	11:30 am	11	30	am
#2	0	7:00pm	         7	00	pm
#3	0	11:15 pm	11	15	pm
#4	0	08:10 am	08	10	am
#       1	09:00am	        09	00	am

