student={'name':'David','age':20,'courses':['Maths','Computer']}
print(student['name']) 
print(student.get('phone','not found')) #get a particular key from the dictionary
student['address']='Kathmandu'
print(student)
student['name']='Piyush' #name update from david to piyush
print(student)
#to update the whole dictionary at once we use update()
student.update({'name':'Krish','age':25,'courses':['Nepali','Hindi']})
print(student)
popped=student.pop('name') #poping is one of the method to delete keys from dictionary
print(student)#gives the value after poping the name
print(popped)#gives the popped value i.e name
del student['address'] #del is another way to delete keys 
print(student)

food={'Location':'Thapathali','time':'Morning','day':['Sun','Mon']}
print(food.keys()) #gives only keys
print(food.values()) #gives values of keys
print(food.items()) #gives keys along with the values

#loop
for key,value in food.items():
    print(key,value)
