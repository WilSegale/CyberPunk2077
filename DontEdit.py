from datetime import datetime
import time

now = datetime.now()
TimeRightNow = now.strftime('%I:%M %p') #12-hour format

# yes or no function for the players option
yes = ["yes","Yes","YES","y","Y"]
no = ["no","No","NO","n","N"]

YesOrNO = ": Yes or No?"

#Invalid input
InvalidInput = "Invalid input. plz use Yes or No for the input field."