#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a python program for the following:
#– Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the #resultantstring and print it.


a='python'# input string is taken as 'a'
print (a)# printing the input string
reversed1 = a[:-2]# removing 2 characters from string
result1 = reversed1[::-1]# reversing the string after removing characters
print (result1)# printing the resultant string
#– Take two numbers from user and perform at least 4 arithmetic operations on them.
k1=int(input('n1:')) # taking 1st input from user
k2=int(input('n2:')) # taking 2nd input from user
a1= k1+k2 # applying addition (+) operator on inputs
print(a1) # printing result of addition 
a2= k1-k2 # subtraction (-)
print(a2) # printing result of subtraction
a3= k1*k2 # multiplication (*)
print(a3) # printing result of multiplication
a4= k1/k2 # division (/)
print(a4) # printing result of division


#2. Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.

a=input("Enter String ") # taking input string
k=a.replace('python','pythons') # replacing the desired string
print(k) # printing the desired string


#3. Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the
#grading scheme we are using in this class.


score=int(input('enter to check grade:')) # taking input from user
if(score>=90): # applying if condition
    print('grade is A')
elif(score>=80): 
    print('grade is B')
elif(score>=70):
    print('grade is C')
else:
    print("grade is Fail") # printing the grade according to the resultant  percentage 





    




# In[ ]:





# In[ ]:





# In[ ]:




