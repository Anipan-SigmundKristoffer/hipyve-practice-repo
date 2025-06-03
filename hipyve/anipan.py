import os

def buffer():
   os.system('cls')

def anipan_menu():
    print("Hello! My name is Sigmund Kristoffer S. Anipan.")

    while True:
        print("\nPlease choose an option:")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            buffer()

            print("Basic Information")
            print("\n1. I am a second year college student.")
            print("2. I am 20 years old")
            print("3. I live in Ibayo-Tipas, Taguig City. ")
        elif choice == '2':
            buffer()

            print("Goals")
            print("\n1. To be successful in the future.")
            print("2. Learn a lot of paying skills.")
        elif choice == '3':
            buffer()

            print("\nGoodbye! Thank you for visiting.")
            break
        else:
            print("\nInvalid input. Please try again.")
