from colorama import Fore, Style, init

init(autoreset=True)

def jaira_main_menu():
    while True:
        print(Fore.LIGHTMAGENTA_EX 
              + "\n=== Welcome to Jaira Isabel Ocariza's Menu ===")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Fun Facts")
        print("4 - Anipan Comment")
        print("0. Exit")

        try:
            choice = int(input(Fore.LIGHTYELLOW_EX + "\nEnter your choice: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Please enter a valid number.")
            continue

        print()

        match choice:
            case 1:
                show_basic_info()

            case 2:
                show_goals()

            case 3:
                show_fun_facts()

            case 4: 
                anipan_comments()

            case 5:
                bartolome_comments()
                
            case 0:
                print(Fore.LIGHTYELLOW_EX + "Exiting menu... Goodbye!")
                break

            case _:
                print(Fore.LIGHTRED_EX + "Invalid choice. Please try again.")

def show_basic_info():
    print(Fore.LIGHTMAGENTA_EX + "Basic Information")
    print("Name: Jaira Isabel F. Ocariza")
    print("Age: 19")
    print("Sex: Female")
    print("Birthday: October 2, 2005")
    print("Status: Student at PUP Taguig - BSIT 2-1")

def show_goals():
    print(Fore.LIGHTMAGENTA_EX + "Goals")
    print("- I aspire to become a skilled Full Stack Developer,")
    print("- who crafts intuitive and elegant digital experiences!")

def show_fun_facts():
    print(Fore.LIGHTMAGENTA_EX + "Fun Facts")
    print("- I enjoy skincare routines as self-care.")
    print("- Patch, my dog, is my coding buddy!")
    print("- I secretly enjoy debugging—it's like solving a mystery.")

def anipan_comments():
    print(Fore.LIGHTMAGENTA_EX + "Anipan Comment")
    print("pogiako123")
    print("You're very good at programming!")

def bartolome_comments():
    print(Fore.LIGHTMAGENTA_EX + "Bartolome's Comment")
    print("Your dog is so cute!")

