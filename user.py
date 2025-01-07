# Main function for the user module
def main(books):
    # List to keep track of books borrowed by the user
    borrowed_books = []

    while True:  # Infinite loop to keep showing the user menu until the user decides to go back
        # Display the user menu options
        print("\nUser Menu:")
        print("1. View Available Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. View Borrowed Books")
        print("5. Exit User")

        # Prompt the user to select an option
        choice = input("Select an option (1/2/3/4/5): ").strip()

        if choice == "1":  # Option to view available books
            if books:  # Check if there are books available in the library
                print("\nAvailable Books:")
                for i, book in enumerate(books, 1):  # Enumerate to show a numbered list of books
                    print(f"{i}. {book}")
            else:
                print("No books available. Please check with the admin.")  # Notify user if no books exist

        elif choice == "2":  # Option to borrow books
            if books:  # Ensure there are books available to borrow
                print("\nAvailable Books:")
                for i, book in enumerate(books, 1):  # Display a numbered list of books
                    print(f"{i}. {book}")
                try:
                    # Prompt the user to select the book to borrow by its number
                    book_index = int(input("Enter the number of the book to borrow: ")) - 1
                    if 0 <= book_index < len(books):  # Validate the input number
                        borrowed_books.append(books[book_index])  # Add the selected book to borrowed books
                        print(f"You have borrowed the book '{books[book_index]}'.")
                    else:
                        print("Invalid book number.")  # Handle invalid book number
                except ValueError:
                    print("Invalid input. Please enter a number.")  # Handle non-numeric input
            else:
                print("No books available to borrow.")  # Notify user if no books exist

        elif choice == "3":  # Option to return books
            if borrowed_books:  # Check if there are books to return
                print("\nBorrowed Books:")
                for i, book in enumerate(borrowed_books, 1):  # Display a numbered list of borrowed books
                    print(f"{i}. {book}")
                try:
                    # Prompt the user to select the book to return by its number
                    book_index = int(input("Enter the number of the book to return: ")) - 1
                    if 0 <= book_index < len(borrowed_books):  # Validate the input number
                        returned_book = borrowed_books.pop(book_index)  # Remove the selected book from borrowed list
                        print(f"Book '{returned_book}' returned successfully!")
                    else:
                        print("Invalid book number.")  # Handle invalid book number
                except ValueError:
                    print("Invalid input. Please enter a number.")  # Handle non-numeric input
            else:
                print("No borrowed books to return.")  # Notify user if no books have been borrowed

        elif choice == "4":  # Option to view borrowed books
            if borrowed_books:  # Check if there are borrowed books
                print("\nYour Borrowed Books:")
                for i, book in enumerate(borrowed_books, 1):  # Display a numbered list of borrowed books
                    print(f"{i}. {book}")
            else:
                print("You have not borrowed any books.")  # Notify user if no books have been borrowed

        elif choice == "5":  # Option to return to authentication
            print("Returning...")
            break  # Exit the loop to return to authentication

        else:  # Handle invalid menu option
            print("Invalid choice! Please try again.")
