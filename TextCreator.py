# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 2018

@author: HendR

This program creates a body of text similar to another body of text. It parses 
the txt file provided, creates an array of the words used and the most likely 
word to be used after each word, and creates a body of text based on this array
using the first word entered in by the user. The first word must be a word contained
in the original body of text or the output will be blank. The txt file entered
in by the user should be in the same folder as this program, or an error will return.
"""

from WordList import WordList
from Parser import Parser

#Returns a list of the words in the document, which are each objects with a list
#of their following words and how many times they show up
def getArrayOfFollowingWords(wordList):
    
    #Initializing the list
    followingWordsList = WordList(wordList[0], wordList[1])
    
    #Looping through the word list that was fed in as a parameter, which would 
    #just be a list of the parsed words in the file to be analyzed
    for x in range(1, len(wordList)):
        if (x + 1 != len(wordList)):
            #If the word is already in the list, add its following word to the
            #following words list
            if not followingWordsList.addWordToList(wordList[x], wordList[x+1]):
                followingWordsList.addFollowWord(wordList[x], wordList[x+1])
    return followingWordsList.getList()

def main():
    file = input("Which file would you like to get data from? " +
                 "\nOptions included in this GitHub: " +
                 "\nShorterTrumpSpeech.txt" +
                 "\nRobertFrostPoems.txt" +
                 "\nAllTrumpSpeeches.txt **" +
                 "\n**This one takes much longer to run" +
                 "\n")
    word = input("Please enter the first word you would like to use: ")
    number = input("How many words would you like the output to contain? ")
    
    #Parsing the input file for a list of the words
    parser = Parser(file)
    fileList = parser.getData()
    
    #Getting the array of the following words
    listOfWords = getArrayOfFollowingWords(fileList)
    string = word

    #Creating a string with the length equal to the amount of words the user
    #wanted the output to be
    for y in range(int(number)):
        for x in listOfWords:
            if x.getWord() == word:
                word = x.returnMostLikelyFollowWord()
                while (word == None):
                    word = x.returnMostLikelyFollowWord()
                string += " " + word

    print("\nYour output: " + string)

if __name__ == "__main__":
    main()
