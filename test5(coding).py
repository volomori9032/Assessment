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


def fa_main_page():
    """Learn or quit."""
    fa = buttonbox(msg="""
Welcome Foedus Aquilarum  personnel,\n
What would you like to learn about today?
""", choices=["Management", "Return"])

    if fa == "Management":
        msgbox(msg="""
Management!\n

Owner - “Nivea” (Snowy)\n

Director - “HELIANTHUS” (Sunflower)\n

High Ranks\n

Principal Director - “Aenean” (Jasmine)\n

Specialized Investigator - “Saxum” (Rock)\n
""")
        fa_main_page()

    elif fa == "Return":
        main()

    else:
        sys.exit()


def societas_spiritus():
    """Gathers password before proceeding to page or back to main."""
    ss_password = passwordbox(msg="Please enter personnel password: ")

    if ss_password == "Societas Spiritus":
        ss_main_page()

    else:
        msgbox(msg="Oops! That is incorrect!")
        main()


def ss_main_page():
    """Learn or return."""
    ss = buttonbox(msg="""
Welcome Societas Spiritus  personnel,\n
What would you like to learn about today?
""", choices=["Mutations", "Management", "Return"])

    if ss == "Mutations":
        experimentation()

    elif ss == "Management":
        msgbox(msg="""
Management\n

Leader - “Aquae” (Water)\n

Research Director - “Ignis” (Fire)\n

High Ranks\n

Data Coordinator - “Lunae” (Moon)\n

Regulatory Coordinator - “Sol” (Sun)\n
""")
        ss_main_page()

    elif ss == "Return":
        main()

    else:
        sys.exit()


def experimentation():
    """Learn or return."""
    mutations = buttonbox(msg="""
Societas Spiritus human mutations.
""", choices=["Fish", "Cat", "Wolf", "Bird", "Dog", "Return"])

    if mutations == "Fish":
        p1 = msgbox(msg="""
Fish mutations are purely made for the male gaze and aesthetic.\n
Fish normally appear visually with large fins or tail.\n
Small additions which aren't as visual as the fins or tail are
    Gills, webbed hands and feet, scales.\n
Fish mutations can be all colours of the the rainbow,
    due to the range of fish genes used in experimentation.\n
""", ok_button="Continue")

        if p1 is None:
            sys.exit()

        p2 = msgbox(msg="""
Fish mutations length, strength, and other qualities will vary greatly,
    depending on the person's genes.\n
Fish mutations can go wrong and affect a person insides instead of outsides.\n
""", ok_button="Continue")

        if p2 is None:
            sys.exit()

        experimentation()

    elif mutations == "Cat":
        p1 = msgbox(msg="""
Cat mutations are basic, they are ears and tail,
    with the slight chance of pupils and claws.\n
Cat mutations can only be black, white, grey, orange, or brown,
    as cat genes are limited to certain colours.\n
Cat mutations length, strength, and other qualities will vary greatly,
    depending on the person's genes.\n
Cat mutations can go wrong and affect a persons insides instead of outsides.\n
""", ok_button="Continue")

        if p1 is None:
            sys.exit()

        experimentation()

    elif mutations == "Dog":
        p1 = msgbox(msg="""
Dog mutations are basic, they are ears and tail,
    with the slight chance of pupils and claws.\n
Dog mutations can only be black, white, grey, or brown,
    as dog genes are limited to certain colours.\n
Dog mutations length, strength, and other qualities will vary greatly,
    depending on the person's genes.\n
Dog mutations can go wrong and affect a persons insides instead of outsides.\n
""", ok_button="Continue")

        if p1 is None:
            sys.exit()

        experimentation()

    elif mutations == "Wolf":
        p1 = msgbox(msg="""
Wolf mutations are basic, they are ears and tail,
    with the slight chance of pupils and claws.\n
Wolf mutations can only be black, white, grey, or brown,
    as wolf genes are limited to certain colours.\n
Wolf mutations length, strength, and other qualities will vary greatly,
    depending on the person's genes.\n
Wolf mutations can go wrong and affect a person insides instead of outsides.\n
""", ok_button="Continue")

        if p1 is None:
            sys.exit()

        experimentation()

    elif mutations == "Bird":
        p1 = msgbox(msg="""
Bird mutations are made for flight..\n
Bird mutation visually shows as wings, be that on the back,
    legs, arms, chest, head, ears, eyes, wrists, ankles or whatever.\n
Small additions which aren't as visual as the wings are
    Feathers.\n
Bird mutations can be all colours of the the rainbow,
    due to the range of bird genes used in experimentation.\n
""", ok_button="Continue")

        if p1 is None:
            sys.exit()

        p2 = msgbox(msg="""
Bird mutations length, strength, and other qualities will vary greatly,
    depending on the person's genes.\n
Bird mutations can go wrong and affect a person insides instead of outsides.\n
""", ok_button="Continue")

        if p2 is None:
            sys.exit()

        experimentation()

    elif mutations == "Return":
        ss_main_page()

    else:
        sys.exit()


def circulus_aeternitatis():
    """Gathers password before proceeding to page or back to main."""
    ca_password = passwordbox(msg="Please enter personnel password: ")
    if ca_password == "30":
        ca_main_page()

    else:
        msgbox(msg="Oops! That is incorrect!")
        main()


def ca_main_page():
    """Learn or return."""
    ca = buttonbox(msg="""
Welcome Circulus Aeternitatis personnel,\n
What would you like to learn about today?
""", choices=["Management", "Return"])

    if ca == "Management":
        msgbox(msg="""
Management\n

Boss - “Corvus” (Raven)\n

Under boss - “Cornix” (Crow)\n

High Ranks\n

Director Capo - “Succubus”\n

Specialized Capo - “Umbra” (Shadow)\n
""")
        ca_main_page()

    elif ca == "Return":
        main()

    else:
        sys.exit()


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
        sys.exit()


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

    if race in races:
        age = choicebox(msg="Pick a age: ", choices=ages)

        if age in ages:
            height = choicebox(msg="Pick a height: ", choices=heights)

            if height == "4'11 and below":
                msgbox(msg="I'm watching you...")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender in sex:
                    hair_stuff()

                else:
                    main()

            elif height == "5'0 - 5'11":
                msgbox(msg="Average height!")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender in sex:
                    hair_stuff()

                else:
                    main()

            elif height in ["6'0 - 6'11", "7'0 and above"]:
                msgbox(msg="Interesting height you got there!")
                gender = choicebox(msg="Pick a gender: ", choices=sex)

                if gender in sex:
                    hair_stuff()

                else:
                    main()

            else:
                main()

        else:
            main()

    else:
        main()


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

        if f_length in f_hair:
            hair_colour = choicebox(msg="Pick a colour: ", choices=h_colour)

            if hair_colour in h_colour:
                others()

            else:
                main()

        else:
            main()

    elif gender == "Male":
        m_length = choicebox(msg="Pick a hair length: ", choices=m_hair)

        if m_length in m_hair:
            hair_colour = choicebox(msg="Pick a colour: ", choices=h_colour)

            if hair_colour in h_colour:
                others()

            else:
                main()

        else:
            main()

    else:
        main()


def others():
    """Choice of other."""
    global skin_colour
    global eye_colour

    s_colour = ["Black", "Brown", "White"]
    e_colour = ["Blue", "Green", "Brown", "Gray", "Gold", "Red", "Purple"]

    if hair_colour in ["Blonde", "Black", "Brown"]:
        skin_colour = choicebox(msg="Pick a skin: ", choices=s_colour)

        if skin_colour in s_colour:
            eye_colour = choicebox(msg="Pick a eye: ", choices=e_colour)

            if eye_colour in e_colour:
                aftermath()

            else:
                main()

        else:
            main()

    else:
        main()


def aftermath():
    """Finial."""
    score = 0
    years = ["25", "30", "35", "100", "150", "200", "250", "300", "350", "400"]
    q_answer = ["30", "100", "400"]
    msgbox(msg="Congratulations! You did it.")
    msgbox("""
Your final outcome is-\n
OH WAIT LOOK A POP QUIZ!
""")
    while score == 0:
        q = multchoicebox(msg="""
What is the current run times for each group?
""", choices=years)

        if q == q_answer:
            score = score + 5

        else:
            aftermath()

    msgbox(msg="Well done!")
    if gender == "Male":
        msgbox(f"""
Anyways. You have picked:
A {gender} {race} with {skin_colour} skin and {eye_colour} eyes.
{age} years old, standing at {height} tall.
{m_length} (length) {hair_colour} hair.
""")
        main()

    elif gender == "Female":
        msgbox(f"""
Anyways. You have picked:
A {gender} {race} with {skin_colour} skin and {eye_colour} eyes.
{age} years old, standing at {height} tall.
{f_length} (length) {hair_colour} hair.
""")
        main()


cc_main_page()
user_selector()
main()
