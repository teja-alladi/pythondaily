# # variables
# # datatypes
# # operators

# # variables - are the container for storing the data and data could be anything

# # how to define a variable
# # identifier=value 



# # identifier rules
# # it should start with _ or alphabet but not with number or special symbols
# _data=10
# data10=10

# 1=10
# &data=10

# #reserved words cannot be used a identifers
# if=10
# for=20
    
# #it should contain space
# father name="venkat"

# fatherName="venkat"
# fathername="venkat"

# # identifiers are case sensitive
# a=10
# A=10

# # if it is start with _ private __strongrpivat __magical__
# _salary=100000 #private
# __password="jsfdf"
# __partime__="jdfjd"


# a=10

# b,c=30,40

# d=e=f=100

# print(d)
# print(e)
# print(f)


# datatypes- 
# primitive and non primitive data types
# single values and multiple data types

# primitive
# int- number - 0 ,-10,10 100
#float - decimal - 10.10 10.50 5.2
#strings- sequence of characters which are encloses in single, double quote,
#boolean - True / False
#Nonetype
a=100
print(a)
b=10.5
print(b)
c="teja"
print(c[0])

print(c)
d=True
print(d)
e=False
print(e)
f=None
print(f)

# non primitive data types- which comes in collection
#list - used to store multiple values- vname=[1,2,3,"hello", True]
#  can be accessed using index -starts with 0
#it is mutable
data=[1,2,2,2,2,3,"hello", True, False]
# print(data)

#set - unordered collection of unique values
uni={"raju", "ramu","raju"}
print(uni)

#tuple - ordered collection of values and but immmutable
val=(1,1,2,2,3,3,"helllo","python")

print(val[0])



# dict- key value pair - key is unique and value can be duplicate
std={"rank":1, "age":25, "batchno":7}
print(std)

#range - it is a sequence
a=range(5,15)
print(a)



# type
a="hello"
b=True
print(type(val))

