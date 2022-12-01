from game import *
from DontEdit import *
def gameOver():

    print(f'''\nGame over''',
          f'''\nDo you want to play again: {YesOrNO}''')
    
    choice = input(">>> ") 
    
    if choice in yes:
        start()

    elif choice in no:
        print(f"Good bye")
        print(f'Writer: wilsegale')
        print(f'Programmer: wilsegale')
        print(f'Developer: wilsegale')
        os.system('exit')
    else:
        return gameOver()
gameOver()