'''
operators --> Operators helps us to perform operations between operands
Arithmetic Operators -->+,-,*,/,**,//(Integer or floor division),%(modulus -->remainder)
assignment operators --> it helps to assign,update(increment),decrement values
# =(assinging),+=(addition&assign),-=(substraction&assign),*=(multiplication&assign) /=,//=,**=,%=

data=20
print(data)
print(type(data))

stock=data
print(stock)

#increment the value of stock
stock=stock+5 #stock+=5
print(stock)
print(data)

#decrement the value of data by 2 values
data=data-2 #data-=2
print(data)

data*=2
print(data)

data/=2
print(data)

data//=2
print(data)

data**=2
print(data)

data%=2
print(data)

stock=100
stock**=2
print(stock)
'''
#comparision operators (relational operators) --> it performs
#comparision between the operands and results in boolean True/false
#--> conditions ==,!=,<,<=,>=>=
'''
name='vinay'
vinay_attendance=75
print(vinay_attendance>=80)
print(vinay_attendance==80)
print(vinay_attendance<=80)
print(vinay_attendance<80)
print(vinay_attendance>80)
print(vinay_attendance!=80)
'''
#logical operators --> and,or,not(keywords)
#and --> it needs all conditions to be satisfied (two or more) -->True
#or --> it need any one condition to be satisfied
#not -->opp to existing
'''
max_marks=80
vinay_marks=75
max_att=75
vinay_att=70
vinay_marks+=10
certificate=vinay_marks>=max_marks and vinay_att>=max_att
print(certificate)
chance=vinay_marks>=max_marks or vinay_att>=max_att
print(chance)
data=[]
print(data)
print(not(data)) #returns True
data=[12,3,4]
print(not(data)) #returns false as data is existing
#both logical and comparision operators will return result in boolean
'''
#membership operators --> in,not in
#check for the existance in sequence (str,list,seet,tuple,dict)
'''
names=['vardhan','balu','praveen','ruhul']
name='teja'
print(name in names) #returns false
print(name not in names) #returns True
print('12' in '121')
#print(12 in 121) #typeerror as we have taken int type
print('vardhan' in 'vardhan') #returns true as we are checking type as string
print(['vardhan'] in ['vardhan'])#returns false as its a list
'''
#identity operators --> it specifically refers to the object(memory location)
#id --> is, is not
'''
a=15
b=15
print(a==b)
print(id(a))
print(id(b))
c=a
print(id(c))
print(c is a) #as id of both a and c are same -> True
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with similar value identity
print(a is b)
c=a
print(id(c))
print(c is a) #returns True as we are assigning same object
'''
#when we check with the interpreter mode and scripting mode above tuple result changes
#logical membership,identity,comparision(relational) --> always result is in boolean

#bitwise operators --> it performs bitwise operations --> %(bitwise and)
#|(bitwise or) ^(bitwise xor)
#an integer will be converted binary format and perfoms bitwise
#operation following integer to binary conversion

print(7&3)
print(7|3)
print(7^3) #xor operation it returns 4
#7 to binary --> 0111
#3 to binary --> 0011
#7^3 --> 0100

#shifting operations (<<,>>)
print(7<<1)












