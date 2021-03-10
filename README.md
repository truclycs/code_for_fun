PEP 8 -- Style Guide for Python Code 


###Introduction

###A Foolish Consistency is the Hobgoblin of Little Minds

###Code Lay-out

####Indentation
Use 4 spaces per indentation level.

    \#Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

    \# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
    def long_function_name(
                var_one, var_two, var_three,
                var_four):
            print(var_one)

    \# Hanging indents should add a level.
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)


The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list, as in:

    my_list = [
        1, 2, 3,
        4, 5, 6,
        ]

    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
        )

####Tabs or Spaces?
Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is already indented with tabs.

Python 3 disallows mixing the use of tabs and spaces for indentation.

####Maximum Line Length
Limit all lines to a maximum of 79 characters.

    with open('/path/to/some/file/you/want/to/read') as file_1, \
         open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())

####Should a Line Break Before or After a Binary Operator?
    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest)

####Blank Lines

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.
    
####Source File Encoding
Code in the core Python distribution should always use UTF-8 (or ASCII in Python 2).

Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration.

####Imports
    import os
    import sys
    from subprocess import Popen, PIPE
    
####Module Level Dunder Names
Module level "dunders" (i.e. names with two leading and two trailing underscores) such as \__all__, \__author__, \__version__, etc. should be placed after the module docstring but before any import statements except from \__future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings:

    """This is the example module.

    This module does stuff.
    """

    from __future__ import barry_as_FLUFL

    __all__ = ['a', 'b', 'c']
    __version__ = '0.1'
    __author__ = 'Cardinal Biggles'

    import os
    import sys

###String Quotes
In Python, single-quoted strings and double-quoted strings are the same.

###Whitespace in Expressions and Statements

####Pet Peeves
Immediately inside parentheses, brackets or braces:

    spam(ham[1], {eggs: 2})

Between a trailing comma and a following close parenthesis:

    foo = (0,)

Immediately before a comma, semicolon, or colon:

    if x == 4: print x, y; x, y = y, x

However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted:

    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ham[lower + offset : upper + offset]


####Other Recommendations

    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)

    def munge(input: AnyStr): ...
    def munge() -> PosInt: ...

    def complex(real, imag=0.0):
        return magic(r=real, i=imag)

    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()
###When to Use Trailing Commas

    FILES = ('setup.cfg',)

    FILES = [
        'setup.cfg',
        'tox.ini',
        ]
    initialize(FILES,
            error=True,
            )

###Comments
    
- Block Comments
    
- Inline Comments

- Documentation Strings

###Naming Conventions
    
####Overriding Principle
####Descriptive: Naming Styles
####Prescriptive: Naming Conventions
- Names to Avoid: l, I, O
- ASCII Compatibility
- Package and Module Names
- Class Names
- Type Variable Names
- Exception Names
- Global Variable Names
- Function and Variable Names
- Function and Method Arguments
- Method Names and Instance Variables
- Constants
- Designing for Inheritance
####Public and Internal Interfaces

###Programming Recommendations

###Function Annotations

###Variable Annotations
    code: int

    class Point:
        coords: Tuple[int, int]
        label: str = '<unknown>'
