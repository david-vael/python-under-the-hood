# 🧪 Type Conversion Lab

A beginner friendly Python project from **Python Under the Hood**.

This project demonstrates how Python handles type conversion using built in functions such as:

* `int()`
* `float()`
* `str()`
* `bool()`

It helps learners understand one of the most important concepts in Python: **data types and explicit type casting**.

## Concepts Covered

* Variables
* Data Types
* User Input (`input()`)
* Type Conversion
* Error Handling (`try` / `except`)
* Strong Typing

## How It Works

The program accepts a value from the user and attempts to convert it into different Python data types.

Example input:

```text
25
```

Example output:

```text
int()   -> 25 (int)
float() -> 25.0 (float)
bool()  -> True (bool)
str()   -> 25 (str)
```

## Run the Project

```bash
python type_conversion_lab.py
```

## Learning Objective

By completing this project, students will learn that:

* `input()` always returns a string.
* Different data types require explicit conversion.
* Invalid conversions raise exceptions.
* Python is a strongly typed language.

## Under The Hood

When a conversion function such as `int()` or `float()` is called, Python creates a new object of the target type rather than changing the original object.

Example:

```python
value = "25"
number = int(value)
```

The string `"25"` remains unchanged, while `number` becomes a new integer object.

## Part of Python Under the Hood

This project accompanies **Chapter 1: Variables & Data Types** and provides hands on practice with the concepts introduced in the chapter.

---

Created for the Python Under the Hood handbook.
