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
a = 10</br>
b = 1</br>
while a > b :</br>
    a = a - 1</br>
c = 1</br>


RESULT</br>

Instruction List:</br>
0 a = 10</br>
1 b = 1</br>
2 BLE a, b, 5</br>
3 a = a - 1</br>
4 branch 2</br>
5 c = 1</br>
_________________________________________
Garbage values are:  [10]</br>
Variable values are:</br>
a  =  9</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9]</br>
Variable values are:</br>
a  =  8</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8]</br>
Variable values are:</br>
a  =  7</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7]</br>
Variable values are:</br>
a  =  6</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6]</br>
Variable values are:</br>
a  =  5</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5]</br>
Variable values are:</br>
a  =  4</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5, 4]</br>
Variable values are:</br>
a  =  3</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3]</br>
Variable values are:</br>
a  =  2</br>
b  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3, 2]</br>
Variable values are:</br>
a  =  1</br>
b  =  1</br>
________________________________________

After complete execution:</br>
Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3, 2]</br>
Variable values are:</br>
a  =  1</br>
b  =  1</br>
c  =  1</br>








# Example2
i = 0 </br>
while i < 3 :</br>
    j = 1</br>
    while j < 2 :</br>
        x = i + j</br>
        j = j + 1</br>
    i = i + 1</br>
y = 0</br></br>



RESULT</br>
Instruction List:</br>
0 i = 0</br>
1 BLE 3, i, 9</br>
2 j = 1</br>
3 BLE 2, j, 7</br>
4 x = i + j</br>
5 j = j + 1</br>
6 branch 3</br>
7 i = i + 1</br>
8 branch 1</br>
9 y = 0</br>
_________________________________________
Garbage values are:  [3]</br>
Variable values are:</br>
i  =  0</br>
j  =  2</br>
x  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [0, 3]</br>
Variable values are:</br>
i  =  1</br>
j  =  2</br>
x  =  1</br>
________________________________________
_________________________________________
Garbage values are:  [0, 3]</br>
Variable values are:</br>
i  =  1</br>
j  =  2</br>
x  =  2</br>
________________________________________
_________________________________________
Garbage values are:  [0, 3, 1]</br>
Variable values are:</br>
i  =  2</br>
j  =  2</br>
x  =  2</br>
________________________________________
_________________________________________
Garbage values are:  [0, 1]</br>
Variable values are:</br>
i  =  2</br>
j  =  2</br>
x  =  3</br>
________________________________________
_________________________________________
Garbage values are:  [0, 1]</br>
Variable values are:</br>
i  =  3</br>
j  =  2</br>
x  =  3</br>
________________________________________

After complete execution:</br>
Garbage values are:  [1]</br>
Variable values are:</br>
i  =  3</br>
j  =  2</br>
x  =  3</br>
y  =  0</br>



