# -*- coding: utf-8 -*-
#Author: Paul Le Manh

class binaryClassifier(object):
    '''
    This object will be used to classify verbatims into 2 categories
    Arguments: List of transformers [transformer1, transformer2, ...] used to transform text into vector and the classifier.
    '''
    def __init__(self, listOfTransformers, classifier):
        self._listOfTransformers = listOfTransformers
        self._classifier = classifier
        
    def _transformText(self, text):
        '''
        input: a string
        '''
        transformedText = [text]
        for transformer in self._listOfTransformers:
            transformedText = transformer.transform(transformedText)
        return transformedText
        
    def predictLabel(self, text):
        '''
        input: a string
        '''
        transformedText = self._transformText(text)
        prediction = self._classifier.predict(transformedText)
        labelPredicted = prediction[0]
        return labelPredicted