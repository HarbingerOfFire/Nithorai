#The NithoRai.py will run the loading screen; allow for the user to be introduced to the game i.e. location, account, pay, and database parts.   

#The NithoRai.py will allow the user to save and reset the game when needed. 

import movement, settings, intro, outro

def main():
    print("loading...")
    intro.intro()
    try:
        ACCOUNT, PAY, DATABASE_PARTS, = settings.load_data()
        if DATABASE_PARTS < 6:
            character, location, ACCOUNT, PAY, DATABASE_PARTS = intro.begin(ACCOUNT, PAY, DATABASE_PARTS)
            character, location, ACCOUNT, PAY, DATABASE_PARTS = movement.leave_realm(character, location, ACCOUNT, PAY, DATABASE_PARTS)
        else:
            outro.outro()
    except ValueError:
        exit()
    except:
        print("An error occured. Saving and resetting.")
        settings.save_data(ACCOUNT, PAY, DATABASE_PARTS)
        main()

if __name__=="__main__":
    try:
        main()
    except:
        exit()
