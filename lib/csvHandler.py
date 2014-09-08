'''
csvHandler
'''

import csv
import sys
import codecs
import cStringIO

class csvHandler(object):
    '''
    This class will be used to handle .csv files (ie convert .csv files to python list and conversely) and avoid encoding issues.
    '''
    def __init__(self, encoding="utf-8"):
        self._encoding = encoding

    def _increaseLimit(self):
        '''
        This script is used to increase the csv size limit to the max the system can afford 
        '''
        
        maxInt = sys.maxsize
        decrement = True 
        while decrement:
            # decrease the maxInt value by factor 10 
            # as long as the OverflowError occurs.
        
            decrement = False
            try:
                csv.field_size_limit(maxInt)
            except OverflowError:
                maxInt = int(maxInt/10)
                decrement = True  
        return    
    
    def generateCsv(self, filePath):
        self._increaseLimit()
        with open(filePath, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                unicodeRow = [unicode(cell, self._encoding) for cell in row]
                yield unicodeRow
        return
        
    def printCsvRows(self, filePath, numberOfRows):
        csvGenerator = self.generateCsv(filePath)
        count = 0
        for row in csvGenerator:
            if count < numberOfRows:
                print(row)
                count+=1
            else:
                break
        return
    
    def csvToList(self, filePath):
        '''
        output: [[], [], [], ...]
        '''
        csvGenerator = self.generateCsv(filePath)
        output = []
        for row in csvGenerator:
            output.append(row)
        return output
        
    def csvToListBis(self, filePath):
        '''
        When rows of the csv file contain only 1 element, this function gives in output a list [word1, word2, ...]
        '''
        csvGenerator = self.generateCsv(filePath)
        output = []
        for row in csvGenerator:
            if len(row[0]) > 0:
                output.append(row[0])
        return output
        
    def listToCsv(self, l, filePath):
        '''
        l must comply with the following template: [[], [], [], ..., []] where all elements are string
        '''            
        with open(filePath, 'w') as writingFile:
            writingFile.write(codecs.BOM_UTF8)
            writer = UnicodeWriter(writingFile)
            writer.writerows(l)
                 
    
    def listOfVerbsToCsv(self, listOfVerbs, matchedWordsListNames, filePath):
        '''
        verbatim complies with {u"webentity", u"url", u"sentenceID", u"content", u"tokens", matched (True or False) , matchedWordsList}
        matchedWordsListNames = [u"name of list1", u"name of list2", etc...]
        '''
        rows = []
        
        header = [u"Web Entity", "URL", "Sentence Index", "Content", "Matched"]
        for name in matchedWordsListNames:
            header.append(name)
        rows.append(header)
        
        for verbatim in listOfVerbs:
            row = []    
            row.append(verbatim['entity'])
            row.append(verbatim['url'])
            row.append(verbatim['sentenceID'])
            row.append(verbatim['content'])
            row.append(unicode(str(verbatim['matched']), "utf-8"))
            for matchedList in verbatim['matchedWordsList']:
                wordsString = u""
                for word in matchedList: 
                    wordsString = wordsString+" "+word
                row.append(wordsString)
            rows.append(row)
                    
        with open(filePath, 'w') as writingFile:
            writingFile.write(codecs.BOM_UTF8)
            writer = UnicodeWriter(writingFile)
            writer.writerows(rows)
            
    def annotedCsvToLearningData(self, filePath):
        csvGenerator = self.generateCsv(filePath)
        contents = []
        labels = []
        for row in csvGenerator:
                contents.append(row[0])
                labels.append(int(row[1]))
        return contents, labels
            
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)