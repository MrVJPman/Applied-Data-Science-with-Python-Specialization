#Advanced NLP Tasks with NLTK

#========================POS TAGGING=================================
#---------------------------------------------------------------------
nltk.help.upenn_tagset('MD') #gets information about one of the tags
#MD: modal auxiliary
#    can cannot could couldn't dare may might must need ought shall should
#    shouldn't will would


#---------------------------------------------------------------------

tokenized_words = nltk.word_tokenize("Children shouldn't drink a sugary drink before bed.")
nltk.pos_tag(tokenized_words)
#[('Children', 'NNP'),
# ('should', 'MD'),
# ("n't", 'RB'),
# ('drink', 'VB'),
# ('a', 'DT'),
# ('sugary', 'JJ'),
# ('drink', 'NN'),
# ('before', 'IN'),
# ('bed', 'NN'),
# ('.', '.')]

text14 = nltk.word_tokenize("Visiting aunts can be a nuisance")
nltk.pos_tag(text14)
#[('Visiting', 'VBG'),
# ('aunts', 'NNS'),
# ('can', 'MD'),
# ('be', 'VB'),
# ('a', 'DT'),
# ('nuisance', 'NN')]

#---------------------------------------------------------------------

# Parsing sentence structure
text15 = nltk.word_tokenize("Alice loves Bob")
grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text15)
for tree in trees:
    print(tree)
#(S (NP Alice) (VP (V loves) (NP Bob)))

#---------------------------------------------------------------------

text16 = nltk.word_tokenize("I saw the man with a telescope")
grammar1 = nltk.data.load('mygrammar.cfg')
"""
S -> NP VP
VP -> V NP | VP PP
PP -> P NP
NP -> DT N | DT N PP | 'I'
DT -> 'a' | 'the'
N -> 'man' | 'telescope'
V -> 'saw'
P -> 'with'
"""

parser = nltk.ChartParser(grammar1)
trees = parser.parse_all(text16)
for tree in trees:
    print(tree)
#(S
#  (NP I)
#  (VP
#    (VP (V saw) (NP (Det the) (N man)))
#    (PP (P with) (NP (Det a) (N telescope)))))

#(S
#  (NP I)
#  (VP
#    (V saw)
#    (NP (Det the) (N man) (PP (P with) (NP (Det a) (N telescope)))))


#---------------------------------------------------------------------

from nltk.corpus import treebank
text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
print(text17)

#(S
  #(NP-SBJ
    #(NP (NNP Pierre) (NNP Vinken))
    #(, ,)
    #(ADJP (NP (CD 61) (NNS years)) (JJ old))
    #(, ,))
  #(VP
    #(MD will)
    #(VP
      #(VB join)
      #(NP (DT the) (NN board))
      #(PP-CLR (IN as) (NP (DT a) (JJ nonexecutive) (NN director)))
      #(NP-TMP (NNP Nov.) (CD 29))))
  #(. .))
  
  
#========================POS tagging and parsing ambiguity=================================
  
text18 = nltk.word_tokenize("The old man the boat")
nltk.pos_tag(text18)
#[('The', 'DT'), ('old', 'JJ'), ('man', 'NN'), ('the', 'DT'), ('boat', 'NN')]

text19 = nltk.word_tokenize("Colorless green ideas sleep furiously")
nltk.pos_tag(text19)
#[('Colorless', 'NNP'),
# ('green', 'JJ'),
# ('ideas', 'NNS'),
# ('sleep', 'VBP'),
# ('furiously', 'RB')]