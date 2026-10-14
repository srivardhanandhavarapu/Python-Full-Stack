'''
datatypes --> numeric datatypes --> int ,float,complex
-->boolean datatype -->true/false
none type
--> sequences -->str,lists[],tuples(),sets set(),mapping(dictionaries)
{}frozenset
'''
#lists --> a list is an ordered,mutable,indexed and heterogenous collection
#we use [] to represent lists
#students details,order details,stock entires.....
'''
details=[1, 'vardhan','pfs7','vizag',56.7]
print(len(details))
print(type(details))%

stu_ids=['cgvi0134','cgvi0135','cgvi0136']
#print(stu_ids[1])
stu_ids[0]='codegnan'   #here we are using indexing
print(stu_ids[0])
'''
#tuples --> tuples are also immutable,ordered,indexed and heterogenous
#collections, we use () paranthesis
#dimensions,coordinates
'''
places=('hyderabad','vijayawada','vizag')
print(places)
#print(len(places))
#print(type(places))
places[0]='chennai'   #it is not possible as tupleare immutable
print(places)

dimensions=10,20,30    #by default it becomes tuple
print(dimensions)
print(type(dimensions))
'''
#sets--> a set is a unique collection(removes duplicates)
# a set is an unordered,unindexed,mutable collection
'''
ids=set()  #empty set
print(ids)
ids=set([123,134,135,123])
print(ids)
courses={'pfs','jfs','da'}
print(courses)
print(type(courses))
print(courses[0])  #as set is unordered there is no index
'''
#dictionaries -->a dictonary (mapping object) is a collection of
#key value pairs --> dict={k:v},we access only by keys (indexed by keys)
#dicrionary is also mutable collection
#keys must be unique in a dictionary(keys can be int,float,str)
#order complete information
'''
details={'branch':'vizag',
         'batches':['pfs-vsp-007','pfs-vsp-006','pfs-vsp-005','pfs-vsp-004'],
         'course':'pfs',
         'count':19}
print(details)
print(type(details))
print(len(details))
print(details['batch'])   #we access by giving only keys
'''
#every built-in datatype is a built-in function
#int,float,complex,bool,str,list,tuple,set,dict
#lists --> tuples,sets,dict,str
'''
marks=[35,24,54]
a=tuple(marks)
print(a)
b=set(marks)
print(b)
c=str(marks)
print(c)
print(len(c))

marks=(34,12,45)
a=set(marks)
print(a)
b=str(marks)
print(b)
c=list(marks)
print(c)

marks=[35,24,54]
#d=dist(marks) #its not possible like this
e=dist.fromkeys(marks) #we need to use fromkeys(), whatever elements we have taken will come become keys and values will be none
print(e)

#dictionaries --> lists,tuples,sets
ids={1:123,2:124}
a=list(ids)   #it will only fetch keys
print(a)
b=tuple(ids)
print(b)
c=set(ids)
print(c)
d=str(ids)  #every symbol/object will be a character
print(d)
print(len(d))
'''
#frozensets --> it is an immutable set,unindexed,unordered
#we can typecase it to list,tuple,set
'''
a=frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))
b=list(a)
print(b)
c=tuple(a)
d=set(a)
e=dict.fromkeys(a)
f=str(a)
print(c,d,e,f)
print(len(f))

d='vardhan'
e=list(d)
f=tuple(d)
g=set(d)
h=dict.fromkeys(d)
print(e,f,g,h)
'''

#operators --> arithmetic operators,assignment,comparision,logical,membership,identity,bitwise operators

#arithmetic -->+,-,*,/(float division),//(floor division) quotient %modulus(remainder),**(exponential)
a=3
b=2
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)
