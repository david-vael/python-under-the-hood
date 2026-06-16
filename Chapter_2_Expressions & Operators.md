© 2026 David Vael | Licensed under CC-BY 4.0
## Expressions in Python
An __expression__ is a combination of values, variables, operators, and function calls that Python evaluates to produce a result.

In simple terms, **an expression is anything that returns a value when executed**. When you write an expression in Python, the interpreter processes it and reduces it down to a single value.

**Examples of Expressions**

```Python
5 + 3          # Evaluates to 8
10 * 2         # Evaluates to 20
x + 5          # Evaluates to a value depending on the current state of x
len("hello")   # Evaluates to 5
3 < 5          # Evaluates to True
```

### Key Points:

**Always yields a value**: Every valid expression evaluates to a specific result or data object.

**Versatile components**: They can seamlessly mix raw numbers, namespace variables, symbols, and function return values.

**Varying complexity**: Expressions can range from simple, single-step operations `(2 + 3)` to highly complex, nested computations (`(a + b) * c / (d - 2)`).

**Flexible execution**: You can plug expressions into any slot where Python expects a value, including variable assignments, function arguments, or conditional statements.

## Types of Expressions
**Arithmetic Expressions**
Arithmetic expressions use mathematical operators to perform calculations on numeric data types (`int` and `float`).

```python
5 + 2    # Addition: 7
10 - 3   # Subtraction: 7
4 * 6    # Multiplication: 24
15 / 3   # Division: 5.0 (Always returns a float)
17 // 5  # Floor division: 3 (Rounds down to the nearest integer)
17 % 5   # Modulus: 2 (Returns the remainder of the division)
2 ** 3   # Exponentiation: 8 (2 raised to the power of 3)
```

### 🧠 What's happening behind the scenes:
When CPython evaluates arithmetic expressions, it manages memory allocation, operator selection, and optimization using specific internal engine rules:

- **Binary Operator Dispatch**: Every time you use an arithmetic symbol like `+` or `%`, CPython does not interpret the symbol directly at runtime. Instead, the virtual machine checks the type descriptor slot of the left-hand operand object (e.g., `PyLong_Type` for integers) and dispatches the calculation directly to its corresponding native C functions, such as `long_add`, `long_sub`, or `long_mod`.

- **Fixed Allocation vs. Integer Caching**: Because numeric types in Python are strictly **immutable** objects, any arithmetic operation must conceptually generate a brand-new numeric object on the heap to store the resulting payload. However, to eliminate massive performance overhead, CPython optimizes memory usage:

 -If your expression evaluates to a small integer between `-5` and `256`, CPython bypasses raw heap allocation entirely and instantly returns a pointer to a pre-allocated integer from its global **Small Integer Cache**.

 -If the result falls outside this range (e.g., `4 * 6 = 24` hits the cache, whereas `300 + 200 = 500` misses it), CPython dynamically allocates a completely new block of heap memory to instantiate a new `PyLongObject`.

-**Truncation Mechanics in Floor Division (`//`)**: Unlike true division (`/`), which invokes `long_true_divide` and automatically promotes the output to a `PyFloatObject`, floor division (`//`) invokes `long_floor_divide`. At the C layer, this performs truncating division that floors the mathematical quotient toward negative infinity. If both operands are integers, the returned chunk remains a pure `PyLongObject`, avoiding floating-point execution and precision overhead entirely. 
