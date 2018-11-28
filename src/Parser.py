'''

Parses a body of text for words, removind spaces, endline characters, and most
forms of punctuation.

'''


import re

class Parser():
    
    #Initializes the parser to have data that is a list of all of the words
    #in the file document fed in as a parameter; removes punctuation and endline
    #characters as well as spaces
    def __init__(self, fileName):
        self.data = []
        
        with open(fileName, encoding="utf8") as file:
            #Reading each line of the file
            line = file.readline()
            while line:
                #Replacing punctuaton with empty characters
                for char in '-_–().,?!""':
                    line = line.replace(char, '')
                #Splitting the line along spaces and endline characters
                if (line != "\n"):
                    array = re.split(' |\n', line)
                    for x in range(len(array)):
                        self.data.append(array[x])
                line = file.readline()
                
        #Removing and null or empty characters that were created by the split
        self.data = list(filter(lambda a: a != None, self.data))
        self.data = list(filter(lambda a: a != "", self.data))
    
    #Returns the data list created by the parser
    def getData(self):
        return self.data