''''
Welcome. (Click 'A' for admin and 'U' for user: )
'''

user_role = None
admin_password = None
user_password = None

def getUserRole():
    global user_role
    user_role = input("Click 'A' for Admin and 'U' for User: ")
    if user_role != "A" and user_role != "U":
        print("Invalid input!")
        getUserRole()
    else:
        return user_role

getUserRole()

def collectPasswordForRole():
    global admin_password
    global user_password
    if user_role == "A":
        while True:  # Keep looping until a valid password is entered
            admin_input = input("Enter admin password (123): ")
            if admin_input.isdigit() and int(admin_input) == 123:
                admin_password = int(admin_input)
                return admin_password
            else:
                print("Invalid password! Please enter a valid password")
    else:
        while True:  # Keep looping until a valid password is entered
            user_input = input("Enter user password (321): ")
            if user_input.isdigit() and int(user_input) == 321:
                user_password = int(user_input)
                return user_password
            else:
                print("Invalid password! Please enter a valid password.")

collectPasswordForRole()