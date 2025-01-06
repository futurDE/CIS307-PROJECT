import authentication

admin_password = authentication.collectPasswordForRole()

if admin_password == 123:
    menu_option_selected = None
    book_name_bool = True
    show_admin_books = []  # List to store the current books
    
    def selectOption():
        global menu_option_selected
        valid_options = ['add books', 'update books', 'delete books']
        while True:  # Keep looping until a valid option is selected
            menu_option_selected = input("Add Books\nUpdate Books\nDelete Books\n")
            if menu_option_selected.lower() in valid_options:
                return menu_option_selected
            else:
                print("Invalid option! Please enter 'Add Books', 'Update Books', or 'Delete Books'.")

    # Main loop to allow the user to repeatedly select options
    while True:
        selectOption()

        if menu_option_selected.lower() == "add books":
            while book_name_bool:
                book_name = input("Input book name (type 'exit' to exit): ")
                if book_name == "exit":
                    book_name_bool = False
                    break
                else:
                    with open("book_library.txt", "a") as f:
                        f.write(f"{book_name}\n")
                    # Update show_admin_books after adding a book
                    show_admin_books.append(book_name)
                    print("Book added successfully!")
            book_name_bool = True  # Reset the book_name_bool for the next operation

        elif menu_option_selected.lower() == "update books":
            while book_name_bool:
                print("Current books:", show_admin_books)  # Display current books
                book_name = input("Input book name to update (type 'exit' to exit): ")
                if book_name == "exit":
                    book_name_bool = False
                    break
                else:
                    book_found = False
                    for i, book in enumerate(show_admin_books):
                        if book == book_name:
                            new_name = input("Enter the new book name: ")
                            show_admin_books[i] = new_name  # Update the book in the list
                            book_found = True
                            break
                    
                    if book_found:
                        # Re-write updated books to the file
                        with open("book_library.txt", "w") as f:
                            for book in show_admin_books:
                                f.write(f"{book}\n")
                        print("Book updated successfully!")
                    else:
                        print("Book not found in the library.")
            book_name_bool = True  # Reset the book_name_bool for the next operation

        elif menu_option_selected.lower() == "delete books":
            while book_name_bool:
                print("Current books:", show_admin_books)  # Display current books
                book_name = input("Input book name to delete (type 'exit' to exit): ")
                if book_name == "exit":
                    book_name_bool = False
                    break
                else:
                    if book_name in show_admin_books:
                        show_admin_books.remove(book_name)  # Remove book from the list
                        # Re-write updated books to the file
                        with open("book_library.txt", "w") as f:
                            for book in show_admin_books:
                                f.write(f"{book}\n")
                        print("Book deleted successfully!")
                    else:
                        print("Book not found in the library.")
            book_name_bool = True  # Reset the book_name_bool for the next operation

else:
    print("Access denied!")
