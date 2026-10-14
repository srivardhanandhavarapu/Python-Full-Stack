'''
Datatypes --> It will tell us how to define the date
Numeric datatyes --> integer,float,complex
Boolean type --> true/false
None type --> None
Sequence types --> strings,lists,sets,frozensets,mappings(dictionaries)
'''
#numeric datatypes -> integer -->quantities,ids,order ids,stock,age-->int
'''
age=32
print(age)
prin(type(age))
stock=35
print(type(stock))
batch_rank=1
print(batch_rank)
'''
#float values --> salaries,price,percentage calculations,temp....--> float
'''
salary=15125.45
print(salary)
print(type(salary))
temp =34.5
print(type(temp))
'''
#complex -->real and imaginary values-->scientific charecters,simple processing
'''
i5 = 23
data=3+i5 #in this case addition will be done
print(data)

data = 3+5j
print(data)
print(type(data))
'''
#boolean --> true/false --> validations
'''
access=True
print(type(access))
result=False
print(type(result))
'''
#nonetype --> None
##none --> 0,False,'',[],(),{},set() --> none cases in python
'''
branch_rank=None
print(type(branch_rank))
'''
#typeconversions -> converting one datatype to another datatype
#explict conversion
#integer --> float,complex,boolean
#every built-in datatype is a built-in function
'''
rank=5
print(type(rank))
b=float(rank)
print(b)
print(type(b))
c=complex(rank)
print(c)
d=bool(rank)
print(d)
print(type(d))
#space is also a character in python
print(bool([])) #empty string inside a list
'''
#float-->integer,complex,boolean
'''
temperature=27.45
print(type(temperature))
a=int(temperature)
print(a)
b=complex(temperature)
print(b)
c=bool(temperature)
print(c)
'''
#complex --> int,float,bool
'''
signal=5+6j
#c= int(signal) #raises Typeerror (invalid datatype)
#print(c)
#d=float(signal)
e=bool(signal)
print(e)
'''
#boolean-->int,float,complex
'''
access=True
a=int(access)
print(a)
b=float(access)
print(b)
c=complex(access)
print(c)

a=int(float(bool(5)))
print(a)
b=bool(float(int(35))) #check for the outer one
print(b)

c=True+35+3.5+(6+5j) #True becomes 1
print(c)
'''

#sequence types --> strings,lists,sets,frozensets,dictionaries
#strings --> groupof charecters
#quotations --> single,double,triple quotes
'''
place="codegnan"
print(type(place))
name="vardhan"
print(name)
#strings are immutable,ordered,indexed collection
print(len(name)) #len(obj) -->returns the number of items in a collection
print(len(place))
print(len('qwerty'))
'''

#space is also a charecter
a=" "
print(a)
print(len(a))

#converting string --> int,float,complex,boolean
course = 'python'
#print(int(course)) #value error
#print(float(course)) #value error
#print(complex(course)) #value error
print(bool(course))

#int --> str
#float --> str
#complex --> str
#bool --> str

data=56
b=str(data) #it becomes numeric srting
print(b)
mileage= 13.5
c=str(mileage)
print(type(c))
d=str(3+5j)
print(d)
e=str(true)
print(e)





























