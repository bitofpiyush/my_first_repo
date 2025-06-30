food='MOMO'
if food =='MOMO': #if statement
    print('Favourite food')
    
language='HTML' #use of elif statement
if language=='python':
    print('Language is Python')
elif language=='Java':
    print('Language is Java')
elif language=='JS':
    print('language is JS')
else:
    print('Language not found')   
    
#Booleans:and,or,not
name='John'
log_in=True

if name=='John' and log_in: #and
    print('Valid')
else:
    print('Invalid')
    
user='Admin'
log_in=False

if user=='Admin' or log_in: #or
    print('Valid')
else:
    print('Invalid')
    
course='python'
password=False

if not password: #not
    print('Python course')
else:
    print('Not a python course')
   
#object identity=each variable ko value diff memory location ma hunxa so id differenet 
#vaye paxi we can't consider it as equal

a=[1,2,3,4,5]
b=[1,2,3,4,5]

print(id(a))
print(id(b))

print(a is b)#this gives false cuz a and b have diff id 

c=[1,2,3,4,5]
d=c
print(id(c))
print(id(d))
print(c is d)#this give true cuz c and d has same id

#False values in Python
#False
#None
#zero of any numeric type ->0
#Any empty sequence e.g. '',[],() 
#Any empty mapping e.g. {}

condition=['done']#if the bracket is empty then it gives invalid result
if condition:
    print('Valid result')
else:
    print('Invalid result')