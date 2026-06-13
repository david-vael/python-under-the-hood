© 2026 David Vael | Licensed under CC-BY 4.0
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

### Rules for Naming Python Variables
Python has specific rules and conventions for naming variables to ensure code clarity
and avoid errors.
### Required Rules

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
> print(AGE)  # Output: 40 ```

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
> count = "Twenty" # Reassign to a string
> print(count)     # Output: Twenty
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
   print(type(x))```

2. Fix the error:
   ```python 
   price = "100"
   total = price + 50```

3. Write code to swap two variables without using a third variable.
4. Explain in one line: What is Dynamic Typing?

**All questions in this document have been carefully designed to align with the concepts covered in your class. They progress from foundational understanding to advanced application, ensuring comprehensive practice at every level.**
   
### Level 3    

1. Predict the output:
   ```python
   a = b = 5
   a = 10
   print(b)```

2. What will be the output and why?
   ```python
   x = "5"
   y = 2
   print(x * y)```

3. Identify valid variable names and explain why or why not:
   ```text
   _user
   2value
   total_price
   class
   userName```

4. Convert the following into correct types and print their types:
    ```python
    "50", 20, 3.5, 0```

          
#### Level 4
1. Explain the difference between `==` and `is`:
   ```python
   a = 1000
   b = 1000
   print(a == b)
   print(a is b)```

2. Predict output and explain memory behavior:
   ```python
   a = [1, 2, 3]
   b = a
   a.append(4)
   print(b)```

3. What will be the output?
   ```python
   x = True
   y = 10
   print(x + y, type(x + y))```

4. Why does the data type change here?
   ```python
   x = 5
   x = x / 2
   print(type(x))```

5. Identify the error and fix it:
   ```python
   age = "18"
   if age > 10:
   print("Adult")```         

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
The `type()` function returns the data type of a variable. This is useful for debugging or when you need to verify what kind of data you're working with. In this example, **type(x)** returns `<class 'int'>` because `x` holds an integer value.

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
In Python, booleans are a subclass of integers. This means `True` equals `1` and `False` equals `0` when used in mathematical operations. This can be useful in certain calculations but should be used carefully to avoid confusion.

#### 2. Case Sensitivity Reminder
Strings are case-sensitive (`"Hello"` ≠ `"hello"`).

```python
word1 = "Hello"
word2 = "hello"
print(word1 == word2)  # False
```
Python treats uppercase and lowercase letters as different characters. When comparing strings, `"Hello"` and `"hello"` are not equal. This is important to remember when working with user input, file names, or any text comparison.

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
F-strings (formatted string literals) provide a clean and readable way to embed expressions inside string literals. They start with an `f` or `F` before the opening quote, and expressions are **placed inside curly braces `{}`**. This is the recommended approach for string formatting in modern Python.

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
This raises a `SyntaxError` because the closing parenthesis is missing. Python expects proper structure and will refuse to run code with syntax mistakes.

#### 2. NameError
A NameError happens when you try to use a variable or function name that Python doesn't recognize. This typically means you're referencing something before it has been defined or you've misspelled the name.

Example:

```python
print(age)  # age not defined
```
Since `age` was never created or assigned a value, Python doesn't know what you're referring to and raises a `NameError`.

#### 3. TypeError
A `TypeError` occurs when you try to perform an operation on incompatible data types. Python is strict about how different types interact, so mixing types inappropriately will cause this error.

Example:

```python
   "5"+5
```
Here, you're trying to add a string (` "5" `) to an integer (`5`). Python doesn't know whether to treat this as text concatenation or mathematical addition, so it raises a `TypeError`.

#### 4. IndentationError
An IndentationError is unique to Python, which uses whitespace (spaces or tabs) to define code blocks. If your indentation is inconsistent or incorrect, Python can't determine the structure of your code.

Example:

  ```python
     if True:
     print("Hello")
```
The `print` statement should be indented to show it belongs inside the `if` block. Without proper indentation, Python raises an `IndentationError`.

#### Quick Tips
**Always close parentheses, brackets, and quotes** to avoid `SyntaxErrors`.

**Define variables before using them** to prevent `NameErrors`.

**Be mindful of data types** when performing operations to avoid `TypeErrors`.

**Use consistent indentation** (typically 4 spaces) throughout your code to prevent `IndentationErrors`.

---

# 🔑 Answer Key – Chapter 1

#### Level 1
1. Create three variables to store your name, age, and height. Print their types.

```python
# Assigning values
my_name = "David"       # String (str)
my_age = 18            # Integer (int)
my_height = 5.9        # Floating-point number (float)

# Printing their values and types
print("Name:", my_name, "Type:", type(my_name))
print("Age:", my_age, "Type:", type(my_age))
print("Height:", my_height, "Type:", type(my_height))
```
**What's happening behind the scenes:**
Python is a dynamically typed language. You don't have to explicitly declare whether a variable is a text or a number before using it; Python automatically figures out the data type at runtime based entirely on the value you assign to it.

2. Assign value 50 to two variables in a single line.

```python
# Chained assignment
x = y = 50

print("x:", x)
print("y:", y)
```
**What's happening behind the scenes:**
This is called a chained assignment. Instead of creating two separate memory spaces holding the integer 50, both variable labels (`x` and `y`) point directly to the exact same single integer object 50 in Python's internal heap memory.

3. Convert string "25" into integer and multiply it by 2.

```python
# Raw string value
string_val = "25"

# Type casting to integer
converted_int = int(string_val)

# Mathematical operation
result = converted_int * 2
print("Result:", result)  # Output: 50
```
**What's happening behind the scenes:**
If you don't explicitly cast the string using `int()`, running ` "25" * 2 ` triggers string replication, which would yield the text ` "2525" ` instead of performing math. Using ` int() ` changes the data type completely.

4. Write a variable name that is invalid and explain why.

```python
# Invalid example:
1st_place = "Gold Medal"  # Throws a SyntaxError
```
**What's happening behind the scenes:**
Python syntax strictly prohibits variable names from beginning with a number. They must always start with either a letter or an underscore (`_`). If the compiler sees a numeric digit at the very beginning of a word label, it fails to parse it and instantly flags a `SyntaxError`.

#### Level 2
1. What will be the output?

```python
x = 10
x = "Ten"
print(type(x))
```
Answer: `<class 'str'>`

**What's happening behind the scenes:**
Python is a dynamically typed language, which means variable names are not typed containers; they are merely references (or labels) pointing to concrete objects allocated on the heap memory.

**First Assignment** (`x = 10`): CPython allocates a `PyLongObject` structure in memory to represent the integer `10`. The identifier `x` is added to the local namespace dictionary (`locals()`), pointing directly to this integer object's memory address. The object's reference count is incremented to `1`.

**Reassignment** (`x = "Ten"`): CPython creates a brand new `PyUnicodeObject` structure to represent the string `"Ten"`. The reference pointer inside the `x` label is updated to point to this new string address.

**Memory Cleanup**: Because `x` shifted its focus, the reference count of the integer object `10` drops by 1. Since its reference counter hits exactly `0`, CPython's reference counting mechanism immediately deallocates the object (or leaves it to the cyclical Garbage Collector if it were a container type), freeing up that heap space.

2. Fix the error:

```python
price = "100"
total = price + 50
```
```python
price = "100"
total = int(price) + 50  # Type casting the string to an integer
print(total)             # Output: 150
```
**What's happening behind the scenes:**
Python is a **strongly typed** language, meaning the interpreter strictly enforces type boundaries and refuses to implicitly coerce incompatible data types during operations.

**The Failure Mechanics** (`"100" + 50`): When CPython encounters the binary addition operator (`+`), it checks the left operand's type structure. For a string, it looks for an internal C slot function named `nb_add` (numeric addition) or `sq_concat` (sequence concatenation). A string object knows how to concatenate with another string, but when it detects that the right operand is a `PyLongObject` (integer), it fails to find a valid operation rule and immediately raises a `TypeError`.

**The Memory Fix** (`int(price)`): By calling the `int()` constructor, you tell CPython to spin up a new integer object in memory by parsing the character array inside the string. Once both objects share the same numeric type system, CPython can safely execute the underlying C-level addition and bind the result to `total`.

3. Write code to swap two variables without using a third variable.

```python
a = 5
b = 10

# The Pythonic tuple unpacking swap
a, b = b, a

print("a:", a, "b:", b)  # Output: a: 10 b: 5
```
**What's happening behind the scenes:**
In many traditional languages, swapping values requires a manual third variable to avoid overwriting data in memory. Python elegantly resolves this using an optimization called **tuple packing and unpacking.**

**The Right-Hand Evaluation** (`b, a`): CPython executes from right to left. When it evaluates `b, a`, it pushes the memory addresses of both objects onto its internal evaluation stack. At the bytecode level, it reads these values sequentially using `LOAD_NAME`.

**The Stack Swap Optimization**: Historically, Python would explicitly call `BUILD_TUPLE` to wrap these references into a temporary heap-allocated `PyTupleObject`. However, modern CPython implementations feature a specific bytecode optimization for small swaps. Instead of allocating an actual tuple object in memory, it keeps the references directly on the evaluation stack and utilizes the highly optimized `SWAP` **bytecode instruction** to reorder the top elements of the stack.

**Unpacking** (`a, b =`): Finally, the reordered values on the stack are popped off sequentially via `STORE_NAME` and bound to the identifiers on the left-hand side. The labels are updated seamlessly in a single atomic instruction cycle without any heap allocation overhead.

4. Explain in one line: What is Dynamic Typing?

**Answer:** Dynamic typing means variable data types are checked and associated at runtime (when the program executes) rather than at compile time, allowing a single variable label to reference completely different data types over time.

**What's happening behind the scenes:**
In statically typed languages (like C++ or Java), type information belongs to the *variable slot* itself, which is fixed in memory during compilation. In Python, **variables have absolutely no type; only the objects themselves carry types.** Every single entity in Python is a C structure wrapped as a `PyObject`. Inside the foundational header of every object is a field called `ob_type`, which is a pointer pointing directly to its type descriptor object (such as `PyLong_Type` for integers or `PyUnicode_Type` for strings). Because data names are just simple string pointers in a dictionary namespace tracking these structures, the interpreter doesn't care what type an object is until it attempts an operation on it at runtime, fetching and checking the object's `ob_type` layout on the fly.

#### Level 3
1. Predict the output:

```python
a = b = 5
a = 10
print(b)
```
Answer: `5`

**What's happening behind the scenes:**
This question highlights the foundational mechanics of namespace pointer manipulation and object immutability in Python.

**The Chained Assignment** (`a = b = 5`): Python executes this from right to left. Because `5` falls within CPython's static global integer cache (which pre-allocates integers from `-5` to `256` at interpreter startup), CPython doesn't even need to allocate new heap memory. It fetches the existing, permanent `PyLongObjec`t address for `5`. The keys `"b"` and then `"a"` are inserted into the local namespace dictionary (`locals()`), with both storing a pointer to this exact same memory address. The cached object's internal reference counter is incremented.

**The Reassignment** (`a = 10`): Because integers are strictly )**immutable**, the interpreter cannot modify the value inside the memory address to which `a` points. Instead, when `a = 10` runs, CPython fetches the memory address of the cached integer object `10` and updates the pointer of the key `"a"` in the namespace dictionary to point to it.

**The Result:** The pointer for the key `"b"` remains completely untouched, securely anchored to the original shared memory address of `5`. Thus, printing `b` outputs `5`.

2. What will be the output and why?

```python
x = "5"
y = 2
print(x * y)
```
**Answer: 55**

**What's happening behind the scenes:**
This question demonstrates **operator overloading**, where the exact C-level function executed by a symbol (`*`) is determined dynamically by the type structures of the objects involved.

**The Slot Lookup Mechanics:** When CPython evaluates the binary multiplication operator (`*`), it looks at the operands. Because the left operand `x` is a `PyUnicodeObject` (string), the interpreter does not trigger standard numeric multiplication. Instead, it looks up the object's type descriptor (`PyUnicode_Type`) and routes the operation to its sequence repetition slot function, historically known as `sq_repeat`.

**Memory Execution & Immutability:** Because strings are strictly **immutable**, CPython cannot alter the existing string buffer of `"5"`. The `sq_repeat` function calculates the exact required size of the final string ($1 \text{ byte} \times 2 = 2 \text{ bytes}$ plus the null terminator), requests a brand-new memory allocation on the heap, and sequentially copies the character data into the new buffer.

**The Result:** A fresh string object containing the character array `"55"` is instantiated, pushed to the evaluation stack, and printed, while the original objects `x` and `y` remain entirely unchanged in memory.

3. Identify valid variable names and explain why or why not:

* `_user`
* `2value`
* `total_price`
* `class`
* `userName`

**Answer & Breakdown:**

* **`_user` (Valid):** CPython's lexical analyzer permits variable identifiers to begin with an underscore. Internally, a single leading underscore is structurally treated as a valid character but conventionally flags a variable as intended for internal or private scope within a module or class.
* **`2value` (Invalid):** This triggers a `SyntaxError: invalid decimal literal` (or `invalid token`). The lexical analyzer requires all identifiers to match a strict grammar rule where the first character must be a non-digit (a letter or underscore). If it encounters a leading digit, it attempts to parse it as a numeric literal, causing a structural parsing failure when alphabetic characters immediately follow it.
* **`total_price` (Valid):** This is completely valid and perfectly adheres to PEP 8's standard `snake_case` convention. It contains only permissible alphanumeric characters and underscores.
* **`class` (Invalid):** This triggers a `SyntaxError: invalid syntax`. The string `class` is a hard-coded keyword reserved by Python's grammar rules to define object structures. Reserved keywords are registered directly in the compiler's token table and cannot be re-mapped as variable identifiers in any namespace dictionary.
* **`userName` (Valid):** This is lexically valid and follows `camelCase` conventions. Because Python is strictly case-sensitive, it processes lowercase and uppercase characters as distinct byte streams, meaning `userName` is treated as a completely different identifier from `username`.

**🧠 Under the Hood (Identifier Interning):**
Whenever CPython parses a valid variable identifier (like `total_price` or `userName`), it doesn't just treat it as a random string. To maximize performance during namespace lookups, CPython automatically passes all valid identifier strings through an internal C function called `PyUnicode_InternInPlace()`.

This process ensures that only a **single unique instance** of that identifier string exists in a global interned dictionary. When Python looks up a variable name later during execution within `locals()` or `globals()`, it doesn't waste clock cycles checking the string character-by-character; instead, it performs a lightning-fast C-level **pointer comparison** (`address_a == address_b`)!

4. Convert the following into correct types and print their types: `"50"`, `20`, `3.5`, `0`

```python
# Performing explicit type casting on the values
print(type(int("50")))   # Output: <class 'int'>
print(type(str(20)))     # Output: <class 'str'>
print(type(int(3.5)))    # Output: <class 'int'>
print(type(bool(0)))     # Output: <class 'bool'>
```
**What's happening behind the scenes:**
Explicit type casting instructs CPython to invoke the target type's constructor function (`_ _init_ _` or `_`_new_`_` slots at the underlying C layer) to translate data configurations across distinct memory representation systems:

`int("50")`: CPython passes the string to an internal text-to-integer parsing loop. It reads the Unicode code points of the character array, confirms they are valid numeric base-10 digits, and allocates a new binary `PyLongObject` on the heap to store the integer value `50`.

`str(20)`: CPython reads the raw binary value of the integer object and converts it into its equivalent human-readable ASCII/Unicode character representation, wrapping the byte stream in a brand new immutable `PyUnicodeObject`.

`int(3.5)`: When casting a float to an integer, CPython does not perform mathematical rounding. Instead, it invokes truncation logic inside the float's native type slot, slicing away the decimal fractional part entirely from the `PyFloatObject` structure to yield a clean integer value of `3`.

`bool(0)`: In CPython, integers, empty sequences, and `None` are structurally mapped to evaluate as falsy. To optimize performance and conserve system memory, CPython maintains two permanent, pre-allocated boolean objects globally. Passing `0` to the boolean constructor tells the interpreter to drop a fresh allocation completely and instantly point your execution reference link straight to the immutable global `PyBool_False` singleton address.

#### Level 4 (Expert Level)
1. Explain the difference between `==` and `is`:

```python
a = 1000
b = 1000
print(a == b)
print(a is b)
```
**Answer** : 
`print(a == b)` outputs `True`
`print(a is b)` outputs `False`

**What's happening behind the scenes:**
Python treats value comparison and structural identity as two fundamentally distinct low-level operations inside its runtime engine.

**The Value Comparison Operator (`==` Mechanics):** When CPython encounters the `==` operator, it performs a structural equality check by looking up the left operand's type descriptor and invoking its native comparison slot function, known at the C layer as `tp_richcompare` (which maps to the special method `__eq__` in Python). For integers, this function bypasses memory address locations entirely. It reads the raw sign-and-digit bit arrays inside both `PyLongObject` structures on the heap, notices that the numeric payload values are both exactly `1000`, and returns a pointer to the global `PyBool_True` singleton object.

**The Identity Operator (`is` Mechanics):** The `is` operator checks for object identity. At the bytecode level, it translates to a highly optimized, lightning-fast `IS_OP` instruction. Unlike `==`, it does not trigger any type descriptor method lookups or slot evaluations. Instead, it evaluates the pointers directly on the virtual machine stack. It behaves exactly like comparing raw memory addresses in C:
           
$$
id(a) == id(b)
$$

Because the integer `1000` falls completely outside of CPython’s static small integer cache range (which permanently binds objects from `-5` to `256` at startup), each assignment statement forces CPython to allocate a brand-new, isolated memory block on the heap. Since `a` and `b` reference two entirely different `PyLongObject` memory addresses, the pointer comparison fails and returns `PyBool_False`.

### 📋 Key Structural Breakdown

| Feature | == (Equality) | is (Identity) |
| :--- | :--- | :--- |
| **What it checks** | Do the objects have the same value/content? | Do the variables point to the exact same memory address? |
| **CPython Mechanics** | Calls the type's `tp_richcompare` (`__eq__`) slot loop. | Executes the `IS_OP` instruction (pointer comparison). |
| **Performance Overhead** | Slower (requires object attribute evaluation). | Incredibly fast (direct memory address match). |
| **Primary Use Case** | Data checks, structural/mathematical comparisons. | Checking singleton references (e.g., `variable is None`). |

**2. Predict the output and explain the underlying memory behavior:**
```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)
```
Answer: `[1, 2, 3, 4]`

**What's happening behind the scenes:**
This question targets the architectural mechanics of mutable objects and pointer alias replication inside Python's heap space.

**The List Allocation (`a = [1, 2, 3]`):** When CPython evaluates a list literal, it allocates a mutable container object known at the C layer as a `PyListObject`. Crucially, a Python list does not actually store raw data items sequentially inside its own block. Instead, a `PyListObject` contains a pointer (`ob_item`) pointing to a secondary, dynamically allocated array of memory addresses. Each address in that array holds a pointer to a separate `PyLongObject` on the heap (representing 1, 2, and 3). The variable `a` inside your local namespace dictionary (`locals()`) is assigned a direct pointer to this master `PyListObject`.

**The Pointer Copy (`b = a`):** The assignment statement `b = a` does not copy the list object, nor does it duplicate the items inside it. Instead, CPython executes a lightweight pointer assignment. The identifier string `"b"` is added to your namespace dictionary, and it is given a copy of the exact same memory address value held by `a`. At this step, both `a` and `b` are reference labels pointing to the identical `PyListObject` structure. The internal reference counter (`ob_refcn`t) of that specific list object is incremented to 2.

**In-Place Mutation (`a.append(4)`):** Because lists are mutable, operations like `.append()` modify the existing object directly in memory rather than generating a new one. When `a.append(4)` is called, CPython invokes its internal C function `list_append()`. It checks if the underlying contiguous pointer array has enough allocated capacity slot padding. If it does (or after resizing via `list_resize()`), it inserts a new pointer to a `PyLongObject` representing 4 at the end of the internal array.

**The Output (`print(b)`):** When you pass b to the `print()` function, the interpreter looks up the identifier `"b"` in the namespace, follows its pointer address to the heap, and reads the target `PyListObject`. Because `a` and `b` point to the exact same object, any modification performed via the label `a` is instantly visible when inspecting the object through the label `b`.
           
$$
id(a) == id(b)
$$

### 📋 Key Structural Breakdown

| Action | Memory State / Allocation Overhead | Impact on Reference Count |
| :--- | :--- | :--- |
| `a = [1, 2, 3]` | Allocates one `PyListObject` structure + an array of 3 item pointers on the heap. | `ob_refcnt` of the list = 1 |
| `b = a` | Zero heap allocation overhead. Copies a single 8-byte memory address into the namespace map. | `ob_refcnt` of the list = 2 |
| `a.append(4)` | Modifies the existing array buffer in-place (may trigger a C `realloc` if array capacity limits are hit). | No change to the list's reference count |

3. What will be the output?

```python
x = True
y = 10
print(x + y, type(x + y))
```
Answer: `11 <class 'int'>`

**What's happening behind the scenes:**
This question highlights the structural architecture of the boolean type system and implicit numeric promotion inside the CPython runtime engine.

**CPython Object Architecture (`bool` subclassing `int`):** In Python, booleans are not an independent primitive type. At the core C layer, the boolean type structural definition (`PyBool_Type`) explicitly inherits from the integer type structural definition (`PyLong_Type`).
```c
// Conceptual CPython under-the-hood structural definition
PyTypeObject PyBool_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "bool",
    sizeof(PyLongObject), // Booleans use the exact same memory footprint as a standard integer!
    ...
};
```
Because of this architectural decision made early in Python's development to preserve backward compatibility, every boolean object is structurally a `PyLongObject` under the hood.

**The Singleton Memory Mapping:** To avoid allocating memory constantly during runtime execution, CPython initializes exactly two permanent boolean objects globally at interpreter startup:

  * `_Py_TrueStruct` (referenced via `True`) holding an internal value payload of `1`.

  * `_Py_FalseStruct` (referenced via `False`) holding an internal value payload of `0`.

The variable `x` simply holds a pointer directly to the immutable global `True` singleton object on the heap.

**Binary Addition & Type Promotion Mechanics (`+`):** When CPython executes the binary addition instruction (`BINARY_OP`), it inspects the type descriptors of both operands. The left operand x points to `PyBool_Type`, while the right operand y points to `PyLong_Type`. Because `PyBool_Type` inherits from `PyLong_Type`, it does not implement its own unique arithmetic slot logic. Instead, the operator lookup loops directly up to the parent integer type slot function, known as `long_add`. The `long_add` function reads the integer value payload of `True` (which is `1`) and the value payload of `10`, performing standard native C-level binary addition.

**The Output and Final Type:** The arithmetic operation yields a value of `11`. Because the operation was executed by the integer type’s native arithmetic system (`long_add`), the resulting memory chunk is packed inside a standard, brand-new `PyLongObject` on the heap. The structural identity of the boolean is entirely shed during the math conversion pass. Therefore, calling `type(x + y)` evaluates directly to `<class 'int'>` instead of keeping any boolean traits.

**📋 Key Behavior Verification**
```python
print(True + True)      # Output: 2   -> (1 + 1) via long_add()
print(False * 100)      # Output: 0   -> (0 * 100) via long_mul()
print(True - False)     # Output: 1   -> (1 - 0) via long_sub()
```

4. Why does the data type change here?

```python
x = 5
x = x / 2
print(type(x))
```

Answer: The data type changes from `<class 'int'>` to `<class 'float'>` because standard division (`/`) in Python is explicitly defined to perform true division, which always returns a floating-point number.

**What's happening behind the scenes:**
This question highlights the structural divergence between integer and floating-point representations inside the CPython virtual machine and how operator slots manage numeric precision.

 **The Bytecode Divergence (`/` vs `//`):** When the CPython compiler parses your script, the specific arithmetic operator determines which bytecode instruction is emitted to the stack:

1. The floor division operator (`//`) emits the `BINARY_FLOOR_DIVIDE` bytecode.

2. The true division operator (`/`) emits the `BINARY_TRUE_DIVIDE` bytecode.

When the virtual machine encounters `BINARY_TRUE_DIVIDE` with two integer operands, it bypasses integer math systems entirely.

**Slot Lookup & Implicit C Coercion:** At the C layer, CPython looks up the numeric type slots inside the left operand's `PyLong_Type` descriptor. It routes the operation to the true division slot function, known natively as `long_true_divide`. Inside `long_true_divide`, CPython extracts the raw numerical value from the `PyLongObject` structure of 5 and the `PyLongObject` structure of 2. It converts both values into native C `double` primitives on the execution stack and executes a standard hardware-level floating-point division:

$$
\text{result} = 5.0 / 2.0 = 2.5
$$

**Heap Reallocation and Label Binding:** Because a primitive C `double` cannot reside inside an integer type container wrapper, CPython allocates a brand-new `PyFloatObject` on the heap to house the decimal payload `2.5`. Finally, the assignment operator updates the pointer of the key `"x"` inside your local namespace dictionary (`locals()`). The label breaks its original reference link with the cached integer `5` and binds directly to the memory address of this new floating-point structure. Because Python is dynamically typed, the variable label accepts this pointer transition seamlessly at runtime.

### 📋 Key Structural Breakdown

| Operation Type | Bytecode Instruction | C-Level Function Executed | Resulting Heap Structure |
| :--- | :--- | :--- | :--- |
| `5 / 2` (True Div) | `BINARY_TRUE_DIVIDE` | `long_true_divide` | Allocates a new `PyFloatObject` (2.5) |
| `5 // 2` (Floor Div) | `BINARY_FLOOR_DIVIDE` | `long_floor_divide` | Allocates a new `PyLongObject` (2) |

5. Identify the error and fix it:

```python
age = "18"
if age > 10:
print("Adult")
```
Answer: This snippet contains two distinct structural errors that completely prevent execution:

   1. `IndentationError`: The execution block directly following the conditional statement is not indented.

   2. `TypeError`: An un-cast string (`"18"`) is being compared directly to a numeric integer (`10`).

**The Fixed Code:**    
```python
age = "18"
if int(age) > 10:
    print("Adult")  # Explicit type casting and correct block indentation
```
**🧠 What's happening behind the scenes:**
This scenario perfectly illustrates how CPython bifurcates its pipeline into a strict compile-time parsing phase and a dynamic runtime execution phase.

**Phase 1: Lexical Parsing and the `IndentationError` (Compile-Time):** Before CPython looks at variable values or data types in memory, it feeds the raw source code through its tokenizer and structural parser. Python's grammar uniquely relies on indentation tokens (`INDENT` and `DEDENT`) to delimit logical code blocks. When the parser processes an `if` statement token, it alters its state to expect a mandatory `INDENT` token on the subsequent line. Because `print("Adult")` is flush with the left margin, the parser fails to construct the Abstract Syntax Tree (AST), instantly halts compilation, and throws an `IndentationError: expected an indented block` before a single line of code actually runs.

**Phase 2: Runtime Evaluation and the `TypeError` Mechanics:** Once the indentation is syntactically corrected, the script successfully compiles to bytecode and proceeds to runtime execution. When the virtual machine reaches the conditional evaluation line, it processes the greater-than operator (`>`), triggering the `COMPARE_OP` bytecode instruction. CPython checks the type descriptor of the left operand (`age`). Because it points to a `PyUnicodeObject` (string), the interpreter evaluates the string's native C comparison slot function, `tp_richcompare`.

**The Type Fallback Loop:** The string's `tp_richcompare` function is designed to evaluate text characters. When it detects that the right-hand operand is a `PyLongObject` (integer), Python's strict **strong typing** design philosophy prevents it from performing an implicit runtime conversion. The slot function breaks off execution and returns an internal sentinel pointer constant called `Py_NotImplemented`. Upon receiving `Py_NotImplemented`, the virtual machine attempts a reversed fallback check: it asks the right-hand integer object if it knows how to compare itself to a string. The integer's slot function also returns `Py_NotImplemented`. Having exhausted all type-safe operation avenues, CPython immediately raises a `TypeError: '>' not supported between instances of 'str' and 'int'`.

**The Resolution (`int(age)`):** By wrapping the identifier inside the `int()` constructor, you explicitly command CPython to parse the Unicode array buffer of `"18"`, verify its digits, and instantiate a fresh `PyLongObject` housing the numeric value `18` on the heap. When `COMPARE_OP` executes now, both pointers point to integer type descriptors. The runtime routes the evaluation directly to `long_compare`, which successfully assesses the underlying numeric payload bits ($18 > 10$), pushes `PyBool_True` to the evaluation stack, and safely enters the indented execution block.

