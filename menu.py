def display_menu():
    print("Library Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Lend a book")
    print("5. Return a book")
    print("6. View lent books")
    print("7. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")