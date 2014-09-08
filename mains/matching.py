# -*- coding: utf-8 -*-
#Author: Paul Le Manh

import csv
import sys
import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from algos.tokenizer import tokenizer
from algos.lexicalExtractor import lexicalExtractor
from algos.corpusMatcher import corpusMatcher  
from algos.binaryClassifier import binaryClassifier
from algos.trainBinaryClassifier import trainBinaryClassifier
from lib.csvHandler import csvHandler
import pickle

def fromAnnotedDataToClassifier(annotedData):
    '''
    This function creates a classifier from annoted data.
    annotedData complies with the following structure: [["verbatim", annotation],...,["verbatim", annotation]]
    '''
    listOfVerbatims = []
    listOfAnnotations = []
    for row in annotedData:
        listOfVerbatims.append(row[0])
        listOfAnnotations.append(int(row[1]))        
    trainBinaryClassifierObj = trainBinaryClassifier(listOfVerbatims, listOfAnnotations)
    countVectorizer, tfidfTransformer, classifier = trainBinaryClassifierObj.train()
    listOfTransformers = [countVectorizer, tfidfTransformer]
    binaryClassifierObj = binaryClassifier(listOfTransformers, classifier)
    return binaryClassifierObj


if __name__ == "__main__":

    
    csvHandlerObj = csvHandler()
    directory = '/Users/paullemanh/Dev/nostalgia_detection/data/'
    
    ###Dictionaries###
    
    nostalgiaDict = csvHandlerObj.csvToListBis(directory+'dictionaries/nostalgia_french_moroccan.csv')
    moroccoDict = csvHandlerObj.csvToListBis(directory+'dictionaries/morocco_french.csv')
    
    ###Machine Learning models###
    
    #Noise classification
    annotedNoise = pickle.load(open(directory+'machine_learning/noise_classification/learning_corpus/annotedNoise.p', 'rb'))
    noiseClassifierObj = fromAnnotedDataToClassifier(annotedNoise)
    #Nostalgia classification
    annotedNostalgia = csvHandlerObj.csvToList(directory+'machine_learning/nostalgia_classification/learning_corpus/annotedNostalgia.csv')
    nostaClassifierObj = fromAnnotedDataToClassifier(annotedNostalgia)
        
    ###Creating tokenizer###
    tokenizerObj = tokenizer('french', stemming=True)
    
    ###Creating lexical extractor###
    lexicalExtractorObj = lexicalExtractor([nostalgiaDict, moroccoDict], 'french', stemming=True)
    
    ###Creating corpus matcher###
    corpusMatcherObj = corpusMatcher('french', tokenizerObj, lexicalExtractorObj, noiseClassifier = noiseClassifierObj, nostaClassifier = nostaClassifierObj, avoidDuplications = True)
    
    ###Loading Web content###
    corpus = csvHandlerObj.generateCsv(directory+'corpus/moroccan_corpus.csv')
    
    frequency = 1 #this number defines in which proportion the corpus will be explored. Example: if frequency = 1, the whole corpus will be explored; if frequency = 10, only 1/10 of the webentities will be explored.
    listOfMatchedVerbatims = corpusMatcherObj.processCorpus(corpus, frequency)
    csvHandlerObj.listOfVerbsToCsv(listOfMatchedVerbatims, [u"nostalgia", u"morocco"], directory+'results/moroccan_corpus/listOfMatchedVerbatims_frequency%d.csv' % frequency)

    