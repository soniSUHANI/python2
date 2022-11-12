print("Welcome! to State Bank Of India")
restart= ('y')
balance = 328
chances = 3
while chances >= 0:
    pin = int(input("Enter the 4 digit pin here: "))
    if pin == "1234":
        print("you entered your pin correctly\n")
        while restart not in ('n','no','NO','N'):
            print("please press 1 for your balance\n")
            print("please press 2 to withdrawl money\n")
            print("please press 3 to pay in\n")
            print("please press 4 to return card\n")
            option = int(input("what would you like to chose?"))
            if option == 1:
                print("your balance is $",balance,'\n')
                restart = input('would you like to go back?')
                if restart in ('n','N','no','No'):
                    print("Thank you")
                    break
            elif option == 2:
                option = ('y')
                withdrawl = float(input("how much you would like to withdraw \n $10/$20/$40/$60/$80/$100"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance = balance-withdrawl
                    print('\n your balance is now $',balance)
                    restart = input('would you like to go back?')
                    if restart in ('n','N','No','no'):
                        print("Thank you")
                        break
                elif withdrawl!= ['10','20','40','60','80','100']:
                    print('Invalid amount , Please try again\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please entered the required amount:'))
            elif option == 3:
                pay_in= float(input('How much you want to pay in?'))
                balance = balance + pay_in
                print('/n your balance is now $',balance)
                restart = input("would you like to go back? ")
                if restart in ['n','N','no','No']:
                    print("Thank you")
                    break
            elif option == 4:
                print('please wait while your card is returned...\n')
                print('thank you for your service')
                break
            else:
                print('please enter a corrrect number\n')
                restart = ('y')
else:
    if pin != "1234":
        print("incorrect password")            
        chances = chances -1
    if chances == 0:
        print("\n no more tries")
        break

