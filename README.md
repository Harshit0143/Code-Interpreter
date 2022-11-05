# Code-Interpreter
An interpreter for restricted syntax to understand working of the Python Interpreter


# For the allowed Syntax see the Problem.pdf

**** Variable names should be alpha strings only

**** if " : " is missing at end of while statement
or if " : " is not separated by space from expression.
    eg. while z > 9:  --is invalid
        while z > 9 : --is valid
        

**** Unexpected statement type!!
Only unary and binary expressions are alloweD on on the RHS in assignment

**** if expression inside while contains non-boolean expression or non binary expresssion
    eg. while a + b > 9 is not allowed or while True is not allowed
only a ~ b is allowed where ~ is in [> , < , <= , >= ,==, !=,and, or]
returns "Unexpected Operator!!" if while statement uses operator other than these

**** "Unexpected Operator!!" --
if unary expression is other than [ '-', 'not']
if binary expression is other than [> , < , <= , >= ,==, !=, and , or , +, - , * , / , //]
if any other type of expression
NOTE '/' and '//' are both treated as // (integer division)

**** Variable "x" not defined type error if a variable is mentioned before declaring it's value
Any syntax error like whle insted of while
'=' instead of '==' in while condition
the code will not provide final result if stuck in a while loop that doesn't terminate

**** There should not be empty lines in input_file else it will not function correctly




SAMPLE TESTCASES AND EXPLANATION :
# Test Cases
# EXAMPLE 1
a = 10
b = 1
while a > b :
    a = a - 1
c = 1


RESULT

Instruction List:
0 a = 10
1 b = 1
2 BLE a, b, 5
3 a = a - 1
4 branch 2
5 c = 1
_________________________________________
Garbage values are:  [10]
Variable values are:
a  =  9
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9]
Variable values are:
a  =  8
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8]
Variable values are:
a  =  7
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7]
Variable values are:
a  =  6
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6]
Variable values are:
a  =  5
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5]
Variable values are:
a  =  4
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5, 4]
Variable values are:
a  =  3
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3]
Variable values are:
a  =  2
b  =  1
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3, 2]
Variable values are:
a  =  1
b  =  1
________________________________________

After complete execution:
Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3, 2]
Variable values are:
a  =  1
b  =  1
c  =  1








# Example2
i = 0 </br>
while i < 3 :
    j = 1
    while j < 2 :
        x = i + j
        j = j + 1
    i = i + 1
y = 0



RESULT
Instruction List:
0 i = 0
1 BLE 3, i, 9
2 j = 1
3 BLE 2, j, 7
4 x = i + j
5 j = j + 1
6 branch 3
7 i = i + 1
8 branch 1
9 y = 0
_________________________________________
Garbage values are:  [3]
Variable values are:
i  =  0
j  =  2
x  =  1
________________________________________
_________________________________________
Garbage values are:  [0, 3]
Variable values are:
i  =  1
j  =  2
x  =  1
________________________________________
_________________________________________
Garbage values are:  [0, 3]
Variable values are:
i  =  1
j  =  2
x  =  2
________________________________________
_________________________________________
Garbage values are:  [0, 3, 1]
Variable values are:
i  =  2
j  =  2
x  =  2
________________________________________
_________________________________________
Garbage values are:  [0, 1]
Variable values are:
i  =  2
j  =  2
x  =  3
________________________________________
_________________________________________
Garbage values are:  [0, 1]
Variable values are:
i  =  3
j  =  2
x  =  3
________________________________________

After complete execution:
Garbage values are:  [1]
Variable values are:
i  =  3
j  =  2
x  =  3
y  =  0



