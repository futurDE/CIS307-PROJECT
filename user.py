import authentication

# Collect user password
user_password = authentication.collectPasswordForRole()

if user_password == 321:
    print("Access granted! Welcome, User.")

    # List to track books the user has borrowed
    borrowed_books = []

    # Function to display available books from the library file
    def display_available_books():
        try:
            with open("book_library.txt", "r") as file:
                books = file.readlines()
                books = [book.strip() for book in books]  # Remove trailing newlines
                return books
        except FileNotFoundError:
            print("Library file not found!")
            return []

    # Function to borrow books
    def borrow_books():
        available_books = display_available_books()

        if not available_books:
            print("No books are available to borrow.")
            return

        print("Available books to borrow:")
        for book in available_books:
            print(f"- {book}")

        book_name = input("Enter the name of the book to borrow (or type 'exit' to return to the menu): ").strip()
        if book_name.lower() == "exit":
            return
        elif book_name in available_books:
            borrowed_books.append(book_name)
            available_books.remove(book_name)

            # Update the library file
            with open("book_library.txt", "w") as file:
                for book in available_books:
                    file.write(f"{book}\n")

            print(f"You have successfully borrowed '{book_name}'.")
        else:
            print(f"'{book_name}' is not available to borrow.")

    # Function to return books
    def return_books():
        if not borrowed_books:
            print("You haven't borrowed any books yet.")
            return

        print("Books you have borrowed:")
        for book in borrowed_books:
            print(f"- {book}")

        book_name = input("Enter the name of the book to return (or type 'exit' to return to the menu): ").strip()
        if book_name.lower() == "exit":
            return
        elif book_name in borrowed_books:
            borrowed_books.remove(book_name)

            # Add the returned book back to the library file
            with open("book_library.txt", "a") as file:
                file.write(f"{book_name}\n")

            print(f"You have successfully returned '{book_name}'.")
        else:
            print(f"You haven't borrowed '{book_name}'.")

    # User menu loop
    while True:
        print("\nUser Menu:")
        print("1. Borrow Books")
        print("2. Return Books")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ").strip()

        if choice == "1":
            borrow_books()
        elif choice == "2":
            return_books()
        elif choice == "3":
            print("Exiting user menu. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
else:
    print("Access denied! Invalid password.")
