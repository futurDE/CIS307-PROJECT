import admin  # Importing the admin module to handle admin operations
import user   # Importing the user module to handle user operations

# Shared list to store books, accessible by both admin and user
books = []

# Main function to control the authentication flow
def main():
    while True:  # Infinite loop to keep the program running until explicitly exited
        # Display menu for selecting Admin or User
        print("\nClick 'A' for Admin and 'U' for User:")
        role = input("Enter your choice (A/U): ").strip().upper()  # Get user input and standardize to uppercase

        if role == "A":  # If user selects Admin
            # Prompt for admin password
            password = input("Enter admin password (123): ").strip()
            if password == "123":  # Check if the password is correct
                print("\nAccess Granted. Welcome, Admin!")
                admin.main(books)  # Call the admin module's main function and pass the shared book list
            else:
                print("Incorrect password. Try again.")  # Display error for incorrect password

        elif role == "U":  # If user selects User
            print("\nAccess Granted. Welcome, User!")
            user.main(books)  # Call the user module's main function and pass the shared book list

        else:  # If an invalid input is entered
            print("Invalid choice! Please enter 'A' for Admin or 'U' for User.")

# Entry point of the script
if __name__ == "__main__":
    main()  # Start the authentication process
