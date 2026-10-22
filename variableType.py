name="vinay"
name1='vinay'
name2="""vinay"""
age=22
mob=9900416208
isStudent=True
height=5.8

# Printing all variables
print("name",name)
print("name1",name1)
print("name2",name2)
print("mobile",mob)
print("isStudent",isStudent)
print("height",height)
print("age",age+1)

#rule for variable name
#1. Variable name should start with a letter or underscore
#2. Variable name can only contain letters, numbers, and underscores
#3. Variable names are case-sensitive
#4. Variable name should not be a reserved keyword
#5. Variable name should not contain any special characters or spaces

#number data types
#1. int
#2. float
print("int data type",type(age))
print("float data type",type(height))
print("string data type",type(name))

#dynamic typing
x=10
print("x",x)
x="vinay"
print("x",x)

nothing=None
print("nothing",type(nothing))

#type conversion and type casting
#1. Implicit type conversion
x=10
y=5.5
z=x+y
e=int("7")  # forcefully convert string to int
print("x",type(x))
print("y",type(y))
print("z",type(z))
print("e",type(e))