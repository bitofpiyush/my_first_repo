#here I learned about strings in Python
message = "Hello, World"
print(message)

print(len(message)) #length of string

print(message[0:6]) #prints character upto certain range
print(message[:3])
print(message[7:])
print(message[5:0]) #no output?

print(message.lower()) #strings in lower case
print(message.upper()) #strings in upper case
print(message.count('l')) #counts how many times the character l is repeated 
name = "My name is Piyush Bhatt"
print(name.find('y')) #find func indicates that y is in 1st index of name var
#In the var name we have y at two indexes but it gives the output of one which comes 1st

new_name = name.replace('Piyush Bhatt','David Laid')
print(new_name)#replacing the character 

greet = "Hello"
name = "Piyush!"
concatenate=greet+' ' + name #method 1 to concatenate
con='{},{} Welcome'.format(greet,name) #method 2 to concatenate
add_string=f'{greet},{name}.Welcome' #method 3 simplest using fstring feature
print(concatenate)
print(con)
print(add_string)

print(dir(message)) #show all the attributes that we have used with var message
