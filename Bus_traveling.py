print("----------------------------------------")
print("            MANI BUS TRAVELS            ")
print("----------------------------------------")

def menu():

    print("\nWELCOME TO MANI BUS TRAVELS\n")
    print("\n1. AVAILABLE ROATE LIST\n2. BOOKING TICKETS\n")

    user = int(input("Enter your choice:"))
    
    if user ==1:
        print("-----------------------------------")
        print("             ROTE LIST             ")
        print("-----------------------------------")
        print("1) CHENNAI TO COIMBATORE\n2) CHENNAI TO MADURAI\n3) CHENNAI TO SALEM")

        user_city = int(input("Choice your wanted place:"))

        if user_city == 1:
            print("\nCHENNAI TO COIMBATORE\nPackage Information\n")
            print("This trip start on 5.12.2022\n")
            print("That trip start at 8:30 pm\n")
            print("This trip coverd in some five place, the palce name is (viluppuram, salem, erode)\n")
            print("This route cost is Rs.1000")
        elif user_city == 2:
            print("\nCHENNAI TO MADURAI\nPackage Information\n")
            print("This trip start on 6.12.2022\n")
            print("That trip start at 9:30 pm\n")
            print("This trip coverd in some five place, the palce name is (viluppuram, perambalur, tiruchirappalli)\n")
            print("This route cost is Rs.500")
        elif user_city == 3:
            print("\nCHENNAI TO SALEM\nPackage Information\n")
            print("\nThis trip start on 7.12.2022\n")
            print("That trip start at 7:30 pm\n")
            print("This trip coverd in some five place, the palce name is (viluppuram, chinnasalem, attur)\n")
            print("This route cost is Rs.800")
        else:
            print("** Please give valuable information **")
            ask = input("Do you want to continue(YES/No)").lower()

            if ask == "yes":
                user = int(input("Enter your choice:"))
                main_function(user)
            else:
                print("Thank to come....Have nice journey")
            
        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come....Have nice journey")


    elif user ==2:
        print("-----------------------------------")
        print("          BOOKING TICKETS          ")
        print("-----------------------------------")
        print("CHENNAI TO COIMBATORE\nCHENNAI TO MADURAI\nCHENNAI TO SALEM")

        ticktes=["COIMBATORE","MADURAI","SALEM"]

        coimbatore_amount=1000
        madurai_amount=500
        salem_amount=800

        your_ticktes=input("\nEnter your Destination:").upper()

        if your_ticktes in ticktes:
            print(f"\nyes!...{your_ticktes} ticktes is available")
            how_many=int(input(f"\nhow many {your_ticktes} ticktes you want:"))
            if your_ticktes=="COIMBATORE":
                total=coimbatore_amount*how_many
                if total>=5000:
                    final_total=total-500
                    print(f"\nyour total bill is {total}\n offer 500 so,your final total is {final_total}")
                else:
                    print(f"\nyou orderded {how_many} tickets so,your total bill is {total}")

            elif your_ticktes=="MADURAI":
                total=madurai_amount*how_many
                if total>=3000:
                    final_total=total-300
                    print(f"\nyour total bill is {total}\n offer 300 so,your final total is {final_total}")
                else:
                    print(f"\nyou orderded {how_many} tickets so,your total bill is {total}")

            elif your_ticktes=="SALEM":
                total=salem_amount*how_many
                if total>=4000:
                    final_total=total-400
                    print(f"\nyour total bill is {total}\n offer 200 so,your final total is {final_total}")
                else:
                    print(f"\nyou orderded {how_many} tickets so,your total bill is {total}")

        else:
            print("Choose your right choice")
        
        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come....Have nice journey")

def feedback():    

    print("-----------------------------------")
    print("             Feedback              ")
    print("-----------------------------------")
    
    user_feedback = input("\nEnter your feedback:")
    feedback = []
    feedback.append(feedback)
    if user_feedback:
        print(f"\n Your Feedback is successfully Added.\n")
        print("Comeing again.")
    else:
        print("Please leave your feedback")

    ask = input("\nDo you want to continue(YES/No):").lower()

    if ask == "yes":
        main_function()
    else:
        print("Thank to come....Have nice journey")
        
def login():

    print("\n WELCOME TO MANI BUS TRAVELS\n")
    print("1. SIGN UP\n2. SIGN IN")

    user = int(input("\n Enter your choice:"))

    if user == 1:
        print("\n WELCOME TO SIGNUP PAGE\n")
        print("Please Enter your singup details\n")

        user_name = input("Enter your Name:")
        user_phone_number = int(input("\n Enter your phone number: "))
        user_mail = input("\n Enter your Valuale Mail ID:")
        user_password = int(input("\n Enter your password:"))

        print(f"{user_name}, your are successfully singup \n")
        print(f"CHECK OUT YOUR INFORMATION,\nYour Name is = {user_name},\n Your phone number= {user_phone_number},\n Your mailID = {user_mail}")

        # user_name = []
        # user_phone_number = []
        # user_mail = []
        # user_password = []

        # user_name.append(user_name)
        # user_phone_number.append(user_phone_number)
        # user_mail.append(user_mail)
        # user_password.append(user_password)

    elif user == 2:
        print("\n WELCOME TO SIGNIN PAGE\n")
        print("Please Enter your singin details\n")

        user_name = input("Enter your username/mailid:").upper()
        user_password = input("\nEnter your password:")

        print(f"\n{user_name},You are successfully signin this page.")
        
    ask = input("\nDo you want to continue(YES/No):").lower()

    if ask == "yes":
        main_function()
    else:
        print("Thank to come....Have nice journey")

def main_function():

    print('''1. MENU\n2. FEEDBACK\n3. LOGIN\n''')
    user = int(input("Enter your choice:"))
    if user ==1:
        menu()
    elif user ==2:
        feedback()
    elif user == 3:
        login()
    else:
        print("\n ******* Please choose your right choice *******")

main_function()