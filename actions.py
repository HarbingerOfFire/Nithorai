#The actions.py will allow the user to perform actions at the several locations. 

import nithorai
#options if character at their own workplace
def leave(ACCOUNT, PAY, DATABASE_PARTS):
    print("You Leave")
    return ACCOUNT, PAY, DATABASE_PARTS

def work(ACCOUNT, PAY, DATABASE_PARTS):
    print("You go to work and earn 5 dollars.")
    PAY += 5
    print(f"You have ${PAY}")
    return ACCOUNT, PAY, DATABASE_PARTS

#options for other places

def new_york_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the New York Lab and received a tour of the facilities and it costed 10.00 dollars.")
    PAY -= 10
    return ACCOUNT, PAY, DATABASE_PARTS
#"New York Lab Tour"
    

def new_york_sports_game(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the home Baseball game at the New York Sports Arena and it costed 20.00 dollars.")
    PAY -= 20
    return ACCOUNT, PAY, DATABASE_PARTS
#"New York Baseball game"

def new_york_bank(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the New York Bank to withdrawal 20.00 dollars.")
    if ACCOUNT >= 20:
        ACCOUNT -= 20
        PAY += 20
    else:
        print("insufficient funds")
    return ACCOUNT, PAY, DATABASE_PARTS
#"Withdrawal money at New York bank"

def new_york_store(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the New York store to purchase goods which costed you 15.00 dollars.")
    PAY -= 15
#"Purchase goods at New York Store"
    if DATABASE_PARTS==0:
        print("You found a part of the database!")
        DATABASE_PARTS += 1
    return ACCOUNT, PAY, DATABASE_PARTS

#options for other places

def Washington_DC_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Washington DC Lab and received a tour of the facilities which costed you 5.00 dollars.")
    PAY -= 5
    return ACCOUNT, PAY, DATABASE_PARTS
#"Washington DC Lab Tour"

def Washington_DC_sports_game(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the home basketball game at the Washington DC Sports Arena and it costed 35.00 dollars.")
    PAY -= 35
#"Washington DC Basketball Game
    if DATABASE_PARTS==1:
        print("You found a part of the database!")
        DATABASE_PARTS += 1
    return ACCOUNT, PAY, DATABASE_PARTS

def Washington_DC_bank(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Washington DC Bank to withdrawal 30.00 dollars.")
    if ACCOUNT >= 30:
        ACCOUNT -= 30
        PAY += 30
    else:
        print("insufficient funds")
    return ACCOUNT, PAY, DATABASE_PARTS
#"Withdrawal money at Washington DC Bank"

def Washington_DC_store(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Washington DC store to purchase goods which costed you 45.00 dollars.")
    PAY -= 45
    return ACCOUNT, PAY, DATABASE_PARTS
#"Purchase goods at Washington DC Store"

#options for other places

def Chicago_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Chicago Lab and received a tour of the facilities which costed you 10.00 dollars.")
    PAY -= 10
#"Chicago Lab Tour"
    if DATABASE_PARTS==2:
        print("You found a part of the database!")
        DATABASE_PARTS += 1
    return ACCOUNT, PAY, DATABASE_PARTS

def Chicago_Tennis_Match(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Pro Tennis Match at the Chicago Sports Arena and it costed you 50.00 dollars.")
    PAY -= 50
    return ACCOUNT, PAY, DATABASE_PARTS
#"Chicago Tennis Match"

def Chicago_bank(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to Chicago Bank to deposit 40.00 dollars.")
    if ACCOUNT >= 40:
        ACCOUNT -= 40
        PAY += 40
    else:
        print("insufficient funds")
        return ACCOUNT, PAY, DATABASE_PARTS
#"Deposit money at Chicago bank"

def Chicago_store(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Chicago store to purchase goods which costed you 50.00 dollars. Somebody mentioned someone name Aldrich?")
    PAY -= 50
    return ACCOUNT, PAY, DATABASE_PARTS
#"Purchase goods at Chicago Store"

#options for other places

def Miami_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Miami Lab and received a tour of the facilities which costed you 25.00 dollars.")
    PAY -= 25
    if DATABASE_PARTS==4:
        DATABASE_PARTS += 1
    return ACCOUNT, PAY, DATABASE_PARTS
#"Miami Lab Tour"

def Miami_Football_Game(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the home football game at the Miami Sports Arena and it costed you 55.00 dollars.")
    PAY -= 55
    return ACCOUNT, PAY, DATABASE_PARTS
#"Miami Football Game"

def Miami_Bank(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Miami Bank to deposit 75.00 dollars.")
    if PAY >= 75:
        ACCOUNT += 75
        PAY -= 75
    else:
        print("insufficient funds")
#"Deposit money at Miami bank"
    if DATABASE_PARTS==3:
        print("You found a part of the database!")
        DATABASE_PARTS += 1
    return ACCOUNT, PAY, DATABASE_PARTS

def Miami_store(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Miami store to purchase goods which costed you 15.00 dollars.")
    PAY -= 15
    return ACCOUNT, PAY, DATABASE_PARTS
#"Purchase goods at Miami Store"

def cuba_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Cuba Lab and received a tour of the facilities which costed you 35.00 dollars.")
    PAY -= 35
    return ACCOUNT, PAY, DATABASE_PARTS
#"Miami Lab Tour"

def cuba_poker_Game(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the poker tournament at the Cuban recreation center and it costed you 65.00 dollars.")
    PAY -= 65
    if DATABASE_PARTS==5:
        print("You found the last part of the database! You give it to one of the members of the group searching for it. You won! Read what happens below!")
        DATABASE_PARTS += 1
        nithorai.main()
    return ACCOUNT, PAY, DATABASE_PARTS
#"Miami Football Game"

def Cuban_Bank(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Cuban Bank to deposit 50.00 dollars.")
    if PAY >= 50:
        ACCOUNT += 50
        PAY -= 50
    else:
        print("insufficient funds")
#"Deposit money at Miami bank"
    return ACCOUNT, PAY, DATABASE_PARTS

def Cuban_store(ACCOUNT, PAY, DATABASE_PARTS):
    print("You went to the Cuban store to purchase goods which costed you 25.00 dollars.")
    PAY -= 25
    return ACCOUNT, PAY, DATABASE_PARTS
#"Purchase goods at Miami Store"






def main(character, realm, location, ACCOUNT, PAY, DATABASE_PARTS):
    print(location.get_name())
    if location.get_name() == character.get_job():
        while True:
            print("""Here, you can: 
        1) work
        2) leave""")
            answer=input("What do you want to do: ")
            if answer.lower()=="work" or "1" in answer:
                ACCOUNT, PAY, DATABASE_PARTS=work(ACCOUNT, PAY, DATABASE_PARTS)
                break
            if answer.lower()=="leave" or "2" in answer:
                ACCOUNT, PAY, DATABASE_PARTS=leave(ACCOUNT, PAY, DATABASE_PARTS)
                break
            else:
                print("Invalid Input")
                
    else:
        if "lab" in location.get_name() and "New York" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=new_york_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS)
        if "arena" in location.get_name() and "New York" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=new_york_sports_game(ACCOUNT, PAY, DATABASE_PARTS)
        if "bank" in location.get_name() and "New York" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=new_york_bank(ACCOUNT, PAY, DATABASE_PARTS)
        if "store" in location.get_name() and "New York" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=new_york_store(ACCOUNT, PAY, DATABASE_PARTS)
        if "lab" in location.get_name() and "Chicago" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Chicago_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS)
        if "arena" in location.get_name() and "Chicago" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Chicago_Tennis_Match(ACCOUNT, PAY, DATABASE_PARTS)
        if "bank" in location.get_name() and "Chicago" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Chicago_bank(ACCOUNT, PAY, DATABASE_PARTS)
        if "store" in location.get_name() and "Chicago" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Chicago_store(ACCOUNT, PAY, DATABASE_PARTS)
        if "lab" in location.get_name() and "Miami" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Miami_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS)
        if "arena" in location.get_name() and "Miami" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Miami_Football_Game(ACCOUNT, PAY, DATABASE_PARTS)
        if "bank" in location.get_name() and "Miami" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Miami_Bank(ACCOUNT, PAY, DATABASE_PARTS)
        if "store" in location.get_name() and "Miami" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Miami_store(ACCOUNT, PAY, DATABASE_PARTS)
        if "lab" in location.get_name() and "Washington D.C." in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Washington_DC_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS)
        if "arena" in location.get_name() and "Washington D.C." in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Washington_DC_sports_game(ACCOUNT, PAY, DATABASE_PARTS)
        if "bank" in location.get_name() and "Washington D.C." in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Washington_DC_bank(ACCOUNT, PAY, DATABASE_PARTS)
        if "store" in location.get_name() and "Washington D.C." in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Washington_DC_store(ACCOUNT, PAY, DATABASE_PARTS)
        if "Lab" in location.get_name() and "Cuba" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=cuba_Lab_tour(ACCOUNT, PAY, DATABASE_PARTS)
        if "Arena" in location.get_name() and "Cuba" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=cuba_poker_Game(ACCOUNT, PAY, DATABASE_PARTS)
        if "Bank" in location.get_name() and "Cuba" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Cuban_Bank(ACCOUNT, PAY, DATABASE_PARTS)
        if "Store" in location.get_name() and "Cuba" in realm.name:
            ACCOUNT, PAY, DATABASE_PARTS=Cuban_store(ACCOUNT, PAY, DATABASE_PARTS)

    return character, realm, location, ACCOUNT, PAY, DATABASE_PARTS
