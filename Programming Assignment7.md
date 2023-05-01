1. Write a Python Program to find sum of array?


```python
# initialize the array
arr = [1, 2, 3, 4, 5]

# calculate the sum of array
array_sum = sum(arr)

# print the sum of array
print("The sum of array is:", array_sum)

```

    The sum of array is: 15
    

2. Write a Python Program to find largest element in an array?


```python
# initialize the array
arr = [10, 50, 20, 30, 40]

# initialize the maximum element as the first element of the array
max_element = arr[0]

# iterate through the array to find the maximum element
for element in arr:
    if element > max_element:
        max_element = element

# print the maximum element
print("The largest element in the array is:", max_element)

```

    The largest element in the array is: 50
    

3. Write a Python Program for array rotation?


```python
def rotate_array(arr, n):
    # get the length of the array
    length = len(arr)
    # calculate the number of positions to rotate
    rotate_by = n % length
    # rotate the array
    rotated_array = arr[rotate_by:] + arr[:rotate_by]
    return rotated_array

# example usage
arr = [1, 2, 3, 4, 5]
n = 2
rotated_array = rotate_array(arr, n)
print(rotated_array) # output: [3, 4, 5, 1, 2]

```

    [3, 4, 5, 1, 2]
    

4. Write a Python Program to Split the array and add the first part to the end?


```python
def split_and_add(arr, n):
    temp = [0] * n
    for i in range(0, n):
        temp[i] = arr[i]
    for i in range(0, len(arr)-n):
        arr[i] = arr[i+n]
    for i in range(0, n):
        arr[len(arr)-n+i] = temp[i]
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
n = 2
print("Original array: ", arr)
print("After splitting and adding: ", split_and_add(arr, n))

```

    Original array:  [1, 2, 3, 4, 5]
    After splitting and adding:  [3, 4, 5, 1, 2]
    

5. Write a Python Program to check if given array is Monotonic?


```python
def is_monotonic(arr):
    """
    Checks if an array is monotonic.
    """
    n = len(arr)
    if n <= 2:
        return True
    inc = dec = True
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dec = False
        elif arr[i] < arr[i-1]:
            inc = False
        if not inc and not dec:
            return False
    return True

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [1, 2, 3, 2, 1]
print(is_monotonic(arr1)) # Output: True
print(is_monotonic(arr2)) # Output: True
print(is_monotonic(arr3)) # Output: False

```

    True
    True
    False
    
