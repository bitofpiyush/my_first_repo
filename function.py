#function
#to make function we use def(defination) keyword

def hello():
    print('Hello! everyone')
    
hello()
hello()
hello()
hello()
hello()

def hello_world():
    return "Hello World"

print(hello_world())
print(hello_world().upper())

#argument
def hello_func(greeting,name='David'):
    return '{},{}'.format(greeting,name)
print(hello_func('Hi'))

#args and Kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_info('Maths','CompSci',name='David',age=20)
 
def stu_info(*args,**kwargs):
    print(args)
    print(kwargs)
subject=['Maths','Arts']
info={'name':'Ram','age':20}
    
stu_info(*subject,**info)    
     