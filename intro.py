#The intro.py is the introductory to the story and allows the user to select their character. 

import people
def intro():
    input("""   / | / (_) /_/ /_  ____        _________ _(_)
  /  |/ / / __/ __ \/ __ \______/ ___/ __ `/ / 
 / /|  / / /_/ / / / /_/ /_____/ /  / /_/ / /  
/_/ |_/_/\__/_/ /_/\____/     /_/   \__,_/_/   
Press enter to start: """)
    input("""     In the year 3025, a civil war broke out. AI had reached a new peak, \
and the people were scared. But people still forced the building of AI. \
As people became more terrified of the prospect of the new AI, unrest grew \
until the first shots were fired over what is left of London.
Press enter to continue:""")
    input("""     As war raged over the world, cities were torn down. And for a long \
time it seemed the AI supporters would win. They had pushed so hard they forced people \
to flee to the land of Australia, where they were held. The war reached a stale mate for \
4 long years, until the AI's Adversaries did the unthinkable.
Press enter to continue:""")
    input("""     The opponents of AI created a new bomb, controlled by a force like \
antigravity. Within weeks of the first detonation, the AI sympathizers were forced back, \
until the only held the old US lands east of the Mississippi river. To this day (July 14, 3030), \
this is where the AI supporters live, treated as they treated the AI's opponents. But they still \
create their AI's in their labs, and some AIs worked in the labs, and yet everyone is forced to \
stay in their realms.
Press enter to continue:""")    
    input("""     As time passed after the AI War, rumors spread between the 4 leftover realms of United Nitho-rai. \
These four realms are the lands of New York, Washington D.C., Chicago, and Miami. In each realm, \
people are allowed to have a lab, a sports arena, a bank, and a store. The rest of the area was \
reserved for living. The suppressed AI Supporters started plotting news ways to regain control of their land \
and talked about old stories of a new AI prototype, that could solve all their problems.
Press enter to continue:""")
    input("""     In the past month, bits and pieces of the New AI's code had been found, confirming it's existance \
and the best of the labs (all four of them) had been able to reconstruct most of the New AI. However, one thing \
was missing. A database so large it was split into 6 pieces and hidden throughout the realms. Many believed them to be lost. 
Press enter to continue:""")
    input("""     However, a group of young citizens of United Nitho-rai didn't believe this and banded together to search for them \
They wanted to find these parts of the database and finally be free of the oppression they face, however it happened. \
When they first started they only had two clues:
    The first was that the pieces were hidden in public places, and that they needed to keep their eyes peeled for them.
    Second was that one piece was believe not to exist in the 4 realms. It was rumorred it was handed to a AI Sympathizer \
who lived outside the 4 realms. They had to hope this sympathizer would find them.
Press enter to continue:""")
    print("""     With these in mind, they started on their quest to free their country, each of them eager to start. \
At this time, the group consists of:
1)  Azure
2)  Mig
3)  John
4)  Michael
5)  Tobias
6)  Chloe
7)  Hailey
8)  Sarah
9)  Alex
10) Sam
11) Max""")
    
def begin(ACCOUNT, PAY, DATABASE_PARTS):
    while True:
        character, type=people.set_character(input("Who do you want to be: "))
        if character != "Invalid Input":
            break
    location=character.get_job()
    print(f"You have chosen to be {character.get_name()}. \
{type.pronouns[0].capitalize()} {type.pronouns[2]} a {character.get_age()} year old {type.type}. \
{type.pronouns[0].capitalize()} stands at {character.get_height()} and works at the {character.get_job()}. \
{type.pronouns[0].capitalize()} can be descibed as {character.get_personality()}. \
You have ${PAY} and have found {DATABASE_PARTS} database parts. There is ${ACCOUNT} in your account \
\nLet's Begin!")   

    if character.get_name()=="Aldrich":
        print("""Congratulations! You have found the hidden character! You are in the mainland realm Cuba, where you must find \
the last piece of the dataset that you have and return it to the group. You will always have the choice to come back using the \
hidden choice 6) Cuba \n Go on! You're Almost there! The rest of the game depends on you!\n""")
    return character, location, ACCOUNT, PAY, DATABASE_PARTS
