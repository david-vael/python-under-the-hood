print("=" * 50)
print("🧪 PYTHON TYPE CONVERSION LAB")
print("=" * 50)

value = input("Enter any value: ")

print("\nOriginal Information")
print(f"Value : {value}")
print(f"Type  : {type(value).__name__}")

print("\nConversion Results")
print("-" * 50)

# Integer Conversion
try:
    integer_value = int(value)
    print(f"int()   -> {integer_value} ({type(integer_value).__name__})")
except ValueError:
    print("int()   -> Conversion Failed")

# Float Conversion
try:
    float_value = float(value)
    print(f"float() -> {float_value} ({type(float_value).__name__})")
except ValueError:
    print("float() -> Conversion Failed")

# Boolean Conversion
try:
    bool_value = bool(value)
    print(f"bool()  -> {bool_value} ({type(bool_value).__name__})")
except ValueError:
    print("bool()  -> Conversion Failed")

# String Conversion
string_value = str(value)
print(f"str()   -> {string_value} ({type(string_value).__name__})")

print("\n💡 Under The Hood")
print("input() always returns a string.")
print("Type conversion functions create new objects of different types.")
