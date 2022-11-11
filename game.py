from DontEdit import *
from CanEdit import *
import os

print(f"Input your name")
playerName = input(">>> ")
name = playerName.capitalize()

def start():
    print(f"You get out of bed and get dressed.",
          f"\nYou hear something ringing.")
    
    print(f"\nDo you see find what's ringing: {YesOrNO}")

    choice = input(">>> ")
    #You find whats ringin
    if choice in yes:
        print(f'''You find what the ringing is, and find out that it's your phone.''',
              f'''\nYou pick up your phone and answer saying. "Hello this is {name}."''',
              f'''\n"Hello {name} this is your landloard. You are behind on your rent."''')
        
        print(f'''\nDo you tell him how much you have on you right now: {YesOrNO}''')

        choice = input(">>> ")

        if choice in yes:
            print(f'''"Ya sorry about that. I only have ${PlayerCash} on me right now will that work?"''',
                  f'''\n"Your rent is $4942. I'll take it but you will still own me ${int(4942) - PlayerCash}"''',
                  f'''"How am I going to make that much money?" You think to yourself.''')

    #You leave your aparment
    elif choice in no:
        print(f'''You walk out the door without checking what the ringing is.''',
              f'''\nAs you walk out the door you rilise your forgot your phone.''',
              f'''\n"Ah shit I forgot my phone"''')
    
    #if the user donet input the correct input value
    else:
        os.system('clear')
        return start()
start()