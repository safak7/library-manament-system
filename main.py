from Models.Library import Library

lib = Library()

while True:
    print("*** MENU ***")
    print("1) Add a Book")
    print("2) List All Books")
    print("3) Remove a Book")
    print("4) Quit")

    user_input = input("Welcome to LMS . What is the desired action to be taken? (1-4): ")

    if user_input == "1":
        lib.add_book()
    elif user_input == "2":
        lib.list_all_books()
    elif user_input == "3":
        lib.remove_book() 
    elif user_input == "4":
        print("Good Bye...")
        break
    else:
        print("You entered wrong input. Enter a number between 1 and 4.")