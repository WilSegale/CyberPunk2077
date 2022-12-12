# Programer: will segale
# Date: 12/01/22
# Description: CyberPunk2077 Game Program
# Mod history
# Programer, date, Mod Descrptioin
# Will Segale, 12/01/22, intele code

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

      print(f'''\nDo you pick up the phone{YesOrNO}''')

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
            return start()
      
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
      
      print(f'''\nDo you get lunch with your co-workres{YesOrNO}''')
      
      choice = input(">>> ")

      if choice in yes:
            getLunch();

      elif choice in no:
            getBackToWork()
      
      else:
            print(f'''{InvalidInput}''')
            return work()

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
      print(f'''You get back to work. 5 minutes later you hear your boss say''',
            f'''\n"Hey {playerName} can I talk to you in my office?"''',
            f'''\nYou start to get scared that you did something wrong, but you keep your compuoser and say''',
            f'''\n"Ya sure Im coming right now."''')
      GoToTheBossOffice();

#player goes into the bosses office and gets talked too
def GoToTheBossOffice():
      print(f'''\n"I would like to talk to you about the sales that have happend." Your boss tells you.''',
            f'''\n"Ya what abouth them?" You ask your boss.''',
            f'''\n"They are riseing at a fast rate. I think this is because of you?" He says''',
            f'''\n"Thank you boss. Is that all? Can I go back to work" You say.''',
            f'''\n"What, oh yes you can go back to work." He says.''',
            f'''\n*8 hours later* "Time to go back home."''')
      home()

#player gets home and calls friend
def home():
      print(f'''\nAs you get home you pick up your phone and call your friend.''',
            f'''\n"Hello {FriendsName} how are you doing sorry for the long wait"''',
            f'''\n"That's ok I understand that you have work to do." He says'''
            f'''\nYou talk for awhile and then go to bed''')
      wakeUp()

#player wakeups and see there sister in there appartment 
def wakeUp():
      print(f'''\nYou wake up and get dressed for work.''',
            f'''\nYou walk down stairs and find your sister at the table''',
            f'''\n"What are you doing here?" You say.''',
            f'''\nYour sister looks at you and says. "What you dont want to see me?"''',
            f'''\n"No dont get me wrong it's greate to see you again."''',
            f'''\n"But I have work soon. So can you plase get out of my way so I can get to work?"''',
            f'''\n"Can we talk I have something important to tell you." She says to you.''')
      
      print(f'''\nDo you hear what she has to say to you{YesOrNO}''')

      choice = input(">>> ")

      if choice in yes:
            hearHerOut();

      elif choice in no:
            dontHearHerOut();

      else:
            print(f'''{InvalidInput}''')
            return wakeUp()

#Player hears what there sister has to say
def hearHerOut():
      print(f'''\n"Ok you have 5 minutes." You say to your sister.''',
            f'''\n"Ok {playerName} I have a job for you the client will pay you very well." She says.''',
            f'''\n"Ok you have my attention." You say'''
            f'''\n"Ok so it pays you at least 10K"''')
      ThinkAboutIt();

#Player doesn't hears what there sister has to say
def dontHearHerOut():
      print(f'''\n"Sorry but I really have to go to work" You say to your sister''',
            f'''\n"Can I at least give you my new number, so you can call me if you change you mind?" She says.''')
      
      print(f'''Do you let your sister give you her number{YesOrNO}''');
      choice = input(">>> ")

      if choice in yes:
            SayOk()

      elif choice in no:
            SayNo()

      else:
            print(f'''{InvalidInput}''')
            return dontHearHerOut()
      
#player thinks about the job
def ThinkAboutIt():
      print(f'''\n"Ok I'll think about it." You say to your sister''',
            f'''\nYour sister walks out of your aparment''',
            f'''\n"At last I can think about what she said about the job." You think to yourself.''',
            f''' \nYou start to get tired and think about heading to bed. But you still have a lot of work to do.''')

def SayOk():
      print(f'''\n"Fine I'll take your number if I change my mind." You say.''',
            f'''\n"Ok heres my number 818-240-6888." She says''',
            f'''\n"Thanks {SisterName}"''')

def SayNo():
      print(f'''\n"Looks like your time is up. Now plase get out of my appartment please." You say to your sister.''')
      
start()