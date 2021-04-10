print ("Welcome to ASDF Bank. ")
what = input("What would you like to do: Login (1) or Sign Up (2)? ")

if what == "1":
    username = input("Username: ")
    password = input("Password: ")

elif what == "2":
    new_username = input("Please create a username for this account: ")
    new_password = input("Please create a password for this account: ")
    print("Your new account has been created. ")

else:
    print("Please enter a valid input. ")

