1. Is the Python Standard Library included with PyInputPlus?
Ans:
 No
 
2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
Ans:
  To provide a shorthand alias for the module name. This can make the code more readable and easier to write
  
3. How do you distinguish between inputInt() and inputFloat()?

Ans:
inputInt() is used to take integer input from the user. It checks whether the input is an integer, and returns the integer value if the input is valid. If the input is not an integer, it will prompt the user to enter a valid integer.
inputFloat() is used to take floating-point input from the user. It checks whether the input is a float, and returns the float value if the input is valid. If the input is not a float, it will prompt the user to enter a valid float.

4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

Ans:
To ensure that the user enters a whole number between 0 and 99 using PyInputPlus, you can use the inputInt() function with the min and max parameters

5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

Ans:
allowRegexes: If specified, PyInputPlus only accepts the input that matches one of the regex in this list.
blockRegexes: If specified, PyInputPlus rejects the input that matches any of the regex in this list.

6. If a blank input is entered three times, what does inputStr(limit=3) do?
Ans:
inputStr(limit=3), the function raises a TimeoutException. This is because the limit parameter sets the number of attempts the function will give the user before raising this exception. In this case, if the user enters a blank input three times, the function will stop and raise the exception.

7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
ans:
If blank input is entered three times and inputStr(limit=3, default='hello') is used, then the input function will return the default value of 'hello'.

The limit parameter specifies the maximum number of attempts the user has to enter valid input before an exception is raised. The default parameter specifies the default value to return if the user fails to enter input within the given number of attempts. In this case, since the user has failed to enter valid input within the specified limit, the default value of 'hello' will be returned.