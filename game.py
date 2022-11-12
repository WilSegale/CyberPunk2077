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
                  f'''\n“I'm doing good thanks for asking.” You say.''')
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
      print(f'''\n“Can I call you back? I have to go to work.” You say to your friend.''',
            f'''\n“Ya sure.” He replies.''')
      outside();

#player goes outside to get in there car
def outside():
      print(f'''\nYou go outside and look around and see the street filled with people going along with their business.''',
            f'''\n“Man, this city never sleeps." You think to yourself.''',
            f'''\nYou walk towards your {PlayerCar} and start it up. The car hums with life.''',
            f'''\n“You haven't left me yet have you.” You say to your old car.''')
      DriveToWork();

#player goes to work and gets stuck in traffic
def DriveToWork():
      print(f'''\nYou get on the highway and find that there is traffic.''',
            f'''\nYou look at your watch and see that the time is {TimeRightNow}.''',
            f'''\nAfter a while you get to work.''')
      work();

#player gets into work and clocks in
def work():
      print(f'''\nYou get to work and clock in like you do every day.''',
            f'''\nYou go to your desk and turn on your computer.''',
            f'''\n"Time to get back to work." You say to yourself.''')
      wait(2)
      print(f'''"Hey {playerName} we are going to get lunch want to come?"''')
      
      print(f'''\nDo you get lunch with your co-workres. {YesOrNO}''')
      
      choice = input(">>> ")

      if choice in yes:
            getLunch();

      elif choice in no:
            getBackToWork()
      
      else:
            print(f'''{InvalidInput}''')

#player gets lunch with there co-workres
def getLunch():
      print(f'''\n"Ya sure I'll have lunch with you guys." You say to your co-workres.''',
            f'''\nYou and your co-workres walk to get lunch at the nearest resteront.''',
            f'''\nYou sit down at your seat and talk to your co-workres.''',
            f'''\nAfter you finish eating you and your co-workres go back to work.''')
      BackToWork();

#player doesnt go and get lunch with there co-workres
def getBackToWork():
      print(f'''\n"Sorry I cant I have a lot of work to do. Mabye next time?"''')
      BackToWork()

#player goes back to work and then gets called to the bosses office
def BackToWork():
      print(f'''\nYou get back to work. 5 minutes later you hear your boss say''',
            f'''\n"Hey {playerName} can I talk to you in my office?"''',
            f'''\nYou start to get scared that you did something wrong, but you keep your compuoser and say''',
            f'''\n"Ya sure Im coming right now."''')
      GoToTheBossOffice();

#player goes into the bosses office and gets talked too
def GoToTheBossOffice():
      print(f'''\n"I would like to talk to you about the sales that have happend." Your boss tells you.''')
  
start()