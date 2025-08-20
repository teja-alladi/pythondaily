# # #functons - block of reusable code

# # # arguments and parameters
# # #types of argumets - positional,keyword, default,varibale engt and kwargs
# # #return - to end the func and to store the end result
# # #lamba- simplest way of creating small anonymous functions-single line code


# # #what is strings and what are the built in methods
# # #strings- collection of characters which are enclose in single quotes or double
# # # quotes

# # # how many types of strings are there?
# # a="hello"
# # a='hello'
# # a='''hello''' #triple single quotes are used for multi-line strings
# # a="""hello""" #triple double quotes are used for multi-line strings

# # #how to access string
# # a="hello"

# # print(a)#hello
# # #individual characters can be accessed via index
# # print(a[0])#h
# # print(a[1])#e

# # #string are immutable
# # data="hello world"
# # data[0]="z"
# # print(data[0])

# # #string concatination
# # a="hello"
# # b="world"
# # c="Mr"

# # print(c+" "+a+" " +b)

# # #string multiplication
# # print(a*3)  #hellohellohello

# # #string formatting
# # name="teja"
# # age=26
# # print("hello mr ",name," welcome to our page")
# # print("hello"+ name+" welcome to our page")

# # # for formatting
# # print(f"hello mr {name} welcome to our page your age is {age}")

# # #slicing-extracting the part of the string
# # name="ravi teja"

# # # str[startindex:endindex:step]
# # print(name[5:9])
# # print(name[::2]) # skips every second character
# # print(name[::-1]) # reverses the string
# # print(name[5:])#teja


# # string  escape characters
# # \n -next line
# # \t -tab
# # \\ -backslash
# # \' -single quote
# # \" -double quote

# # a="hello \' world"
# # print(a)

# # python string built in methods
# # # len()- it returns the total no of characters
# # a="hello World PYTHON is Amazing"
# # print(len(a))

# # #case conversion methods
# # print(a.upper())  # HELLO
# # print(a.lower())  #  hello
# # print(a.capitalize())  # Hello world python is amazing
# # print(a.title())  # Hello World Python Is Amazing
# # print(a.swapcase())  # hELLO wORLD python IS aMAZING



# #string searching and replacing
# # s="Hello world python is amazing"

# # #find-it is used return the index no of a substring - it returns -1 if not found
# # print(s.find("java")) # -1
# # print(s.find("python"))  # 12

# # print(s.index("world"))  # it returns index if not found it returns ValueError: substring not found

# # print(s.count("py")) # it returns the no of occurences of a substring - 3

# # print(s.replace("python is amazing", "django is easy"))

# # print(s)




# s="Hello@ world @python is amazing"
# print(s.split("@"))  # it splits the string into a list of words


# a=["html","css","js"]
# print("#".join(a))  # it joins the list of words into a string with space as separator


# s="hello world                         "
# print(len(s))  # 50
# print(s.strip())  # it removes the leading and trailing spaces

# print(s.startswith("hello"))  # it checks if the string starts with "hello"
# print(s.endswith("hello"))  # it checks if the string ends with "hello"