#The settings.py will allow the user to load and save data, as well as leave the game and show map. 

import time, nithorai, movement, tkinter
from PIL import ImageTk, Image

def load_data():
    with open("save_data.txt", "r") as in_file:
        ACCOUNT=int(in_file.readline(-1))
        PAY=int(in_file.readline(-2))
        DATABASE_PARTS=int(in_file.read(-3))
    return ACCOUNT, PAY, DATABASE_PARTS

def save_data(ACCOUNT,PAY, DATABASE_PARTS):
    print("Saving...")
    with open("save_data.txt", "w") as out_file:
        out_file.write(str(ACCOUNT)+"\n")
        out_file.write(str(PAY)+"\n")
        out_file.write(str(DATABASE_PARTS))
    print("Data is saved.")

def leave_game():
    print(f"Thanks for playing!")
    time.sleep(1)
    exit()

def show_map():
    root = tkinter.Tk()
    root.title("Nitho-Rai Map")
    img = ImageTk.PhotoImage(Image.open("Dystopia_map.png"))
    panel = tkinter.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()

def main(character, location, ACCOUNT, PAY, DATABASE_PARTS):
    while True:
        answer=input("""1) Change Character
2) Save Game State
3) Leave Game
4) Show Map

What do you want to do: """)
        
        if "change" in answer.lower() or "1" in answer:
            save_data(ACCOUNT, PAY, DATABASE_PARTS)
            nithorai.main()
        elif "save" in answer.lower() or "2" in answer:
            save_data(ACCOUNT, PAY, DATABASE_PARTS)
        elif "leave" in answer.lower() or "3" in answer:
            save_data(ACCOUNT, PAY, DATABASE_PARTS)
            leave_game()
        elif "map" in answer.lower() or "4" in answer:
            show_map()
        else: print("Invalid Input")
        return character, location, ACCOUNT, PAY, DATABASE_PARTS
