# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> **Context:** I have a python function that is having trouble returning the sum of even numbers and instead returning the sum of odd numbers. 
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```
> **Persona:** I am a senior Python developer
> **Task:** Please find the bug and provide a fixed version
> **Format:** Breif explanation and corrected code block with comments in the code

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        # Changed the condition from == 1 to == 0 to correctly target even numbers
        if num % 2 == 0:
            total += num
    return total
```

**What I Learned:**
I learned that when AI knows what you are looking for and has all the information it can fix bugs in code very well. 

---

## Problem 2: Refactoring

**My Prompt:**
> **Context:** I have a working function but it uses a index based loop
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```
> **Persona:** I am a senior Python developer
> **Task:** Recreate this code for a more modern format with the same logic
> **Format:** Provide the updated code with comments

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users who are 18 or older."""
    # This list comprehension replaces the 4-line loop with one readable line
    return [user['name'] for user in users if user['age'] >= 18]
```

**What I Learned:**
AI can restructure older code and make it into more modern coding standards
-----

## Problem 3: Documenting

**My Prompt:**
> **Context:** I have a working prompt that calculates the area of a rectangle but there is no documenation 
```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
> **Persona:** I am a senior Python developer
> **Task:** Please write a complete NumPy-style docstring for this prompt
> **Format:** Provided the full prompt with NumPy-style docstring comments in the code

**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Returns
    -------
    float
        The calculated area (length * width).

    Raises
    ------
    ValueError
        If length or width are less than or equal to zero.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
I learned the in addition to fixing code AI can also comment in the code in specific formats

