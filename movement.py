#The movement.py defines the characters current realm and location and allows them to move between realms. 

import places, settings, hidden_character, actions

def move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS):
    print("""You can go to
1) lab
2) arena
3) bank
4) store
5) leave realm
          """)
    while True: 

        answer = input("Where do you want to go: ")

        if answer.lower() == "lab" or "1" in answer:
            location=realm.Lab()
            print(f"You are in the {location.get_name()}. There are {location.get_floors()} floors used for {location.get_purpose()}. This is a {location.get_testingunit()}")
            character, realm, location, ACCOUNT, PAY, DATABASE_PARTS = actions.main(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif answer.lower() == "arena" or "2" in answer:
            location=realm.Sports_arena()
            print(f"You are in the {location.get_name()}. Here they have {location.get_purpose()} for {location.get_sport()}. They have {location.get_teams()}.")
            character, realm, location, ACCOUNT, PAY, DATABASE_PARTS = actions.main(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif answer.lower() == "bank" or "3" in answer:
            location=realm.Bank()
            print(f"You are in the {location.get_name()}. Here you can {location.get_ATM()} for {location.get_purpose()}")
            character, realm, location, ACCOUNT, PAY, DATABASE_PARTS = actions.main(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
        
        elif answer.lower() == "store" or "4" in answer:
            location=realm.Store()
            print(f"You are in the {location.get_name()}. Like most stores, you can see the {location.get_warehouse()}. They {location.get_purpose()} and {location.get_merchandise()}.")
            character, realm, location, ACCOUNT, PAY, DATABASE_PARTS = actions.main(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif answer.lower() == "leave" or "5" in answer:
            leave_realm(character, location, ACCOUNT, PAY, DATABASE_PARTS)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        else:
            print("Invalid Input")
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
        return character, realm, location, ACCOUNT, PAY, DATABASE_PARTS



def leave_realm(character, location, ACCOUNT, PAY, DATABASE_PARTS):
    print("""You can go to the realms of: 
1) New York
2) Washington D.C.
3) Chicago
4) Miami
5) Settings

""")

    while True:
        answer = input("Where do you want to go: ")

        if answer.lower() == "new york" or "1" in answer:
            realm = places.Places.Realm_New_York()
            print("You are in "+realm.name)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif answer.lower() == "washington d.c." or "2" in answer:
            realm = places.Places.Realm_Washington_DC()
            print("You are in "+realm.name)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif answer.lower() == "chicago" or "3" in answer:
            realm = places.Places.Realm_Chicago()
            print("You are in "+realm.name)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif answer.lower() == "miami" or "4" in answer:
            realm = places.Places.Realm_Miami()
            print("You are in "+realm.name)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

        elif "settings" in answer.lower() or "5" in answer:
            settings.main(character, location, ACCOUNT, PAY, DATABASE_PARTS)
            try:
                realm=realm
            except:
                realm=character.realm
                print("You are in "+realm.name)
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
            break

        elif "cuba" in answer.lower() or "hidden" in answer.lower() or "6" in answer:
            if character.get_name()=='Aldrich':
                realm=hidden_character.HiddenCharacter.Realm_Cuba()
                print("You are in "+realm.name)
                move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)
            else:
                print("Invalid input")
        
        else:
            print("Invalid input")
            move(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS)

    return character, realm, location, ACCOUNT, PAY, DATABASE_PARTS
