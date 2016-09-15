# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:32:43 2016

@author: Xiao Zeng

Homework 1

"""

#Question 1
def translate(text):
  """
  This function translates {merry christmas and happy new year} to Swedish.
  
  """
  
  english = text.split(' ') #Splits a sentence into separate words
  swedish = '' #Initiation of a new string
  for i in english:
      """
      translates every word, and add the translated word to a new string
      """
      if i =='merry':  
         swedish += 'god' +' '   #translates merry
 
      if i =='christmas':
         swedish += 'jul'+' '    #translates chiristmas

      if i=='and':
         swedish += 'och'+' '    #translates and
     
      if i =='happy':
         swedish +='gott'+' '    #translates happy
         
      if i =='new':
         swedish +='nytt'+' '    #translates new
         
      if i =='year':
         swedish += 'år'+' '     #translates year

  return swedish
  
def char_freq(string):
    
    freq={} #freq is a dictionary
    for i in string:
        if i in freq:
            
           freq[i] += 1
        else:
            freq.update{i,1}
            freq[i] = 1
 
    return freq


#question3
key={'a':'n', 'b':'o','c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
'Z':'M'}

def encoderdecoder(code):
    '''
    This function can encode and decode string using dictionary "key".
    My thought: find the values of every letters in code, and add them up. For punctuations, when can not find 
    keys in "key", keep them and also add them up.
    '''
    answer="" #creat an empty "answer" 
    for i in code:
        if i in key:
            answer=answer+key[i] #key[i] can find the mathaced values in dictionary. Add the value up to form a word or sentence
        else:
            answer=answer+i #for punctuations and spaces, keep them and also add them up to form a sentence
    return answer
    
print(encoderdecoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))

#question4
import re #import regular expression module
def correct(string):
    '''
    Define a simple "spelling correction" function correct()that takes a
    string and sees to it that 1) two or more occurrences of the space
    character is compressed into one, and 2) inserts an extra space
    after a period if the period is directly followed by a letter.
    My thought: use regular expression, correct the sentence in two steps.
    '''
    string=re.sub('\ +',' ',string) #substitute one or more spaces between two words to one space
    string=re.sub('\.','. ',string) #substitute period end with no space to period end with one space
    return(string)
    
print(correct("This  is very funny    and cool.Indeed!"))


def make_3sg_form(word):
    
    #If the word ends in y
    if word.endswith('y') == True :
        newword= word[:-1] + 'ies'
    #If the word ends in o, ch, s, sh, x or z
    elif word.endswith('o') == True :
            newword= word + 'es'
    elif word.endswith('ch') == True :
            newword= word + 'es'
    elif word.endswith('s') == True :
            newword= word + 'es'
    elif word.endswith('sh') == True :
            newword= word + 'es'
    elif word.endswith('x') == True :
            newword= word + 'es'
    elif word.endswith('z') == True :
            newword= word + 'es'
    else:
        newword = word +'s'
  
    
    return newword
    

def make_ing_form(word):
    
    newword = ''
    consonant = 'bcdfghjklmnpqrstvxz'
    vowel ='aeiou'
    if len(word)>2:
        if word.endswith('ie') == True :
            newword = word[:-2] + 'ying'
        elif word.endswith('ee') == True :
            newword = word + 'ing'
        elif word.endswith('e') == True :
            newword = word[:-1] + 'ing'
        elif word[-1] in consonant:
            if word[-2] in vowel:
                if word[-3] in vowel:
                    newword = word + word[-1]+'ing' 
                
            
                else:
                   newword = word +'ing'  
            else:
             newword = word +'ing'
      
        else:
             newword = word +'ing'

    else:
        newword = word +'ing'

    return newword
