from DontEdit import *
import os

def start():
    print(f"You get out of bed and get dressed.",
          f"\nYou hear something ringing.")
    
    print(f"\nDo you see find what's ringing: {YesOrNO}?")

    choice = input(">>> ")
    #You find whats ringin
    if choice in yes:
        print(f"You find what the ringing is, and find out that it's your phone.",
              f"\n")
              
    #You leave your aparment
    elif choice in no:
        print(f"You walk out the door with out checking what the ring is")
    
    else:
        os.system('clear')
        return start()





start()