'''
trainBinaryClassifier test
'''
import pickle
import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from algos.trainBinaryClassifier import trainBinaryClassifier
from algos.binaryClassifier import binaryClassifier

directory = '/Users/paullemanh/Dev/nostalgia_detection/tests/trainBinaryClassifier/'

annotedNoise = pickle.load(open(directory+'annotedNoise.p', 'rb'))

listOfVerbatims = []
listOfAnnotations = []

for row in annotedNoise:
    listOfVerbatims.append(row[0])
    listOfAnnotations.append(row[1])
    
trainBinaryClassifierObj = trainBinaryClassifier(listOfVerbatims, listOfAnnotations)
countVectorizer, tfidfTransformer, classifier = trainBinaryClassifierObj.train()

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

print("%d successfull over %d verbatims analysed. (Test run on the training set.)" % (succeedPrediction, totalNumber))

