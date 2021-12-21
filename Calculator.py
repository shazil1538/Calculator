#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Calculator

def menu():
    a=int(input("Enter the number for the corresponding function you want to carry out:\n1 for addition.\n2 for subtraction.\n3 for multiplication.\n4 for division.\n5 to exit.\n"))
    if a==5:
        pass
    elif a==1:
        return add()
    elif a==2:
        return subtract()
    elif a==3:
        return multiply()
    elif a==4:
        return divide()
    b="Invalid choice. Please check your eyesight."
    return b

def add():
    first=int(input("Enter the first number:\n"))
    second=int(input("Enter the second number:\n"))
    print("The sum of the two numbers is:",first+second,end='.\n')
    a=int(input("Would you like to execute any other function? If yes, press 1. To exit, press 0.\n"))
    if a==1:
        return menu()
    elif a==0:
        b="Thank you for using this calculator."
        return b
    c="Invalid choice. Please check your eyesight."
    return c

def subtract():
    first=int(input("Enter the first number:\n"))
    second=int(input("Enter the second number:\n"))
    print("The difference of the two numbers is:",first-second,end='.\n')
    a=int(input("Would you like to execute any other function? If yes, press 1. To exit, press 0.\n"))
    if a==1:
        return menu()
    elif a==0:
        b="Thank you for using this calculator."
        return b
    c="Invalid choice. Please check your eyesight."
    return c

def multiply():
    first=int(input("Enter the first number:\n"))
    second=int(input("Enter the second number:\n"))
    print("The product of the two numbers is:",first*second,end='.\n')
    a=int(input("Would you like to execute any other function? If yes, press 1. To exit, press 0.\n"))
    if a==1:
        return menu()
    elif a==0:
        b="Thank you for using this calculator."
        return b
    c="Invalid choice. Please check your eyesight."
    return c

def divide():
    first=int(input("Enter the first number:\n"))
    second=int(input("Enter the second number:\n"))
    print("The division of the two numbers yields:",first/second,end='.\n')
    a=int(input("Would you like to execute any other function? If yes, press 1. To exit, press 0.\n"))
    if a==1:
        return menu()
    elif a==0:
        b="Thank you for using this calculator."
        return b
    c="Invalid choice. Please check your eyesight."
    return c

print(menu())


# In[ ]:




