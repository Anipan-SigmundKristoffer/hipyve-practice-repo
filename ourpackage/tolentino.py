def show_basic_info():
    print("\nAge: 20 years old.")
    print("Gender: Female.")
    print("School: PUP - Taguig.\n")
    input("Press Enter to return to the menu...")

def show_quotes():
    print("\n“Keep your face always toward the sunshine—and shadows will fall behind you.” – Walt Whitman")
    print("\n“The best preparation for tomorrow is doing your best today.” – H. Jackson Brown")
    print("\n“Opportunities don't happen, you create them.” – Chris Grosser\n")
    input("Press Enter to return to the menu...")

def exit_program():
    clear()
    print("Thank you for using my menu! Exiting...")

def tolentino_menu():
    while True:
        clear()
        print("==========================================")
        print("  Good Day! I'm Ma. Rose L. Tolentino. ")
        print("==========================================\n")
        print("1. Basic Info")
        print("2. Motivational Quotes")
        print("3. Exit\n")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            input("Press Enter to continue...")
            continue

        match user_choice:
            case 1:
                show_basic_info()
            case 2:
                show_quotes()
            case 3:
                exit_program()
                break
            case _:
                print("\nInvalid input! Please try again.\n")
                input("Press Enter to continue...")

tolentino_menu()