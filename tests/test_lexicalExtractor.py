# -*- coding: utf-8 -*-
'''
test lexicalExtractor.py
'''

import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from algos.lexicalExtractor import lexicalExtractor
from lib.csvHandler import csvHandler

    
directory = '/Users/paullemanh/Dev/nostalgia_detection/data/'
csvHandlerObj = csvHandler()

nostalgiaDict = csvHandlerObj.csvToListBis(directory+'dictionaries/nostalgia_french_moroccan.csv')
moroccoDict = csvHandlerObj.csvToListBis(directory+'dictionaries/morocco_french.csv')

lexicalExtractorObj = lexicalExtractor([nostalgiaDict, moroccoDict], 'french', stemming=False)
lexicalExtractorObjStemming = lexicalExtractor([nostalgiaDict, moroccoDict], 'french', stemming=True)

print('---Dictionnaries---')
print('---Standard---')
wordListsList = lexicalExtractorObj.getWordListsList()
print(wordListsList)
print('---With Stemming---')
wordListsList = lexicalExtractorObjStemming.getWordListsList()
print(wordListsList)

print('---Match a list with tokens---')
matched, matchedWords = lexicalExtractorObjStemming.matchListWithTokens([u"this", u"is", u"a", u"test"], [u"is", u"test", u"te", u"blabla"])
print(matched)
print(matchedWords)

print('---Process a list of tokens---')
output, matchedWordsList = lexicalExtractorObjStemming.processTokens([u"j'", u"ai", u"eu", u"une", u"enfance", u"heureuse", u"au", u"maroc", u"qui", u"aujourd'hui", u"me", u"manque"])
print(output)
print(matchedWordsList)
output, matchedWordsList = lexicalExtractorObjStemming.processTokens([u"j'", u"aime", u"le", u"maroc"])
print(output)
print(matchedWordsList)