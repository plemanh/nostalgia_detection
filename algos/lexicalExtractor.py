# -*- coding: utf-8 -*-
#Author: Paul Le Manh

from nltk.stem import SnowballStemmer

class lexicalExtractor(object):
    '''
    This class will be used to extract some given words from a verbatim.
    Arguments: wordListsList complies with the following format: [[word1, word2, ...], [wordA, wordB, ...], ...] and sentences with at least one word in each list will be selected. 
    When stemming = True, SnowballStemmer is used to stem each word of the analysed sentences.
    '''
    def __init__(self, wordListsList, lang, stemming=False):
        tmp = []
        if stemming:
            self._stemmer = SnowballStemmer(lang)
        for l in wordListsList:
            tmp2 = []
            for word in l:
                word2 = word.lower()
                tmp2.append(word2)
                if stemming:
                    stem = self._stemmer.stem(word2)
                    if stem != word2:
                        tmp2.append(stem)
            tmp.append(tmp2)
        self._wordListsList = tmp
        self._numberOfLists = len(self._wordListsList)
                        
    def matchListWithTokens(self, tokens, matchingList):
        matchedWords = []
        matched = False
        for word in matchingList:
            if word in tokens:
                matched = True
                matchedWords.append(word)
                
        return matched, matchedWords
        
    def processTokens(self, tokens):
        '''
        input = list of tokens [word1, word2, ... ]
        output = True or False and list of matched words ([["word1", "word2",...], ["wordbis1", "wordbis2", ...], ...])
        '''     
        numberOfMatchedLists = 0
        matchedWordsList = []
        output = False
        
        for matchingList in self._wordListsList:
            matched, matchedWords = self.matchListWithTokens(tokens, matchingList)
            matchedWordsList.append(matchedWords)
            if matched:
                numberOfMatchedLists += 1  
                  
        if numberOfMatchedLists == self._numberOfLists:
            output = True   
        
        return output, matchedWordsList
    
    def getWordListsList(self):
        return self._wordListsList