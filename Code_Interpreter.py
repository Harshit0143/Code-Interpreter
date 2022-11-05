import sys

### if " : " is missing at end of while statement
### or if " : " is not separated by space from expression.
#   eg. while z > 9:  --is invalid
#       while z > 9 : --is valid
# Unexpected statement type!!
# Only unary and binary expressions are allowen on on the RHS in assignment

### if expression inside while contains non-boolean expression or non binary expresssion
#   eg. while a + b > 9 is not allowed or while True is not allowed
#   only a ~ b is allowed where ~ is in [> , < , <= , >= ,==, !=,and, or]
# returns "Unexpected Operator!!" if while statement uses operator other than these

### "Unexpected Operator!!" --
# if unary expression is other than [ '-', 'not']
# if binary expression is other than [> , < , <= , >= ,==, !=, and , or , +, - , * , / , //]
# if any other type of expression
#  NOTE '/' and '//' are both treated as // (integer division)

### Variable "x" not defined type error if a variable is mentioned before declaring it's value
### Any syntax error like whle insted of while
### '=' instead of '==' in while condition
### the code will not provide final result if stuck in a while loop that doesn't terminate

### There should not be empty lines in input_file else it will not function correctly

DATA = []  ## DATA list-- Global Variable
# DATA entries are
# tuple eg. ('x',i) 0<= i < len(DATA)
# integers
# bool

instruction_list = [] ## Instruction list-- Global Variable
# instruction_list entries are:
# objects of class Instructions


def categorize_obj(token_list):
    # token_list -- list  type(token_list[i]) == str
    # token list is one complete statement in the input file as list of tokens
    # assigns these parametersto statwement:
    # (type, further, operator, operand1, operand2, operand3)
    # this output is used to __init__ object later
    # type - 'loop'  /  'var=exp' / 'branch'
    # further - it represents 'subtypes' of each 'type'


    if token_list[0] == 'while':  ### Conditional Branch
        ### Detecting Syntax Error
        if token_list[-1] != ':':
            print('Expected " : " after end of while statement!!')
            print('Or " : " should be separted by space from the expressoin!!')
            print("Ensure all operators and operands are separated by spaces ' '")
            sys.exit()

        operator = token_list[2]
        operand1 = token_list[1]
        operand2 = token_list[3]
        # type -- loop ;  further -- BLE/BLT/BE ;
        # operator, operand1, operand2 -- from expression inside while
        # operand3(Target) carries index of instruction to jump to if while condtion if False

        # Target can't be specified (will be stored in operand3 later)
        # as complete program has not been read yet

        ## NOTE The operaor is not used further. Only category BLE, BE, BLT is used
        if operator == '>':
            return('loop', 'BLE','>',operand1,operand2,None)

        elif operator == '>=':
            return('loop', 'BLT','>=',operand1,operand2,None)
        elif operator == '<':
            return('loop', 'BLE','<',operand2,operand1,None)
        elif operator == '<=':
            return('loop', 'BLT','<=',operand2,operand1,None)

        ## NOTE - I have places != , = , and , or all in BE category, but their execution is done correctly
        elif operator == '==':
            return('loop', 'BE','==',operand1,operand2,None)

        elif operator == '!=':
            return('loop', 'BE','!=',operand1,operand2,None)
        elif operator == 'and':
            return('loop', 'BE','and',operand1,operand2,None)
        elif operator == 'or':
            return('loop', 'BE','or',operand1,operand2,None)
        else:
            print('Syntax Error!! Expected Boolean expression in "while".')
            sys.exit()



    elif token_list[0] == 'branch': # Unconditional Branch

        #(type,further,operator, operand1, operand2, operand3)

        # type == 'branch' , 'operand3' == Target -- index of while statement it is connected with
        # rest attributes not used
        return ('branch','always', None, None,None, token_list[1] )

    else:
    # (type,further,operator, operand1, operand2, operand3)
    # type--'var=exp' ; further--'binary' / 'unary'       / 'assignment'
    # ==>               x = v + 6         / x = not True  / x = 99
    # operand3 is LHS variable
    # if attribute is not applicable then None

        # "Detecting Error"
        if token_list[1]!= '=':
            print('Syntax Error: Expected "=" ')
            sys.exit()
        a =len(token_list)

        # No Error
        if a == 3:
            return ('var=exp','assignment', None ,token_list[2] , None ,token_list[0])
        elif a == 4:
            return ('var=exp','unary',token_list[2],token_list[3],None,token_list[0])
        elif a == 5:
            return ('var=exp','binary' ,token_list[3],token_list[2],token_list[4], token_list[0])

        else:
            print('Unexpected statement type!!')
            sys.exit()
# Time Complexitty == O(1) -- length of token list is at max 5
# and we just need to access each element of token_list

def str_to_bool(x):
    # x is str -- 'True' or 'False'
    # returns: bool -- True if x == 'True' , False if x == 'False'
    # for converting token(str) into bool

    if x == 'True':
        return True
    else: # so x == 'False'
        return False
## Time Complexity == O(1) -- Simple Comparision

def get_type(x):
    # x -- token -- string
    # returns --
    # 'bool' if token is one of the strings --  'True' or 'False'
    # 'number' if token is numeric  example '34'
    # None -- otherwise

    if x.isalpha():
        if x in ('True', 'False'):
            return 'bool'
    else:
        return 'number'

    ## Assuming x.isalpha() is O(1) ==> works if x is not a very large string
    ## Time complexity == O(1)
    ## taking the general case will make rest of the analysis complex



def get_value(x):
    # DATA -- DATA list
    # x -- string-- existing variable whose value to be found from DATA
    # returns: bool/ int -- value of x from  data list
    # returns: Error if 'x' does not exist in DATA

    n = len(DATA)
    for i in range (0,n):
        element = DATA[i]
        if type(element) == tuple:
            (a,b) = DATA[i]  # b is the address(index) of th evalue of x in list
            if a == x:
                return DATA[b] ### return value of variable i.e. DATA[b]

    ## If not returned yet ===> 'x' not in DATA ==> ERROR
    print( '"Variable ',x, ' is not defined."')
    sys.exit()

    # Time Complexity == O(len(DATA)) -- In worst case ('x', reference)
    # is the last element in DATA or not present so search through entire list


def search_or_create_it(e):
    # e-- bool/int
    # returns: int
    # if e is already present in DATA, returns its index
    # if e is not present, append it and return its index

    n = len(DATA)
    for i in range (0,n):
        if DATA[i] == e and (type(DATA[i]) == type(e)):
            return i

    # If not returned ==> 'e' is not in DATA
    DATA.append(e) # loof finished so e is not in DATA ==> add e to DATA
    return n # length of DATA increased by 1, n is index of e in the modified list

    # Time Complexity == O(len(DATA)) -- In worst case 'e' is not in list
    # Then we have to search through entire list and then append it


def modify_or_create_variable(x, new_address):
    # new_address: int-- value of index(refernece) to be assigned to x so 0<= c < len(DATA)
    # x: string -- name of variable
    # DATA -- DATA list
    # modifies address assigned to x to new_address if x is already in list
    # else creates new place for x
    # returns None

    n = len(DATA)
    for i in range (0,n):
        element = DATA[i]
        if type(element) == tuple:
            (a,b) = element
            if a == x : # if this is the required variable
                DATA[i] = (a,new_address)  # assign new address to x
                return None ## To exit immediately from here

    DATA.append((x,new_address)) # if x is not already present then add it to list

    ## Time Complexity == O(len(DATA)) -- In worst cast when variable 'x'
    # is not in DATA then search through entire list and then append ('x',new_address)


def actual_value(x):
    # x -- string / bool / int
    # if x is bool or int -- return x itself and add it to DATA if not already present
    # if x -- srting ==> x is variable return value of variable from DATA
    if type(x) == int or type(x) == bool:
        search_or_create_it(x)  ## This adds to DATA if not present already
        y = x

    else: # so it's a variable
        y = get_value(x) ## find value of 'x' from DATA
    return y
    # Time Complexity = O(len(DATA)) ==> time of search_or_create_it(x)== O(len(DATA))
                                     # or time of get_value(x) == O(len(DATA))

def get_garbage_values(L):
    # L  DATA list
    # retunrns -- tuple -- (a,b) -- a: list , b: list
    # a is list of garbage values
    # b is list of tuples of form ('vaiables', final value of variables)
    # final values of variables are int or bool
    n = len(L)
    l_variables = []
    l_is_used = [] # To keep track which element in DATA is referred to none of the variables
    for i in range (0,n):  ## O(len(DATA))
        l_is_used.append(False) # All False in start

    for i in range (0,n): ## Time Complexity == O(len(DATA)) -- analyse each element then append
        # to l_variables if req and change state of l_is_used[i] from False to True
        element = L[i]
        if type(element) == tuple:
            l_is_used[i] = True  # This tuple itself is not garbage
            (variable, address) = element
            l_variables.append((variable, L[address])) # store the actual value of variable
            l_is_used[address] = True # its not garbage so make it true


    # construction list of garbage elements
    l_garbage = []
    for i in range (0,n): ## Length OF l_garbage < length(DATA)
        if l_is_used[i] == False: # if garbage only then append
            l_garbage.append(L[i])

    return (l_garbage,l_variables)
    # Time Complexity == O(len(DATA))


class Instructions:
    def __init__(self, tabs , index , token_list):

        # Generated when input file is being read
        self.tokens = token_list ## token list from which we get its attributes
        self.tabs = tabs         ## tab level of each instruction
        self.index = index       ## index of each instruction in instruction_list

        ## output of categorize_obj ==> (type,further,operator, operand1, operand2, operand3)
        (a,b,c,d,e,f) = categorize_obj(token_list)  ## O(1) in time -- found earlier

        if type(d) == str: ## to avoid None  ## O(1) in time
            if get_type(d) == 'bool':
                d = str_to_bool(d) ## Store attrubute True/False as bool not string
            elif get_type(d)== 'number':
                d = int(d) ## Store attribute integer as int not string

        if type(e) == str: ## to avoid None  ## O(1) in time
            if get_type(e) == 'bool':
                e = str_to_bool(e)
            elif get_type(e) == 'number':
                e = int(e)

        # operand3 is
        # None for 'loop' (at this stage)
        # str - represents LHS variable for 'var=exp'
        # int - Target index for 'branch' i.e. Unconditional Branch
        #       it was added to token_list as integer only

        self.type = a      # str
        self.further = b   # str
        self.operator = c  # str
        self.operand1 = d  # int/ bool / None
        self.operand2 = e  # int/ bool / None
        self.operand3 = f  ## discussed above

    ## Overall O(1) in time

    def assign_target_to_loop(self):
        ## To assign Target/operand3 to while after conplete input_file is read

        if self.type == 'loop':
            (a,b) = self.tokens[-1] ## this is done while reading file -- referred later
            ## a == 'jump'
            self.operand3 = b  # to 'jump' to index 'b' instruction if loop condition is False
    ## Time complexity == O(1) ==> check type - O(1) then access last element of list --> O(1)
                            ##     then assign --> O(1)  overall
                            # ##Accessing any element of list is O(1) in time

    def give_result_exp(self): ## for evaluating 'var=exp' type
        f = self.operand1
        g = self.operand2
        # f , g -- None/ int / bool / str (i.e. variable)


        if self.further == 'assignment':
            z = actual_value(f) ## Find its value from DATA if it's a variable
                                ## actual_value() also UPDATES DATA as per its specification

        elif self.further == 'unary':
            x = actual_value(f)

            if self.operator == '-':
                z = (-1)*x
            elif self.operator == 'not':
                z = not x
            else:
                print('Unexpected Operator!!')
                sys.exit()

        else: ### further--'binary'
            # ['+','−', '∗', '/','>','<', '>=', '<=', '==', '!=', 'and' , 'or']

            x = actual_value(f) # O(len(DATA))
            y = actual_value(g) # O(len(DATA))

            # Evaluating
            op = self.operator
            if op == '+':
                z = x + y
            elif op == '-':
                z = x - y
            elif op == '*':
                z = x * y
            elif op == '/' or op == '//' :
                z = x // y
            elif self.operator == '>' :
                z = x > y
            elif self.operator == '<':
                z = x < y
            elif self.operator == '>=':
                z = x >= y
            elif self.operator == '<=':
                z = x <= y
            elif self.operator == '==':
                z = x == y and type(x) == type(y) ## to aviod 0 == False as bein reported True
            elif self.operator == '!=':
                z = x != y
            elif self.operator == 'and':
                z = x and y
            elif self.operator == 'or':
                z = x or y

            else:
                print('Unexpected Operator!!')
                sys.exit()

        address = search_or_create_it(z) # index of the answer from DATA (pre-existing or add it) # TIME O(len(DATA))
        modify_or_create_variable(self.operand3,address) # O(len(DATA)) TIME
        # operand3 is LHS Variable -- change it's reference/ or create it if not pre-existing


        ## Time Complexity -- O(len(DATA)) Accessign values/modifying DATA and simple arithmetic

        return (self.index)+1 ###==> NEXT STATEMENT TO EXECUTE AFTER THIS

    def give_result_branch(self):
        ### if self.type == 'branch' -- Unconditional Branch
        return self.operand3 ### RETURN REFERENCE TO INSTRUCTION WHERE WE TO GO NEXT
        ## O(1) -- accessing and attribute of an object is O(1)

    def give_result_while(self):
        f = self.operand1
        g = self.operand2

        x = actual_value(f)
        y = actual_value(g)
        if self.further == 'BLE':
            if x <= y :
                z = self.operand3
            else:
                z = (self.index)+1

        elif self.further == 'BLT':
            if x < y:
                z = self.operand3
            else:
                z = (self.index)+1
        else: ## BE
            if self.operator == '==':
                if x == y:
                    return (self.index) +1
                else:
                    return self.operand3
            elif self.operator == '!=':
                if x != y :
                    return (self.index)+1
                else:
                    return self.operand3
            elif self.operator == 'and':
                if x and y :
                    return (self.index)+1
                else:
                    return self.operand3
            elif self.operator == 'or':
                if x or y :
                    return (self.index)+1
                else:
                    return (self.operand3)
            else:
                print('Unexpected Operator!!')
                sys.exit()
        return z
        ## self.operand3 will have the Target stores, by the time this is called
        ## self.operand3 is Target statement(skip while body if while condtion is False)
        ## (self.index + 1) -- execute this next if while condtion is True i.e. get into loop body

        ## Time complexity -- O(len(DATA))-- SAME as give_result_exp()


    def execute(self):
        if self.type == 'var=exp':
            next = self.give_result_exp()
        elif self.type == 'loop':
            next = self.give_result_while()
        else:## self.type == 'branch'

            (a,b) = get_garbage_values(DATA) ##O(len(DATA)) -- FOUND EARLIER
            print('_________________________________________')
            print('Garbage values are: ', a)
            print('Variable values are: ', )
            for i in range (0,len(b)): ## O(len(b)) <= O(len(DATA))
                (variable,value) = b[i]
                print(variable, ' = ', value )
            print('________________________________________')
            next = self.give_result_branch()
        return next
        ## as explained above, each one returns the reference to the next statement that has to
        ### be executed after exection of the statement itself -- this reference(index) is next

        ## Time complexty -- O(len(DATA)) -- combining above results

    ## string representation
    def __str__(self):
        if self.type == 'loop':
            return self.further+ ' ' + str(self.operand1)+ ', ' + str(self.operand2)+', ' + str(self.operand3)
        elif self.type == 'var=exp':
            if self.further == 'assignment':
                return str(self.operand3) + ' = ' + str(self.operand1)
            elif self.further == 'unary':
                return str(self.operand3) + ' = ' + self.operator+ ' ' + str(self.operand1)
            else:
                return str(self.operand3)+' = '+str(self.operand1)+' '+ self.operator+' '+ str(self.operand2)
        else: ## for branch
            return self.type + ' ' + str(self.operand3)
    ## O(1) in time -- accessing attributes of object (at max 5 attributes)




def index_of_while(req_tabs):
    # tab_list with branch not appended
    # this function is used while reading input_file, if we detect a decrement in 'tab level'
    # this means that a 'while body' is finished.
    # At this stage, we need to add an Unconditional branch with reference to while statement it is connected with.
    # req_tab --int -  'tab level' of while statement required
    # returns -- int -- index in instruction list of the connected 'while statement'

    i = len(tab_list)-1
    while True:
        if tab_list[i] == req_tabs and instruction_list[i].type == 'loop': ## type of obj should be 'loop'
            return i
        i-=1
    ## O(len(tab_list)) in time -- in worst case -- 'while' is first element if instruction list


tab_list = [] ## instruction_list and tab_list run parallely
## instruction_list[i].tabs == tab_list[i]
i = 0
lines = [] # initalise to empty list

with open('/home/Harshit0143/input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
for statement in lines: # each statement is on a separate line
    tabs = 0
    statement = statement.replace("    ", '\t')
    while statement[tabs] == '\t':
        tabs += 1
    token_list = statement.split() # split a statement into a list of tokens
    if token_list == []: ## when we reach end of input code
        break            ## break loop else it shows indexing error for empty token_list
    if i >=1: ## for detecting a reduction in tab level -- obviously not applicabe to first instruction
        last_tab = tab_list[-1] ## tab level of previous statement

        if  tabs < last_tab :  #==> while body ended
            for j in range (0, last_tab - tabs): # ==> A direct reduction of two or tab levels is possible
                h = last_tab-j-1  ## this is equal to tab level of while statement it is connected with

                corresponding_while = index_of_while(h)  ## index of while connected with the Uncond Branch
                instruction_list.append(Instructions(h, i , ['branch', corresponding_while]) )
                                            # Add this (target) index to attribute

                instruction_list[corresponding_while].tokens.append( ('jump:',  i+1))
                # Go to the while Instruction connected with Uncond branch and to it add index if uncond branch +1
                # We will jump to this index if while condtion is False
                # Clearly, this attribute couldn't be assigned to 'while statement' before entire code was read

                tab_list.append(h) ## tab level of uncond branch
                i+=1 ## increase idex by 1

    instruction_list.append( Instructions(tabs,i,token_list))
    ## Add the statement--  done always whether or not there is a tab reduction
    tab_list.append(tabs)
    i +=1

### for the case when when there is no statement after the end of a while loop
### now 'tabs' is not read as there are no more instructions
last_tab = tab_list[-1]
if last_tab != 0:
    for j in range (0, last_tab):
            h = last_tab-j-1  ## this is equal to tab level of while statement it is connected with
            corresponding_while = index_of_while(h)  ## line number of while connected with it
            instruction_list.append(Instructions(h, i , ['branch', corresponding_while]) )
                                                    # Add this (target) index to attribute
            instruction_list[corresponding_while].tokens.append( ('jump:',  i+1))
            # Go to the while Instruction connected with Uncond branch and to it add index if uncond branch +1
            # We will jump to this index if while condtion is False
            tab_list.append(h)
            i+=1
### n is the numbe rof lines in code
### creating objects and appending them if O(1) time (found earlier)
## Time complexity for creating instruction_list <= O(n^2)  -- considering we also have to call index_of_while()
## but this is called only if change in tab level is found which will happen <= n times so n*O(n) == O(n^2)

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




print()
print('After complete execution: ')
(a,b) = get_garbage_values(DATA)  ##O(len(DATA))
print('Garbage values are: ', a)
print('Variable values are: ', )
for i in range (0,len(b)):   ## O(len(DATA))
    (variable,value) = b[i]
    print(variable, ' = ', value )
print('________________________________')


# print('DATA: ')
# print(DATA)

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












