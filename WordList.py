'''

Creates a list of word objects, which each have a list of follow words and the
likelihood that they follow the original word.

'''

from Word import Word

class WordList():

    #Initializes a wordlist with the first word and second word fed in as parameters
    def __init__(self, firstWord, secondWord):
        word = Word(firstWord, secondWord)
        self.wordList = [word]

    #Returns true if a word is already in the list and false otherwise
    def wordInList(self, word):
        for x in self.wordList:
            if x.getWord() == word:
                return True
        return False

    #Tries to add a word and its following word to the list if the word is not 
    #already there and returns true if successful; if the word is already in 
    #the list it returns false
    def addWordToList(self, word, fWord):
        if self.wordInList(word):
            return False
        else:
            newWord = Word(word, fWord)
            self.wordList.append(newWord)
            return True

    #Adds a follow word to the list of follow words for a specific word already
    #in the list; should only be called after checking that the word is already
    #a part of the list using the method above
    def addFollowWord(self, word, fWord):
        for x in range(len(self.wordList)):
            if self.wordList[x].getWord() == word:
                self.wordList[x].addFollowingWord(fWord)

    #Returns a printable strong of the words in the list; helpful for debugging
    def getPrintableList(self):
        string = ""
        for x in range(len(self.wordList)):
            string += self.wordList[x].getPrintableWord()
            string += "\n"
        return string

    #Returns the list of word objects
    def getList(self):
        return self.wordList
