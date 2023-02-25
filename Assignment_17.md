1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.

```python
guess_me=7
n=int(input("Guess_me:"))

if n<guess_me:
    print("Too Low")
elif n==guess_me:
    print("just Right")
else:
    print("Too High")
```

    Guess_me:6
    Too Low
    
2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.

```python
guess_me=7
start=1
while True:
    if start<guess_me:
        print('too_low')
    elif start==guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start+=1
```

    too_low
    too_low
    too_low
    too_low
    too_low
    too_low
    found it
    
3. Print the following values of the list [3, 2, 1, 0] using a for loop.



```python
list=[3,2,1,0]
for i in list:
    print(i)
```

    3
    2
    1
    0
    
5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.

```python
squares={x:x**2 for x in range(10)}
print(squares)
```

    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    
6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

```python
odd={x for x in range(10) if x%2!=0}
print(odd)
```

    {1, 3, 5, 7, 9}
    
7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

```python
generator =('Got :' +str(num) for num in range(10))
for item in generator:
    print(item)
```

    Got :0
    Got :1
    Got :2
    Got :3
    Got :4
    Got :5
    Got :6
    Got :7
    Got :8
    Got :9
    
8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione']

```python
def good():
    l=['Harry', 'Ron', 'Hermione']
    return l
good()
```




    ['Harry', 'Ron', 'Hermione']


9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

```python
def get_odds():
    for i in range(1,10,2):
        yield i
       
```


```python
count=1
for i in get_odds():
    if count==3:
        print("third odd number:",i)
        break
    count+=1
```

    third odd number: 5
    
10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.

```python
class OopsException(Exception):
    pass
```


```python
raise OopsException('Wronggg')

```


    ---------------------------------------------------------------------------

    OopsException                             Traceback (most recent call last)

    Cell In [39], line 1
    ----> 1 raise OopsException('Wronggg')
    

    OopsException: Wronggg



```python
try:
    raise OopsException("Something Went wrong")
except OopsException:
    print('Caught an oops')
```

    Caught an oops
    
11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].

```python
titles = ['Creature of Habit', 'Crewel Fate'] 
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies=dict(zip(titles,plots))
print(movies)
```

    {'Creature of Habit': 'A nun turns into a monster', 'Crewel Fate': 'A haunted yarn shop'}
    
