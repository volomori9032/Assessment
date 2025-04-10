"""This file explains book groups and creatures."""

# Importing easygui module

from easygui import *

import sys


def main():
    """Learn or quit."""
    main_page = buttonbox(msg=f"""
Welcome {user_name} to Societas Spiritus's guide.
Societas Spiritus is the name of the book and a group within.\n
Please select what you would like to learn about.
""", choices=["Overview", "F.A", "S.S", "C.A", "H", "Exit"])

    if main_page == "Overview":
        over_view()

    elif main_page == "F.A":
        foedus_aquilarum()

    elif main_page == "S.S":
        societas_spiritus()

    elif main_page == "C.A":
        circulus_aeternitatis()

    elif main_page == "H":
        hint()

    elif main_page == "Exit":
        sys.exit()

    else:
        sys.exit()


def user_selector():
    """Gathers username or quits."""
    global user_name
    user_name = enterbox(msg="Please enter identification: ")

    if user_name:
        if ccbox(msg=f"Please confirm, {user_name}, is your user."):
            msgbox(msg=f"Your user is {user_name}.")

        else:
            user_selector()

    else:
        quit_choice = buttonbox(msg="""
No username entered\n
You must select a user if you wish to continue.\n
Do you wish to choose a user or quit?
""", choices=["Choose user", "Quit"])

        if quit_choice == "Choose user":
            user_selector()

        else:
            sys.exit()


def over_view():
    """Explains the basics of the book."""
    p1 = msgbox(msg="""
Societas Spiritus focuses mainly on the group, Societas Spiritus.\n
S.S's main goal is to create human animal mutations.\n
S.S has been in running for about 200~+ years, close to 400~ years.\n
S.S ignores ethical and safety concerns,
leading to many deaths of staff due to trying to stop their crimes.\n
""", ok_button="Continue")

    if p1 is None:
        sys.exit()

    p2 = msgbox(msg="""
Over the years, two personnel managed to successfully defect,
starting a detectives firm called, Foedus Aquilarum.\n
F.A has been running for about 100~ years.\n
F.A has had many encounters with S.S,
many leading in deaths on both sides.\n
F.A attempts to destroy S.S's sites and facilities.
""", ok_button="Continue")

    if p2 is None:
        sys.exit()

    p3 = msgbox(msg="""
One of the defected personnel corrupted and left F.A,
starting an underground organisation called, Circulus Aeternitatis.\n
C.A serves to bring a multitude of hostile organizations
together to locate and capture escaped or injured S.S experiments.\n
To either recruit or throw into very top secret biddings.\n
C.A has been in business in for 30 years.
""", ok_button="Continue")

    if p3 is None:
        sys.exit()

    main()


def foedus_aquilarum():
    """Gathers password before proceeding to page or back to main."""
    fa_password = passwordbox(msg="Please enter personnel password: ")

    if fa_password == "League of Eagles":
        fa_main_page()

    else:
        msgbox(msg="Oops! That is incorrect!")
        main()

# finish below
def fa_main_page():
    """Learn or quit."""
    fa = buttonbox(msg="""
Welcome Foedus Aquilarum  personnel,\n
What would you like to learn about today?
""", choices=["placeholder", "Management", "Return"])

    if fa == "placeholder":
        msgbox(msg="placeholder")
        fa_main_page()

    elif fa == "Management":
        msgbox(msg="Management")
        fa_main_page()

    elif fa == "Return":
        main()

    else:
        sys.exit


def societas_spiritus():
    """Gathers password before proceeding to page or back to main."""
    ss_password = passwordbox(msg="Please enter personnel password: ")

    if ss_password == "Societas Spiritus":
        ss_main_page()

    else:
        msgbox(msg="Oops! That is incorrect!")
        main()

# finish below
def ss_main_page():
    """Learn or return."""
    ss = buttonbox(msg="""
Welcome Societas Spiritus  personnel,\n
What would you like to learn about today?
""", choices=["Mutations", "Management", "Return"])

    if ss == "Mutations":
        msgbox(msg="placeholder")
        ss_main_page()

    elif ss == "Management":
        msgbox(msg="Management")
        ss_main_page()

    elif ss == "Return":
        main()

    else:
        sys.exit


def circulus_aeternitatis():
    """Gathers password before proceeding to page or back to main."""
    ca_password = passwordbox(msg="Please enter personnel password: ")
    if ca_password == "30":
        ca_main_page()

    else:
        msgbox(msg="Oops! That is incorrect!")
        main()

# finish below
def ca_main_page():
    """Learn or return."""
    ca = buttonbox(msg="""
Welcome Circulus Aeternitatis personnel,\n
What would you like to learn about today?
""", choices=["placeholder", "Management", "Return"])

    if ca == "placeholder":
        msgbox(msg="placeholder")
        ca_main_page()

    elif ca == "Management":
        msgbox(msg="Management")
        ca_main_page()

    elif ca == "Return":
        main()

    else:
        sys.exit


def hint():
    """Hints to each password."""
    msgbox(msg="""
S.S always loved to use their name as a password.
F.A always loved to use their English name as a password.
C.A always loved to use how long they have been active for as a password.
""")

    choice = buttonbox(msg=".", choices=["Return", "Character"], title="?")

    if choice == "Return":
        main()

    elif choice == "Character":
        character_creation()

    else:
        sys.exit


def character_creation():
    """Gathers password before proceeding to page or back to main."""
    c_c = passwordbox(msg="Enter all passwords: ")

    if c_c == "Societas Spiritus League of Eagles 30":
        cc_main_page()

    else:
        msgbox(msg="Yikes! Tried and you failed, maybe learn some more?")
        main()


def cc_main_page():
    """Create or return."""
    msgbox(msg="""
Welcome to character creator.\n
Here using the mutations mentioned in S.S's lore,
you get to make your own!\n
Well own referring to how it looks.\n
Not a new mutation!\n
Be warned!
Once you enter you can't back out!
""", ok_button="Continue")

    main_four()


def main_four():
    """Choice of race, gender, height, age."""
    global race
    global gender
    global age
    global height

    races = ["Human", "Fish", "Bird", "Cat", "Dog", "Wolf"]
    sex = ["Female", "Male"]
    ages = ["13", "14", "15", "16", "17", "18", "19", "20", "20+"]
    heights = ["4'11 and below", "5'0 - 5'11", "6'0 - 6'11", "7'0 and above"]

    race = choicebox(msg="Pick a race: ", choices=races)

    if race == "Human" or "Fish" or "Bird" or "Cat" or "Dog" or "Wolf":
        age = choicebox(msg="Pick a age: ", choices=ages)

        if age == "13" or "14" or "15" or "16" or "17" or "18":
            height = choicebox(msg="Pick a height: ", choices=heights)

            if height == "4'11 and below":
                msgbox(msg="Sorry bud, too similar to a child!")
                main()

            elif height == "5'0 - 5'11":
                msgbox(msg="Average height!")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender == "Female":
                    hair_stuff()

                elif gender == "Male":
                    hair_stuff()

            elif height == "6'0 - 6'11" or "7'0 and above":
                msgbox(msg="Interesting height you got there!")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender == "Female" or "Male":
                    hair_stuff()

        elif age == "19" or "20" or "21+":
            height = choicebox(msg="Pick a height: ", choices=heights)

            if height == "4'11 and below":
                msgbox(msg="Sorry bud, too similar to a child!")
                main()

            elif height == "5'0 - 5'11":
                msgbox(msg="Average height!")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender == "Female" or "Male":
                    hair_stuff()

            elif height == "6'0 - 6'11" or "7'0 and above":
                msgbox(msg="Interesting height you got there!")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender == "Female" or "Male":
                    hair_stuff()


def hair_stuff():
    """Choice of hair."""
    global f_length
    global m_length
    global hair_colour

    f_hair = ["Short", "Medium", "Long"]
    m_hair = ["Bald", "Buzz", "Ear length", "Neck length"]
    h_colour = ["Blonde", "Black", "Brown"]

    if gender == "Female":
        f_length = choicebox(msg="Pick a hair length: ", choices=f_hair)

        if f_length == "Short" or "Medium" or "Long":
            hair_colour = choicebox(msg="Pick a colour: ", choices=h_colour)

            if hair_colour == "Blonde" or "Black" or "Brown":
                others()

    elif gender == "Male":
        m_length = choicebox(msg="Pick a hair length: ", choices=m_hair)

        if m_length == "Bald" or "Buzz" or "Ear length" or "Neck length":
            hair_colour = choicebox(msg="Pick a colour: ", choices=h_colour)

            if hair_colour == "Blonde" or "Black" or "Brown":
                others()


def others():
    """Choice of other."""
    global skin_colour
    global eye_colour

    s_colour = ["Black", "Brown", "White"]
    e_colour = ["Blue", "Green", "Brown", "Gray", "Gold", "Red", "Purple"]

    if hair_colour == "Blonde" or "Black" or "Brown":
        skin_colour = choicebox(msg="Pick a skin: ", choices=s_colour)

        if skin_colour == "Black" or "Brown" or "White":
            eye_colour = choicebox(msg="Pick a eye: ", choices=e_colour)

            if eye_colour == "Blue" or "Green" or "Brown" or "Gray":
                aftermath()

            elif eye_colour == "Gold" or "Red" or "Purple":
                aftermath()


def aftermath():
    """Finial."""
    score = 0
    years = ["25", "30", "35", "100", "150", "200", "250", "300", "350", "400"]
    msgbox(msg="Congratulations! You did it.")
    msgbox("""
Your final outcome is-\n
OH WAIT LOOK A POP QUIZ!
""")
    if score == 0:
        q = multchoicebox(msg="""
What is the current run times for each group?
""", choices=years)

        if q == "30" and "100" and "400":
            score = score + 5

        elif q is None:
            sys.exit()

        else:
            score = 0

    msgbox(msg="Well done! (totally wasn't added because required)")
    if gender == "Male":
        msgbox(f"""
Anyways. You have picked:
A {gender} {race} with {skin_colour} skin and {eye_colour} eyes.
{age} years old, standing at {height} tall.
{hair_colour} {m_length}.
""")
    elif gender == "Female":
        msgbox(f"""
Anyways. You have picked:
A {gender} {race} with {skin_colour} skin and {eye_colour} eyes.
{age} years old, standing at {height} tall.
{hair_colour} {f_length} hair.
""")
        main()


user_selector()
main()
