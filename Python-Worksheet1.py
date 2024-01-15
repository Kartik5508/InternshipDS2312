#!/usr/bin/env python
# coding: utf-8

# 1.C

# 2.B

# 3.C

# 4.A

# 5.None of these(3.0)

# 6.C

# 7.A

# 8.C

# 9.A,C

# 10.A,B

# Question 11, Write a Python Program to find the fctorial of a number

# In[4]:


def factorial(n):
 
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
 

num = 5
print ("Factorial of",num,"is",
      factorial(num))


# Question12- Write a Python Program to find out weather the number is prime or composite

# In[12]:


n=int(input('Enter value to test for primality: '))

# assume n > 3

if n % 6 in (1, 5):
    print("Prime Number")
else:
    print("Composite number")


# 13. Write a python program to check whether a given string is palindrome or not

# I have a problem into it

# In[ ]:


14. Write a Python program to get the third side of right-angled triangle from two given sides


# My program is not giving correct answer on running for this question so i am unable to do it

# 15. Write a python program to print the frequency of each of the characters present in a given string

# In[21]:


string = "German Shepherd"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " +str(frequency), end=", ")


# In[ ]:




