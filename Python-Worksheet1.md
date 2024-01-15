1.C

2.B

3.C

4.A

5.None of these(3.0)

6.C

7.A

8.C

9.A,C

10.A,B

Question 11, Write a Python Program to find the fctorial of a number


```python
def factorial(n):
 
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
 

num = 5
print ("Factorial of",num,"is",
      factorial(num))
```

    Factorial of 5 is 120
    

Question12- Write a Python Program to find out weather the number is prime or composite


```python
n=int(input('Enter value to test for primality: '))

# assume n > 3

if n % 6 in (1, 5):
    print("Prime Number")
else:
    print("Composite number")
```

    Enter value to test for primality: 3
    Composite number
    

13. Write a python program to check whether a given string is palindrome or not

I have a problem into it


```python
14. Write a Python program to get the third side of right-angled triangle from two given sides
```

My program is not giving correct answer on running for this question so i am unable to do it

15. Write a python program to print the frequency of each of the characters present in a given string


```python
string = "German Shepherd"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " +str(frequency), end=", ")
```

    G: 1, e: 3, r: 2, m: 1, a: 1, n: 1,  : 1, S: 1, h: 2, e: 3, p: 1, h: 2, e: 3, r: 2, d: 1, 


```python

```
