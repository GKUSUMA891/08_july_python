print("Hello python")
print("hello thundersoft")
var="mango"
print(var)
var1=100,1000   #assigning
print(var1)
var11,var2=200,300  #assigning
print(var11,var2)
match="kohli"   #format
print("king of the cricketer is {0}".format(match))

a=50    
b="mango_appple"
c=a+8j
print(type(a))  #int
print(type(b))  #string
print(type(c))   #complex
var11=str(30)
var12=int(30)
var13=float(30)
print(var11)   #string --->30
print(var12)   #int--->30
print(var13)    #float--->30.0

a=20
A=30
A=40  
print(a)
print(A)       #print updated one
#------------------------------------------------------------
#------------------------LISTS---------------------------
list1=["MANGO","APPLE","orange"]
print(list1)
list1.append("grapes")
print(list1)
#append
a=[10,20,30,40,50,60,70]
b=[]
print("a is:",a)
a.append(90)
print("a is:",a)
b.append(1000)
print(b)
#extend
b=["tcs","wipro","thundersoft"]
a.extend(b)
print(list(a))

for i in b:
    print(i)
if i=="thundersoft":
    print(list[b])
else:
    print("thundersoft")
#insert
a=["mango","apple",10,20,30,"string"]
print(tuple(a))
a.insert(1,89)
print(a)
n=len(a)
m=10
for i in range(0,n):
    a.insert(5,m)
    i=i+1
    m=m+10
print(a[i])

num=[10,20,30,40,[12,13,14,15],80]
for i in num:
    if [12,13,14,15] in num:
        print(num)
        if i==num[1]:
            break
            print(i)

#remove
prime=[2, 3, 5, 7, 9, 11]

prime.remove(9)

print('print prime numbers: ', prime)
for i in range(0,6):
    if i==9:
        prime.remove(i)
        print(prime)
        break
print(prime[1:])
#pop()
message= ['Python', 'Java', 'C++', 'French', 'C']

return_value = message.pop(3)

print('Return Value:', return_value)

print('Updated List:', message)

message.pop(-1)
#clear

prime = [2, 3, 5, 7, 9, 11]

prime.clear()

print('List after clear():', prime)


mango=["apple","vingo","maxi",100,2003,445]

mango.clear()
print("after clear the list:",mango)

#index
list1=[10,20,30,40,'johny']
for i in range(0,len(list1)):
    m=list1.index(list1[i])
print(m)



maxi = ['a', 'e', 'i', 'o', 'i', 'u']

index =maxi.index('e')

print('The index of e is:', index)

index = maxi.index('i')

print('The index of i:', index)
#count

numbers = [2, 3, 5, 2, 11, 2, 7]

count = numbers.count(2)


print('Count of 2:', count)

man=[100,200,300,400,500]
man.extend([300,203,104,105,[1,2,3,4,5],300])
print(man)
man.append(555)
print(man)
man.remove(100)
print(man)
man[2]=180
print(man)
n=man.count(300)
print("count:",n)

random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

count = random.count(('a', 'b'))

print("The count of ('a', 'b') is:", count)


#sort
man=[10,2,32,43,50,26,57,88,79]
man.sort()
print("sorting:",man)

man.sort(reverse=True)
print("descending:",man)

man.sort(reverse=False)
print("ascending:",man)
systems = ['Windows', 'macOS', 'Linux']
print('before List:', systems)

reversed_list = systems[::-1]
print('Updated List:', reversed_list)
#copy
maxi=[]
maxi=man.copy()
print("after copying list is:",man)


 #all(),any(),enumarate(),len() ,list(),max(),min()                   
a=['True',1,2,3,4]
b=[1,0,50,77]
print(all(a))
print(any(a))
print(all(b))
print(any(b))
print("length of a:",len(a))
print("max element is:",max(b))
print("min element is:",min(b))
print("list of the elementas is:",list(a+b))
for i in enumerate([1,2,3,4,'mango',6,50]):
    print(i)
    
#sum of elements
list1=[10,30,40,50]
sum=0
n=len(list1)
for i in range(0,n):
    sum=sum+list1[i]
print(sum)





































