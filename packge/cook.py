# # def start_cook():
# #     print("dishes are ready.")


# name = {
#     "abi": 12,
#     "sakthi": 34,
#     "nisha": 56,
#     "sneha": 67,
#     "anitha": 89
# }

# atm = input("Enter your name: ")
# try:
#     pin = int(input("Enter your pin: "))
    
#     if atm in name:
#         if pin == name[atm]:
#             print("Your name and password are correct.")
            
#             enq = input("Choose your option (a) Balance enquiry / (b) Withdraw: ").lower()
            
#             if enq == "a" or enq == "balance enquiry":
#                 print("Your maximum amount is RS.5000")
                
#             elif enq == "b" or enq == "withdraw":
#                 am = input("Enter your amount details: (c) 500 / (d) 1000 / (e) 2000 / (f) Other amount: ").lower()
                
#                 if am == "c":
#                     print("500 collected. Thank you!")
#                 elif am == "d":
#                     print("1000 collected. Thank you!")
#                 elif am == "e":
#                     print("2000 collected. Thank you!")
#                 elif am == "f":
#                     other = int(input("Enter your amount: "))   
#                     if other <= 5000:
#                         print(f"{other} collected. Thank you!")
#                     else:
#                         print("Your bank limit is RS.5000. Please enter a valid amount.")
#                 else:
#                     print("Invalid choice.")
#             else:
#                 print("Invalid option.")
#         else:
#             print("Your password is incorrect.")
#     else:
#         print("Your name is incorrect.")
# except ValueError:
#     print("Invalid input. Please enter only numbers for PIN and amount.")


name = {
    "abi": 12,
    "sakthi": 34,
    "nisha": 56,
    "sneha": 67,
    "anitha": 89
}


atm = input("enter your name :").strip().lower()  
if atm in name:  
    try:
        pin = int(input("Enter your pin: "))  

        if pin == name[atm]: 
            print("Your name and password are correct")


            enq = input("Choose your option (a) Balance Enquiry / (b) Withdraw: ").strip().lower()

            if enq == "a" or enq == "balance enquiry":
                print("Your maximum amount is RS.5000")

            elif enq == "b" or enq == "withdraw":
                am = input("Enter your amount details: (c) 500 / (d) 1000 / (e) 2000 / (f) Other amount: ").strip().lower()

                if am == "c" or am == "500":
                    print("500 collect your amount, thank you")

                elif am == "d" or am == "1000":
                    print("1000 collect your amount, thank you")

                elif am == "e" or am == "2000":
                    print("2000 collect your amount, thank you")

                elif am == "f" or am == "other amount":
                    other = int(input("Enter your amount: "))

                    if other <= 5000:
                        print(f"{other} collect your amount, thank you")
                    else:
                        print("Your limit bank amount is RS.5000")

                else:
                    print("Invalid option")
            else:
                print("Invalid option")

        else:
            print("Your password is wrong") 

    except ValueError:
        print("Invalid pin number, please enter only numbers")  

else:
 
    print("your name is not define")