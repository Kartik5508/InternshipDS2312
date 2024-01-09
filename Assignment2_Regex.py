#!/usr/bin/env python
# coding: utf-8

# Ques1: replace occurance of , pace or dot with colon

# 'Python:Exercises::PHP:exercises.'

# In[ ]:


Que1 


# In[3]:


import re
text='Python:Exercises::PHP:exercises.'
print(re.sub(',.',':',text))


# Ques2_Create a dataframe

# In[4]:


import pandas as pd
data={'Summary':['hello,world!','XXXXX test','123four,five:;six...']}
df=pd.DataFrame(data)
df['Summary']=df['Summary'].str.replace('[^a-zA-Z\s]',' ',regex=True)

# In[5]:

df

# Ques3 Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory

# In[6]:


import regex as re
str1='Rohit Sharma is a great indian batsman'
str_pattern='\w{4,}'
regex_pattern=re.compile(str_pattern)
print(type(regex_pattern),'\n')
result=regex_pattern.findall(str1)
print(result)


# Question4: Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[9]:

import regex as re
str1='Rohit Sharma is a good hitter'
str_pattern='\b\w{3,}\b'
regex_pattern=re.compile(str_pattern)
print(type(regex_pattern),'\n')
result=regex_pattern.findall(str1)
print(result)


# Ques5 Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.

# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
I have a problem into it i tried out i am unable to do it

Ques 6- I am unable to do it because i cant understand

# ques7-Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# 

# In[12]:


import re
text = "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*', text))


# Ques 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[1]:


import re

def insert_spaces(text):
    
    result = re.sub(r'(?<=[a-zA-Z])(\d)', r' \1', text)
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(sample_text)

print(output)

    

#  Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython
# 

# In[3]:


import re

def insert_spaces(text):
    
    result = re.sub(r'(?<=[a-z0-9])([A-Z0-9])', r' \1', text)
    
    
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(sample_text)

print(output)


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# unable to do it
# 

# Question 11 Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[26]:


import re

def match_string(string):
    pattern = r'^[a-zA-Z0-9_]+$'
    
    if re.match(pattern, string):
        
        print("String matches the pattern")
    else:
        print("String does not match the pattern")
        
sample_text = "@"
output = match_string(sample_text)
print(output)

sample_text = "DataScience_123"
output = match_string(sample_text)

print(output)


# Question 12- Write a Python program where a string will start with a specific number.

# In[33]:


def check_starting_number(string, number):
  if string.startswith(str(number)):
    return True
  else:
        return False

#Example-
string = "0523DataScience"
number = '0523'

if check_starting_number(string, number):
  print("The string starts with the specified number.")
else:
  print("The string does not start with the specified number.")


# Question 13- Write a Python program to remove leading zeros from an IP address

# In[34]:


import re
ip = "516.07.043.254"
string = re.sub('\.[0]*', '.', ip)
print(string)


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.

# In[37]:


import re

text = 'Gandhi ji was born on October 2nd 1869'
pattern = r"\b([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)? \d{4})\b"

matches = re.findall(pattern, text)
date_string = matches[0] if matches else None

print(date_string)


# Question 15- Write a Python program to search some literals strings in a string. Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[44]:


import re
patterns = [ 'fox', 'dog', 'horse' ]
Sample_text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, Sample_text),)
    if re.search(pattern, Sample_text):
        print('Matched!')
    else:
        print('Not Matched!')
        


# Question 16 Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[46]:


import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))


# Ques 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[49]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[50]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# Question19 Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

# I dont know how to program this,i have doubt into it

# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[51]:


import re

def find_decimal_numbers(string):
  pattern = re.compile(r'\d+\.\d{1,2}')
  decimal_numbers = re.findall(pattern, string)
  return decimal_numbers
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print(output)


# Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[52]:


import re
text = "Virat Kohli has made 80 Centuries"

for number in re.finditer("\d+", text):
    print(number.group(0))
    print("Index position:", number.start())


# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950
# 

# In[56]:


import re

Sample_text= 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

numeric_values = re.findall(r'\d+',Sample_text)
numeric_values = [int(value) for value in numeric_values]

max_value = max(numeric_values)

print(max_value)


# Question23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython" 

# In[62]:


import re

def insert_spaces(text):
    pattern = r'([A-Z][a-z]+)'
    result = re.sub(pattern, r' \1', text)
    result = result.strip()
    return result


# In[63]:


sample_text = "RegularExpressionIsAnImportantTopicInPython"
output = insert_spaces(sample_text)
print(output)


# Ques24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[65]:


import re

pattern = r'[A-Z][a-z]+'
text = "Regular Expression is an important Topic inPython"

matches = re.findall(pattern, text)
print(matches)


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 

# In[66]:


import re

def remove_duplicates(sentence):
  pattern = r'\b(\w+)(\s+\1\b)+'
  result = re.sub(pattern, r'\1', sentence)
  return result

# Example usage
sentence = "Hello hello world world"
output = remove_duplicates(sentence)
print(output)


# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character

# In[76]:


import re

def check_string(string):
    pattern = r"\w$"
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False

# Example usage
input_string = input("Enter a string: ")
if check_string(input_string):
  print("String ends with an alphanumeric character")
else:
  print("String does not end with an alphanumeric character")


# Ques27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS 
# 

# In[78]:

import re

def extract_hashtags(text):
  hashtags = re.findall(r'#\w+', text)
  return hashtags


Sample_text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'

hashtags = extract_hashtags(Sample_text)

# Print the extracted hashtags
print(hashtags)


# Question 28- unable to understood

# Ques 29- unable to understood

# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly
# 

# In[79]:


import re

def remove_words(string):
    pattern = re.compile(r'\b\w{2,4}\b')
    modified_string = re.sub(pattern, '', string)
    return modified_string


# In[80]:


Sample_Text= "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly"
result=remove_words(Sample_Text)
print(result)


# In[ ]:

