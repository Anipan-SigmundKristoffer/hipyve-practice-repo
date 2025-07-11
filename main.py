import os
from hipyve import ocariza

def clear():
    os.system('cls')

while True:
    clear()
    print("==========================================")
    print("          Welcome to HighPyve!         ")
    print("==========================================")
    print("Select a developer module to continue:\n")
    print("  [1] Kristoffer Anipan")
    print("  [2] Ma. Rose Tolentino")
    print("  [3] Mikaela Joy Bartolome")
    print("  [4] Jaira Isabel Ocariza")
    print("  [5] Eurielle Bayos")
    print("  [6] Exit\n")
    
    try:
        user_choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("\nInvalid input! Please enter a number.")
        input("Press Enter to continue...")
        continue
        
    match user_choice:
        case 1:  
            # TODO (ANIPAN): Add Module
            pass
        case 2: 
            # TODO (TOLENTINO): Add Module
            pass
        case 3:  
            # TODO (BARTOLOME): Add Module
            pass
        case 4:  
            ocariza.jaira_main_menu()
            pass
        case 5:  
            # TODO (BAYOS): Add Module
            pass
        case 6:
            clear()
            print("Thank you for using HighPyve Main Menu! Exiting...")
            break
        case _:
            print("\nInvalid choice! Please select a number from 1 to 6.")
            input("\nPress Enter to continue...")