# PEP 8

For better viewing of the PEP 8 standards recommended to maintain, this .md file is to enable better viewing of the standards as it won't be necessary to keep a window open to view the standards.

The more commonly used practises are compiled[^1] in this .md file. The full PEP 8 standards can be viewed [here](https://peps.python.org/pep-0008/).


## Consistency
Ensure that the code is consistent, and that good readability is maintained throughout the code. However, in certain situations this is not necessarily applicable.

## Code Layout
### Indentation
Python is indent-sensitive. 
Continuation lines should be enclosed in parenthesis, or using hanging indents,
```py
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

```py
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

where indentation may not necessarily be four spaces. Note: **PYTHON DISALLOWS MIXING OF TAB AND SPACES INDENTS.**

### Line Breaking for Binary Operators
Breaking of lines when using a binary operator, it is more readable when breaking is done before an operator.
```py
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### Blank Lines
Top-level functions and class definitions are surrounded by **TWO** blank lines.
Functions defined in a class are surrounded by **ONE** blank line.

### Imports
- Imports should be done on separate lines, unless importing multiple functions from the same library.
```py
import os
import sys
from subprocess import Popen, PIPE
```
- Imports should be grouped, where each group are separated by one blank line, in this order:
    1. Standard library imports
    2. Related third party imports
    3. Local application / Library specific imports.
- Absolute imports are recommended.
```py
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

### Module Level Dunders
Dunders, ie. `__all__`, `__version`, etc. should be placed before imports and after docstrings. `from __future__` imports should be directly after docstrings, which means they must appear before any code.
```py
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## Whitespaces
Avoid redundant whitespaces. Examples:
- Start of parenthesis
```py
# Correct
spam(ham[1], {eggs: 2})

# Wrong
spam( ham[1], {eggs: 2})
```
- Trailing comma and closing parenthesis
```py
# Correct
foo = (0,)

# Wrong
foo = (0, )
```
- In a slice
```py
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```

```py
# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```
### Other recommendations
- **Avoid trailing whitespaces**
- Use a single whitespace on either side of a binary operator
- When indicating a keyword argument, do not use a whitespace around the `=` sign,
```py
# Correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong
def complex(real, imag = 0.0):
    return magic(r=real, i=imag)
```
unless combining an argument annotation with a default value.
```py
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```
- Avoid folding of lines unless for a very small body on the same line.

## Comments
`# Comments should start with a capital letter, and in a complete sentence like this.` In-line comments should be avoided as well unless really necessary.

## Docstrings
Docstrings should be added for every public modules, functions, and classes.
Comments are used for non-public methods, and should be after the `def` line.
- For multi-line docstrings, the `"""` that ends the docstring should be on a line by itself.
```py
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```
- For single-line docstrings, that `"""` should be kept on the same line as the docstring.
```py
"""Return an ex-parrot."""
```

## Naming Conventions
- `lowercase`
- `lower_case_with_underscores`
- `UPPERCASE` and `UPPER_CASE_WITH_UNDERSCORES` are used to name constants, and are usually defined on a module level.
- `CamelCase` (Acronyms should still be fully uppercased, ie. `HTTPServerError`.)
- `mixedCase`
- `_single_leading_underscore` is used to indicate internal use, ie. non-public methods and instance variables. `from M import *` will not import objects that start with an underscore.
- `single_trailing_underscore_` is used to avoid conflict with keywords.
- Class names should implement `CamelCase`.
- Exceptions that are actual errors should end in an "Error" suffix.
- Function and variable names should be lowercase, with each word separated by underscores. 
- `self` and `cls` should be used as the first argument for instance methods and class methods respectively.
- As there are controversies about the usage of double leading underscore names, their usage should be avoided. Only builtins should be used.
- Packages and modules should be named in all lowercase, and the usage of underscores is discouraged.

### Inheritance
A class's attributes should be decided beforehand whether to be public or non-public. If ever in doubt, it is recommended to make it non-public as it is easier to make it public rather than the other way round.

## Programming Recommendations
- Use `def` statements for binding a lambda experssion to an identifier rather than assignment statement.
- Derive exceptions from `Exception` rather than `BaseException`. 
- Specific exceptions should be mentioned whenever possible when catching an exception. `except Exception` can be used to catch all exceptions that signals program errors.
- Minimise `try` clauses to the absolute minimum amount of code necessary.
- All `return` statements in a function should either return an expression, or none of them should. In the case where some statements returns an expression and some don't, the ones that don't should be stated as `return None`.
- `"".startswith()` and `"".endswith()` can be used to see if a prefix or suffix exists in a string instead of slicing.
- Comparing of object types should be done using `isInstance()`.
- The fact that empty sequences (strings, lists, tuples) are false can be used. 
- Don't compare boolean values using `==`. It should be `if x:`.
- Use of `return`/`break`/`continue` in a `finally` clause where they might jump out of the clause is discouraged.

[^1]: PEP 8 standards retrieved from https://peps.python.org/pep-0008/.