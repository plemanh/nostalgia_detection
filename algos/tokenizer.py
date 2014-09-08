# -*- coding: utf-8 -*-
#Author: Paul Le Manh

import nltk
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.stem import SnowballStemmer

class tokenizer(object):
    '''
    This object will tokenize a verbatim into sentences and sentences into tokens with stems as an option
    '''
    def __init__(self, lang, stemming = False):
        '''
        lang must be given in a string (ex: 'english', 'french', etc...)
        '''
        self._sentenceTokenizer = nltk.data.load('tokenizers/punkt/'+lang+'.pickle')
        self._wordTokenizer = PunktWordTokenizer()
        self._stemming = stemming
        if stemming:
            self._stemmer = SnowballStemmer(lang)
    
    def getSentences(self, text):
        sentences = self._sentenceTokenizer.tokenize(text)
        return sentences
        
    def getTokens(self, sentence):
        words = self._wordTokenizer.tokenize(sentence)
        tokens = []
        for word in words:
            tokens.append(word.lower())
        if self._stemming:
            newTokens = []
            for token in tokens:
                stem = self._stemmer.stem(token)
                newTokens.append(token)
                if stem != token:
                    newTokens.append(stem)
            tokens = newTokens
        return tokens