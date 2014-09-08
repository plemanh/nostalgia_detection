'''
binaryClassifier test
'''
import pickle
import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from algos.binaryClassifier import binaryClassifier

directory = '/Users/paullemanh/Dev/nostalgia_detection/tests/binaryClassifier/'

#Load classifier example 
classifier = pickle.load(open(directory+'classifier.p', 'rb'))
#Load features creators examples
countVectorizer = pickle.load(open(directory+'countVectorizer.p', 'rb'))
tfidfTransformer = pickle.load(open(directory+'tfidfTransformer.p', 'rb'))
#Load data set example
'''
format = [[content, label],[content, label],...]
'''
annotedNoise = pickle.load(open(directory+'annotedNoise.p', 'rb'))
    
#create binaryClasifier object
listOfTransformers = [countVectorizer, tfidfTransformer]
binaryClassifierObj = binaryClassifier(listOfTransformers, classifier)

#Estimate prediction quality
totalNumber = 0
succeedPrediction = 0
for row in annotedNoise:
    predictedLabel = binaryClassifierObj.predictLabel(row[0])
    if predictedLabel == row[1]:
        succeedPrediction += 1
    totalNumber += 1

print("%d successfull over %d verbatims analysed" % (succeedPrediction, totalNumber))

