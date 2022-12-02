from datetime import datetime
import os

now = datetime.now()
TimeRightNow = now.strftime('%I:%M %p') #12-hour format

# yes or no fucntion for the players option
yes = ["yes","Yes","YES","y","Y"]
no = ["no","No","NO","n","N"]

YesOrNO = ": Yes or No?"

#Invalid input
InvalidInput = "Invalid input. Plase use Yes or No for the input field."