import Folder_List_Handler
import Usercase_config



def main_menu():
    print("1.Select target folders for backup.\n")
    print("2.Check status of recovery for my folders.\n")
    print("3.Set time of recovery cycle.\n")
    print("4.list out files/folders in target folders\n")
    print("5.Quit.\n")

def introduction():
    print("hello!! welcome to the application!")
    username = input("What is your name, dear?\n")
    #function that will define the Json for the user, ask once then remember
    print(f"alright {username}, how may i take your order?")

while True:
    main_menu()
    try:
        main_choice = int(input("select the option you wish \n"))
        if main_choice == 1:
            print(f"você escolheu {main_choice}")
        elif main_choice == 2:
            print(f"você escolheu {main_choice}")
        elif main_choice == 3:
            print(f"você escolheu {main_choice}")
        elif main_choice == 4:
            print(f"você escolheu {main_choice}")
            #list out files/folders on the sellection//not tied to selection yet
            Folder_List_Handler.list_directory_tree()
            break
        elif main_choice == 5:
            print(f"você escolheu {main_choice}")
            break
        else:
            print(f"{main_choice} isn't a valid number, please try again")
    except ValueError:
        print("please use numbers.")




