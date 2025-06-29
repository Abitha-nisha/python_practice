# Addition (+), Subtraction (-), Multiplication (*), Division (/), and Modulus (%). 

# Addition (+)
# a=int(input("enter your num:"))
# b=int(input("enter your num:"))
# c=a+b
# print(c)

# def add(a,b):
#     return a+b
# print(add(78,8))


# Explanation of ** Operator
# a=5
# b=8
# c=a**b
# print(c)

# a=int(input())
# # b=int(input())
# # c=[]
# for i in range(a):
#     print(i)
  
# a=(input("Insert your ATM card:"))
# b=int(input("please enter your pin:"))
# c="balance enquiry:"
# d="widhthraw:"
# print(c)
# print(d)
# e=input("edhavadhu ondrai select seiyavum:")
# print(e)

name={
    "abi":12,
    "sakthi":34,
    "nisha":56,
    "sneha":67,
    "anitha":89
}
atm=input("enter your name:")
if atm in name:
    try:
    
      pin=int(input("enter your pin:"))
      if pin==name[atm]:
          print("your name and password is correct")
          enq=(input("choose your option((a)balance enquiry/(b)withdraw):"))
          if enq=="a" or enq=="balance enquiry":
              print("your maximum amount is RS.5000")
        
          elif enq=="b" or enq=="withdraw":
        
             am=(input("enter your amount details:(c)500/(d)1000,(e)2000/(f) other amount:"))

             if am=="c" or am==500:
              print("500 collect your amount,thank you")
      
             if am=="d" or am==1000:
              print("1000 collect your amount,thank you")
         
             elif am=="e" or am==3000:
              print("2000 collect your amount,thank you")
         
             elif am=="f" or am=="other amount":
                other=int(input("enter your amount:"))   
                if  other =="f" or other<=5000:
                  print(f"{other} collect your amount, thank you")
                else:
                   print("your limit bank amount is RS.5000")
          else:
              print("invalid option")
      else:
          print("your password is worng")
    
        
    except ValueError:
        print("invalid pin num please enter only num")
else:
       print("your name is not define")

  


# d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}
# if '6' in d.keys():
#     print(True)
# else:
#     print(False)
