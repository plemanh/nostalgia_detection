# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm, grid_search
import numpy as np

class trainBinaryClassifier(object):
    '''
    arguments: list of verbatims, list of annotations (0 or 1)
    This object will include a function used to return a classifier as well as features transformers (countvectorizer and tfidf)
    '''
    def __init__(self, listOfVerbatims, listOfAnnotations):
        self._listOfVerbatims = listOfVerbatims
        self._listOfAnnotations = listOfAnnotations
        
    def train(self):
        labels = np.asarray(self._listOfAnnotations)
        vectorizer = CountVectorizer()
        X_counts = vectorizer.fit_transform(self._listOfVerbatims)
        tfidf_transformer = TfidfTransformer()
        X_tfidf = tfidf_transformer.fit_transform(X_counts)
        parameters = [{'kernel':('linear', 'rbf'), 'C':[1, 10], 'class_weight':['auto', None]}]
        svr = svm.SVC()
        clf = grid_search.GridSearchCV(svr, parameters)
        clf.fit(X_tfidf, labels)
        return vectorizer, tfidf_transformer, clf