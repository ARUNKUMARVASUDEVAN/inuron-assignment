1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.

```python
test1 = 'This is a test of the emergency text system,'

with open('test.txt', 'w') as file:
    file.write(test1)

```
2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?

```python
with open('test.txt', 'r') as file:
    test2 = file.read()

print(test1 == test2)  

```

    True
    
No difference3. Create a CSV file called books.csv by using these lines:
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992


```python
import csv

header = ['title', 'author', 'year']
rows = [
    ['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],
    ['Perdido Street Station', 'China Miéville', '2000'],
    ['Thud!', 'Terry Pratchett', '2005'],
    ['The Spellman Files', 'Lisa Lutz', '2007'],
    ['Small Gods', 'Terry Pratchett', '1992']
]

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

```
4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).

```python
import sqlite3
conn = sqlite3.connect('books.db')
cur = conn.cursor()
sql_create_table = '''CREATE TABLE books (
                        title TEXT,
                        author TEXT,
                        year INTEGER
                    )'''
cur.execute(sql_create_table)
conn.commit()
conn.close()

```
5. Read books.csv and insert its data into the book table.

```python
import csv
import sqlite3


with open('books.csv', 'r') as f:
    
    reader = csv.reader(f)
    
    
    next(reader)
    
    
    conn = sqlite3.connect('books.db')
    
   
    cur = conn.cursor()
    
 
    for row in reader:
        
        title, author, year = row
        
       
        sql_insert = f"INSERT INTO books VALUES ('{title}', '{author}', {year})"
        
       
        cur.execute(sql_insert)
    
   
    conn.commit()
    
   
    conn.close()

```
6. Select and print the title column from the book table in alphabetical order.

```python
import sqlite3


conn = sqlite3.connect('books.db')


c = conn.cursor()


c.execute("SELECT title FROM books ORDER BY title ASC")
results = c.fetchall()


for row in results:
    print(row[0])


c.close()
conn.close()

```

    Perdido Street Station
    Small Gods
    The Spellman Files
    The Weirdstone of Brisingamen
    Thud!
    
7. From the book table, select and print all columns in the order of publication.

```python
import sqlite3

conn = sqlite3.connect('books.db')


c = conn.cursor()

c.execute("SELECT * FROM books ORDER BY year ASC")
results = c.fetchall()

for row in results:
    print(row)


c.close()
conn.close()

```

    ('The Weirdstone of Brisingamen', 'Alan Garner', 1960)
    ('Small Gods', 'Terry Pratchett', 1992)
    ('Perdido Street Station', 'China Miéville', 2000)
    ('Thud!', 'Terry Pratchett', 2005)
    ('The Spellman Files', 'Lisa Lutz', 2007)
    
8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.

```python
from sqlalchemy import create_engine


engine = create_engine('sqlite:///books.db', echo=True)



```
9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.

```python
import redis

# Create a Redis client object
r = redis.Redis(host='localhost', port=6379, db=0)

# Create the Redis hash
r.hset('test', 'count', 1)
r.hset('test', 'name', 'Fester Bestertester')
# Print all the fields for the test hash
print(r.hgetall('test'))
{b'count': b'1', b'name': b'Fester Bestertester'}

```
10. Increment the count field of test and print it.

```python
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Increment the count field of the test hash
r.hincrby('test', 'count', 1)

# Print the count field
print(r.hget('test', 'count'))

```
