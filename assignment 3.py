#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?
# 
# Ans:
# 
# Function are advantage for python,the function is increase the code readability and reusability.The function Will increase the modularity of the code we can debug very easily if the function  is assigned to a specific tasks
# 

# 2. When does the code in a function run: when it's specified or when it's called?
# 
# Ans:
# 
# Function run when it is called,Def in function which will make the function run the function will not run unless if we call the 
# function on the other part of code.The function called at the point at which the code in the function is executed and any specified return value is returned to the calling code.

# 3. What statement creates a function?
# 
# Ans:
# 'def' creates the function.

# 4. What is the difference between a function and a function call?
# 
# Ans:
# A function is a set of code that will executes specific tasks.
# function call, is set to call the function when we want a specific return of the value the function will only run after calling the function.

# 5. How many global scopes are there in a Python program? How many local scopes?
# 
# Ans:
#   
#   only one global scope. The global scope is the top-level scope, and it contains all the variables and functions that are not defined within any other scope.
#   
#   local scopes, there can be multiple local scopes within a program, depending on how many functions and classes are defined. Each function and class creates a new local scope, and within that scope, any variables or functions defined are only accessible within that scope

# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
# 
# 
# Ans:
# 
# Return value is the value that a function returns to the calling code when it has finished executing. A function can return a value by using the return statement followed by the value or expression to be returned.
#   Expression is a piece of code that results in a value, and a function can return an expression. The expression is evaluated, and its value is returned to the calling code.

# 8. If a function does not have a return statement, what is the return value of a call to that function?
# 
# Ans:
#  The value should be None

# 9. How do you make a function variable refer to the global variable?
# 
# Ans:
#     by using global keyword before the varible like 
#     
#     x=1
#     
#     global x

# 10. What is the data type of None?
# 
# Ans:
# 
#   It is a constant value ,It doesn't have a value or attributes. It Represents the absence of a value or a null value. It is an object of its own datatype, NoneType

# 11. What does the sentence import areallyourpetsnamederic do?
# 
# Ans:
# 
# It return import error, because the areallyourpetsnamederic module is not there in python libraries

# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 
# Ans:
# 
# import spam
# 
# from spam import bacon

# 13. What can you do to save a programme from crashing if it encounters an error?
# 
# Ans:
#   
#   By using exception handling. 

# 14. What is the purpose of the try clause? What is the purpose of the except clause?
# 
# Ans:
# 
# The try clause is used to enclose a block of code that may raise an exception. If an exception is raised within the try block, the code following the try block is skipped, and the code in the except block is executed instead.
# The except clause is used to handle exceptions that are raised within the try block. It specifies which exception to catch and what to do when the exception occurs. You can have multiple except clauses to handle different types of exceptions.
# 

# In[ ]:




