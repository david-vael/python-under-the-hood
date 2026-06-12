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

### Practice Questions – Variables & Types

#### Level 1
1. Create three variables to store your name, age, and height. Print their types.
2. Assign value 50 to two variables in a single line.
3. Convert string "25" into integer and multiply it by 2.
4. Write a variable name that is invalid and explain why.

#### Level 2
1. What will be the output?
   ```python
   x = 10
   x = "Ten"
   print(type(x))

2. Fix the error:
   ```python 
   price = "100"
   total = price + 50

3. Write code to swap two variables without using a third variable.
4.Explain in one line: What is Dynamic Typing?

**All questions in this document have been carefully designed to align with the concepts covered in your class. They progress from foundational understanding to advanced application, ensuring comprehensive practice at every level.**
   
### Level 3    

1. Predict the output:
   ```python
   a = b = 5
   a = 10
   print(b)

2. What will be the output and why?
   ```python
   x = "5"
   y = 2
   print(x * y)

3. Identify valid variable names and explain why or why not:
   ```text
   _user
   2value
   total_price
   class
   userName

4. Convert the following into correct types and print their types:
    ```python
    "50", 20, 3.5, 0

          
#### Level 4
1. Explain the difference between `==` and `is`:
   ```python
   a = 1000
   b = 1000
   print(a == b)
   print(a is b)

2. Predict output and explain memory behavior:
   ```python
   a = [1, 2, 3]
   b = a
   a.append(4)
   print(b)

3. What will be the output?
   ```python
   x = True
   y = 10
   print(x + y, type(x + y))

4. Why does the data type change here?
   ```python
   x = 5
   x = x / 2
   print(type(x))

5. Identify the error and fix it:
   ```python
   age = "18"
   if age > 10:
   print("Adult")           

### Data Types in Python
A data type defines the kind of value a variable can hold. Python automatically assigns a data type based on the value stored in the variable.

#### 1. Integer (`int`)
Stores whole numbers (positive or negative).

```python
x = 10
y = -5
```
Integers are used when you need to work with whole numbers without decimal points. They can be positive, negative, or zero.

#### 2. Float (`float`)
Stores decimal numbers.

```python
price = 19.99
pi = 3.14
```
Floats are used for numbers that require precision with decimal points. They're essential for calculations involving money, measurements, or mathematical constants.

#### 3. String (`str`)
Stores text inside quotes.

```python
name = "Alex"
message = 'Hello'
```
Strings represent text data. You can use either single (') or double (") quotes. Strings are used for names, messages, or any textual information.

#### 4. Boolean (`bool`)
Stores only two values: `True` or `False`.

```python
is_active = True
is_logged_in = False
```
Booleans are used for logical conditions and control flow in programs. They help make decisions (like in if statements) and represent yes/no or on/off states.

#### 5. NoneType (`None`)
Represents the absence of a value.

```python
x = None
```
__None__ is a special constant in Python that represents "nothing" or "no value." It's often used as a placeholder or to indicate that a variable hasn't been assigned a meaningful value yet.

### Checking Data Type

```python
x = 5
print(type(x))  # <class 'int'>
```
The **type()** function returns the data type of a variable. This is useful for debugging or when you need to verify what kind of data you're working with. In this example, **type(x)** returns **<class 'int'>** because **x** holds an integer value.

### Key Takeaways

* **Python is dynamically typed:** You don't need to declare data types explicitly; Python figures it out based on the value you assign.
* **Type conversion:** You can convert between types using functions like `int()`, `float()`, `str()`, and `bool()`.
* **Understanding data types:** Knowing which data type to use helps you write efficient code and avoid errors in your programs.

  
### Additional Notes

#### 1. Boolean Internal Behavior
`True` behaves like `1` and `False` behaves like `0` in arithmetic operations.

```python
print(True + 5)    # 6
print(False * 10)  # 0
```
In Python, booleans are a subclass of integers. This means **True** equals **1** and **False** equals **0** when used in mathematical operations. This can be useful in certain calculations but should be used carefully to avoid confusion.

#### 2. Case Sensitivity Reminder
Strings are case-sensitive (`"Hello"` ≠ `"hello"`).

```python
word1 = "Hello"
word2 = "hello"
print(word1 == word2)  # False
```
Python treats uppercase and lowercase letters as different characters. When comparing strings, **"Hello"** and **"hello"** are not equal. This is important to remember when working with user input, file names, or any text comparison.

### Input and Output

#### 1. `input()` Function
The `input()` function allows your program to receive data from the user through the keyboard. It pauses the program execution and waits for the user to type something and press Enter. By default, whatever the user types is returned as a string, even if they enter numbers. User input is always stored as text unless converted.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

#### 2. Type Casting with Input
Since `input()` always returns a string, you'll need to convert it to other data types when working with numbers or other data types. This is done using type casting functions like `int()`, `float()`, or `bool()`. Invalid input may cause errors.

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print(f"You are {age} years old and {height}m tall.")
```

#### 3. `print()` Function
The `print()` function displays output to the console. It can handle multiple values separated by commas, which are automatically separated by spaces when printed. You can also use the `sep` and `end` parameters to customize the output format.

```python
print("Hello", "World")
print("Python", "is", "fun", sep="-")
print("Hello", end=" ")
print("World")
```

#### 4. Formatted Output (f-strings)
F-strings (formatted string literals) provide a clean and readable way to embed expressions inside string literals. They start with an `f` or `F` before the opening quote, and expressions are placed inside curly braces `{}`. This is the recommended approach for string formatting in modern Python.

```python
name = "Alex"
age = 18
score = 95.5
print(f"My name is {name} and I am {age} years old.")
print(f"I scored {score:.1f}% on the test.")
```

#### 5. Escape Characters
Escape characters are special sequences that start with a backslash `\` and allow you to include special characters in strings. 

The most common ones are:
* `\n` $\rightarrow$ Creates a new line
* `\t` $\rightarrow$ Inserts a tab space
* `\\` $\rightarrow$ Inserts a backslash
* `\'` and `\"` $\rightarrow$ Insert quotes without ending the string

Example:

```python
print("Hello\nWorld")
print("Name:\tAlex\nAge:\t18")
print("She said, \"Python is awesome!\"")
```

### Comments in Python

#### 1. Single-Line Comments
Single-line comments are used for short explanations or notes about specific lines of code. They start with the `#` symbol, and everything after it on that line is ignored by Python.

Example:

```python
# This is a comment
x = 10  # variable storing age
```

#### 2. Multi-Line Comments
Python doesn't have a dedicated multi-line comment syntax, but there are two common approaches:
* **Multiple `#` symbols:** Use `#` at the beginning of each line.
* **Triple quotes:** Use triple quotes `"""` or `'''` (primarily used for documentation strings or docstrings).

Example using multiple `#` symbols:
```python
# This function calculates the area of a rectangle
# It takes width and height as arguments
# and returns the calculated area value
def calculate_area(width, height):
    return width * height
```

### Basic Errors / Exceptions in Python

#### 1. SyntaxError
A `SyntaxError` occurs when Python encounters code that doesn't follow the language's grammatical rules. This is like making a spelling or punctuation mistake that prevents Python from understanding what you're trying to do.

Example:

```python
print("Hello"
```
This raises a **SyntaxError** because the closing parenthesis is missing. Python expects proper structure and will refuse to run code with syntax mistakes.

#### 2. NameError
A NameError happens when you try to use a variable or function name that Python doesn't recognize. This typically means you're referencing something before it has been defined or you've misspelled the name.

Example:

```python
print(age)  # age not defined
```
Since **age** was never created or assigned a value, Python doesn't know what you're referring to and raises a *'NameError'.


  
