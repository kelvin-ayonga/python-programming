# Understanding data types and how to manipulate strings
- primitive datatypes
    - Strings
    - Integers
    - Booleans
    - Floats
- Type Errors, checking and convertion.
    - type checking using the type function
        - type("string") <class str>
        - type(True) <class bool>
        - type(1234) <class int>
        - type(12.45) <class float>
    - type convertion
        - int("123") - to - 12
        - str(12) - to - "12"


### Mathematical operations.
**PEDMAS** order of execution of a mathematical expression# 
- () parenthesis
- ** Exponent
- `* OR / Multiplication or division both are of equal importance execution is from left to right
- `+ OR - Adding or subtraction

NB: execution is from right to left.

### Assignement operations
Example 

Instead of `score = score + 1` this can be simplified
- score += 1
- score *= 1
- score /= 1
- score -= 1

introduction for `f-string` for string interpolation instead of the headache of type conversion and concatination of strings
meaning **interpolation** - the insertion of something of a different nature into something else.

Example: 
``` python
 age = 12
 is_valid = True
 print(f"Some string with number {age}, then a boolean {is_valid}")
```