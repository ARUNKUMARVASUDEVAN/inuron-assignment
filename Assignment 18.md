1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

```python
f=open('zoo.py','w')
```


```python
import zoo
zoo.hours()
```

    Open 9-5 daily
    
2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

```python
import zoo as menagerie
menagerie.hours()
```

    Open 9-5 daily
    
3. Using the interpreter, explicitly import and call the hours() function from zoo.

```python
import zoo
from zoo import hours
```
4. Import the hours() function as info and call it.

```python
from zoo import hours as info
info()
```

    Open 9-5 daily
    
5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

```python
dict={'a':1,'b':2,'c':3}
print(dict)
```

    {'a': 1, 'b': 2, 'c': 3}
    
6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

```python
from collections import OrderedDict
fancy=OrderedDict({'a':1,'b':2,'c':3})
print(fancy)
```

    OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    
yes it is printing in same order but format is different7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

```python
from collections import defaultdict
dict_of_list=defaultdict(list)
dict_of_list['a'].append('something for a')
```


```python
print(dict_of_list['a'])
```

    ['something for a']
    
