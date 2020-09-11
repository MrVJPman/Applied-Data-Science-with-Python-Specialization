import nltk
#nltk.download("book")
from nltk.book import *

len(set(text7)) #unique # of words
list(set(text7))[:10] #first 10 words

#==========================Frequency of words==========================

dist = FreqDist(text7) #create a dictionary of every word with their frequencies
vocab1 = dist.keys() #All the words in a text 
dist['four'] #frequency of "four"
#list of words that are greater than 5 letters and at least greater than 100
freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 100] 


#==========================Normalization and stemming==========================

porter = nltk.PorterStemmer()
[porter.stem(t) for t in "list listed lists listing listings".split(' ')]
#['list', 'list', 'list', 'list', 'list']

#==========================Lemmatization==========================

udhr = nltk.corpus.udhr.words('English-Latin1')

#Version 1: lemmatizes word to isolate only the prefix
[porter.stem(t) for t in udhr[:20]]

#Version 2: lemmatizes word but forms actual words 
WNlemma = nltk.WordNetLemmatizer()
[WNlemma.lemmatize(t) for t in udhr[:20]]

#==========================Tokenization==========================

nltk.word_tokenize("Children shouldn't drink a sugary drink before bed.")
#['Children',
# 'should',
# "n't", <------
# 'drink',
# 'a',
# 'sugary',
# 'drink',
# 'before',
# 'bed',
# '.'] <------

nltk.sent_tokenize("This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!")
#['This is the first sentence.',
# 'A gallon of milk in the U.S. costs $2.99.',
# 'Is this the third sentence?',
# 'Yes, it is!']