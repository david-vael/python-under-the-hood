## Variables
__Variables__ are used to store data values in Python. Unlike other programming languages,
Python has no command for declaring a variable - you simply assign a value to it using
the equals sign (=).
Use **print()** to display output to the console.
```python
x = 5
name = "John"
print("x:", x)
print("Name:", name)
```
> **Output:**
> `x: 5`
> `Name: John`​​

Python is dynamically typed, meaning you don't need to specify the variable type, and
variables can change type after they have been set.

__Variables (Alternative Definition)__
A variable is a named container used to store data values in a program. It allows the
programmer to save information and reuse or modify it later during execution.

###Rules for Naming Python Variables
Python has specific rules and conventions for naming variables to ensure code clarity
and avoid errors.
###Required Rules

**- Must start with a letter or underscore:** Variable names cannot begin with a number.

> [!NOTE]
> **Valid**
> ```python
> name = "Alice"
> _count = 10
> user_age = 25
> ```
> 
> **Invalid**
> ```python
> 1st_name = "Bob"    # SyntaxError
> ```

**- Can only contain alphanumeric characters and underscores:** Letters (a-z, A-Z), numbers (0-9), and underscores (`_`) are allowed. Special characters like `@`, `#`, `$`, `%`, etc. are not allowed.

> [!NOTE]
> **Valid Examples**
> ```python
> my_variable = 100
> data2 = "test"
> _private_var = True
> ```
> 
> **Invalid Examples**
> ```python
> my-variable = 50     # SyntaxError: can't assign to expression
> user@name = "John"   # SyntaxError: invalid syntax
> ```

- **Case-sensitive:** Variables with different cases are treated as different variables.
> [!NOTE]
> ```python
> age = 20
> Age = 30
> AGE = 40
> 
> print(age)  # Output: 20
> print(Age)  # Output: 30
> print(AGE)  # Output: 40


  
