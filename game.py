from DontEdit import *
from CanEdit import *
import time

wait = time.sleep
print(f"Input your name")
playerName = input(">>> ")
name = playerName.capitalize()

def start():
      print(f'''You get up and get dressed.''',
            f'''\nYou hear your phone ringing.''')

      print(f'''\nDo you pick up the phone: {YesOrNO}''')

      choice = input(">>> ")
      #you pick up the phone and 
      if choice in yes:
            print(f'''\nYou look at the caller ID and find it's your friend {FriendsName}.''',
                  f'''\n“Hello {FriendsName} how are you doing?”''',
                  f'''\n“Good how are you {name}?”''',
                  f'''\n“I'm doing good thanks for asking.” You say.'''
                  f'''\n"Hey I have to go can I call you back."''')
            HangUp();

      #You dont pick up the phone and desided to go to work 
      elif choice in no:
            print(f'''You look at the caller ID and find its your friend {FriendsName}''',
                  f'''\n“I can call him back.” You think to yourself.''')
            outside();

      #if the users doent input anythin it say InvalidInput
      else:
            print(f'''{InvalidInput}''')
      
#player hanges up so they can go to work
def HangUp():
      print(f'''“Can I call you back? I have to go to work.” You say to your friend.''',
            f'''\n“Ya sure.” He replies.''')
      outside();

#player goes outside to get in there car
def outside():
      print(f'''\nYou go outside and look around and see the street filled with people going along with their business.''',
            f'''\n“Man, this city never sleeps." You think to yourself.''',
            f'''\nYou walk towards your {PlayerCar} and start it up. The car hums with life.''',
            f'''\n“You haven't left me yet have you.” You say to your old car.''')
      DriveToWork();

def DriveToWork():
      print(f'''\nYou get on the highway and find that there is traffic.''',
            f'''\nYou look at your watch and see that the time is {time}.''',
            f'''\nAfter a while you get to work.''')
      work();

def work():
      print(f'''\nYou get to work and clock in like you do every day.''',
            f'''\nYou go to your desk and turn on your computer.''',
            f'''\n"Time to get back to work." You say to yourself.''')
      wait(2)
      print(f'''\nAs you get lost in your job you hear on the P.A "This is not a drill we are going on lock down!"''')
start()