'''
test corpusMatcher
'''
import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from algos.corpusMatcher import corpusMatcher
from algos.tokenizer import tokenizer
from algos.lexicalExtractor import lexicalExtractor


tokenizerObj = tokenizer('french', stemming=True)
nostalgiaDict = [u"manque"]
moroccoDict = [u"maroc"]
lexicalExtractorObj = lexicalExtractor([nostalgiaDict, moroccoDict], 'french', stemming=True)
corpusMatcherObj = corpusMatcher('french', tokenizerObj, lexicalExtractorObj)

#Language detection
print('---Language detection---')
text = u"Ceci est un texte de test"
lang = corpusMatcherObj.getLanguage(text)
print(text)
print(lang)
text = u"This is a test"
lang = corpusMatcherObj.getLanguage(text)
print(text)
print(lang)
text = u"Eso es un test"
lang = corpusMatcherObj.getLanguage(text)
print(text)
print(lang)

#Row processing
print('---Row Processing---')
row = [u"16738", u"http://website1", u"J'aime le maroc, c'est un pays magnifique! Mais je suis bien en France aussi. En fait je pense que je pourrais vivre n'importe ou."]
listOfVerbs = corpusMatcherObj.processRow(row)
print(listOfVerbs)
row = [u"16739", u"http://website2", u"Le Maroc me manque, j'aimerais y retourner! Je suis un peu nostalgique en ce moment..."]
listOfVerbs = corpusMatcherObj.processRow(row)
print(listOfVerbs)

#Corpus processing
print('---Corpus Processing---')
corpus = [[u"16738", u"http://website1", u"J'aime le maroc, c'est un pays magnifique! Mais je suis bien en France aussi. En fait je pense que je pourrais vivre n'importe ou."], 
[u"16739", u"http://website2", u"Le Maroc me manque, j'aimerais y retourner! Je suis un peu nostalgique en ce moment..."], 
[u"16740", u"http://website3", u"I love my country and I miss it so much... I wish I had a few holidays so that I could go back for a while."]]
print('-Corpus-')
print(corpus)
listOfMatchedVerbatims = corpusMatcherObj.processCorpus(corpus)
print('-ListOfMatchedVerbs-')
print(listOfMatchedVerbatims)
