# # # break and continue
# # # while loop
# # # nested loop

# # #functions
# # # it a block of code that performs a specific task when something invokes it
# # # it is defined with def keyboard followed by funciton name followed by 
# # # parameters followed by block of code

# # # login -operation
# # # signup-operation
# # # payment-operation
# # # logout-operation
# # # addtocart-operation
# # # how to define a function
# # # Syntax   

# # # def teja():
# # #     print("hi, this is Teja's function")
# # #     print("Hello, this is Teja's function")
# # #     print("how r u, this is Teja's function")
    
# # # invoke a function - calling a function
# # # teja()
# # # teja()




# # # parameters and arguments- variable names and variable values

# # # syntax 
# # # def name(param1,param2,param3):
# # #     print("some content",param1)

# # # name(arg1,arg2,arg3)
# # # name(arg1,arg2,arg3)


# # # def greet(a,b):
# # #     print("hello ",a," your age is ",b)

# # # greet("john", 24)
# # # greet("teja", 25)
# # # greet('divya',26)


# # # def click(num):
# # #     print("Button clicked", num)

# # # click(10)
# # # click(1)



# # # def add(a,b):
# # #     print(a+b)
# # # # add(10,20)
# # # # add(3,8)
# # # # add(1,2)

# # # def seq(a):
# # #     for i in range(a):
# # #         if i%2==0:
# # #             print(i, "is even")
       
# # # seq(5)
# # # seq(3)


# # # return - it is used to exit a function and return a value-function name

# # # 1) function name stores the function defintion
# # # print(greet)----referecne id

# # # 2) function calling- execution of the function
# # # greet()

# # # 3) printing the function calling - func execute and return value
# # # print(greet("john"))
# # # def greet(name):
# # #     print("hi")
# # #     return "hello python"
# # #     print("hello")
# # #     print("hi again")

# # # print(greet)
# # # greet("john")
# # # print(greet("john"))

# # # def form1(a,b,c):
# # #     return (a+b/c+a-b)
    
# # # def form2(d,e):
# # #     return (d*e/e+100)

# # # data1 = form1(10,20,30)
# # # data2 = form2(40,50)

# # # print(data1)
# # # print(data2)
# # # print(data1+data2)


# # #types of arguments
# # #positional arguments
# # def add(a,b):
# #     return a+b

# # print(add(10,20))  

# # #keyword arguments
# # def add(a,b):
# #     return a+b

# # print(add(b=30,a=40))

# # #default arguments
# # def greet(name="guest"):
# #     print("hello",name)

# # greet("teja")
# # greet("john")
# # greet()

# # #variable length arguments- *args
# # def add(*a):
# #     return sum(a)

# # d1=add(10,20,30)
# # d2=add(10,20,30,40,50)  

# # print(d1+d2)

# # #kwargs- keyword arguments
# # def display(**a):
# #     print(a)
 
# # display(name="teja", age=25, city="hyderabad")


# #named functions

# #lambda function- it a concise way to define a function- anonymous function

# # syntax/

# # varname= lambda parameters: expression

# # add=lambda a,b: a+b

# # print(add(10,20))
# # print(add(100,20))
# # print(add(8,2))

# # scopes - life of an variable -accessibility of a variable
# # global varaibla- which can accessed from anywhere in the program
# # local varaibel- whch can accessed only within the function


# x=10--global

# def fun():
#     x=30--local
#     print(x)

# fun()

# print(x)


# #global key word is used to manipulate the local to the global
# def fun():
#     global x
#     x=10
# fun()
# print(x)