channel : 15 minute coding
Day1 : Introduction and Installation
    Python is open-source, freeware, general purpose, functional, Object oriented Programming language.
==============================================================
Day 2: Identifiers

Identifiers: name given to variable, method, function 
Identifier is case Sensitive.
Naming convention:
1. Allowed character for identifier : a-z, A-Z, 0-9 and _
2. Identifier cannot start from number.
3. Identifier is case sensitive.
4. Keyword are reserved are not allowed.
5. Python is case sensitive.
--------------------------------------------
_a    = private variable
__a   = protected variable
__a__ = Magic variable || Dunder variable

```
import keyword 
print(keyword.kwlist)
```
print all keyword  use in python.

```
type() : print the data type of variable.
id()   : print the address of variable.
```
-----------------
DATA TYPES:
Python contain 14 data types.
fundamental related data type
1. int 
2. float
3. complex
4. Bool 
5. Str 
----------------------
collection related data type
6. byte
7. Bytearray 
8. Range 
9. List
10. Tuple
11. Set
12. Frozenset
13. Dict
-None

14. None

Base Conversion Method:
Binary      : bin()
Octal       : oct()
Hexadecimal : Hex()
=====================================================
Session 3
complex number = (ai+bj)  form
 j^2 = -1
a = real part 
b = imaginary part
-----------------------
Boolean 

True& False 
True  : 1 
False : 0  

-----------------
String = array of character
"""" """"  = doc string ==> doc string are enclosed by triple single or double quotation

----------- --------
Type Casting = changeing the data type of one variable into another


------------------------------------------
immutable = we cannot change the data
Fundamental Data Type : int , float, complex, string, boolean ==> fundamental data are immutable, if andy changes happen a new object is created
===========================================================
Session 4: 
Fundamental data type f vs Immutablility

immutable = if the value of varaibel is changed then the object is also changed , that"s why fundamental data tyoe are immutable 

mutable = if the  value of varaibale is changed , then the oobejct is not changed,(e,g List)
 
-------------------------------------------------
Collection Releated Data Type = These Data type can hold more than one value 

1.List :
    In list insertion order are preserved and duplicate value are also allowed. list are enclosed by Big Bracket. []. Heteregenous data are allowed
syntax 
    list_name = [value1, 1, value2]
eg. 
city = ["ktm", "pkr", "htd", "chitwan"]
-----------------------------------------
Tuple : Same as the list  but immutable and vlaue cannot changed. enclosed by small bracket ()

e.g, t1=(10,20,30,40,5)  ==> tuple
 t2 = (3) ==> integer
 t2 = (3,) ==> tuple 

------------------------------------------------------
Set  : 
Duplicate value are not allowed.
Heterogenous object are allowed and ther are mutable. 
Insertion order are not preserved.
We can add and remove the value of set. 
There is no any indexing concept in the set.
Indexing and Slicing are not allowed.
    empty set : s=set()
n = {1,2,3,4}

----------------------------------------------------------
FrozenSet : 
set but immutable (we cannot add an element)
syntax : 
fn = {1,2,3,4} ==> frozen set of n 
-----------------------------------------------------------
Dictionary : 
key value pair.

e.g 
    s = {
        1 : "Ram",
        2 : "Hari",
        3 : "Nepal" 
    }
-----------------------------------------------------------
Range :
    Range data type contain sequence of number. 
    they are immutable. there are multiple forms of range data type 
1. range(10) ==> 0-9 
2. range(10,21) ==> 10-20
3. range(10,21,2) (with interval of 2) ==> 10,12,14,16,18,20 
-----------------------------------------------------------
Bytes: 
    collecion of bytes.
    bytes are immutabel 


e,g 
s = [1,2,3,4]
si = bytes(s)
print(s i)
-----------------------------------------------------------
Bytes Array :
    Exactly same as bytes but it is mutable .
    Mutable bytes
e,g 
b = [1,2,3,4]
by = bytearray(b)
print(by)
-----------------------------------------------------------
Non-Datatype :
 None

def f() :
    a = 10 
// a function should return someting 
f() ==> None

=========================================================
session 5 :
Escape sequence 

\n => new line 
\t => tab 
\r => carriage return 
\b => backspace
\v => verticaltab 
\" => double quotation
\' => single quotation
\\ => slash
----------------------
constant :
     There is not any provision of constant.
     but in python we denote constant by  CAPITAL LETTERS.
------------------------
operator :

1. Arithmetic operator 
2. Relational Operator / comparison operator = 
3. Logical Operator 
4. Bitwise Operator
5. Assignment operator 
6. Equality Operator 
7. shift Operator 
8. Ternary Operator 
9. Special Operator 
    a. identity Operator
    b. Membership Operator 

1. Arithmetic Operator 
    +,-,*,%,/
    // = Floor Division operator 
    ** = power operator 




==========================================================
Core Python in Nepali | Session 6 
TERNARY OPERATOR:
syntax:
    x = <first_value> if <condition> else <second value> 


Nesting of Ternary operator :

min = a if a < b and a < c else b if b > c else c 
-------------
Identity operator :
   1. is == >  return true if the  the address of variable is data type
   2. is not  ==> return False if the  the address of variable is data type

Membership operator :
     to check the value is included or not in the collection related data type.
    1. in  = 
    2. not in
---------------------
Operator precedence :
priority of operator  
1. ()
2. ** exponential
3. ~
4. *, /,% ,//
5. Bitwise
6. comparison operator 
7. Assignment operator 
8. identity and membership operator 
9. logical operator 

-------------
math module

module : collection of function, variables, class .
===========================================================
Core Python in Nepali | Session 7

python input / output :

input() ==> input function are used to take input

split()

List comprehensive .
List Unpacking.


Eval(Evaluate) Function :
 automatically type caste the value.
 