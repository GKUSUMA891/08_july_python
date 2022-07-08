#tuple
#count
rossy= ("apple", "banana", "cherry","banana")
print("count is:",rossy.count("banana"))

#index
rossy.index("banana")
print("index of banana is:",rossy)
print("len is:",len(rossy))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


doggy = ("apple", "banana", "cherry")
for x in doggy:
  print(x)
  print(type(doggy))


#all(),any(),enumarate(),len() ,list(),max(),min()                   
a=('True',1,2,3,4)
b=(1,0,50,77)
print(all(a))
print(any(a))
print(all(b))
print(any(b))
print("length of a:",len(a))
print("max element is:",max(b))
print("min element is:",min(b))
print("list of the elementas is:",list(a+b))
for i in enumerate((1,2,3,4,'mango',6,50)):
    print(i)
    
#sum of elements
list1=(10,30,40,50)
sum=0
n=len(list1)
for i in range(0,n):
    sum=sum+list1[i]
print(sum)

