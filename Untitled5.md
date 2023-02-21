1. To what does a relative path refer?
ans:
A relative path refers to a file or directory path that is relative to the current working directory or another specified directory, instead of being specified as a full or absolute path starting from the root directory. A relative path allows you to navigate to a file or directory by specifying the path relative to your current location in the file system.

2. What does an absolute path start with your operating system?

Ans:
An absolute path starts with the root directory of the operating system. In Unix-based systems like Linux or macOS, the root directory is represented by a forward slash (/), while in Windows, it is represented by a drive letter followed by a colon

3. What do the functions os.getcwd() and os.chdir() do?

Ans:
The os.getcwd() function returns the current working directory as a string. The os.chdir() function changes the current working directory to the directory provided as an argument.

4. What are the . and .. folders?

Ans:

The . (dot) folder represents the current directory. It is used to refer to the directory itself. For example, if you are currently in the /home/user/documents directory, you can refer to it as ..

The .. (dot dot) folder represents the parent directory. It is used to refer to the directory that contains the current directory. For example, if you are currently in the /home/user/documents directory, you can refer to its parent directory (which is /home/user) as ...

5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

Ans:
spam.txt is the base name, which is the actual name of the file.
bacon\eggs is the directory path or folder path, which is the name of the directory or folder that contains the file. The directory path bacon\eggs represents a subdirectory named "eggs" inside a directory named "bacon".

6. What are the three “mode” arguments that can be passed to the open() function?

Ans:
'r': This mode is used for reading files. It opens a file for reading, and if the file does not exist, it will raise a FileNotFoundError. This is the default mode if no mode is specified.

'w': This mode is used for writing files. It opens a file for writing, and if the file exists, it will truncate the file to zero length. If the file does not exist, it will create a new file.

'a': This mode is used for appending to files. It opens a file for writing, and if the file exists, it will append new data to the end of the file. If the file does not exist, it will create a new file for writing.


7. What happens if an existing file is opened in write mode?

Ans:
when a file is opened in write mode, the file pointer is positioned at the beginning of the file, and any data that was previously in the file is deleted. Any data that is written to the file is then written from the beginning of the file, overwriting any existing data.

Therefore, opening an existing file in write mode is a destructive operation that can result in the loss of data if the file contains important information. If you want to append new data to the existing file without overwriting the existing data, you should open the file in append mode using 'a' instead of write mode using 'w'


8. How do you tell the difference between read() and readlines()?

Ans:
read() method: This method reads the entire contents of the file as a single string and returns it. If no size argument is provided to the read() method, it will read the entire file at once. If a size argument is provided, it will read that many bytes from the file.

readlines() method: This method reads the entire contents of the file and returns a list of strings, where each string is a single line from the file. The newline character at the end of each line is included in the string.

The read() method returns the entire contents of the file as a single string, while the readlines() method returns a list of strings, where each string is a single line from the file.

9. What data structure does a shelf value resemble?
Ans:

Shelf stores key-value pairs, where each key is unique and is associated with a value. However, unlike a regular dictionary, the data in a shelf is persisted to disk and can survive across program runs. A shelf can be used to store and retrieve large amounts of data in a relatively easy and efficient way, without having to load and save the data manually.

To use a shelf in Python, you need to first import the shelve module. Then, you can create or open a shelf by calling the shelve.open() function, which returns a dictionary-like object. You can use this object to store and retrieve data by using keys that are hashable. The data can be any object that can be pickled using the pickle module.


```python

```
