#strings concept
a="hello python!"
print(a.index('python'))
print(a)
print(a[0:])
print(a[5])
print(len(a))
b="here python is easy\n"
b=a+b
print(b)
for i in b:
    print(i,end="")
n="hi prema,how are you {},i am {}"
name="prema"
age=20
print(n.format(name,age))

print(n[-5:-2])
print(n.upper())
m=n.upper()
print(m)
mm="    Hi ma,HOW are you APPA    "
mm=mm.lower()
print(mm)
mm=mm.strip()
print(mm)

print(mm.replace('appa','pappa'))
print(mm.strip('hi'))
maxi="hello Rossy.how is \"Prajju\" and deepa"
maxi=maxi.strip('and deepa')
print(maxi)
print(maxi.capitalize())
print(maxi.casefold())
maxo=maxi.center(20,"*")
print(maxo)

maxx="dea§"
maxoo="deass"
if maxx.casefold()==maxoo.casefold():
    print("both are equal")
else:
    print("both are not equal")

maxi=maxi.count('s')
print("count of 's' is:",maxi)

maxx=maxx.encode()
maxoo=maxoo.encode()
print(maxx)
print(maxoo)
maggy="hi dear!.how are you my dear"
if maggy.endswith("my dear"):
    print("True")
else:
    print("False")

maggy=maggy.expandtabs(15)

print(maggy)
maxy="thun@der"
maxy.encode()
print(maxy)

print("number of  'o' is:",maggy.find('o'))
message="hi dear {},how is your {}"
print(message.format('kussu','health'))

print("all numeric:",message.isalnum())
print("all alphabetical:",message.isalpha())
messy='123456'
print("is decimal:", messy.isdecimal())
print("is digit:",messy.isdigit())
messagee="PYython"
if messagee:
    print("all identifier:",messagee.isidentifier())
messii="pytho n"
if messii:
    print("identifier:",messii.isidentifier())
else:
    print("not identifier:",messii.isidentifier())

print("lowercase:",messagee.islower())
print("uppercase:",messagee.isupper())
print("swapcase:",messagee.swapcase())
if messy:
    print("isnumeric:",messy.isnumeric())
else:
    print("not isnumeric:")
string=" \tstrinng calculation"
print("remove white space:",string.isspace())
print("is title:",message.istitle())

print("upper:",message.upper())
print("is upper:",message.isupper())
print("lower:",message.lower())
print("is lower:",message.islower())
print("join another string:",messagee.join(messy))

ab="    abcdefgh    "
mo="    123"
nn=len(ab)
#for ab[i] in range(0,n,3):
print(ab.join(mo))
print("is r just:",ab.rjust(10,"@"))
print("is l just:",ab.ljust(10,"@"))
print("before swap case:",ab)
print("after swap case:",ab.swapcase())
print("is right strip:",ab.rstrip())
print("is left strip:",ab.lstrip())
print("is remove space using 'strip':",ab.strip())
print("string partition:",message.partition('is'))
print("string before replace:",message)

print("string after replace:",message.replace('is','are you gud'))
moj="let me sing a kutty story play attension"
print("replace string:",moj.replace("attension","sing sing sing",2))
print("find the 't' in string:",moj.rfind("t",2))
print("return index:",moj.index('kutty story'))
moj="let me sing a,kutty story ,play attension"
print("split string:",moj.split(',',4))
print("split right side string:",moj.rsplit(',',2))
print("split string:",moj.split(':',2))
print("split right side string:",moj.rsplit(',',3))

mojjy="let me sing a\n,kutty story\n ,play \n,attension"
print("split lines in a string:",moj.splitlines())
if mojjy=="let me":
    print("starts with words:",mojjy.startswith('letme'))
else:
    print(" else starts with words:",mojjy.startswith('let me'))
print("return first letter capitel:",mojjy.title())
print("fill zero:",mojjy.zfill(10))
print("fill zero:",mojjy.zfill(15))

mofe="abcdef"
make="123456"
mos="abcaus"
mny="@"
print("return true if letter is ascii:",mny.isascii())
print("maketrans:",mos.maketrans(mofe,make))

str={'x':40,'y':30}
print('{x}{y}'.format_map(str))

a="marsh"
b="mallow"
print(a+b)
print(a * 2)
print(a[1])
print(a[1:3])
print('m' in a)
print('marc' not in a) 
print('jam' not in a)















































































      







































