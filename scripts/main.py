import Folder_List_Handler
import Usercase_config
from datetime import datetime
import time

def main_menu():
    print("1.Select target folders for backup.\n")
    print("2.Check status of recovery for my folders.\n")
    print("3.Set time of recovery cycle.\n")
    print("4.list out files/folders in target folders\n")
    print("5.Quit.\n")

def introduction():
    print(".step 1.")
    notintroduced()

def notintroduced():
    print(".step 2.") #debug
    print("hello!! welcome to the application!")
    time.sleep(1.5)
    greetings_user(captured_name)
    #function that will define the Json for the user
    print(".step 4.")
    print("json archive goes here")
    print(f"alright {captured_name}, how may i take your order?")

def usercatcher():
    print(".step 3.")
    username = input("What is your name, dear?\n")
    return username

def greetings_user(name):
    print(f"{name}")

captured_name = usercatcher()

#flavortext time

def greetings():
    now = datetime.now()
    current_hour = now.hour
    if (current_hour >= 0) and (current_hour < 12):
        greetings_intro = "morning"
        print(f"{greetings_intro}")
        return greetings_intro
    elif (current_hour >= 12) and (current_hour < 18):
        greetings_intro = "afternoon"
        print(f"{greetings_intro}")
        return greetings_intro
    elif (current_hour >= 18) and (current_hour <=23):
        greetings_intro = "night"
        print(f"{greetings_intro}")
        return greetings_intro

#username for flavortext


def wasintroduced():
    print(f"Good {greetings()}, {captured_name} welcome to the application!")
    time.sleep(1.5)
    print("How may i help you?")



#start of application
introduction()

while True:
    print(".step 5.")
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




