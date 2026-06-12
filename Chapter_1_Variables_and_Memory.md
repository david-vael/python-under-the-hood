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

- **Cannot use Python keywords:** Reserved words like if , for , while , class , etc.
cannot be used as variable names.
> [!NOTE]
> **Invalid Examples**
> ```python
> class = "Math"          # SyntaxError
> for = 5                 # SyntaxError
> ```
> **Valid Examples**
> ```python
> class_name = "Math"
> for_loop_count = 5
> ```

### Best Practices (Conventions)
- **Use descriptive names:** Choose names that clearly indicate what the variable represents.

> [!NOTE]
> **Good**
> ```python
> student_name = "Alex"
> total_price = 99.99
> ```
> 
> **Poor**
> ```python
> x = "Alex"
> tp = 99.99
> ```

- **Use snake_case for variable names:** Separate words with underscores (Python convention).

> [!NOTE]
> **Recommended**
> ```python
> first_name = "John"
> account_balance = 1000.50
> ```
> 
> **Not recommended (but valid)**
> ```python
> firstName = "John"          # camelCase
> AccountBalance = 1000.50   # PascalCase
> ```

- **Avoid single-character names:** Except for counters in loops or very short scopes.

> [!NOTE]
> **Good for loops**
> ```python
> for i in range(10):
>     print(i)
> ```
> 
> **Better for meaningful data**
> ```python
> user_score = 85
> temperature = 72.5
> ```

### Assigning Values to Variables
In Python, you assign values to variables using the equals sign (`=`). The variable name goes on the left, and the value goes on the right.

> [!NOTE]
> **Assigning different types of values**
> ```python
> x = 10              # Integer
> price = 19.99       # Float
> name = "Alice"      # String
> is_active = True    # Boolean
> ```
> 
> **Output**
> ```text
> print(x)          # 10
> print(price)      # 19.99
> print(name)       # "Alice"
> print(is_active)  # True
> ```

### Multiple Assignments
Python allows you to assign values to multiple variables in a single line.

> [!NOTE]
> **Assign same value to multiple variables**
> ```python
> a = b = c = 100
> ```
> 
> **Output**
> ```text
> print(a, b, c)  # 100 100 100
> ```
> 
> **Assign different values to multiple variables**
> ```python
> x, y, z = 5, 10, 15
> ```
> 
> **Output**
> ```text
> print(x)  # 5
> print(y)  # 10
> print(z)  # 15
> ```

### Reassigning Variables
Variables can be reassigned to new values, even of different types, since Python is dynamically typed.

> [!NOTE]
> **Reassigning a variable**
> ```python
> count = 10
> print(count)  # Output: 10
> 
> count = 20    # Reassign to a new integer
> print(count)  # Output: 20
> 
>count = "Twenty" # Reassign to a string
>print(count)     # Output: Twenty
> ```  

### Dynamic Typing
Python is a dynamically typed language, which means you don't need to declare the type of a variable when you create it. The Python interpreter automatically determines the variable's type based on the value assigned to it.

This flexibility makes Python code more concise, but it also means you need to be careful about variable types when performing operations.

> [!NOTE]
> **Python automatically determines the type**
> ```python
> x = 10        # x is an integer
> x = "Hello"   # x is now a string
> x = 3.14      # x is now a float
> x = True      # x is now a boolean
> ```
> 
> **Output**
> ```text
> print(type(x))  # <class 'bool'>
> ```

### Type Checking
You can check the type of a variable using the `type()` function.

> [!NOTE]
> **Checking variable types**
> ```python
> age = 25
> name = "David"
> price = 19.99
> is_student = True
> ```
> 
> **Output**
> ```text
> print(type(age))         # <class 'int'>
> print(type(name))        # <class 'str'>
> print(type(price))       # <class 'float'>
> print(type(is_student))  # <class 'bool'>
> ```

### Type Conversion
You can convert between different types using built-in functions like `int()`, `float()`, `str()`, and `bool()`.

> [!NOTE]
> **Converting to different types**
> ```python
> # Converting to integer
> x = int(5.9)        # x = 5
> y = int("10")       # y = 10
> 
> # Converting to float
> a = float(5)        # a = 5.0
> b = float("3.14")   # b = 3.14
> 
> # Converting to string
> s1 = str(100)       # s1 = "100"
> s2 = str(3.14)      # s2 = "3.14"
> ```
> 
> **Converting to boolean**
> ```python
> bool(1)             # True
> bool(0)             # False
> bool("")            # False
> bool("Hello")       # True
> ```

### Common Type Errors
One of the most common mistakes in Python is trying to concatenate or perform operations between incompatible types, such as strings and integers.

> [!NOTE]
> **This will cause a TypeError**
> ```python
> age = 25
> message = "I am " + age + " years old"  # TypeError: can only concatenate str (not "int") to str
> ```
> 
> **Solution:** Convert the integer to a string before concatenating.
> 
> **Correct way**
> ```python
> age = 25
> message = "I am " + str(age) + " years old"
> print(message)  # Output: I am 25 years old
> ```
> 
> **Alternative using f-strings (recommended)**
> ```python
> message = f"I am {age} years old"
> print(message)  # Output: I am 25 years old
> ```

- **Why this happens:** Python does not automatically mix different data types in operations.

> [!NOTE]
> **Type Safety**
> Python is a strongly typed language, meaning it won't implicitly force a data type change (like turning an integer into a string) during a concatenation operation. You must explicitly convert the types yourself.
