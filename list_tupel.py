#List: are mutable means we can modify them
food =['MOMO','Pizza','Burger']
print(len(food))
print(food[0:2]) #here firstindex 0 is included but 2nd index 2 is not included
food.append('Samausha') #append:add if anything is missing
print(food)
food.insert(1,'Noodles')#insert:add food in particular index
print(food)
new_food=['rice','meat']
food.insert(0,new_food) #adding content of two variable using insert is not systematic
print(food) 
print(food[0]) #index 0 must contain rice but using insert it gives both rice and meat
food.extend(new_food)
print(food)
print(food[0])
new_food.remove('rice')#remove:remove any content from the list
print(new_food)
popped=food.pop() #pop:removes the last content of the list
print(food)
print(popped) #returns the popped value
#Sorting
courses=['Math','English','Comp_Science']
courses.reverse() #reverse:reverse the content of courses
print(courses)
courses.sort() #sort:Ascending or Descending order
print(courses)
num = [9,6,4,8,1]
num.sort()#ascending order
print(num)
num.sort(reverse=True)#descending order
print(num)

#min max and sum
nums=[5,6,3,8,1,2,]
print(min(nums))
print(max(nums))
print(sum(nums))

names=['Piyush','Gaurav','Chetan','David']
print(names.index('David'))
print('Prekshya' in names)

for index,name in enumerate(names,start=1):
    print(index,name)
    
names=['Piyush','Gaurav','Chetan','David']
name_str=' - '.join(names)#converts list into string
new_list=name_str.split(' - ') #converts string into list
print(name_str)
print(new_list)

#tuples:are immutable means we can't modify them,we use () parenthesis in tuples
#so what's difference betn list and tuples,let's understand with code
#code for list
list_1=['Maths','English','Neplai']#to make list we use []bracket
list_2=list_1
list_1[0]='CompSci'#We can make changes on list
print(list_1)
print(list_2)
#code for tuples
tuple_1=('Maths','English','Neplai')#to make tuples we use ()parenthesis
tuple_2=tuple_1
#tuple_1[0]='History' we cannot make anu changes in tuples
print(tuple_1)
print(tuple_2)
#Conclusion of lists and Tuples:List is used to make changes and also used in loops 
#but when there is no need to make any changes and we only have to make loops then we 
#use tuples

#Sets:In sets we use {} braces,it doesn't care about order,it's order changes with each
#execution,bcz sets test whether the value is present or not and removes the duplicate
#values
clz_1={'KEC','PUL','ADV','Thap'}
clz_2={'KEC','PUL','ERC','WRC'}
print('KEC' in clz_1)#checks whether KEC is present in set clz_1
print(clz_1.intersection(clz_2))
print(clz_1.difference(clz_2))
print(clz_1.union(clz_2))

#Creating Empty Lists,tuples and Sets
 
empty_list1=[] #1
empty_list2=list() #2

empty_tuple1=() #1
empty_tuple2=tuple()

empty_set1={} #we can't use it 
empty_set=set()
 