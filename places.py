#The Places.py will allow for the user to select the realm and location within the realm, i.e. laboratory, sports arena, bank, or store. 

import hidden_character
class Places:
    class Realm_New_York:
        def __init__(self):
            self.name="New York"

        class Lab:
            def __init__(self):
                self.purpose="AI Construction"
                self.floors="5"
                self.testingunit="AI testing facility"
                self.name="New York lab"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_floors(self):
                return self.floors

            def get_testingunit(self):
                return self.testingunit

        class Sports_arena:
            def __init__(self):
                self.purpose="Sporting events"
                self.teams="12 teams"
                self.sport="Baseball"
                self.name="New York Sport arena"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_teams(self):
                return self.teams

            def get_sport(self):
                return self.sport
            
        class Bank:
            def __init__(self):
                self.purpose="Money Transactions"
                self.vault="Money Storage"
                self.ATM="Withdrawal Funds System"
                self.name="New York bank"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_vault(self):
                return self.vault

            def get_ATM(self):
                return self.ATM

        class Store:
            def __init__(self):
                self.purpose="Sell goods"
                self.merchandise="Sell Merchandise"
                self.warehouse="Merchandise storage unit in back of store"
                self.name="New York store"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_merchandise(self):
                return self.merchandise

            def get_warehouse(self):
                return self.warehouse

    class Realm_Washington_DC:
        def __init__(self):
            self.name="Washington D.C."

        class Lab:
            def __init__(self):
                self.purpose="AI Construction"
                self.floors="5"
                self.testingunit="AI testing facility"
                self.name="Washington DC lab"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_floors(self):
                return self.floors

            def get_testingunit(self):
                return self.testingunit

        class Sports_arena:
            def __init__(self):
                self.purpose="Sporting events"
                self.teams="12 teams"
                self.sport="Basketball"
                self.name="Washington DC Sport arena"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_teams(self):
                return self.teams

            def get_sport(self):
                return self.sport
            
        class Bank:
            def __init__(self):
                self.purpose="Money Transactions"
                self.vault="Money Storage"
                self.ATM="Withdrawal Funds System"
                self.name="Washington DC bank"

            def get_name(self):
                return self.name 

            def get_purpose(self):
                return self.purpose

            def get_vault(self):
                return self.vault

            def get_ATM(self):
                return self.ATM

        class Store:
            def __init__(self):
                self.purpose="Sell good"
                self.merchandise="Sell Merchandise"
                self.warehouse="Merchandise storage unit in back of store"
                self.name="Washington DC store"

            def get_name(self):
                return self.name 

            def get_purpose(self):
                return self.purpose

            def get_merchandise(self):
                return self.merchandise

            def get_warehouse(self):
                return self.warehouse

    class Realm_Chicago:
        def __init__(self):
            self.name="Chicago"

        class Lab:
            def __init__(self):
                self.purpose="AI Construction"
                self.floors="5"
                self.testingunit="AI testing facility"
                self.name="Chicago lab"

            def get_name(self):
                return self.name

            def get_testingunit(self):
                return self.testingunit

            def get_purpose(self):
                return self.purpose

            def get_floors(self):
                return self.floors

        class Sports_arena:
            def __init__(self):
                self.purpose="Sporting events"
                self.teams="12 teams"
                self.sport="Tennis"
                self.name="Chicago Sport arena"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_teams(self):
                return self.teams

            def get_sport(self):
                return self.sport
            
        class Bank:
            def __init__(self):
                self.purpose="Money Transactions"
                self.vault="Money Storage"
                self.ATM="Withdrawal Funds System"
                self.name="Chicago bank"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_vault(self):
                return self.vault

            def get_ATM(self):
                return self.ATM

        class Store:
            def __init__(self):
                self.purpose="Sell good"
                self.merchandise="Sell Merchandise"
                self.warehouse="Merchandise storage unit in back of store"
                self.name="Chicago store"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_merchandise(self):
                return self.merchandise

            def get_warehouse(self):
                return self.warehouse

    class Realm_Miami:
        def __init__(self):
            self.name="Miami"

        class Lab:
            def __init__(self):
                self.purpose="AI Construction"
                self.floors="5"
                self.testingunit="AI testing facility"
                self.name="Miami lab"

            def get_name(self):
                return self.name

            def get_testingunit(self):
                return self.testingunit

            def get_purpose(self):
                return self.purpose

            def get_floors(self):
                return self.floors

        class Sports_arena:
            def __init__(self):
                self.purpose="Sporting events"
                self.teams="12 teams"
                self.sport="Football"
                self.name="Miami Sport arena"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_teams(self):
                return self.teams

            def get_sport(self):
                return self.sport
            
        class Bank:
            def __init__(self):
                self.purpose="Money Transactions"
                self.vault="Money Storage"
                self.ATM="Withdrawal Funds System"
                self.name="Miami bank"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_vault(self):
                return self.vault

            def get_ATM(self):
                return self.ATM

        class Store:
            def __init__(self):
                self.purpose="Sell good"
                self.merchandise="Sell Merchandise"
                self.warehouse="Merchandise storage unit in back of store"
                self.name="Miami store"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_merchandise(self):
                return self.merchandise

            def get_warehouse(self):
                return self.warehouse


New_york_lab=Places.Realm_New_York.Lab()
New_york_arena=Places.Realm_New_York.Sports_arena()
New_york_bank=Places.Realm_New_York.Bank()
New_york_store=Places.Realm_New_York.Store()

Washington_lab=Places.Realm_Washington_DC.Lab()
Washington_arena=Places.Realm_Washington_DC.Sports_arena()
Washington_bank=Places.Realm_Washington_DC.Bank()
Washington_store=Places.Realm_Washington_DC.Store()

Chicago_lab=Places.Realm_Chicago.Lab()
Chicago_arena=Places.Realm_Chicago.Sports_arena()
Chicago_bank=Places.Realm_Chicago.Bank()
Chicago_store=Places.Realm_Chicago.Store()

Miami_lab=Places.Realm_Miami.Lab()
Miami_arena=Places.Realm_Miami.Sports_arena()
Miami_bank=Places.Realm_Miami.Bank()
Miami_store=Places.Realm_Miami.Store()

Cuba_lab=hidden_character.HiddenCharacter.Realm_Cuba.Lab()
Cuba_arena=hidden_character.HiddenCharacter.Realm_Cuba.Sports_arena()
Cuba_bank=hidden_character.HiddenCharacter.Realm_Cuba.Bank()
Cuba_store=hidden_character.HiddenCharacter.Realm_Cuba.Store()
