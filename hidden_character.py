#The hidden_character.py allows the user to locate the hidden character which is a key component to winning the game.

import places
class HiddenCharacter:
    def __init__(self):
        self.pronouns=["He","Him", "is"]
        self.type="guy"

    class Realm_Cuba:
        def __init__(self):
            self.name="Cuba"
        class Lab:
            def __init__(self):
                self.purpose="Particle Physics"
                self.floors="5"
                self.testingunit="Physics Observation Lab"
                self.name="Cuba Lab"

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
                self.sport="Type of Sport"
                self.name="Cuba Sport Arena"

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
                self.name="Cuba Bank"

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
                self.name="Cuba Store"

            def get_name(self):
                return self.name

            def get_purpose(self):
                return self.purpose

            def get_merchandise(self):
                return self.merchandise

            def get_warehouse(self):
                return self.warehouse

    class Aldrich:
        def __init__(self):
            self.name="Aldrich"
            self.height="6'3\""
            self.age="41"
            self.personality="an industrious caretakers"
            self.realm=HiddenCharacter.Realm_Cuba()
            self.job=places.Cuba_lab.get_name()

        def get_job(self):
            return self.job
        
        def get_name(self):
            return self.name
        
        def get_height(self):
            return self.height
        
        def get_age(self):
            return self.age
        
        def get_personality(self):
            return self.personality
