'''
csvHandler test
'''

import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from lib.csvHandler import csvHandler

csvHandlerObj = csvHandler()
directory = "/Users/paullemanh/Dev/nostalgia_detection/tests/csvHandler/"

#Test with a csv file in English
enTestFilePath = directory+'test_english.csv'

#Print some rows of the csv file
print('---Print 1 row---')
csvHandlerObj.printCsvRows(enTestFilePath, 1)
print('---Print 2 rows---')
csvHandlerObj.printCsvRows(enTestFilePath, 2)
print('---Print 3 rows---')
csvHandlerObj.printCsvRows(enTestFilePath, 3)

#Test with a csv file in French

frTestFilePath = directory+'test_french.csv'
print('---Print 1 row---')
csvHandlerObj.printCsvRows(frTestFilePath, 1)
print('---Print 2 rows---')
csvHandlerObj.printCsvRows(frTestFilePath, 2)
print('---Print 3 rows---')
csvHandlerObj.printCsvRows(frTestFilePath, 3)

#Test conversion csv to list

frTestFilePath = directory+'morocco_french.csv'
output = csvHandlerObj.csvToListBis(frTestFilePath)
print('---Print the list---')
print(output)

#Test on real corpus

directory = "/Users/paullemanh/Dev/nostalgia_detection/data/corpus/"
corpusFilePath = directory+'moroccan_corpus.csv'
print('---Print 3 first rows of the moroccan corpus---')
csvHandlerObj.printCsvRows(corpusFilePath, 3)

#Test print verbatims in a csv file

directory = "/Users/paullemanh/Dev/nostalgia_detection/tests/csvHandler/"
filePath = directory+"csv_test.csv"
listOfVerbs = [{'tokens': [u'le', u'maroc', u'me', u'manque', u'manqu', u',', u'j', u"'aimerais", u"'aim", u'y', u'retourner', u'retourn', u'!'], 
'sentenceID': u'0', 'url': u'http://website2', 'entity': u'16739', 'content': u"Le Maroc me manque, j'aimerais y retourner!", 
'matchedWordsList': [[u'manque', u'manqu'], [u'maroc']], 'matched': True}, 
{'tokens': [u'je', u'suis', u'un', u'peu', u'nostalgique', u'nostalg', u'en', u'ce', u'moment', u'...'], 'sentenceID': u'1', 'url': u'http://website2', 
'entity': u'16739', 'content': u'Je suis un peu nostalgique en ce moment...', 'matchedWordsList': [[], []], 'matched': False}]
csvHandlerObj.listOfVerbsToCsv(listOfVerbs, [u"nostalgia", u"morocco"], filePath)
