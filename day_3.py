# strings

# can be write single ,double anf triple also

a = "hello"

print(type(a))

b = 'hello'

print(type(b))

c = """hello
        world"""
        
print(type(c)) 


#slicing of string

a = "amazing world  without stress"

print(a[0:3])   #index starts with 0 where first index included and last index excluded

print(a[0:])    #can be rite like that means len of string minus one 

print(a[:12])   # that means starts with 0 to 12 index

print(a[-7:-1]) #negative indexing starts with -1.


#slicing with step

print(a[1:10:2])  #start with 1 index to 10 index with step of 2 also note that jump of 2 means it will tack last indexed jump number also

print(a[::2])    #if we want to take all string with step of 2 then we can write like that


#some function that manipulate and modify string

print(a.find("  "))  #find the index of first occurrence of string
print(a.count("a"))  #count the number of occurrence of string
print(a.index("world"))  #find the index of first occurrence of string, if not found then it will give error

print(a.replace("  ", " "))  #replace the string with another string

print(a.strip())  #remove the leading and trailing spaces
print(a.lstrip())  #remove the leading spaces
print(a.rstrip())  #remove the trailing spaces  

print(a.upper())  #convert the string to upper case

print(a.lower())  #convert the string to lower case

print(a.swapcase())  #swap the case of the string

print(a.capitalize())  #capitalize the first letter of the string


#some escape sequence

print("\"dear harry, this python course is nice, thanks!\"")  #print the string with double quotes


# Format strings
name = "Amit"
score = 95.567
print("Formatted string:", f"Name: {name}, Score: {score:.2f}")
