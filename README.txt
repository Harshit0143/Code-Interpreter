
## To exit if error is found ## Link to this was given by mam on Piazza in assignment 5A
### to add or and in while???
## Errors:
### if " : " is missing at end of while statement
### or if " : " is not separated by space from expression.
#   eg. while z > 9:  --is invalid
#       while z > 9 : --is valid

### if expression inside while contains non-boolean expression or non binary expresssion
#   eg. while a + b > 9 is not allowed or while True is not allowed
#   only a ~ b is allowed where ~ is in [> , < , <= , >= ,==, !=,and, or]
# returns "Unexpected Operator!!" if while statement uses operator other than these

### "Unexpected Operator!!" --
# if unary expression is other than [ '-', 'not']
# if binary expression is other than [> , < , <= , >= ,==, !=, and , or , +, - , * , / , //]
#  NOTE '/' and '//' are both treated as // (integer division)

### Variable "x" not defined type error if a variable is mentioned before declaring it's value
### Any syntax error like whle insted of while
### '=' instead of '==' in while condition
### the code will not provide final result if stuck in a while loop that doesn't terminate

### There should not be empty lines in input_file else it will not function correctly





#### Case for jump of more than one tab simultaneously
# x = 1                                   0  x = 1
# z = -4                                  1  z = -4
# while x < 10 :                          2  BLE 10, x , 8
#     x = x + 2                           3  x = x + 2
#     while z < x :                       4  BLE x, z  , 7
#         z = z + 1                       5  z = z + 1
# c = 1 ### change of two tab             6  branch 4
#                                         7  branch 2
#                                         8  c = 1

# RESULT
# Instruction List:
# 0 x = 1
# 1 z = -4
# 2 BLE 10, x, 8
# 3 x = x + 2
# 4 BLE x, z, 7
# 5 z = z + 1
# 6 branch 4
# 7 branch 2
# 8 c = 1

#  <I haven't copied intermediate values here as there were many> <Other Examples are at last>

# After complete execution:
# Garbage values are:  [-4, 10, 2, 3, -3, -2, -1, 0, 5, 4, 7, 6, 9, 8]
# Variable values are:
# x  =  11
# z  =  11
# c  =  1
# ___________________________


## So this case and any case with any number of nesting can be handled


#### Case when there is no statement after end of while loop
# x = 1                                  0 x = 1
# while x < 10 :                         1 BLE 10, x , 4 ==> executuion stops if
#     x = x + 2                          2 x = x + 2      referred index exceeds length of instruction list
#                                        3 branch 1
###RESULT
# Instruction List:
# 0 x = 1
# 1 BLE 10, x, 4
# 2 x = x + 2
# 3 branch 1
# _________________________________________
# Garbage values are:  [1, 10, 2]
# Variable values are:
# x  =  3
# ________________________________________
# _________________________________________
# Garbage values are:  [1, 10, 2, 3]
# Variable values are:
# x  =  5
# ________________________________________
# _________________________________________
# Garbage values are:  [1, 10, 2, 3, 5]
# Variable values are:
# x  =  7
# ________________________________________
# _________________________________________
# Garbage values are:  [1, 10, 2, 3, 5, 7]
# Variable values are:
# x  =  9
# ________________________________________
# _________________________________________
# Garbage values are:  [1, 10, 2, 3, 5, 7, 9]
# Variable values are:
# x  =  11
# ________________________________________

# After complete execution:
# Garbage values are:  [1, 10, 2, 3, 5, 7, 9]
# Variable values are:
# x  =  11





## for such a case we have implemented check that last element of tab_list = 0




## now we assign the operand3 to 'loop' type instruction
tot = len(instruction_list)
for i in range (0,tot):
    instruction_list[i].assign_target_to_loop()  ## O(1 ) in time -- found before-- for 1 value of i
## overall O(len(instruction_list())) in time

print()
print('Instruction List:')
for k in range (0,len(instruction_list)):
    print(k , instruction_list[k]) ## str(instruction_list[k]) is O(1)
## overall O(len(instruction_list())) in time


i = 0

while i < tot :
    i = instruction_list[i].execute() # this returns the index of next statement to go to
    # this continues, loop stops when last statement is executed

### Time complexity of this is not determinable-- it's case dependent
### i is not continuously increasing -- it can jump back when an unconditional branch is encountered
### or i jumps forward if a False while condtion is encountered
### simple example -- if there are no while loops -- i moves straight forward and time complexity ==
### O(length of instruction list) and in that case creating of instruction list will also need O(n)
### time and not O(n^2) (as found in above lines assuming worst case)
#  as there will not be any tab changes then. n -- num of lines in input_file

### Another extreme case is when there is a while loop that doesn't terminate --
# i = 4
# while i < 5 :
#   i = i - 1
# c = 10
# In this case time is infiite as termination never ends





## Test Cases
## EXAMPLE 1
# a = 10
# b = 1
# while a > b :
#     a = a - 1
# c = 1
# RESULT

# Instruction List:
# 0 a = 10
# 1 b = 1
# 2 BLE a, b, 5
# 3 a = a - 1
# 4 branch 2
# 5 c = 1
# _________________________________________
# Garbage values are:  [10]
# Variable values are:
# a  =  9
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9]
# Variable values are:
# a  =  8
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8]
# Variable values are:
# a  =  7
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8, 7]
# Variable values are:
# a  =  6
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8, 7, 6]
# Variable values are:
# a  =  5
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8, 7, 6, 5]
# Variable values are:
# a  =  4
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8, 7, 6, 5, 4]
# Variable values are:
# a  =  3
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3]
# Variable values are:
# a  =  2
# b  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3, 2]
# Variable values are:
# a  =  1
# b  =  1
# ________________________________________

# After complete execution:
# Garbage values are:  [10, 9, 8, 7, 6, 5, 4, 3, 2]
# Variable values are:
# a  =  1
# b  =  1
# c  =  1








# Example2
# i = 0
# while i < 3 :
#     j = 1
#     while j < 2 :
#         x = i + j
#         j = j + 1
#     i = i + 1
# y = 0



#RESULT
# Instruction List:
# 0 i = 0
# 1 BLE 3, i, 9
# 2 j = 1
# 3 BLE 2, j, 7
# 4 x = i + j
# 5 j = j + 1
# 6 branch 3
# 7 i = i + 1
# 8 branch 1
# 9 y = 0
# _________________________________________
# Garbage values are:  [3]
# Variable values are:
# i  =  0
# j  =  2
# x  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [0, 3]
# Variable values are:
# i  =  1
# j  =  2
# x  =  1
# ________________________________________
# _________________________________________
# Garbage values are:  [0, 3]
# Variable values are:
# i  =  1
# j  =  2
# x  =  2
# ________________________________________
# _________________________________________
# Garbage values are:  [0, 3, 1]
# Variable values are:
# i  =  2
# j  =  2
# x  =  2
# ________________________________________
# _________________________________________
# Garbage values are:  [0, 1]
# Variable values are:
# i  =  2
# j  =  2
# x  =  3
# ________________________________________
# _________________________________________
# Garbage values are:  [0, 1]
# Variable values are:
# i  =  3
# j  =  2
# x  =  3
# ________________________________________

# After complete execution:
# Garbage values are:  [1]
# Variable values are:
# i  =  3
# j  =  2
# x  =  3
# y  =  0












