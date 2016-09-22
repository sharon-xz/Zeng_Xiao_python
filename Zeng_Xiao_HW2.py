# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:04:36 2016

Homework 2

@author: Xiao Zeng
"""
import re
from random import randint
 
#Question 1

def is_palindrome(word) :
    """
    This function determines whether a word is a palindrome or not.
    If the word is the same as its reverse, then it is a palindrome. We can examine this by calling the reverse() function.
  
    Parameters:
    A string
  
    Returns:
    Boolean  
    """  
    
    palindrome = False #Setting the default situation
    if reverse(word) == word: #If the reverse of the word is the same as the word, it should be a palindrome
        palindrome = True
    
    
    return palindrome #Returns Boolean
    

def reverse(line):
    """
    This function gives the reverse of a word by putting the last letter to the first, and vice versa. 
  
    Parameters:
    A string
  
    Returns:
    A string, with letters reversed. 
    """ 
    revStr = '' #Initiation of a new string
    
    for i in range(0,len(line)):
        revStr += line[len(line)-1-i] #Adding elements from last to the first to the new string
 
    return revStr  #Returns the reversed string


def palindrome_recogniser(filename):
    """
    This function reads a file line by line, and then prints the lines that are palindromes in this file.
  
    Parameters:
    A string of the input file name
  
    Returns:
    None
    """  
    text = open(filename)  #Open a file
    content = text.readlines()  #Reads the file line by line
    
    for i in range(0,len(content)): 
        word = content[i] #Gets the content of every line
        word=re.sub('\\n','',word)  #Getting rid of the '\n' sign at the end of each line.
        
        if is_palindrome(word) == True:  #Check if the line is palindrome or not
            print(word)   #If it is palindrome, then it needs to be printed.
    text.close

    return None


"""Testing Question 1"""
    
print('Testing Question 1: ', reverse('abcyyy'))
print('Testing Question 1: ',is_palindrome('abtyy'))
print('Testing Question 1: ',is_palindrome('aabbaa'))
print('Testing Question 1: ',is_palindrome('12321'))


#Question 2
def semordnilap_recogniser(filename):
    """
    This function reads a file, and prints all pairs of words that are semordnilaps.
    If the word is the same as the reverse of another word in the file, then it is a palindrome pair. We can examine this by calling the reverse() function.
  
    Parameters:
    A string of file name
  
    Returns:
    None  
    """  
   
    i = 0 #Initiation
    j = 0
    text = open(filename) #Opening file 
    content = text.readlines()  #Reading lines
    
    for i in range(0,len(content)):
        
        word = content[i]    #Getting each line
        word=re.sub('\\n','',word) #Getting rid of the '\n' sign at the end of each line.
   
        for j in range(0,len(content)): 
          if j > i:   #Only compares the words after, so there won't be repetitive pairs
            otherword = re.sub('\\n','',content[j])  
            rev_otherword = reverse(otherword)   #Getting the reverse of other words in the file
        
            if word == rev_otherword:
               print(word, ' ', otherword)  #If they are semordnilap, then prints the result.
    
    text.close  #closes file

    return None

#Question 3
def char_freq_table(filename):
    """
    This function reads a file and builds a frequency listing of the characters contained in the file.
    The frequency of each character is counted, and the frequency table is presented by a dictionary.
  
    Parameters:
    A string of file name
  
    Returns:
    A dictionary 
    """  
    

    text = open(filename)  #Opens file
    content = text.readlines()
    
    freq={} #Initiation of a new dictionary
    
    
    for lines in content:    
        lines=re.sub('\\n','',lines)   #Gets rid of the end of line sign
        for char in lines:   #counts every character
            if char in freq:  #if the character already existed in the dictionary, then add one count       
                 freq[char] += 1
            else:
                 freq[char] = 1  #if the character is not existed in the dictionary, then create a new dictionary key.
 
    return freq
    
    
#Question 4
import os  #Imports the text-to-speech liabrary
import time   #Imports the time liabrary
def speak_ICAO(text,pause_characters, pause_words):  
    """
    This function makes the system read a text letter by letter. 
    The letters are read according to the ICAO rule. The ICAO alphabet assigns 
    code words to the letters of the English alphabet acrophonically, so that critical combinations of 
    letters (and numbers) can be pronounced and understood by those who transmit and receive voice messages by radio or 
    telephone.
  
    Parameters:
    A string of text, a float which is the pause time between characters, 
    and a float which is the pause time between words.
  
    Returns:
    None
    """  
    
    speaktext = '' #Initiation

    dict ={'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
    'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 
    'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 
    'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
    'x':'x-ray', 'y':'yankee', 'z':'zulu'}  #The diactionary for ICAO rule
    alltext = text.split(' ') #Splits the sentence into words
    
    for words in alltext:
        for i in words:
           speaktext = dict[i]  #Pronounces each letter using the corresponding word in dictionary
           os.system('say'+ speaktext) #Speaks the word
           time.sleep(pause_characters) #Pause between letters
        time.sleep(pause_words)  #Pause between words
        
    return None


#Question 5

def hapax(filename):
    """
    This function reads a file and gives all the words that occurs only once in the text. 
    The function counts the frequency of each word, and stores the frequency in a dictionary. 
    If the frequency of a word is 1, the word will be returned.
  
    Parameters:
    A string of filename
  
    Returns:
    A string of hapaxes
    """  

    text = open(filename)
    content = text.readlines() #Opens files
    
    output ='' #Initiation
    
    freq={} #Initiation of a new frequency dictionary
    
    
    for lines in content:    
        lines=re.sub('\\n','',lines) #Gets rid of the end of line sign
        lines.lower() #Makes all letters lower-case, so the capitalized letters will be counted as well
        
        for w in lines.split(' '):     
      
          if w in freq:#if the character already existed in the dictionary, then add one count       
              freq[w] += 1
          else:
              freq[w] = 1  #if the character is not existed in the dictionary, then create a new dictionary key.
              
    for words, f in freq.items(): 
        if f == 1: #Checks if the frequenciesare 1
            output = output + words + '\n'  #If the frequency is 1, then it sould be added to the output string
            
    return output
    



    
        
#Question 6
    
    
def numbered(filename, newfilename):
    """
    This function reads a file and creates a new text file in which all the lines
    from the original file are numbered from 1 to n (where n is the number of lines in the file). 
  
    Parameters:
    A string of filename, and another string of the name of the new file
  
    Returns:
    None
    """  
    text = open(filename)
    content = text.readlines() #Opens file and reads lines
    
    index = 0 #Initiation of the count of lines
    newcontent = '' #Initiation of new content
    
    
    for i in content: 
        index += 1  #For each line, adds one count
        newline = str(index) + '. ' + i +'\n' #Adds the number of lines before the original line
        newcontent += newline #Adds the new line to the output content
    
    new = open(newfilename,'w+') #Open a writing new file.
    new.write(newcontent) #Writes the content to the new file
            
    return None
    
#Question 7

def average_length(filename):
    """
    This function reads a file and gives the average length of words in the file
    Parameters:
    A string of filename
  
    Returns:
    The average length: a float
    """ 

    text = open(filename)
    content = text.readlines() #Opens file and reads lines
    
    wordcount = 0 #Initiation of number of words
    total_length = 0 #Initiation of total length 
    
    for lines in content :
       lines=re.sub('\\n','',lines) #Gets rid of the end of line sign
       line = lines.split(' ') #Splits the line into words

       
       for word in line:
           if word != '' : #We only calculate length for non-empty words
              total_length += len(word) #Adds the length of each word
              wordcount += 1  #Adds one count of word
              
       avg = total_length / wordcount  #Calculates the average length

            
    return avg  

#Question 8



def guess_game():
    """
    This function simulates a guess game. The system would randomly pick an integer from 0 to 20 
    as the correct answer. The user will be asked to guess this number and will receive hints until he gets the
    answer correct.
    
    Parameters:
    None
  
    Returns:
    None
    """ 
    correct_answer = randint(1,21) #Randomly generates a correct answer
    times = 1 #Initiation of guessing times
    
    name = input("What is your name?\n") #Gets the name of users
    print(name, ", I am thinking of a number between 1 and 20. Take a guess.\n")  
    guess = int(input()) #Receives the guess number
    
    while guess != correct_answer: #The game will continue until the user gets the right answer
        if guess  > correct_answer:
            times += 1
            print('Too high') #Gives hints of values that are too high
            guess = int(input( "Take a guess.\n" ))
        if guess  == correct_answer:
            print("Good job. ", name, ", You guessed my number in", times, "guesses!" )#Correct answer, prints how many times the user has guessed
        if guess  < correct_answer:
            times += 1
            print('Too low') #Gives hints of values that are too low
            guess = int(input("Take a guess.\n" ))

    
    return None


#Question 10
def lingo_game(correct_word):
    """
    This function simulates a lingo game of a five-letter word. The user will be asked to guess this
    word. Based on the input of users, some clues will be given to the users. 
    If the character is fully correct, then the character will be shown around [].
    If the character is correct, but position is not, then the character will be shown around ().
    The game continues until all the characters are in square brackets.
    
    Parameters:
    A word of five letters as the correct word
  
    Returns:
    A string
    """ 
   
    guess = input("Welcome to Lingo game! Please type your guess.") #Welcome and gets the input
    
    while True:
        list = ['','','','',''] #Initiation of a list
        output = '' #Initiation of the output string
        for i in range(0, 5):  #Compares each character
            if guess[i] == correct_word[i]: #If the character is fully correct, the square brackets should be added
                list[i] = '['+guess[i] +']'
            elif guess[i] in correct_word:
                list[i] = '('+guess[i] +')'#If the character is in the word but not fully correct, the parentheses should be added
                
            else:
                list[i] = guess[i]  #Anything else keeps the same
           
            
        for j in range(0,5):
            output += list[j]  #converting the output list to a string
        if guess == correct_word:
            
            print('Clue:', output) #Prints the result
            break             #If the guess is correct, the game ends and the loop breaks.
        else:
            print('Clue:', output)#Prints the result
            guess = input()  #If the guess is not correct, continues to get new guesses
    
        
    return output
    
    




#Question 11

def splitter(filename):
    """
    This function reads a text file and splits the sentenses. Each new sentence will be rewritten as 
    a new line.
    There are many rules to define the sentence boundry. Sentences always ends with periods, but periods
    followed by lower-case letters, none white space, titles, digits or punctuations are not sentence boundries.
    
    Parameters:
    A string of filename
  
    Returns:
    None
    """ 
    
    punc='?!' #A string of punctuations that usually means the appearence of a new sentence.
    lower='abcdefghijklmnopqrstuvwxyz' #A string of lower-case letters
    cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #A string of upper-case letters
    num='0123456789' #A string of digits
    title=['Mr','Mrs','Dr'] #A list of titles
    punctuation="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?" #A list of other punctuations
    
    f = open(filename) #Open files and reads text
    string = f.read()
   
    for i in range(1,len(string)-2):
        if string[i]=='.':#Locates the period
            if string[i+1]==' 'and string[i+2] in lower:
                string=string #Periods followed by whitespace followed by a lower case letter are not counted as sentence boundaries.
            elif string[i+1] in num:
                string=string #Periods followed by a digit with no intervening whitespace are not sentence boundaries.
            elif (string[i-2:i] or string[i-3:i]) in title and string[i+1]==' ' and string[i+2] in cap:
                string=string #Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries
            elif string[i-1]!=' ' and string[i+1]!=' ':
                string=string #Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries 
            elif string[i+1] in punctuation:
                string=string #Periods followed by certain kinds of punctuation
            else:
                string=string[:i+1]+'\n'+string[i+2:] #For new sentences, creates a new line
        elif string[i] in punc:
            string=string[:i+1]+'\n'+string[i+2:] #For sentences end with '?' and '!', there's usually a new sentence as well.
 
    
    
    file1=open(filename,'w') #Opens the file again
    file1.write(string)#Writes the new string to the file
    file1.close()
    
    return None
    
