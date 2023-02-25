1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].

Ans:

```python
years_list=[2001,2002,2003,2004,2005,2006]
```
2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.

```python
years_list[3]
```




    2004


3.In the years list, which year were you the oldest?

```python
len(years_list)
```




    6




```python
years_list[5]
```




    2006


2006 is the oldest me4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

```python
elements=["mozzarella", "cinderella", "salmonella"]
```
5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?


```python
elements=["mozzarella", "cinderella", "salmonella"]
for i in range(len(elements)):
    if "cinderella" in elements[i]:
        elements[i] = elements[i].title()
print(elements)
```

    ['mozzarella', 'Cinderella', 'salmonella']
    
6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."


```python
surprise=["Groucho", "Chico", "Harpo"]
```
7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

```python
surprise[-1]=surprise[-1].lower()
surprise[-1]=surprise[-1][::-1]
surprise[-1]=surprise[-1].capitalize()
```
8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

```python
e2f={'dog':'chien','cat':'chat','walrus':'morse'}
```
9. Write the French word for walrus in your three-word dictionary e2f.

```python
print(e2f['walrus'])
```

    morse
    
10. Make a French-to-English dictionary called f2e from e2f. Use the items method.

```python
f2e={'chien':'dog','chat':'cat','morse':'walrus'}
```
11. Print the English version of the French word chien using f2e.


```python
print(f2e['chien'])
```

    dog
    
12. Make and print a set of English words from the keys in e2f.

```python
print(e2f.keys())
```

    dict_keys(['dog', 'cat', 'walrus'])
    
13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.


```python
life={'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':{},'emus':{}},'plants':{},'other':{}}
```
14. Print the top-level keys of life.

```python
print(life.keys())
```

    dict_keys(['animals', 'plants', 'other'])
    
15. Print the keys for life['animals'].

```python
print(life['animals'].keys())
```

    dict_keys(['cats', 'octopi', 'emus'])
    
16. Print the values for life['animals']['cats']

```python
print(life['animals']['cats'])
```

    ['Henri', 'Grumpy', 'Lucy']
    
