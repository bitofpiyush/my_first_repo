#loops in python
#break 
a=[1,2,3,4,5]

for num in a:
    if num==2:
        print('Number Found')
        break 
    print(num)
 
#continue   
b=[1,2,3,4,5]

for num in b:
    if num==2:
        print('Number Found')
        continue
    print(num)
    
#loop inside loop
nums=[1,2,3,4,5]
words=['a','b','c']
for num in nums:
    for letter in words:
        print(num,letter)
        
#print numbers from 1 to 10
for i in range(1,11):
    print(i)
    
#while Loop

x=0
while x<10:
    if x==5:
        break
    print(x)
    x+=1

#for infinite loop
#a=0
#while True:
    #print(a)
   # a+=1