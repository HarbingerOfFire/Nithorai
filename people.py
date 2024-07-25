#The people.py program will allow the user to select their character to play as. As well as characteristics of each player. 

#class of characters in the game
import places, hidden_character


class People:
    class AiCharaters:
        def __init__(self):
            self.pronouns=["They","Them","are"]
            self.type="AI"

        def get_pronouns(self):
            return self.pronouns
        
        class Azure:
            def __init__(self):
                self.name="Azure"
                self.height="6'0\""
                self.age="56"
                self.personality="an analytical problem-solver"
                self.realm=places.Places.Realm_New_York()
                self.job=places.New_york_lab.get_name()

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
            
        class Mig:
            def __init__(self):
                self.name="Mig"
                self.height="6'0\""
                self.age="62"
                self.personality="a gentle caretaker"
                self.realm=places.Places.Realm_Chicago()
                self.job=places.Chicago_lab.get_name()

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
    
    class MaleCharacters:
        def __init__(self):
            self.pronouns=["He","Him","is"]
            self.type="man"

        def get_pronouns(self):
            return self.pronouns

        class John:
            def __init__(self):
                self.name="John"
                self.height="5'10\""
                self.age="32"
                self.personality="a philosophical innovator"
                self.realm=places.Places.Realm_Miami()
                self.job=places.Miami_lab.get_name()

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
            
        class Michael:
            def __init__(self):
                self.name="Michael"
                self.height="6'2\""
                self.age="29"
                self.personality="an idealist organizer"
                self.realm=places.Places.Realm_Washington_DC()
                self.job=places.Washington_store.get_name()

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
            
        class Tobias:
            def __init__(self):
                self.name="Tobias"
                self.height="6'0\""
                self.age="26"
                self.personality="an energetic thrillseeker"
                self.realm=places.Places.Realm_New_York()
                self.job=places.New_york_arena.get_name()

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

    class FemaleCharacters:
        def __init__(self):
            self.pronouns=["She","Her","is"]
            self.type="woman"

        def get_pronouns(self):
            return self.pronouns

        class Chloe:
            def __init__(self):
                self.name="Chloe"
                self.height="5'4\""
                self.age="23"
                self.personality="a creative nuturer"
                self.realm=places.Places.Realm_Chicago()
                self.job=places.Chicago_store.get_name()

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
            
        class Hailey:
            def __init__(self):
                self.name="Hailey"
                self.height="5'7\""
                self.age="28"
                self.personality="a strategic leader"
                self.realm=places.Places.Realm_Chicago()
                self.job=places.Chicago_arena.get_name()

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
            
        class Sarah:
            def __init__(self):
                self.name="Sarah"
                self.height="5'3\""
                self.age="22"
                self.personality="an observant artisan"
                self.realm=places.Places.Realm_Miami()
                self.job=places.Miami_store.get_name()

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
    
    class NonbinaryCharacters:
        def __init__(self):
            self.pronouns=["They","Them", "are"]
            self.type="non-binary person"

        def get_pronouns(self):
            return self.pronouns

        class Alex:
            def __init__(self):
                self.name="Alex"
                self.height="5'5\""
                self.age="26"
                self.personality="an imaginative idealist"
                self.realm=places.Places.Realm_New_York()
                self.job=places.New_york_store.get_name()

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

        class Max:
            def __init__(self):
                self.name="Max"
                self.height="5'11\""
                self.age="25"
                self.personality="an inspired innovator"
                self.realm=places.Places.Realm_Washington_DC()
                self.job=places.Washington_lab.get_name()

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
            
        class Sam:
            def __init__(self):
                self.name="Sam"
                self.height="5'6\""
                self.age="30"
                self.personality="a responsible organizer"
                self.realm=places.Places.Realm_Washington_DC()
                self.job=places.Washington_arena.get_name()

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

mig=People.AiCharaters.Mig()
azure=People.AiCharaters.Azure()
john=People.MaleCharacters.John()
michael=People.MaleCharacters.Michael()
tobias=People.MaleCharacters.Tobias()
chloe=People.FemaleCharacters.Chloe()
hailey=People.FemaleCharacters.Hailey()
sarah=People.FemaleCharacters.Sarah()
alex=People.NonbinaryCharacters.Alex()
sam=People.NonbinaryCharacters.Sam()
max=People.NonbinaryCharacters.Max()
aldrich=hidden_character.HiddenCharacter.Aldrich()

def set_character(name):
    if name.lower() == "mig":
        character=mig
        type=People.AiCharaters()
    elif name.lower() == "azure":
        character=azure
        type=People.AiCharaters()
    elif name.lower() == "john":
        character=john
        type=People.MaleCharacters()
    elif name.lower() == "michael":
        character=michael
        type=People.MaleCharacters()
    elif name.lower() == "tobias":
        character=tobias
        type=People.MaleCharacters()
    elif name.lower() == "chloe":
        character=chloe
        type=People.FemaleCharacters()
    elif name.lower() == "hailey":
        character=hailey
        type=People.FemaleCharacters()
    elif name.lower() == "sarah":
        character=sarah
        type=People.FemaleCharacters()
    elif name.lower() == "alex":
        character=alex
        type=People.NonbinaryCharacters()
    elif name.lower() == "sam":
        character=sam
        type=People.NonbinaryCharacters()
    elif name.lower() == "max":
        character=max
        type=People.NonbinaryCharacters()
    elif name.lower() == "aldrich":
        character=aldrich
        type=hidden_character.HiddenCharacter()
    else:
        message="Invalid Input"
        print(message)
        character="Invalid Input"
        type=message

    return character, type
