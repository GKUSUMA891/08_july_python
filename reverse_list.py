#program for sorting

#list sorting using li.sort()

li = [2,1,4,3]
print("Before sorting: list = ", li)
li.sort()
print("After sorting: list = ", li)

#list sorting using sorted function

li = [2,1,4,3]
print("Before sorting: list = ", li)
new_list = sorted(li)
print("After sorting: list = ", new_list)

#list sorting in descending order using li.sort()

li = [2,1,4,3]
print("Before sorting: list = ", li)
li.sort(reverse = True)
print("After sorting: list = ", li)

#list sorting in descending order using sorted function

li = [2,1,4,3]
print("Before sorting: list = ", li)
new_list = sorted(li, reverse = True)
print("After sorting: list = ", new_list)

