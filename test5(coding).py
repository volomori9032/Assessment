# importing easygui module
from easygui import *


def warning():
    msgbox("Before you continue,\n A pre-warning that clicking the X will do nothing in most situations.\n If you wish to exit the program preferably wait until you have the option to exit.", title = "Warning.")

def exit():
    quit = buttonbox(msg = "Do you wish to quit?", title = "Quit?", choices = ["Continue", "Quit"])
    if quit == "continue":
        pass
    else:
        quit

def userselector():

    username = enterbox(msg = "Please enter your choice of identifcation:\n If you wish to not proceed, do not enter a user.", title = "Username selector.")
    if username:
        if ccbox(msg = f"Please confirm you wish, {username}, as your user."): 
            pass
            msgbox(msg = f"Your user is {username}.", title = "Selected user.")
        else:
            userselector()
            
        

    else:
        quit = buttonbox(msg = "No username entered\n You must select a user if you wish to continue.\n Do you wish to choose a user or quit?", title = "Quit?", choices = ["Choose user", "Quit"])
        if quit == "Choose user":
            userselector()
        
        else:
            quit

def entry():

    msgbox(msg = "Welcome to my guide of Societas Spiritus.")
    
    

warning()
userselector()