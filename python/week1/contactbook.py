while True:
    print('''
    1) Add contact
    2) View contacts
    3) Search contact
    4) Delete contact
    5) Exit...''')

    choice = int(input("Enter your choice: "))

    if(choice == 5):
        print("Goodbye!")
        break

    elif(choice == 1):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        
        duplicate = False

        with open("contactbook.txt","r") as f:
            for line in f:
                exname,exphone,_ = line.strip().split(',')
                if(name.lower() == exname.lower() or phone.lower == exphone.lower()):
                    duplicate = True
                    break
        if(duplicate):
            print("Contact with same name or phone number already exists.")
        else:
            with open("contactbook.txt", 'a') as f:
                f.write(f"{name},{phone},{email}\n")
            print("Contact added successfully.")

    elif(choice == 2):
        with open("contactbook.txt", "r") as f:
            for line in f:
                print(line.strip())
    
    elif(choice == 3):
        found = False
        search_term = input("Enter name to search: ").lower()

        with open("contactbook.txt","r") as f:
            for line in f:
                name, phone, email = line.strip().split(',')
                if(search_term in name.lower()):
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
        
        if(found == False):
            print("No match found")
    
    elif(choice == 4):
        delete_name = input("Enter name to delete: ").lower()
        found = False

        with open("contactbook.txt", "r") as f:
            lines = f.readlines()

        with open("contactbook.txt", "w") as f:
            for line in lines:
                name, phone, email = line.strip().split(',')
                if name.lower() != delete_name:
                    f.write(f"{name},{phone},{email}\n")
                else:
                    found = True

        if found:
            print(f"Contact '{delete_name}' deleted successfully.")
        else:
            print("No contact found with that name.")

    else:
        print("Invalid choice.....")
