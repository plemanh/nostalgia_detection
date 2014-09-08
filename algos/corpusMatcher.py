# -*- coding: utf-8 -*-
#Author: Paul Le Manh

from nltk.corpus import stopwords   # stopwords to detect language

class corpusMatcher(object):
    def __init__(self, lang, tokenizerObj, lexicalExtractorObj, noiseClassifier = None, nostaClassifier = None, avoidDuplications = False):
        '''
        This class is used to explore a corpus and detect sentences with nostalgia. 
        Arguments: corpus language, tokenizer used to tokenize corpus into sentences, lexicalExtractor used to extract some given words from a sentence, and optionnaly noise and nostalgia classifiers
        input : corpus = [[u"webEntity", u"url", u"text"], ... ]
        output : list of verbatims = dico {u"webentity", u"url", u"sentenceID", u"text", u"tokens", matched (True or False) , listOfmatchedWords}
        '''
        self._lang = lang
        self._tokenizerObj = tokenizerObj
        self._lexicalExtractorObj = lexicalExtractorObj 
        self._noiseClassifier = noiseClassifier
        self._nostaClassifier = nostaClassifier
        self._avoidDuplications = avoidDuplications
    
    def _getLanguageLikelihood(self, inputText):
        """
        Return a dictionary of languages and their likelihood of being the
        natural language of the input text
        """
    
        tokens = self._tokenizerObj.getTokens(inputText) 
    
        languageLikelihood = {}
        for language in stopwords._fileids:
            languageLikelihood[language] = len(set(tokens) &
                    set(stopwords.words(language)))
        return languageLikelihood
    
    def getLanguage(self, inputText):
        """
        Return the most likely language of the given text
        """
        likelihoods = self._getLanguageLikelihood(inputText)
        return sorted(likelihoods, key=likelihoods.get, reverse=True)[0]
    
    
    def processRow(self, row):
        '''
        this function processes one row of the corpus.
        input : row = [u"webentity", u"url", u"content"]
        output: list of verbatims = dico {u"webentity", u"url", u"sentenceID", u"content", u"tokens", matched (True or False) , matchedWordsList}
        '''
        listOfVerbs = []
        sentences = self._tokenizerObj.getSentences(row[2])
        sentenceID = 0
        for sentence in sentences:
            verbatim = {}
            verbatim['entity'] = row[0]
            verbatim['url'] = row[1]
            verbatim['sentenceID'] = unicode(sentenceID)
            verbatim['content'] = sentence
            tokens = self._tokenizerObj.getTokens(sentence)
            verbatim['tokens'] = tokens
            matched, matchedWordsList = self._lexicalExtractorObj.processTokens(tokens)
            verbatim['matched'] = matched
            verbatim['matchedWordsList'] = matchedWordsList
            listOfVerbs.append(verbatim)
            sentenceID += 1
        return listOfVerbs
        
    def processCorpus(self, corpus, frequency):
        '''
        frequency = number of entities ignored between two processed entities
        '''
        listOfMatchedVerbatims = []
        if self._avoidDuplications:
            #If avoidDuplications is True, a list of matched contents is used to checker whether a content has already been matched so as to avoid duplications
            listOfMatchedContents = []
        for index, row in enumerate(corpus):
            if index%frequency == 0:
                print('---Web entity %d---' % index)
                verbLang = self.getLanguage(row[2])
                if verbLang == self._lang:
                    listOfVerbs = self.processRow(row)
                    for verbatim in listOfVerbs:
                        if self._noiseClassifier:
                            predictedLabel = self._noiseClassifier.predictLabel(verbatim['content'])
                            if predictedLabel == 0:
                                if verbatim['matched']:
                                    print('sentence matched.')
                                    if self._nostaClassifier:
                                        predictedLabelBis = self._nostaClassifier.predictLabel(verbatim['content'])
                                        if predictedLabelBis == 1:
                                            print("nostalgia detected.")
                                            if self._avoidDuplications:
                                                if verbatim['content'] not in listOfMatchedContents:
                                                    print("New verbatim appended.")
                                                    listOfMatchedVerbatims.append(verbatim)
                                                    listOfMatchedContents.append(verbatim['content'])
                                                else:
                                                    print("Content already detected.")
                                            else:
                                                print("New verbatim appended.")
                                                listOfMatchedVerbatims.append(verbatim)
                                        else:
                                            print("No nostalgia detected.")
                                    else:
                                        print("New verbatim appended.")
                                        listOfMatchedVerbatims.append(verbatim)
                            else:
                                print("Noise detected.")
                        else:
                            if verbatim['matched']:
                                print('sentence matched.')
                                listOfMatchedVerbatims.append(verbatim)
                else:
                    print("Other language found. This verbatim will not be taken into account.")
        return listOfMatchedVerbatims
        
  
            