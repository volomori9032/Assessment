# importing easygui module

from easygui import *

import sys


# Variables of titles

MP = "Societas Spiritus" # Title for main page
W = "Warning!" # Title for warning
Q = "Quit?" # Title for exit_program and quit
US = "Select Identification" # Title for user_selector
C = "Confirmation" # Title for confirmation of user
O = "Overview" # Title for overview


def warning():

    msgbox(msg = """
Before you continue,\n
A pre-warning that clicking the X will do nothing in most situations.\n
If you wish to exit the program wait until you have the option to exit.\n
Makes it easier for both of us.
""", title = W)


def exit_program():

    quit = buttonbox(msg = "Quit?", choices = ["Continue", "Quit"], title = Q)
    if quit == "Quit":
        sys.exit()


def user_selector():

    global user_name
    user_name = enterbox(msg = "Please enter identification: ", title = US)
    if user_name:
        if ccbox(msg = f"Please confirm that, {user_name}, is your user.", title = C):
            msgbox(msg = f"Your user is {user_name}.", title = C)

        else:
            user_selector()


    else:
        quit_choice = buttonbox(msg = """
No username entered\n
You must select a user if you wish to continue.\n
Do you wish to choose a user or quit?
""", choices = ["Choose user", "Quit"], title = Q)
        if quit_choice == "Choose user":
            user_selector()
        
        else:
            sys.exit()
    

def main():

    main_page = buttonbox(msg = f"""
Welcome {user_name} to Societas Spiritus's guide.
Societas Spiritus is the name of the book and a group within.\n
Please select what you would like to learn about.
""", choices = ["Overview", "F.A", "S.S", "C.A", "Exit"], title = MP)

    if main_page == "Overview":
        overview()

    elif main_page == "Exit":
        sys.exit()

def overview():

    msgbox(msg = """
Societas Spiritus focuses mainly on the group, Societas Spiritus.\n
S.S's main goal is to create human animal mutations.\n
S.S has been in running for about 200~+ years, close to 400~ years.\n
S.S ignores ethical and safety concerns,
leading to many deaths of staff due to trying to stop their crimes.\n
""", ok_button = "Continue", title = O)

    msgbox(msg = """
Over the years, two personnel managed to successfully defect,
starting a detectives firm called, Foedus Aquilarum.\n
F.A has been running for about 100~ years.\n
F.A has had many encounters with S.S,
many leading in deaths on both sides.\n
Foedus Aquilarum attempts to destroy S.S's sites and facilities. 
""", ok_button = "Continue", title = O)

    msgbox(msg = """
One of the defected personnel corrupted and left F.A, 
starting an underground organisation called, Circulus Aeternitatis.\n
C.A serves to bring cults, mafias, gangs and a multitude of 
""", ok_button = "Continue", title = O)
    

warning()
user_selector()
main()