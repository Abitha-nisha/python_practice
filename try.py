# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def read_data_from_file(file_path):
#     data = {}
#     with open(file_path, 'r') as file:
#         for line in file:
#             key, value = line.strip().split(':')
#             data[key] = value
#     return data
# data = read_data_from_file('/home/abii/Documents/login_test/jii.txt')

# email = data['email']
# password = data['password']

# driver=webdriver.Chrome()
# driver.get("https://dash.sagasoft.io/sagasuite/signin")
# driver.maximize_window()

# Login_email=WebDriverWait(driver,30).until(
#     EC.presence_of_element_located((By.XPATH,"//*[@id='email']"))

# )
# Login_email.send_keys(email)

# Login_password=WebDriverWait(driver,30).until(
#     EC.presence_of_element_located((By.XPATH,"//*[@id='password']"))
# )
# Login_password.send_keys(password)
# time.sleep(2)
# driver.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import mysql.connector

# def fetch_data_from_mysql():
   
#     db_config = {
#         'host': 'sagasoft',       
#         'user': 'root',   
#         'password': 'Abii@321', 
#         'database': 'abitha'  
#     }

#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor()

#     query = "SELECT username, password FROM automation LIMIT 1"  
#     cursor.execute(query)

#     result = cursor.fetchone()
#     cursor.close()
#     connection.close()

#     if result:
#         return {'username': result[0], 'password': result[1]}
#     else:
#         raise Exception("No data found in the database.")

# data = fetch_data_from_mysql()
# email = data['username']
# password = data['password']

# driver = webdriver.Chrome()
# driver.get("https://dash.sagasoft.io/sagasuite/signin")
# driver.maximize_window()


# Login_email = WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
# )
# Login_email.send_keys(email)

# Login_password = WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='password']"))
# )
# Login_password.send_keys(password)

# Login_password.send_keys(Keys.RETURN)  

# time.sleep(5)  

# # driver.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import mysql.connector



# def fetch_data():
#     db_connection = {
#         'host': 'sagasoft',
#         'user': 'root',
#         'password': 'Abii@321',
#         'database': 'abitha'
#     }
#     conn = mysql.connector.connect(**db_connection)
#     cur = conn.cursor()
#     data = "SELECT username, password FROM automation"
#     cur.execute(data)
#     results = cur.fetchall()  
#     print(results)
#     cur.close()
#     conn.close()
    
#     if results:
#         data = []
#         for result in results:
#             user_name = result[0]
#             password = result[1]
#             data.append({'username': user_name, 'password': password})
#         return data
#     else:
#         raise Exception("No data found in the database")

# database = fetch_data()


# for user in database:
#     email = user['username'] 
#     passw = user['password']
    
#     driver = webdriver.Chrome()
#     driver.get("https://dash.sagasoft.io/sagasuite/signin")
#     driver.maximize_window()

#     login_email = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
#     )
#     login_email.send_keys(email)
#     login_password = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='password']"))
#     )
#     login_password.send_keys(passw)
  
#     time.sleep(5)
#     driver.quit()


# def add_num(a,b):
#     return a*b
# print(add_num(4,5))

# def moky(c,d):
#     reult=c+d
#     print(reult)
# num1=int(input("enter 1 number:"))
# num2=int(input("enter 2 number:"))
# moky(num1,num2)

# def calcu(x,y):
#     addition=x+y
#     subctration=x-y
#     multi=x*y
#     division=x/y
#     return addition,subctration,multi,division
# cde=calcu(7,7)
# print(cde)

# def add():
#     print("Add:")
#     a=int(input())
#     b=int(input())
#     print(a+b)
# def sub():
#     print("Sub:")
#     a=int(input())
#     b=int(input())
#     print(a-b)
# def mul():
#     print("Mul:")
#     a=int(input())
#     b=int(input())
#     print(a*b)
# def div():
#     print("Div:")
#     a=int(input())
#     b=int(input())
#     print(a/b)
# add()
# sub()
# mul()
# div()

# def mess(lkg):
#     print("Message:",lkg)
# mess("Recieved the message")

# def evenodd():
#     num=int(input())
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# evenodd()

# def mail(b):
#     # print(b)
#     if b%2==0:
#         print("even")
#     else:
#         print("odd")
# a=int(input())
# mail(a)

# def mark(c):
#     if c>=35:
#         print("pass")
#     else:
#         print("fail")
# a=int(input("Enter a mark:"))
# mark(a)

# def mess(x1,x2):
#     for i in range(x1,x2):
#         print(i)
# a=int(input("enter 1 num:"))
# b=int(input("enter 2 num:"))
# mess(a,b)

# def abcd():
#     return "tell me"
# print(abcd())

# def valueofa():
#     return 20
# vsc=valueofa()
# print(vsc)

# u_name="abii"
# p_word=123
# a=input("enter the usrname:")
# b=int(input("enter the password:"))
# def validation():
#     if u_name==a and p_word==b:
#         return True
#     else: 
#         return False      
# n=validation()
# print(n)

# def add(c1,c2):
#     return c1+c2
# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# v=add(a,b)  
# print(v)
# mul=v*c
# print(mul)

# def add():
#     a=int(input())
#     b=int(input())
#     return a+b
# print(add())

# def con(c,d):
#     return(c+d)
# a=int(input())
# b=int(input())
# print(con(a,b))

# def add(a,b=2):
#     return a+b
# print(add(4,7))

# def addEM(x,y,z):
#     print(x+y+z)
# x,y,z=1,2,3
# print(addEM(x,y,z),end='')

# def name():
#     nam=input("enter your nam:")
#     print("good morning",nam)
# name()

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# a=int(input("Enter 1 num:"))
# b=int(input("Enter 2 num:"))
# sum=add(a,b)
# sum1=sub(a,b)
# sum2=mul(a,b)
# sum3=div(a,b)
# print(sum,sum1,sum2,sum3)

# def my_function():
#     test_no=4
#     print("Hello",test_no)
# my_function()

# def crake(f_name,l_name):
#     print (f'Hii {f_name} {l_name}')
#     print("welcome")
#     print("How are you")
# crake("Sakthi","Nisha")
# crake("Veera","Kasi")
# crake("Saritha","Abii")

# def mul(a,b=1):
#     return a-b
# print(mul(9))

# def my_fun(name):
#     print(name ,"response")
# my_fun("abi")
# my_fun("sakthi")
# my_fun("nisha")

# def fav_food(firs,last="dosa"):
#     print(firs + " " + last)
# fav_food("biriyani")

# def my_func(*kids):
#     print("The younge name:" + kids[2])
# my_func("Abii","Sakthi","Nisha")

# def my_fun(child1,child2,child3):
#     print("the first child name:",child1)
# my_fun(child1="abii",child2="sakthi",child3="veera")

# def my_name(**kids):
#     print("my name is:",kids["fname"])
# my_name(fname="abitha",lsname="abithakasi")

# def mycon(country="India"):
#     print("I am from:"+country)
# mycon("brazil")
# mycon()
# mycon("sweden")
# mycon("china")

# def my_func(fruits):
#     for i in fruits:
#         print(i)
# my_func(["apple","orange","pineapple","mango"])

# def used(a):
#     return 5 * a
# print(used(3))
# print(used(5))
# print(used(9))

# def myfun(x,/):
#     print(x)
# myfun(3)

# def myfun(a):
#     print(a)
# myfun(a=7)

# def increment(num,by,a=3):
#     return num+by+a
# print(increment(4,by=5))

# def multi(*numbers):
#     total=1
#     for num in numbers:
#         total*=num
#     return total
# print(multi(2,3,4,5))

# def myfun(*child):
#     mob=2
#     for i in child:
#         mob+=i
#     return mob
# print(myfun(3,4,5,6))

# def keyvalue(**dcba):
#     print(dcba['age'])
# keyvalue(id=1,name='abitha',age=21)

# def nam(pinky):
#     for i in pinky:
#         print(i)
# na=['abi','sakthi','nisha']
# nam(na)


# def fizz_buzz(input):
#     if input %3==0 and input %5==0:
#         return "fizzbuzz"
#     if input %3==0:
#         return "fizz"
#     if input%5==0:
#         return "buzz"
#     return input
# print(fizz_buzz(15))

# def my_fun(a,b,/,*,c=7,d):
#     print(a+b+c+d)
# my_fun(5,6,d=8).

# def my_fun(k):
#     if (k > 0 ):
#       result = k + my_fun(k-1)
#       print(result)
#     else:
#      result=0
#     return result
# print("recursion example:")
# my_fun(6)


# li = ["geeks", "for", "geeks"]
# for i in li:
#     print(i)
    
# tup = ("geeks", "for", "geeks")
# for i in tup:
#     print(i)
    
# s = "Geeks"
# for i in s:
#     print(i)
    
# d = dict({'x':123, 'y':354})
# for i in d:
#     print("%s  %d" % (i, d[i]))
    
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i)

# d={'apple':23,'banana':10,'cherry':30}
# for i in d:
#   print(i,d[i])

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(i * j,end="\t")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print(i *j,end='\t')
#     print()

# for i in range(4):
#     for j in range(3):
#         print(i,j)

# li=["apple","banana",'cherry']
# for i in li:
#     print(i)

# tu=("nisha","sakthi","veera")
# for x in tu:
#     print(x)

# dict={'name':"abi",'age':21,'city':"vpm"}
# for n in dict:
#     print(n,dict[n])

# set={"saritha",1,2,3,"kasi"}
# for s in set:
#     print(s)

# v="Hemanthkumar"
# for j in v:
#     print(j)

# for x in "abithasakthinisha":
#     if x=='i'or x=='a':
#         continue
#     print("Current letter:",x)


# for i in "abithasakthi":
#     if i=='b' or i=='t':
#         break
#     print("current letter:",i)

# for x in 'nishaveera':
#     pass
# print(x)

# def add(num1:int,num2:int):a
#     ab=num1+num2
#     return ab
# num1,num2=(10,5)
# ans=add(num1,num2)
# print(f"the addition {num1} add {num2} the values {ans}")


# def myfun(x,y=10):
#     print("x:",x)
#     print("y:",y)
# myfun(13)

# def student(firstname,lastname):
#     print(firstname,lastname)
# student(firstname="abitha",lastname="nisha")

# def nameee(name,age):
#     print("Hi, My name is :",name)
#     print("My age is:",age)
# print("Case -1:")
# nameee("abitha",21)
# print("Case -2:")
# nameee("sakthi",19)

# def house(*gar):
#     for j in gar:
#       print(j)
# house('hello','welcome','to', 'my','home')

# def mycode(**kwargs):
#     for key,value in kwargs.items():
#         print("%s:%s" %(key,value))
# mycode(name='abitha',age=21,city='vpm')

# a=("apple is my  fruits and how many fruit")
# b=a.count("fruit")
# print(b)

# a="abitha"
# b=a.center(20,"o")
# print(b)

# a="abitha@gmail.com"
# print(a[0:-10])
# print(a[-10])
# print(a[7:-4])
# print(a[-4:])

# a=3
# b=2
# c=a+b
# print(c,a-b,a*b)

# a=["abitha","sakthi","nisha"]
# a[1:-1]="veera","saritha"
# print(a)

# a=["apple","orange","banana"]
# a.insert(2,"cheery")
# print(a)

# a=[]
# a.append("nisha")
# a.append("sakthi")
# print(a)

# var=["apple","orange","pineapple"]
# var.insert(1,"cherry")
# print(var)

# var=["apple","orange","pineapple"]
# var1=["cherry","mango","banana"]
# var.extend(var1)
# print(var)

# var=["apple","orange","pineapple"]
# var1=("cherry","mango","banana")
# var.extend(var1)
# print(var)

# a=["abitha","sakthi","nisha","veera"]
# print(a)
# a.pop()
# print(a)

# b=["krishnagir","viluppuram","thirukkovilur"]
# del b[0]
# print(b)

# a=["abitha","anitha","sakthi","nisha"]
# a.clear()
# print(a)

# d=["abitha","sakthi","nisha"]
# for i in range(len(d)):
#     print(d[i])

# d=["abitha","sakthi","nisha"]
# i=0
# while i < len(d):
#     print(d[i])
#     i=i+1

# b=["krishnagir","viluppuram","thirukkovilur"]
# [print(x) for x in b]

# a=["abitha","sakthi","nisha","veera","ksi","saritha"]
# b=[]
# for x in a:
#     if "v" in x:
#         b.append(x)
#         print(b)

# b=["banana","apple","kiwi","cherry","mango","abi"]
# new=[]
# for i in b:
#     if "k" in i:
#         new.append(i)
#         print(new)

# lis=["anitha","kaviya","sneha","suji","picky"]l
# a=[]
# for x in lis:
#     if "i" in x:
#         a.append(x)
# print(a)

# a=["anitha","kaviya","sneha","suji","picky"]
# for i in range(len(a)):
#     print(a[i])

# b=["banana","apple","kiwi","cherry","mango","abi"]
# i=0
# while i < len(b):
#     print(b[i])
# #     i=i+1

# g=["K","S","A","S","V","N"]
# [print(i) for i in g]

# lis=["kasi","saritha","nisha"]
# new=[x for x in lis if "i" in x]
# print(new)

# def factorial(a):
#     if a==0:
#         return 1
#     else:
#         return a * factorial(a-1)    
# print(factorial(4))

# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x * fact(x-1)
# print(fact(3))


# def par(q):
#     """my name is abi"""
#     return q**2
# print(par(2))
# print(par(5))

# def myfu(a):
#     a[0]=10
# lis=[11,20,30,40,50]
# myfu(lis)
# print(lis)

# def value(n):
#     n[4]=8
# m=[1,4,6,8,9,4,9]
# value(m)
# print(m)

# lid=["sniths","abitha","santhiya","sankar"]
# new=[c for c in lid if "s" in c]
# print(new)

# li=["apple","banana","cherry","kiwi"]
# ne=[i for i in li if i !="apple"]
# print(ne)


# def myf(a):
#     a=10
# a=20
# myf(a)
# print(a)

# def add(num:int,num1:int):
#     num2= num+num1
#     return num2
# num,num1=5,8
# an=add(num,num1)  
# print(f"the addion key {num} and {num1} values is {an}")


# def mul(num1:int,num2:int):
#     num3=num1*num2
#     return num3
# num1,num2=4,5
# value=mul(num1,num2)
# print(f"the multiplication num is {num1} and num2 {num2} the values is {value}")

# li=["apple","banana","cherry","kiwi"]
# new=[i.upper() for i in li]
# print(new)

# li=[i for i in range(10) if i < 5]
# print(li)

# num=["abitha","anitha","chithra","nisha"]
# l=[]
# for i in num:
#     if "c" in i:
#         l.append(i)
#         print(l)

# a=[h for h in range(10) if h < 5]
# print(a)

# c=["abitha","anitha","chithra","nisha"]
# m=[x for x in c if x  !="abitha"]
# print(m)

# new=["apple","orange","kiwi","banana"]
# l=[c for c in new]
# print(new)

# lis=["apple","orange","kiwi","banana"]
# n=["apple" for x in lis]
# print(n)

# lis=["apple","orange","kiwi","banana"]
# x=[c if c !="apple" else "nisha" for c in lis]
# print(x)

# b=["banana","apple","kiwi","cherry","mango","orange","abi"]
# b.sort()
# print(b)

# c=[1000,490,7,200,90,390]
# c.sort()
# print(c)

# f=["banana","apple","kiwi","cherry","mango","abi"]
# f.sort(reverse=True)
# print(f)

# c=[1000,39090,7,200,90,390]
# c.sort(reverse=True)
# print(c)

# def myfunction(n):
#     return abs (n-200)
# list=[4,1000,56,601,100,240,]
# list.sort(key=myfunction)
# print(list)

# f=["banana","apple","kiwi","cherry","mango","abi"]
# g=f.copy()
# print(g)

# f=["banana","apple","kiwi","cherry","mango","abi"]
# g=[1,2,5,4,7,9]
# for i in g:
#     f.append(i)
# print(f)

# f=["banana","apple","kiwi","cherry","mango","abi"]
# g=[1,2,5,4,7,9] 
# f.extend(g)
# print(f)

# a=["apple","orange","banana","kiwi","apple"]
# c=a.count("apple")
# print(c)

# b=[7,2,0,7,0,5,7]
# x=b.count(7)
# print(x)

# a="A\tb\ti\tt\th\ta"
# b=a.expandtabs()
# print(b)

# tup=("abitha","nisha","sakthi")
# s=list(tup)
# s[1]="veera"
# tup=tuple(s)
# print(tup)

# a=("apple","banana","kiwi","cherry")
# b=list(a)
# b[3]="orange"
# a=tuple(b)
# print(a)

# a=("apple","banana","kiwi","cherry")
# c=list(a)
# c.append("pineaaple")
# a=tuple(c)
# print(a)

# d=("apple","banana","kiwi","cherry")
# e=("jackfruit",)
# d+=e
# print(d)
# 
# a=("apple","banana","kiwi","cherry")
# b=list(a)
# b.remove("apple")
# a=tuple(b)
# print(b)

# b=("apple","banana","cherry")
# green,red,yellow=b
# print(green)
# print(yellow)
# print(red)

# t=("banana","apple","kiwi","strawberry","blueberry","orange")
# red,green, *yellow=t
# print(red)
# print(green)
# print(yellow)


# t=("banana","apple","kiwi","strawberry","blueberry","orange")
# green,*red,yellow=t
# print(green)
# print(red)
# print(yellow)

# t=("banana","apple","kiwi","strawberry","blueberry","orange")
# for i in range(len(t)):
#     print(t[i])

# t=("banana","apple","kiwi","strawberry","blueberry","orange")
# i=0
# while i < len(t):
#     print(t[i])
#     i=i+1

# a=("apple","banana","orange")
# myf=a*3
# print(myf)

# n=20
# i=1
# while i <=n:
#     if i==9:
#         break
#     print(i)
#     i=i+1

# v=lambda a,b:a*b
# print(v(4,2))

# def myfu(a):
#     return lambda c:a *c
# de=myfu(3)
# print(de(5))

# import datetime as dt
# current=dt.datetime.today()
# print(current)

# import math
# print(math.sqrt(6))
# print(math.ceil(1.6665))
# print(math.floor(1.787667))
# print(math.factorial(5))
# print(math.fabs(-5))

# try:
#     a=10/0  
# except Exception as e:
#     print(e)

# try:
#     a=10/25
# except Exception as e:
#     print(e)
# else:
#     print("value:",a)

# try:
#     a=10/25
# except Exception as e:
#     print(e)
# else:
#     print("value:",a)
# finally:
#     print("thank you")

# try:
#     print(a)
# except NameError as e:
#     print("a is not defined")
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print("not visisble zero")
# try:
#     a=int("abii")
# except ValueError as e:
#     print("please enter the number")

# try:
#     a=[6,13,24,65,867]
#     print(a[0])
# except IndexError as e:
#     print("invalid syntanx")
# try:
#     f=open("jii.txt")
# except FileNotFoundError as e:
#     print("file not found")
# else:
#     print(f.read())

# class person():
#     name="abitha"
#     age=21
# print(getattr(person,'name'))
# print(getattr(person,"age"))
# print(getattr(person,"gender","no such attrubute error"))

# print(person.name)
# setattr(person,'name','sakthi')
# print(person.name)
# setattr(person,'gender','female')
# print(person.gender)
# person.city="viluppuram"
# print(person.city)
# print(person.__dict__)
# delattr(person,"gender")
# print(person.__dict__)
# del person.city
# print(person.__dict__)

# class goa:
#     name="hjhhj"
#     tour=""
#     def dance(self):
#         print("lets dance")
#     def food(self):
#         print("veraity of food")
# ob=goa()
# am=goa()
# ob.name="abii"
# am.name="sakthi" 
# ob.tour="yes"
# am.tour="enjoy"

# print(ob.name)
# print(ob.tour)
# print(am.name)
# print(am.tour)
# ob.dance()
# am.food()

# class laptop:
#     price=""
#     processor=""
#     ram=""
# hp=laptop()
# dell=laptop()
# hp.price=30000
# hp.processor="i5"
# hp.ram="8GB"
# print(hp.price)
# dell.price=50000
# dell.processor="i7"
# dell.ram="16GB"
# print(dell.price)

# class laptop:
#     def __init__(self):
#         self.price=""
#         self.processor=""
#     def display(self):
#         print("price:",self.price)
#         print("processor:",self.processor)
# hp=laptop()
# dell=laptop()
# hp.price=35000
# hp.processor="i5"
# dell.price=60000
# dell.processor="i7"
# hp.display()
# dell.display()

# class student:
#     def __init__(self):
#         self.name="fgfdf"
#         self.regno=7787
#     def display(self):
#         print("name:",self.name)
#         print("regno:",self.regno)
# ob1=student()
# ob1.display()        

# class calculate:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return(a-b)
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         if b ==0:
#             return "zero division error"
#         return a/b
# ob=calculate()
# print(ob.add(3,6))
# print(ob.sub(8,3))
# print(ob.mul(3,4))
# print(ob.div(10,0))

# def cook(balance_mavu):
#     if balance_mavu==1:
#         return 1
#     else:
#         total= 1 + cook (balance_mavu-1)
#         return total
# vada=cook(5)
# print(f"take this {vada} vadai") 

# def addition(num):
#     if num==1:
#         return 1
#     else:
#         return num +addition(num -1)
# total=addition(5)
# print(f'the total addition value is {total}')

# Encapsulation
# class car:
#     def door_open(self):
#         print("door opend.")
#         print("start the car.")
#         self._accelerate()
#     def _accelerate(self):
#         print("throttle increased.")
#         self.__engine()

#     def __engine(self):
#         print("brust inside.")
#         print("car is moving.")

# obj=car()
# obj.door_open()

# class foods:
#     def biriyani(self):
#         print("biriyani is my all time favourite.")
#         print("1st food.")
#         self._ice()
#     def _ice(self):
#         print("butter scotch ice cream is my favourite.")
#         self.__chocolate()
#     def __chocolate(self):
#         print("kitkat,park,munch is always my favourite chocolate. ")
# eat=foods()
# eat.biriyani()

# class acdtion:
#     def dad(self):
#         print("he is use left hand.")
# class reaction(acdtion):
#     def son(self):
#         print("singing the song")
# ob=reaction()

# import Signup as sign
# a=sign.sub(10,4)
# print(a)

# import Signup as si
# si.start()

# class person():
#     def __init__(self,name,age=21):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return (f'{self.name}({self.age})')
# ob=person("abitha")
# print(ob)

# class student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def func(self):
#         print("my name is " + self.name)
# cass=student("Abii",21)
# cass.func()

# class case:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunc(self):
#         print(self.firstname,self.lastname)
#         # print(f"the first name {self.firstname} and secon name is {self.lastname}")
# t=case("sakthi","nisha")
# t.myfunc()

# class kitt():
#     def __init__(self,fname,lname):
#         self.firname=fname
#         self.lasname=lname
#     def meow(abc):
#         print(abc.firname,abc.lasname)
# class per(kitt):
#     pass
# u=per("nisha","veera")
# u.meow()

# tup=("apple","banana","cherry")
# ite=iter(tup)
# print(next(ite))
# print(next(ite))
# print(next(ite))

# tupl="Abitha"
# it=iter(tupl)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class mynumber():
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         c=self.a
#         self.a +=1
#         return c
# vmn=mynumber()
# my=iter(vmn)
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))

# class kkk:
#     def __init__(self,model,brand):
#         self.modd=model
#         self.bran=brand
#     def move(self):
#         print("super")

# class sss:
#     def __init__(self,model,brand):
#         self.modd=model
#         self.bran=brand
#     def move(self):
#         print("wow")
# class vvv:
#     def __init__(self,model,brand):
#         self.modd=model
#         self.bra=brand
#     def move(self):
#         print("escape")
# abc=kkk("abitha","sakthi")
# das=sss("nisha","veera")
# mas=vvv("kasi","saritha")
# for x in (abc,das,mas):
#     x.move()

# import json
# a='{"name":"anitha","age":21,"dept":"computer "}'
# b=json.loads(a)
# print(b["dept"])

# import json
# n='{"class":"a1","name":"abitha","city":"vilppuram"}'
# m=json.loads(n)
# print(m["class"])


# import json
# a={
#     "name":"nisha",
#     "age":19,
#     "city":"viluppuram"
# }
# n=json.dumps(a)
# print(n)

# file=open("jii.txt","r")
# print(file.read(5))


# file=open("jii.txt","r")
# print(file.read())
# file.close()

# file=open("jii.txt","r")
# print(file.readlines())


# file=open("jii.txt","r")
# for x in file:
#     print(x)


# file=open("jii.txt","r")
# print(file.readline())
# print(file.readline())

# file=open("jii.txt","a")
# file.write("my name is abi")
# file.close()

# file=open("jii.txt","r")
# print(file.read())

# import pandas as pd
# dt=pd.read_csv()
# print(dt.to_string)

# class stud():
#     def __init__(self,fname,lname):
#         self.first=fname
#         self.last=lname
#     def display(self):
#         print(self.first,self.last)
# class per(stud):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
# ob=per("abitha","sakthi")
# ob.display()

# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("you are in class a")
# class b():
#     def __init__(self):
#         super().__init__()
#         print("B")
#     def display(self):
#         print("ypu are in class b")
# class c(b,a):
#     def __init__(self):
#         super().__init__()
#         print("C")
#     def display(self):
#         print("you are in class c")
# obje=c()

# def sub(a,b,c=0):
#     print(a-b-c)
# sub(20,12)
# sub(25,10,5)

# class animal():
#     def sounds(self):
#         print("animal make a sounds")
# class dog(animal):
#     def sounds(self):
#         print("dags barks")
# class bird(animal):
#     def sounds(self):
#         print("")
# o=dog()
# o.sounds()

# import Signup as sign
# sign.start()

# import Signup as si
# print(si.add(4,6))
# print(si.sub(10,5))

# import Signup 
# print(Signup.func("abitha",21))

# import Signup as sign
# print(sign.add(10,3))
# print(sign.sub(8,2))
# print(sign.mul(5,5))
# print(sign.div(6,2))

# from packge import decoration,cook
# decoration.start_decoration()
# cook.start_cook()

# string="*******"
# b=0
# for i in string:
#     b=b+1
#     print(string[0:b])
# for i in string:
#     b=b-1
#     print(string[0:b])

# for i in range(1,6):
#     for j in range(i):
#        print("*",end="")
#     print()

# num=int(input("enter the num:"))
# a=1
# for i in range(1,num+1):
#     for j in range(1,a+1):
#         print("*",end="")
#     a=a+2
#     print()

# for i in range(1,11):
#     print(i,"x2=",i*2)

# rcb=input()
# if rcb=="win":
#     print("cup namde")
# else:
#     print("looser")

# megna="die"
# if megna=="died":
#     print("surya weds priya")
# else:
#     print("megna weds surya")

# income=int(input("incpme:"))
# if income >70000:
#     print("eligibile for loan")
# else:
#     print("not eligible for loan")

# a=int(input())
# if a%3==0 and a%5==0:
#     print("divisible by 3,5")
# else:
#     print("not divisible 3,5")

# a=int(input())
# b=int(input())
# operation=(input("add/sub/mul/div:"))
# if operation=="add":
#     print(a+b)
# elif operation=="sub":
#     print(a-b)
# elif operation=="mul":
#     print(a*b)
# elif operation =="div":
#     print(a/b)
# else:
#     print("invalid operation")

# salary=int(input("enter your salary:"))
# age=int(input("enter your age:"))
# if salary >20000 or age <25:
#     loan=int(input("Loan:"))
#     if loan >50000:
#         print("maximum loan amount is 50000")
#     else:
#         print("your not eligible for loan")

# count=0
# for i in range(1,11):
#     if i%2==0:
#         count=count+1
# print(count)
# atm = input("Insert your ATM card: ")
# try:
#     pin = int(input("Enter your PIN: "))
# except ValueError:
#     print("Invalid PIN. Please enter numbers only.")
#     exit()

# enq = input("Choose your option (balance enquiry/withdraw): ").strip().lower()

# if enq == "balance enquiry":
#     print("Your maximum balance is Rs.5000")
# elif enq == "withdraw":
#     try:
#         am = int(input("Enter the amount to withdraw: "))
#         if 1000 <= am <= 5000 and am % 1000 == 0:
#             print(f"Collect your amount: Rs.{am}")
#             print("Thank you for using our ATM!")
#         else:
#             print("Invalid amount. Please enter multiples of 1000 up to Rs.5000.")
#     except ValueError:
#         print("Invalid input. Please enter a numerical amount.")
# else:
    # print("Invalid option. Please choose 'balance enquiry' or 'withdraw'.")



# e_count=0
# o_count=0
# for i in range(1,11):
#     if i %2==0:
#         e_count=e_count+1
#     else:
#         o_count=o_count+1
# print(e_count)
# print(o_count)

# a=[]
# for i in range(10):
#     num=int(input())
#     a.append(num)
# print(a)

# sum=0
# for i in range(1,6):
#     sum=sum+i
# print(sum)

# a=int(input(""))
# c=0
# for i in range(1,a):
#     if a%i==0:
#         c=c+1
# if c==1:
#     print("print number")
# else:
#     print("not prime number")

# import json
# x={
#     "name":"abitha",
#     "age":21,
#     "city":"viluppuram"
# }
# a=json.dumps(x)
# print(a)

# import json
# print(json.dumps({"name":"abi","city":"viluppuram"}))
# print(json.dumps(["apple","cherry"]))
# print(json.dumps(("abitha","sakthi")))
# print(json.dumps("hello"))
# print(json.dumps(12.3))
# print(json.dumps(43))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# n=int(input())
# coun=0
# for i in range(1,n+1):
#     if n%i==0:
#         coun=coun+1
# if coun==2:
#     print(n,"is prime num")
# else:
#     print(n,"is not prime number")

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

 
# for i in range(1,11):
#     print("2 x",i, "=",i*2)
# for j in range(1,11):
#     print("3 x",j," =",j*3)


# c=0
# while c < 10:
#     # c=c+1                       
#     print(c)
#     c=c+1

# import Signup as sig
# print(sig.func("abitha",21))

# a=0
# while a <3:
#     a=a+1
#     print("abitha")
# else:
#     print("loops is over")

# a=0
# while a==0:
#     print("abi")

# a=["abi","sakthi","nisha"]
# for index in range(len(a)):
#     print(a[index])

# for  i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()


# for h in("abithasakthinisha"):
#     if h=="i" or h=="t":
#         continue
#     print(h)

# for i in range(1,11):
#     if i==7:
#         continue
#     print(i)

# for h in("abithasakthinisha"):
#     if h=="s":
#         break
#     print(h)
# print(h)

# name={
#     "abi":12,
#     "sakthi":32,
#     "nisha":34,
#     "veera":56
# }
# at=input("enter your name:")
# try:
#     pin=int(input("enter your pin num:"))
#     if at in name and at[name]==pin:
#         print("your name and password is correct")
#     else


# except ValueError:
#     print("only enter numbers only")
# name = {
#     "abi": 12,
#     "sakthi": 34,
#     "nisha": 56,
#     "sneha": 67,
#     "anitha": 89
# }

# atm = input("Enter your name: ")

# try:
#     pin = int(input("Enter your PIN: "))
    
#     if atm in name and name[atm] == pin:
#         print("Name and password are correct.")
#     else:
#         print("Incorrect name or password.")
        
# except ValueError:
#     print("Invalid PIN. Please enter only numbers.")

# string_one="i am reading"
# string_two="a new great book!"
# string_three=string_one+string_two
# print( string_three)

# a=input("Hi! What's your name?")
# print("Nice to meet you" + a +"!")
# b=input("How olf str you?")
# print("So,you are already" + str(b) + "years old, " + a +"!")

# from flask import Flask

# a=Flask (__name__)
# @a.route('/')
# def doc():
#     return "Home"
# if __name__ == "__main__":
#     a.run (debug=True)


# import csv
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# users = []  # Store user data in memory

# @app.route('/upload_csv', methods=['POST'])
# def upload_csv():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     try:
#         csv_data = csv.DictReader(file.stream.read().decode("utf-8").splitlines())

#         for row in csv_data:
#             new_id = len(users) + 1  # Auto-increment ID
#             user = {
#                 "id": new_id,
#                 "name": row["abi"],
#                 "role": row["dfh"],
#                 "age": row["56"]
#             }
#             users.append(user)

#         return jsonify({"message": "CSV uploaded successfully", "users": users}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     @app.run(debug=True)

# from flask import Flask     
# app = Flask(__name__) 
  
# @app.route('/')       
# def hello(): 
#     return 'HELLO'
  
# if __name__=='__main__': 
#    app.run(debug=True)


# from flask import Flask 
# app = Flask(__name__) 

# @app.route('/hello/<name>') 
# def hello_name(name): 
#     return 'Hello  GeeksforGeeks%s!' % name 

# if __name__ == '__main__': 
#     app.run(debug = True)

# from flask import Flask 

# app = Flask(__name__) 

# @app.route('/blog/<int:postID>')
# def show_blog(postID): 
#     return 'Blog Number %d' % postID  

# @app.route('/rev/<float:revNo>')
# def revision(revNo): 
#     return 'Revision Number %f' % revNo  

# if __name__ == '__main__': 
#     app.run(debug=True)

# from flask import Flask, redirect, url_for
# app = Flask(__name__)


# @app.route('/admin') 
# def hello_admin(): 
#     return 'Hello Admin'


# @app.route('/guest/<guest>')
# def hello_guest(guest):  
#     return 'Hello %s as Guest' % guest


# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':  
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route('/')
# @app.route('/abc')
# def home():
#     return render_template('abc.html')

# if __name__=="__main__":
#     app.run(debug=True)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome()

# try:
#     # 1. Open Google
#     driver.get("https://www.google.com")
#     driver.maximize_window()

#     # 2. Locate the search input box
#     search_box = driver.find_element(By.NAME, "q")

#     # 3. Enter the search query and press Enter
#     search_box.send_keys("Selenium Python tutorial")
#     search_box.send_keys(Keys.RETURN)

#     # 4. Wait for search results to load
#     time.sleep(3)

#     # 5. Collect and print result titles
#     results = driver.find_elements(By.CSS_SELECTOR, "h3")
#     print("Top Search Results:")
#     for index, result in enumerate(results[:10], start=1):
#         print(f"{index}. {result.text}")

# finally:
#     # 6. Close the browser
#     driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# driver=webdriver.chrome()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Start the browser
# driver = webdriver.Chrome()

# # Open a website
# driver.get("https://www.google.com")

# # Wait for search box to appear
# wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

# # Type and search
# search_box.send_keys("Selenium Python")
# search_box.submit()

# # Wait and close
# wait.until(EC.presence_of_element_located((By.ID, "search")))
# driver.quit()







