# importing easygui module

from easygui import *

import sys


def warning():

    msgbox(msg = """
Before you continue,\n
A pre-warning that clicking the X will do nothing in most situations.\n
If you wish to exit the program preferably wait until you have the option to exit.
""")


def exit_program():

    quit = buttonbox(msg = "Quit?", choices = ["Continue", "Quit"])
    if quit == "Quit":
        sys.exit()


def user_selector():

    global user_name
    user_name = enterbox(msg = "Please enter identifcation: ")
    if user_name:
        if ccbox(msg = f"Please confirm that, {user_name}, is your user."):
            msgbox(msg = f"Your user is {user_name}.")

        else:
            user_selector()


    else:
        quit_choice = buttonbox(msg = """
No username entered\n
You must select a user if you wish to continue.\n
Do you wish to choose a user or quit?
""", choices = ["Choose user", "Quit"])
        if quit_choice == "Choose user":
            user_selector()
        
        else:
            sys.exit()
    

def main():

    main_page = buttonbox(msg = f"""
Welcome {user_name} to Societas Spiritus's guide.
(If you couldn't tell, Societas Spiritus is the name of the book and also a group within.)\n
Please select what you would like to learn about.
""", choices = ["Overview", "F.A", "S.S", "C.A", "Exit"])

    if main_page == "Overview":
        msgbox(msg = """
Societas Spiritus focuses mainly on the group, Societas Spiritus.\n
Societas Spiritus's main goal is to create human animal mutations.\n
Societas Spiritus has been in running for about 200~+ years, close to 400~ years.\n
Societas Spiritus ignores ethical and safety concerns,
leading to many deaths of staff due to trying to defect and stop their crimes.\n
""", ok_button = "Continue")
        msgbox(msg = """
Over the years, two personnel managed to successfully defect,
starting a detectives firm called, Foedus Aquilarum.\n
Foedus Aquilarum has been running for about 100~ years.\n
Foedus Aquilarum has had many encounters with Societas Spiritus,
many leading in deaths on both sides.\n
Foedus Aquilarum attempts to destroy Societas Spiritus's sites and facilities. 
""", ok_button = "Continue")
        msgbox(msg = """
One of the defected personnel corrupted and left Foedus Aquilarum, 
starting an underground organisation called, Circulus Aeternitatis
        """)

    elif main_page == "Exit":
        sys.exit()


warning()
user_selector()
main()