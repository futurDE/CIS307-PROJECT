# Main function for the admin module
def main(books):
    while True:  # Infinite loop to keep showing the admin menu until the user decides to go back
        # Display the admin menu options
        print("\nAdmin Menu:")
        print("1. Add Books")
        print("2. View Books")
        print("3. Update Books")
        print("4. Delete Books")
        print("5. Exit Admin")

        # Prompt the admin to select an option
        choice = input("Select an option (1/2/3/4/5): ").strip()

        if choice == "1":  # Option to add books
            # Prompt admin to enter the name of the book to add
            book_name = input("Enter the name of the book to add: ").strip()
            if book_name:  # Ensure the book name is not empty
                books.append(book_name)  # Add the book to the shared book list
                print(f"Book '{book_name}' added successfully!")
            else:
                print("Book name cannot be empty.")  # Handle empty input

        elif choice == "2":  # Option to view books
            if books:  # Check if there are any books in the list
                print("\nCurrent Books:")
                for i, book in enumerate(books, 1):  # Enumerate to show a numbered list
                    print(f"{i}. {book}")
            else:
                print("No books available.")  # Notify admin if no books are available

        elif choice == "3":  # Option to update a book
            if books:  # Ensure there are books to update
                print("\nCurrent Books:")
                for i, book in enumerate(books, 1):  # Display a numbered list of books
                    print(f"{i}. {book}")
                try:
                    # Prompt admin to select the book to update by its number
                    book_index = int(input("Enter the number of the book to update: ")) - 1
                    if 0 <= book_index < len(books):  # Validate the input number
                        new_name = input("Enter the new name for the book: ").strip()
                        if new_name:  # Ensure the new name is not empty
                            books[book_index] = new_name  # Update the book name
                            print("Book updated successfully!")
                        else:
                            print("New book name cannot be empty.")  # Handle empty input
                    else:
                        print("Invalid book number.")  # Handle invalid book number
                except ValueError:
                    print("Invalid input. Please enter a number.")  # Handle non-numeric input
            else:
                print("No books available to update.")  # Notify admin if no books exist

        elif choice == "4":  # Option to delete a book
            if books:  # Ensure there are books to delete
                print("\nCurrent Books:")
                for i, book in enumerate(books, 1):  # Display a numbered list of books
                    print(f"{i}. {book}")
                try:
                    # Prompt admin to select the book to delete by its number
                    book_index = int(input("Enter the number of the book to delete: ")) - 1
                    if 0 <= book_index < len(books):  # Validate the input number
                        removed_book = books.pop(book_index)  # Remove the selected book
                        print(f"Book '{removed_book}' deleted successfully!")
                    else:
                        print("Invalid book number.")  # Handle invalid book number
                except ValueError:
                    print("Invalid input. Please enter a number.")  # Handle non-numeric input
            else:
                print("No books available to delete.")  # Notify admin if no books exist

        elif choice == "5":  # Option to return to authentication
            print("Returning...")
            break  # Exit the loop to return to authentication

        else:  # Handle invalid menu option
            print("Invalid choice! Please try again.")
