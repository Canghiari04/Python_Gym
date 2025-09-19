## 15/09

# OBSERVATIONS
# Environment the association between values and variables
# Python is interpreted but also compiled, few seconds compiled by the Python Machine
# A data type is given from: value, how they are presented, kind of operation possible and the name of the type

# Integer division and module
# 89//2 -> 44
# 89%2 -> 1

# Maximum number for float data types but not for integer, there's no limit for integer

# Difference between commands and expressions, like: v = 3 (CMD) v (EXP)
# Strings, Integers and Floats are immutable

# input() method is always a str type, so I need to change the type with a cast
# input() is a fucking expression, it return a value
# input() receive inside also an initial string printed out the console -> input("Give me a number") ==> Give me a number 

## 18/09 Mattina

### String are immutable

# f' {a=}'
# Condition is a compound command, cause composed by other command
# Lazy evaluation where we suppose a OR condition, if the first condition is TRUE the PythonMachine never judge the final condition after the true one
# Inside the if's block the variables are global, so there is not a local scope inside block

# area_circle is associated to the function text
# a new partition in the internal state will be created, even if a previous variable called "r" has been declared, so each function has their own scope (i.e. of calculate cilinder's area)
# arguments can be expressions, operation between variables, at the same time 
# the variable passed by argument is always the same reference, not a new one
# print(print("Ciao")) -> print "Ciao" and None, cause the inner print return "None"
# cause the small compilation step the PythonMachine know the values assigned to the variables
# is always prefered the local scope, two declaration as below cause an error UnboundLocalError

x = 10
def f():
    v = x # this cause the error during the small step compiling
    x = 100 # we have to define the assignment previously, without that we will have a local bound error
    return x

print(f())

# there are built-in function and function inherited from different kind of libraries, modules (i.e. math)
# iterator inside a for contructor is not local!
e = "1"
s = "Matthew"
for e in s:
    print(e)

print(e) # variable e is the final character of the string s --> always seek to the last assignment, or command!

# never confuse the in command inside the for with the isolated in command -> the isolated in is only for strings, not for every class type
# never combine conditions or other condition in the for's sequence

# an object is a value envelopped in an identity, every declared variable is an object, inside the PythonMachine each variable is related to an object
# different location inside the memmory, even if they have the same value

## 18/09 Pomeriggio

# any operations create a new object, indeed assignment does not create a new object -> (i.e. a = "Ciao" b = a, the last assignment does not create a new object)
# 