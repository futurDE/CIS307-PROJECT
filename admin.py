import authentication

admin_password = authentication.collectPasswordForRole()

if admin_password == 123:
    menu_option_selected = None
    book_name_bool = True
    def selectOption():
        global menu_option_selected
        valid_options = ['add books', 'update books', 'delete books']
        while True:  # Keep looping until a valid option is selected
            menu_option_selected = input("Add Books\nUpdate Books\nDelete Books\n")
            if menu_option_selected.lower() in valid_options:
                return menu_option_selected
                #break  # Exit the loop when a valid option is selected
            else:
                print("Invalid option! Please enter 'Add Books', 'Update Books', or 'Delete Books'.")

    selectOption()

    if menu_option_selected.lower() == "add books":
        while book_name_bool:
            book_name = input("Input book name (type 'exit' to exit): ")
            f = open("book_library.txt", "a")
            if book_name == "exit":
                book_name_bool = False
                break
            else:
                f.write(f"{book_name}\n")
                f.close()
            

else:
    print("Access denied!")
