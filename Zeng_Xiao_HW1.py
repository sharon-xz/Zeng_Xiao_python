# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:32:43 2016

@author: Xiao Zeng

Homework 1

"""

#Question 1 - Correction
##The corrected version changed the type of input variables. 
##Now the input parameter is a list of words instead of a string

def translate(textlist):

  """
  This function translates The words "merry" "christmas" "and" "happy" "new" "year" to Swedish.
  The input list is first splitted into separate words, and then translated one by one. The translated words are added to the new string.
  
  Parameters:
  A list of words
  
  Returns:
  A string of translated Swedish words  
  """  
  
  swedish = '' #Initiation of a new string
  for i in textlist:  #translates every word in the list, and add the translated word to a new string
      
      if i =='merry':  
         swedish += 'god' +' '   #translates merry, use space to separate words
 
      if i =='christmas':
         swedish += 'jul'+' '    #translates chiristmas

      if i=='and':
         swedish += 'och'+' '    #translates and
     
      if i =='happy':
         swedish +='gott'+' '    #translates happy
         
      if i =='new':
         swedish +='nytt'+' '    #translates new
         
      if i =='year':
         swedish += 'år'+' '     #translates year
      

  return swedish  #returns the translated string



#Question 1 - Old version

##Prof G - The assignment required the function to accept a list of strings
def translate1(text):
##Prof G - Good header doc!
  """
  This function translates The words "merry" "christmas" "and" "happy" "new" "year" to Swedish.
  The input string is first splitted into separate words, and then translated one by one. The translated words are added to the new string.
  
  Parameters:
  A string of English words
  
  Returns:
  A string of translated Swedish words  
  """  
  english = text.split(' ') #Splits a sentence into separate words
  swedish = '' #Initiation of a new string
  for i in english:  #translates every word, and add the translated word to a new string
      
      if i =='merry':  
         swedish += 'god' +' '   #translates merry, use space to separate words
 
      if i =='christmas':
         swedish += 'jul'+' '    #translates chiristmas

      if i=='and':
         swedish += 'och'+' '    #translates and
     
      if i =='happy':
         swedish +='gott'+' '    #translates happy
         
      if i =='new':
         swedish +='nytt'+' '    #translates new
         
      if i =='year':
         swedish += 'år'+' '     #translates year
      

  return swedish  #returns the translated string
 




#Question 2 
def char_freq(string):
     """
     This function takes a string and gives a frequency listing of all the characters contained in it.
     For example, input 'hdyyy' should return {h:1, d:1, y:3}
  
     Parameters:
     A string 
  
     Returns:
     A dictionary of every character and its correspnding frequency. 
    
     """  
     freq={} #Initiation of a new dictionary
     for i in string:    #count every character
        if i in freq:    #if the character already existed in the dictionary, then add one count       
           freq[i] += 1
        else:
           freq[i] = 1  #if the character is not existed in the dictionary, then create a new dictionary key.
 
     return freq




#Question 3
def rot13cipher(code):
    
    """
    This function takes a string and gives an encoded or decoded string, which is encrypted by the ROT-13 method.
    For example, input 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!' should return 'Caesar cipher? I much prefer Caesar salad!'
    The function uses a dictionary to encode/decode every character and adds the new result to a new string.
  
    Parameters:
    A string 
  
    Returns:
    A encoded/decoded string. 
    
    """  
    
    key={'a':'n', 'b':'o','c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
   'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
   'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
   'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
   'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
   'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
   'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
   'Z':'M'}   #Difines the encoding/decoding rule.
   
   
    answer=""  #Initiation of a new string

    for i in code:   #For every character of the input string
        if i in key:
            answer=answer+key[i] #key[i] gives the corresponding value of the input character, and the new value is added to the new string
        else:
            answer=answer+i #for other non-English characters, keep them in the new string
    return answer


#Question 4 - Correction
## The corrected function changed the order of two statements so that it can deal with a period followed by mutiple spaces.

import re  #import regular expression 
def correct(string):
    """
    This functions corrects two things of a string
    1)two or more occurrences of the space character is compressed into one
    2)inserts an extra space after a period if the period is directly followed by a letter.
    For example, correct("This     is so  great.Nice.")should return "This is so great. Nice."
    
    The function uses the .sub method of the regular expression module most.
    re.sub(pattern, replacement, string). This method replaces all occurrences of the RE pattern in string with replacement. It returns modified string.
    
    Parameters:
    A string 
  
    Returns:
    A corrected string
    """  
    
    
    string=re.sub('\.','. ',string) #replaces period ended with no space to period ended with one space
    string=re.sub('\ +',' ',string) #replaces one or more spaces between two words to one space
    return(string)
    


#Question 4 - Old version

def correct1(string):
    """
    This functions corrects two things of a string
    1)two or more occurrences of the space character is compressed into one
    2)inserts an extra space after a period if the period is directly followed by a letter.
    For example, correct("This  is so  great.Nice.")should return "Thisis sogreat. Nice."
    
    The function uses the .sub method of the regular expression module most.
    re.sub(pattern, replacement, string). This method replaces all occurrences of the RE pattern in string with replacement. It returns modified string.
    
    Parameters:
    A string 
  
    Returns:
    A corrected string
    """  
    ##Prof G - Ooops. Doesn't handle a period followed by multiple spaces.
    string=re.sub('\ +',' ',string) #replaces one or more spaces between two words to one space
    string=re.sub('\.','. ',string) #replaces period ended with no space to period ended with one space
    return(string)
    

#Question 5 - Correction
## The Corrected version adds a conversion to lower case letters so that the function will handle all cases.

def make_3sg_form(words):
    """
    This functions takes a verb and turns it into third person singular form.
    Usually adding s to the verb would be enough, but for the words ending in y, o, ch, s, sh, x or z , things are diiferent.
    
    Parameters:
    A word as a string 
  
    Returns:
    A string of the third person singular form of the word
    """  
    word = words.lower()  #Converts all the letters to lower case
    newword = ''   #Initiation of a new string
    
    ##Prof G - Nice work but needs to handle mixed case.
    if word.endswith('y') == True :   #If the word ends in y, remove the last character of the word and add ies. 
            newword= word[:-1] + 'ies'
    
    elif word.endswith('o') == True :  #If the word ends in o, ch, s, sh, x or z, then add es to the verb
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
    else:   #By default, in all the other cases, just add s to the verb.
        newword = word +'s'
  
    
    return newword
  
#Question 6 - Correction
## The Corrected version adds a conversion to lower case letters so that the function will handle all cases.

def make_ing_form(words):
    """
    This functions takes a verb and turns it into its present participle form.
    Usually adding ing to the verb would be enough, but for the words ending in e,ee, ie and shorter verbs , things are diiferent.
    
    Parameters:
    A word as a string 
  
    Returns:
    A string of present form of the word
    """  
    
    ##Prof G - Needs to handle mixed case.
    
    word = words.lower()   #Converts all the letters to lower case
    newword = '' #Initiation of a new string
    
    consonant = 'bcdfghjklmnpqrstvxz'    #list all the consonant letters
    vowel ='aeiou'   #list all the vowel letters
    if len(word)>2:    #The rules only apply to words longer than 2 letters
        if word.endswith('ie') == True :  #For verbs ends with ie, ie should be changed to y and then ing will be added to the end
            newword = word[:-2] + 'ying'
        elif word.endswith('ee') == True :  #For verbs ends with ee, ing will be added to the end
            newword = word + 'ing'
        elif word.endswith('e') == True :  ##For verbs ends with e, but not ie or ee, the e in the end will be omitted and ing will be added to the end
            newword = word[:-1] + 'ing'
        elif word[-1] in consonant: #for the verbs whose last three letters are consonant-vowel-consonant, the last letter will be repeated and ing will be added to the end
            if word[-2] in vowel:
                if word[-3] in consonant:
                    newword = word + word[-1]+'ing' 
                
            
                else:
                   newword = word +'ing'  #non consonant-vowel-consonant verbs, just add ing
            else:
             newword = word +'ing'   #non consonant-vowel-consonant verbs, just add ing
      
        else:
             newword = word +'ing'  #By default, in all the other cases, just add ing to the verb.
    else:
        newword = word +'ing'  #For verbs with 2 letters, just add ing to the verb.

    return newword


#Question 7



def max_in_list(list):
    from functools import reduce  #import reduce module
    """
    This function takes a list of numbers and returns the largest number. 
    The reduce function is used most. It compares the items in the list by pairs by using a specific function.
    The advantage of using this function over using the reduce function directly is that it would make programming simpler and easier to read, especially when someone wants to call this function many times.
    
    Parameters:
    A list of numbers 
  
    Returns:
    A number which is the largest one in the list.
    """ 
    return reduce(max,list) #The reduce function gets the max number of the first two numbers, and then gets the max number of the previous number and the third number... and finally gets the max number in the list.



#Question 8

def listlength1(word):
    """
    This function takes a list of words and returns a list of integers which are the lengths of corresponding words. 
    This is achieved by using for loop.
    
    Parameters:
    A list of strings 
  
    Returns:
    A list of integers
    """ 
    
    length = [] #Initiation of a list
    for i in word:
        length.append(len(i)) #Gets the lengths of every string and adds them to the new list
    return length
    
    
def listlength2(word):
    """
    This function takes a list of words and returns a list of integers which are the lengths of corresponding words. 
    This is achieved by using the higher order function map().
    
    Parameters:
    A list of strings 
  
    Returns:
    A list of integers
    """ 
    
    return list((map(len,word))) #the map function applies the len() function to each items in the list and returns the modified list
    

    
def listlength3(word):
    """
    This function takes a list of words and returns a list of integers which are the lengths of corresponding words. 
    This is achieved by using list comprehensions.
    
    Parameters:
    A list of strings 
  
    Returns:
    A list of integers
    """
    length=[len(i) for i in word] #every item in the list is the length of items in the input list
    return length
    


#Question 9

def find_longest_word(inputlist):
    """
    This function takes a list of words and returns the length of the longest one by using higher order function map(). 
    
    Parameters:
    A list of strings 
  
    Returns:
    An integer
    """
    return max(map(len,inputlist)) #maps the length of each string in the list, and then finds the max of them.



#Question 10

def filter_long_words(inputlist, n):
    """
    This function takes a list of words and an integer n, and returns the list of words that are longer than n by using filter() function. 
    
    Parameters:
    A list of strings, and an integer
  
    Returns:
    A list of strings
    """
    return(list(filter(lambda x:len(x)>n,inputlist))) #filter() gets the strings that satisfies lambda x. list() puts the strings into a new list.



#Question 11

def translate2(list1):
    """
    This function translates The words "merry" "christmas" "and" "happy" "new" "year" to Swedish.
    It is achieved by using map() function.
  
    Parameters:
    A list of English words
  
    Returns:
    A list of translated Swedish words  
    """  
    ##Prof G - Need to handle mixed case!
    dictionary={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}  #The dictionary of English to Swedish words
    
    return list(map(dictionary.get,list1)) #.get method gives the corresponding value of the key. The map function applies this to every item in the list


#Question 12
##Prof G - Need to rename to avoid ambiguity with the built-in function
def mymap(function,list1):
    """
    This function implements the higher order function map(). 
    It takes a function and a list, and applies the function to every item in the list and returns the modified list.
  
    Parameters:
    A function and a list
  
    Returns:
    A list   
    """ 
    newlist=[] #Initiation of a new list
    
    for i in list1:
        newlist.append(function(i))   #Adds the modified items to the new list
    return newlist
    

    
def myfilter(function,list1):
    """
    This function implements the higher order function filter(). 
    It takes a function and a list, and keeps the items that satisfy the function conditions.
  
    Parameters:
    A function and a list
  
    Returns:
    A list   
    """ 

    newlist=[]  #Initiation of a new list
    
    for i in list1:
        if function(i)==True:  
            newlist.append(i) #Adds the items that satisfy the conditions to the new list
    return newlist
    

    
def myreduce(function,list1):
    """
    This function implements the higher order function reduce(). 
    It takes a function and a list, and it applies the function to the first two items, and then applies the function to the previously returned result and the next item, until the end of the list.
  
    Parameters:
    A function and a list
  
    Returns:
    An integer or float, or any type returned from the input function  
    """ 
    
    
    accum=list1[0]   #let accum be the first item in list1
    for i in list1[1:]: 
       accum = function(accum,i) #apply the function to accum and the items in list1 in sequence, the result will be accum again and will be compared to the next item.
    return accum








#Testing Section

print('Question 1 test 1:\n', translate(['happy', 'christmas', 'and', 'happy', 'new', 'year']),'\n')
print('Question 1 test 2:\n',translate(['happy', 'NEW', 'year']),'\n')

print('Question 2 test 1:\n',char_freq('abbabcbdbabdbdbabababcbcbab'),'\n')
print('Question 2 test 2:\n',char_freq('hiduhweuhhhuewyrutgggqoooooiuu'),'\n')

print('Question 3 test 1:\n',rot13cipher('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'),'\n')

print('Question 4 test 1:\n',correct("This.    is very funny    and cool.Indeed!"),'\n')

print('Question 5 test 1:\n',make_3sg_form('fly') ,'\n')
print('Question 5 test 2:\n',make_3sg_form('run') ,'\n')
print('Question 5 test 3:\n',make_3sg_form('brush') ,'\n')
print('Question 5 test 4:\n',make_3sg_form('FIX') ,'\n')

print('Question 6 test 1:\n',make_ing_form('be') ,'\n')
print('Question 6 test 2:\n',make_ing_form('see') ,'\n')
print('Question 6 test 3:\n',make_ing_form('hug') ,'\n')
print('Question 6 test 4:\n',make_ing_form('lie') ,'\n')
print('Question 6 test 5:\n',make_ing_form('run') ,'\n')

print('Question 7 test 1:\n',max_in_list([1,2,3,4,5]) ,'\n')

print('Question 8 test 1:\n',listlength1(['I','love','python!!']) ,'\n')
print('Question 8 test 2:\n',listlength2(['I','love','python!!']) ,'\n')
print('Question 8 test 3:\n',listlength3(['I','love','python!!']) ,'\n')

print('Question 9 test 1:\n',find_longest_word(['i','love','python']) ,'\n')

print('Question 10 test 1:\n',filter_long_words(['Today','is','a', 'good', 'day'],3) ,'\n')

print('Question 11 test 1:\n',translate2(['merry','christmas','and','happy','new','year']) ,'\n')

print('Question 12 test 1:\n',mymap(lambda x: x**2,[1,2,3,4,5]),'\n')
print('Question 12 test 2:\n',myfilter(lambda x:x>4,[1,2,3,4,5,6]) ,'\n')
print('Question 12 test 3:\n', myreduce(max,[1,2,3,4,5,6]) ,'\n')
