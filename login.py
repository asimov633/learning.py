def __main__():
    user1="jasonraid"
    password1="jason1997"

    user2="johncaila"
    password2="john1999"

    user3="emywilles"
    password3="emy1998"
    while True:
        print("""
        -----------Login-----------
              """)
        username=input("Username: ")
        password=input("Password: ")
    
        if username==user1:
            if password==password1:
                print("Welcome,{}".format(user1))
                print("Do you want change your password? (yes or not)")
                answer=input("Answer: ")
                
                if answer.lower()=="yes":
                    newpassword1=input("New Password: ")
                    newpassword_1=input("New Password Again:")
                    
                    if newpassword1==newpassword_1:
                        password1=newpassword1
                        print("Your Password was change")
                    else:
                        print("Your Entry Second Password Not Like First Password")
                        continue
                elif answer.lower()=="not":
                    print("Try Again Login")
                    continue
                
                else:
                    print("You Can Entry Only (yes or not)")
                    continue
            
            else:
                print("Your Entry Login is fault!")
            
        elif username==user2:
            if password==password2:
                print("Welcome,{}".format(user2))
                print("Do you want change your password? (yes or not)")
                answer=input("Answer: ")
                
                if answer.lower()=="yes":
                    newpassword2=input("New Password: ")
                    newpassword_2=input("New Password Again: ")
                    
                    if newpassword2==newpassword_2:
                        password2=newpassword2
                        print("Your Password was change")
                    else:
                        print("Your Entry Second Password Not Like First Password")
                        continue
                elif answer.lower()=="not":
                    print("Try Again Login")
                    continue
                else:
                    print("You Can Entry Only (yes or not)")
                    continue
            else:
                print("Your Entry Login is fault!")
                    
            
        elif username==user3:
            if password==password3:
                print("Welcome,{}".format(user3))
                print("Do you want change your password? (yes or not)")
                answer=input("Answer: ")
                
                if answer.lower()=="yes":
                    newpassword3=input("New Password: ")
                    newpassword_3=input("New Password Again: ")
                    
                    if newpassword3==newpassword_3:
                        password3=newpassword3
                        print("Your Password was change")
                    else:
                        print("Your Entry Second Password Not Like First Password")
                        continue
                elif answer.lower()=="not":
                    print("Try Again Login")
                    continue
                else:
                    print("You Can Entry Only (yes or not)")
                    continue
                    
            else:
                print("Your Entry Login is fault!")
            
        else:
            print("Please Enter Username")
        
            
            
__main__()         
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    