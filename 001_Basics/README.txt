1) Python Interpreter (Interactive)
    Python programs are executed by an interpreter. -> Interpreter starts by: by typing python in a command shell such as bash in cmd /Powershell. 
    -> quit() / Ctrl + Z to exit the interprater
    ->Python’s interactive mode is one of its most useful features because you can type any
      valid statement and immediately see the result.
    -> Can be used as calculator too and "_" holds the last value calculated. This "_" var can only be used in the interactive interpreter (not in program).

    >>> 6000 + 4523.50 + 134.25
    10657.75
    >>> _ + 8192.75
    18850.5
    >>>

2) Running a Python Source file: xyz.py
    -> #! : It is common to use #! to specify the interpreter on the first line of a program, like this:

    #!/usr/bin/env python3
    print('Hello World')

    -> On Windows, you can double-click on a .py file or type the name of the program into
    the Run command on the Windows Start menu to launch it. The #! line, if given, is used
    to pick the interpreter version (Python 2 versus 3). Execution of a program might take
    place in a console window that disappears immediately after the program completes—
    often before you can read its output. 

    -> Recommended: Use IDE for running a python script.

3) Primitives, Variables, and Expression
    3.1) Primitives
    Python provides a collection of primitive types such as integers, floats, and strings:

    42              # int
    4.2             # float
    'forty-two'     # str
    True            # bool

    3.2) Variables
    variable is a name that refers to a value. A value represents an object of some type:
    x = 42
    Sometimes you might see a type explicitly attached to a name. For example:
    x: int = 42 -> Not necessary to use, this just improves the code readability

    3.3) Expression
    An expression is a combination of primitives, names, and operators that produces a
    value:
    2 + 3 * 4 # -> 14

4) Arthematic Operations
Operation                               Description
x + y                                   Addition
x - y                                   Subtraction
x * y                                   Multiplication
x / y                                   Division
x // y                                  Truncating division
x ** y                                  Power (x to the y power)
x % y                                   Modulo (x mod y). Remainder.
–x                                      Unary minus
+x                                      Unary plus

The modulo operator returns the remainder of the division x // y. For
example, 7 % 4 is 3. For floating-point numbers, the modulo operator returns the
floating-point remainder of x // y, which is x – (x // y) * y.

    4.1) Some Common Inbuile mathematical functions
    Function                Description
    abs(x)                  Absolute value
    divmod(x,y)             Returns (x // y, x % y)
    pow(x,y [,modulo])      Returns (x ** y) % modulo
    round(x,[n])            Rounds to the nearest multiple of 10 to the nth power.
    -> [round(x, n) → round to n decimal places (you can think of it as rounding to nearest multiple of 10⁻ⁿ).]

eg:

    divmod(7, 3)   # (2, 1)  because 7 // 3 = 2 and 7 % 3 = 1
    divmod(20, 6)  # (3, 2)  because 20 // 6 = 3 and 20 % 6 = 2

    pow(2, 3)    # 8   (same as 2 ** 3)
    pow(2, 5, 5)   # (2 ** 5) % 5 = 32 % 5 = 2
    pow(3, 4, 5)   # (3 ** 4) % 5 = 81 % 5 = 1

    round(3.2)   # 3
    round(3.6)   # 4
    round(3.14159, 2)   # 3.14   (nearest 0.01)
    round(1234, -1)     # 1230   (nearest 10)
    round(1234, -2)     # 1200   (nearest 100)

    4.2) Bit Manipulation Operators

    Operation               Description
    x << y                  Left shift
    x >> y                  Right shift
    x & y                   Bitwise and
    x | y                   Bitwise or
    x ^ y                   Bitwise xor (exclusive or)
    ~x                      Bitwise negation

    eg:

x = 0b0001      # 1
x << 1          # 0b0010  -> 2
x << 2          # 0b0100  -> 4

x = 0b1100      # 12
x >> 1          # 0b0110  -> 6
x >> 2          # 0b0011  -> 3


a = 0b1101      # 13
b = 0b1011      # 11
a & b           # 0b1001  -> 9

x = 0b11001001
mask = 0b00001111
x & mask        # 0b00001001  -> lower 4 bits of x

a = 0b1100      # 12
b = 0b1010      # 10
a | b           # 0b1110  -> 14

Bitwise XOR x ^ y

Result bit is 1 if bits are different.

a = 0b1100      # 12
b = 0b1010      # 10
a ^ b           # 0b0110  -> 6




