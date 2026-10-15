'''
Tokens,Datatypes(numeric,boolean,nonetype,sequences(sr,lists,tuples,sets,frozensets,mapping objects(dicts))) typecasting
operators
input formatting?otput formatting
'''
#input formatting --> input()
#usage of input()
#we can pass any type of objectas input --> result is in only string
'''
name=input("Enter the name:")
print(name)
print(type(name))
'''
#integer input --> int() --> if you missmatch value --> valueerror
'''
roll_number=int(input("Enter the roll number:"))
print(roll_number)
print(type(roll_number))
'''
#float input --> float()
'''
marks=float(input("Enter the marks:"))
print(marks)
print(type(marks))
'''
#group of strings(multiple values as strings)
#space separated values--> we need to give one space after each object
#returns list
'''
names=input().split()#no need of promt(competitive coding)
names=input("Enter the names:").split()
print(names)
print(type(names))
'''
#comma separated values
'''
subjects=input("Enter the names:").split(',')
print(subjects)
print(type(subjects))
'''
#multiple values (more than one) string
#make sure to match the arguments
'''
name,batch=input("Enter the details:").split()
print(name)
print(batch)
'''
#multiple integer values
#we will use map()
'''
order_id,cost=map(int,input().split())
print(order_id)
print(cost)
'''
#we want to take subject marks
'''
py_marks,ap_marks,ss_marks,sql_marks=map(float,input().split())
print(py_marks,ap_marks,ss_marks,sql_marks)
'''
#group of integers,group of float values
'''
stu_marks=list(map(int,input().split(',')))
print(stu_marks)
discounts=list(map(float,input().split(',')))
print(discounts)
'''
#accept the cost of selling the product from user and also the original cost of the product and determine the profit/loss amount for the user
'''
original_amount=float(input())
selling_amount=float(input())
profit=selling_amount-original_amount
print(profit)
'''
#set of integers
#set of float values --> replace int with float
'''
ids=set(map(int,input("Enter the ids:").split(',')))
print(ids)
print(type(ids))
'''
#passing list() as input using eval()
#you can directly pass same as list,tuple,set data as it is
'''
list_data=eval(input("Enter the values"))
print(list_data)
print(len(list_data))
tuple_data=eval(input("Enter the values"))
print(tuple_data)
print(len(tuple_data))
set_data=eval(input("Enter the values"))
print(set_data)
print(len(set_data))
'''
#passing dict data using eval
#so using eval() you can pass any type of data
'''
stu_details=eval(input())
print(stu_details)
'''
#output formatting-->print()
'''
a,b,c=map(str,input().split())
print(a,b,c)
#now we will use sep
print(a,b,c,sep="----")
#end is specifically telling how you wanna end the statements
print(a,b,c,sep=":",end='\t')#there end=tab space character 
print("vardhan","vizag",end=" ")#here end=space character
print(34,4.5)
'''
#1) using commas in print() --> we separate bt commas
'''
name="codegnan";branch="vizag";batch='pfs-vsp-007'
print(name,"is in",branch)
print(batch,"belongs to",branch,"branch")
'''
#2)using %(modulus) formatting --> old style c programming
#%d --> integers,%f --> float,%s --> strings
'''
age=32
price=45.256
place="vizag"
print("age=%d | price=%f | place=%s"%(age,price,place))
print("price is %.f"%price)#in this case complete decimal part is wiped off
print("price is %.2f"%price)#rounding off to two decimals
'''
#3) Usage of  string formatting --> str.format()

name="codegnan";branch="vizag";age=8
print("{} is in {} and its of {} years in edtech industry".format(name,branch,age))

a,b=2,45
print("{1},{0}".format(a,b))
print("value of a is {} and value of b is {}".format(a,b))

#f-string notation --> python 3.9+ versions
print(f'{name} is in {branch}')
#make sure to denote the variables only in curly braces
print(f'value of a is {a} and b is {b}')
print(f'"codegnan is in {branch} and of {age} years in trainings"')







