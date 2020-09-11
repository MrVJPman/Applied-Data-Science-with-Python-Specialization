#Write code that would extract hashtags from the following tweet:

tweet = "@nltk Text analysis is awesome! #regex #pandas #python"

print([t for t in tweet.split(' ') if t.startswith('#')])
#print([word for word in tweet.split() if word.startswith('#')])

#-----------------------------------------------------------------

import re # import re - a module that provides support for regular expressions

[w for w in text8 if re.search('@[A-Za-z0-9_]+', w)]

[w for w in text8 if re.search('@\w+', w)]

#Start with "@"
#[]+ : contains 1 or more
#Has A-Za-z0-9

#===================================================================
#-----------------------------------------------------------------