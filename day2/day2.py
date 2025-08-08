# what is an varibale
# what are the different data types


# type conversion
# 1) implicit type conversion
#  python will automatically conver one type to another

# val1=100
# val2=10.8
# print(val1+val2)
# print(type(val1+val2))

# data=True
# print(True+True)
# print(type(True+100))


# 2) explicit type conversion
#  we will convert one type to another type using built in functions

# val=int("100")
# print(val)

# print(type(val))

# li=[1,1,2,3]
# print(tuple(li))

# how to take input from user
# input always takes strint format --string----convert number
# firstnum=int(input("enter a num1"))
# secondnum=int(input("enter a num2"))
# print(firstnum+secondnum)

# # how to calulate the age in years
# dob=int(input("enter ur dob year")) #2000,1998,1990,1980
# print(2025-dob)#20

# #greet a message
# name=input("enter ur name")
# print("hello welcome ",name, " to our  web page hope ur doing well1") 

# operators
# operators are the symbols that is used to perform different
# mathemetical operations
#arthimetic operators- used to perform basic calculations
# 1) addition +
# 2) subtraction-
# 3) multiplication *
# 4) division /
# 5) modulus % (remainder)
# 6) exponentiation **
# 7) floor division //
# a,b=10,3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b, "4ht line")
# print(a%b) 
# print(a**b)
# print(a//b, "last")


# assignment operators - it perform assignment and some operation at
#  a same time
# += #incrment
# -= #decrement
# *=
# /=
# //=
# **=
# %=

# +(operator)
# 3(operand)

# a=10
# a+=5#a=a+5 a=10+5=15
# print(a)

# cart=0
# cart+=1000
# print(cart)
# cart+=500
# print(cart)
# cart+=300
# print(cart)

# comparsion operators - it compare multiple values returns true or False
# == - to compare values 
# !=
# <- - to compare values
# >
# <=
# >=
# apples="10"
# bananas="10"
# print(apples==bananas)

# usertype="student"
# print(usertype=="admin")

# a=5
# b=5
# print(a!=b)

# print(a<b,"it is small")
# print(a>b, "it is big")
# print(a<=b)
# print(a>=b)

# logical operators- it is used for combining multiple conditions
# and - it is used for both conditions are true
# or - it is used for atleast one condition is true
# not - it is used for negating the condition

# print(True and True ) #return true only if all cond are true
# print(False and True)
# print( True and False)
# print( False and False)

# print(True or True)
# print(False or True)
# print( True or False)
# print( False or False) #return false if all  cond are  false

# print(not True,"val") #return false if cond is true
# print(not False,"val") #return true if cond is false


# a=10
# b=5
# c=-2
# print(a==10 and a<100) #true
# print(a==10 and a<100 and a==c) #false

# print(a==10 or a>100) #true
# print(a==10 or a<100 or a==c) #true

# print(not a==10) #false



#identify operators - it is used to compare the identitiy (address) of two object
# is 
# is not
# a=["teja","bangalore"]
# b=a 
# c=["teja","bangalore"] 
# print(b is a) #true
# print(b is c) #false
# print( b is not a) #false
# print( b is not c) #true

# print(a==c) #true

#membership operator- it check whether a value is present or not in a sequence
#in - value is present or not - if present return true else false
# not in - value is not present or not - 
      #if not present return true else false
# a=["samsung", "redmi", "oneplus"]
# print("oppo" in a)
# print("samsung" in a)

# st="python is a interpreted lang"
# print("interpreted" in st)

# li=[30,40,50]
# print(30 in li)
# print(30 not in li)

# ternary opertor - it assigns the value to an varible based on a condition
# a="value1 " if conditon else  "value2"

# a=50
# b="less than 100" if a<100  else "greater than 100"

# age=int(input("enter ur age mama"))
# voting="allowed for vote" if age>18 else "not allowed for vote"

# print(voting)

# find whether a person has fever or not 
#checking cold , bp , and temp
# cold=True
# bp="normal"
# temp=100

# data=("person dont have fever " if cold==False and bp=="normal"  and 
#       (temp>=98 and temp<=100) else "fever confirmed")
# print(data) 


#find a grade for a person based on marks
#marks>=90 - A
#marks>=80 - B
#marks>=60 - c
#marks<40 - "fails"


# marks=39
# data=( "he got A" if marks>=90 else
#       "B" if marks>=80 else 
#        "c" if marks>60 else 
#        "d" if marks>=40 else "fail")
# print(data)