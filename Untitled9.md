1. What advantages do Excel spreadsheets have over CSV spreadsheets?

Ans:

csv is plain text format in which values are separated by comma (comma separated Values),while XLS file format is an Excel sheets binary file format which holds information about worksheets in a file,including both content and formatting 

2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

Ans:
 csv module, you need to pass a file object as an argument to the csv.reader() and csv.writer() functions.
 
 open the file using the open() function, and then pass the resulting file object to csv.reader()
 
import csv
with open('example.csv', 'r') as csvfile:
   
    csvreader = csv.reader(csvfile)

To create a writer object that can write data to a CSV file, you can open the file using the open() function, and then pass the resulting file object and the desired parameters to csv.writer()

import csv


with open('example.csv', 'w', newline='') as csvfile:
    # Create a writer object
    csvwriter = csv.writer(csvfile, delimiter=',')


3. What modes do File objects for reader and writer objects need to be opened in?

Ans:

creating reader and writer objects in Python's csv module, the corresponding File objects need to be opened in different modes:

reader objects require the file to be opened in 'r' (read) mode.
writer objects require the file to be opened in 'w' (write) mode.
It is also recommended to open the file in binary mode ('b') for portability across different platforms

import csv

# Open the file for reading
with open('file.csv', 'rb') as csvfile:
    # Create the reader object
    reader = csv.reader(csvfile)
    # Read data from the file using the reader object

# Open the file for writing
with open('file.csv', 'wb') as csvfile:
    # Create the writer object
    writer = csv.writer(csvfile)
    # Write data to the file using the writer object

4. What method takes a list argument and writes it to a CSV file?

Ans:
The writerow() method in Python's csv module is used to write a row of data to a CSV file. It takes a list as an argument, where each element in the list corresponds to a value in the row.

import csv


with open('example.csv', 'w', newline='') as csvfile:
    
    csvwriter = csv.writer(csvfile)
    
   
    csvwriter.writerow(['Name', 'Age', 'Gender'])
    
  
    csvwriter.writerow(['Alice', 25, 'Female'])
    csvwriter.writerow(['Bob', 30, 'Male'])
    csvwriter.writerow(['Charlie', 35, 'Male'])

5. What do the keyword arguments delimiter and line terminator do?

Ans:
The delimiter and lineterminator are optional keyword arguments that can be passed to the csv.writer() method in Python's csv module.

The delimiter argument specifies the character that should be used as the field delimiter when writing data to the CSV file.

import csv

# Open the CSV file for writing
with open('example.csv', 'w', newline='') as csvfile:
    # Create a writer object with tab delimiter
    csvwriter = csv.writer(csvfile, delimiter='\t')
    
    # Write data rows
    csvwriter.writerow(['Name', 'Age', 'Gender'])
    csvwriter.writerow(['Alice', 25, 'Female'])
    csvwriter.writerow(['Bob', 30, 'Male'])
    csvwriter.writerow(['Charlie', 35, 'Male'])


the delimiter argument is set to \t, which specifies that a tab character should be used as the field delimiter when writing data to the CSV file.

The lineterminator argument specifies the character(s) that should be used as the line terminator when writing data to the CSV file. By default, the line terminator is the operating system's default line separator (\r\n on Windows, \n on Unix-based systems).

import csv

# Open the CSV file for writing
with open('example.csv', 'w', newline='') as csvfile:
    # Create a writer object with custom line terminator
    csvwriter = csv.writer(csvfile, lineterminator='\n')
    
    # Write data rows
    csvwriter.writerow(['Name', 'Age', 'Gender'])
    csvwriter.writerow(['Alice', 25, 'Female'])
    csvwriter.writerow(['Bob', 30, 'Male'])
    csvwriter.writerow(['Charlie', 35, 'Male'])

6. What function takes a string of JSON data and returns a Python data structure?

Ans:
The json.loads() function in Python's built-in json module is used to parse a string of JSON data and convert it into a Python data structure, such as a dictionary or a list

import json

# Sample JSON string
json_str = '{"name": "Alice", "age": 25, "is_student": true}'

# Parse the JSON string into a Python data structure
data = json.loads(json_str)

# Print the data structure
print(data)


The json_str variable contains a string of JSON data. The json.loads() function is used to parse the JSON data and convert it into a Python data structure, which is then assigned to the data variable. The resulting Python data structure is a dictionary that contains three key-value pairs, where the keys are strings and the values are either strings, integers, or booleans.

7. What function takes a Python data structure and returns a string of JSON data?

Ans:

The json.dumps() function in Python's built-in json module is used to serialize a Python data structure, such as a dictionary or a list, into a string of JSON data.

import json

# Sample Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# Convert the Python dictionary to a JSON string
json_str = json.dumps(data)

# Print the JSON string
print(json_str)


```python

```
