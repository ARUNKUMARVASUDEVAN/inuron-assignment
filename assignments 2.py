#!/usr/bin/env python
# coding: utf-8
1)
What are the two values of the Boolean data type? How do you write them?

Ans)

Two values are True and False
should be written by starting Capital T and F like :True  ,False
2. What are the three different types of Boolean operators?

Ans:
And,Or,Not these are the operators we are using inside the boolean values


And operator (&):

 It returns True both the values are true otherwise false
Or operator(|):

 It returns true if any one value is true.It gives only false on by both the values are false
Not operator(~):

 It returns opposite of the boolean values like if the given value is true it will return false if the value is false it return true
 


3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

And:
 A | B| A & B
 T   T    T
 T   F    F
 F   T    F
 F   F    F
 
OR:
 A | B| A or B
 T   T   T
 T   F   T
 F   T   T
 F   F   F
 
Not:
 A | Not A
 T   F
 F   T
 
4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
Ans:
(5 > 4) and (3 == 5) =====False

(5 > 4) or (3 == 5)  =====True

not ((5 > 4) or (3 == 5))   ====False

(True and True) and (True == False) ====False

(not False) or (not True)  ====True









5. What are the six comparison operators?

Ans:
    Six Operators are '==','>','<','>=','<=','!='

Every operator is used to check different conditions
'==':
    is used to check if both the values are equal if it is equal it will return True if not It returns false
 '>' :
    is used to check if left value is greater than the right value ,If the condition id true it return True,otherwise false
    
 '<':
    used to check if left value is less than the right value
    
 '>=':
    is used to check if the left value is greater than equal to right
    
  '<=':
   is used to check if the left value is less than or equal to right value
   
   '!=':
   is used to check if the value are not equal with them
   
6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
ans:

Assignment operator is used when assigning a value to a variable

x=5

Equal to is used when we check the values or condition for a specific values

if age==18:
      print('get ready to be a part in contry future')
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans:
1:if spam == 10:
print('eggs')

2:if spam > 5:
print('bacon')

3:else:
print('ham')
print('spam')
print('spam')


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

Ans:
spam=0
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings')

9.If your programme is stuck in an endless loop, what keys you’ll press?

ans:
CTRL + C

10. How can you tell the difference between break and continue?
ans:
'Break':
  break is used to exit a loop when a certain conditions met.It will  terminate the loop statement
'continue':
  is used to skip the current iteration and jumps to nest iteration11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans:
Range(10): Prints from 0 to 9 by dafault it will print from 0 to 9 by diiference of 1
Range(0,10): Prints from 0 to 9 default step is 1
Range(0,10,1): Prints from 0 to 9 with the step 112. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Ans:

for i in range(0,11):
    print(i)
    

i=1
while i<=10:
    print(i)
    i+=1
   13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
ans:
from spam import bacon
b=bacon()