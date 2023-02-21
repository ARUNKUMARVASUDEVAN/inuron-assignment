1. How do you distinguish between shutil.copy() and shutil.copytree()?

Ans:
    
shutil.copy() function is used to copy a single file,
while the shutil.copytree() function is used to copy an entire directory and its contents.

2. What function is used to rename files??

Ans:
os.rename()

3. What is the difference between the delete functions in the send2trash and shutil modules?

Ans:
The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files and folders.

4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

Ans:
The zipfile. ZipFile() function is equivalent to the open() function

5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.?






```python
import os, shutil

def selectiveCopy(folder, extensions, destFolder):
	folder = os.path.abspath(folder)
	destFolder = os.path.abspath(destFolder)
	print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			name, extension = os.path.splitext(filename)
			if extension in extensions:
				fileAbsPath = foldername + os.path.sep + filename
				print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.php', '.py']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)
```

    Looking in C:\Users\ARUN KUMAR V\Assignments\randomFolder for files with extensions of .php, .py
    
