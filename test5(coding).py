# importing easygui module
from easygui import *
import sys


def warning():

    msgbox("Before you continue,\n A pre-warning that clicking the X will do nothing in most situations.\n If you wish to exit the program preferably wait until you have the option to exit.", title = "Warning.")


def exit_program():

    quit = buttonbox(msg = "Do you wish to quit?", title = "Quit?", choices = ["Continue", "Quit"])
    if quit == "Quit":
        sys.exit()


def userselector():

    global username
    username = enterbox(msg = "Please enter your choice of identifcation:", title = "Username selector.")
    if username:
        if ccbox(msg = f"Please confirm you wish, {username}, as your user."): 
            msgbox(msg = f"Your user is {username}.", title = "Selected user.")

        else:
            userselector()


    else:
        quit_choice = buttonbox(msg = "No username entered\n You must select a user if you wish to continue.\n Do you wish to choose a user or quit?", title = "Quit?", choices = ["Choose user", "Quit"])
        if quit_choice == "Choose user":
            userselector()
        
        else:
            sys.exit()
    

def main():

    mainpage = buttonbox(msg = f"Welcome {username} to Societas Spiritus's guide.\n (If you couldn't tell, Societas Spiritus is the name of the book and also a group within.)", title = "Welcome!", choices = ["Overview", "Foedus Aquilarum", "Societas Spiritus", "Circulus Aeternitatis", "Maybe Character creation", "Exit"])

    if mainpage == "Overview":
        msgbox(msg = """
               Societas Spiritus focuses mainly on the group, Societas Spiritus.\n
               Societas Spiritus's main goal is to create human animal mutations to use for illegal and dangerous missions that regular humans would struggle with.\n
               Societas Spiritus has been in running for about 200~+ years, closer to 400~ years. Over that time, two people escaped and created a detectives firm called, Foedus Aquilarum.\n
               And a sub-group within Foedus Aquilarum called, Circulus Aeternitatis, who attempt to capture the experiements should they be located.
               """, title = "Societas Spiritus.", ok_button = "Continue.")

    elif mainpage == "Exit":
        sys.exit()


warning()
userselector()
main()