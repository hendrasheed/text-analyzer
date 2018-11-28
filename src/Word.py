'''

Represents a word object, which has a list of following words and a counter
attached to them based on how many times they appear in a certain text.

'''

import random

class Word():
    
    #Initailizes a word with an attribute called word which stores its own
    #string, an attribute called followingWords which is a list of tuples
    #containing this word's following words and how many times they appear,
    #and an attribute called totalFWords which stores the total number of
    #following words (used to create a range for the random number later)
    def __init__(self, word, followingWord):
        self.word = word
        self.followingWords = [[followingWord, 1]]
        self.totalFWords = 1

    #Returns whether the following word is in the list of following words
    def fWordInList(self, word):
        for x in self.followingWords:
            if x[0] == word:
                return True
        return False

    #Adds the parameter word to the list of following words along with a counter
    #of 1 if it does not already appear in the list, or incrementing the counter
    #for the word if it already appears in the list
    def addFollowingWord(self, fWord):
        if not self.fWordInList(fWord):
            self.followingWords.append([fWord, 1])
            self.totalFWords += 1
        else:
            for x in range(len(self.followingWords)):
                if self.followingWords[x][0] == fWord:
                    self.followingWords[x][1] += 1
                    self.totalFWords += 1

    #Returns the word attribute of the object
    def getWord(self):
        return self.word

    #Returns the most likely word to follow the current word
    def returnMostLikelyFollowWord(self):
        
        #If there is only one word in the following words list, returning that word
        if (len(self.followingWords) == 1):
            return self.followingWords[0][0]
        
        #Getting a random integer between 0 and the total number of following words
        randomInt = random.randint(0,self.totalFWords-1)
        
        #Initializing num to be the counter for the first following word
        num = self.followingWords[0][1]
        
        #Checking if the randomInt is less than the current num and returning
        #if it is, or continuing to increment num if it is not
        for y in range(1, len(self.followingWords)):
            if (randomInt < num):
                return self.followingWords[y - 1][0]
            else:
                num +=  self.followingWords[y][1]

    #Returns a string representation of the word and its following words list;
    #useful for debugging
    def getPrintableWord(self):
        string = self.word
        for x in range(len(self.followingWords)):
            string += str(self.followingWords[x])
        return string
