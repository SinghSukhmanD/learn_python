# functions

def ask_what(phonebook):
    print("Welcome to phonebook.")
    what = input("What would you like to do: (A)dd, (V)iew, (S)earch or (D)elete: ")
    if what == "A":
        add_contact(phonebook)
    elif what == "V":
        display_all(phonebook)
    elif what == "S":
        search(phonebook)
    elif what == "D":
        delete_contact(phonebook)
    else:
        print("Sorry, please enter one of the four options. ")
        return

def search(phonebook):
    print("Search a contact: ")
    fl = input("Please type a few characters of first name: ")
    for x in range(0, 5):
        pbitem = phonebook[x]
        name = pbitem.get('NAME')
        if name.find(fl) != -1:
            print(pbitem.get('NAME'), pbitem.get('LASTNAME'), pbitem.get('MOBILE'))
            return
    print("Sorry that was not found. ")

 
def display_all(phonebook):
    # print("DEBUG: Inside display all function")   
    print("Display all contacts: ")
    for index, item in enumerate(phonebook):
        phoneB = item
        print(index, phoneB.get('NAME'), phoneB.get('LASTNAME'), phoneB.get('MOBILE'))
        

def add_contact(phonebook):
    print("Called: Add contact function ")
    name = input("Please enter first name: ")
    Lname = input("Please enter last name: ")
    contact = input("Please enter contact number: ")
    phoneBookItem = {'NAME': name, 'LASTNAME': Lname, 'MOBILE': contact}
    phonebook.append(phoneBookItem)
    display_all(phonebook)


def delete_contact(phonebook):
    display_all(phonebook)
    wht_to_del = int(input("Enter the index of the contact that you would like to delete: "))    
    phonebook.pop(wht_to_del)
    display_all(phonebook)


# the main program
phonebook = []
phoneBookItem1 = {'NAME': 'Jeff', 'LASTNAME': 'Bizos', 'MOBILE': '0912837645'}
phonebook.append(phoneBookItem1)
phoneBookItem2 = {'NAME': 'Jones', 'LASTNAME': 'Farmerson', 'MOBILE': '7182794781'}
phonebook.append(phoneBookItem2)
phoneBookItem3 = {'NAME': 'Hermione','LASTNAME': 'Grandma', 'MOBILE': '2123866037'}
phonebook.append(phoneBookItem3)
phoneBookItem4 = {'NAME': 'Arthur', 'LASTNAME': 'Pendrigon', 'MOBILE': '1354276808'}
phonebook.append(phoneBookItem4)
phoneBookItem5 = {'NAME': 'Anne', 'LASTNAME': 'Fronk', 'MOBILE': '0293817465'}
phonebook.append(phoneBookItem5)

ask_what(phonebook)
        

