import time
import pyttsx3
import os
from datetime import datetime
import keyboard

time_to_remind = 1  # How oten the user gets reminded (sec.) + the time it takes for the tts to finisish talking (4 sec.)

# Making a text to speach function
def tts(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# takes a reminder and returns the epoch time
def slicing(string):
    for i in range(len(string)):
        if string[-i] == " ":
            whitespace =  i
            break
    return int(string[-whitespace+1:])

time_unit_names = ["year", "month", "day", "hour", "minute", "second"]


class Deadline:
    def __init__(self,ID):
        self.ID = ID
        self.time_left = ID - time.time()
        self.years_left = time.gmtime(self.time_left)[0] - time.gmtime(0)[0]
        self.months_left = time.gmtime(self.time_left)[1] - time.gmtime(0)[1]
        self.days_left = time.gmtime(self.time_left)[2] - time.gmtime(0)[2]
        self.hours_left = time.gmtime(self.time_left)[3] - time.gmtime(0)[3]
        self.minutes_left = time.gmtime(self.time_left)[4] - time.gmtime(0)[4]
        self.seconds_left = time.gmtime(self.time_left)[5] - time.gmtime(0)[5]

        self.time_units = [self.years_left, self.months_left, self.days_left, 
                        self.hours_left, self.minutes_left, self.seconds_left]
        self.parts = []

    def print(self):
        print("Time left:",end=" ")

        for i in range(len(self.time_units)):
            if self.time_units[i] != 0:
                self.parts.append(str(self.time_units[i])+" "+time_unit_names[i])
                if self.time_units[i] > 1:
                    self.parts[-1] = self.parts[-1]+"s"
        if self.time_units[-1] == 0:
            self.parts.append(str(self.time_units[-1])+" "+time_unit_names[-1]+"s")

        for i in range(len(self.parts)):
            if self.parts[i] != self.parts[-1]:
                if self.parts[i] == self.parts[-2]: 
                    print(self.parts[i],end=" and ")
                else: print(self.parts[i],end=", ")
            else: print(self.parts[i])


# Main loop
while True:
    choice = input("What would you like to do? [1-4 / END]\n1. Add reminder\n2. Remove reminder\n3. See all reminders\n4. Track reminder\n")
    
    if choice == "1":
        os.system("cls")
        with open("reminder_add.py") as file:
            exec(file.read())
            
    elif choice == "2" or choice == "4":
        os.system("cls")
        f = open("reminders.txt", "r")
        readline = f.readlines()
        for num, line in enumerate(readline, 1):
            print(f"{num}: {line}")
        if choice == "2":
            while True:
                Removed_reminder = input(f"Which reminder would you liken to remove? [1-{num}]\n")
                if Removed_reminder.isnumeric():
                    Removed_reminder = int(Removed_reminder)
                    if Removed_reminder<=num:
                        break
            os.system("cls")
            f = open("reminders.txt", "w")
            for num, line in enumerate(readline, 1):
                if num != Removed_reminder:
                    f.write(f"{line}")
            f.close()
        elif choice == "4":
            targeted_reminder = input(f"Which reminder would you liken to track? [1-{num}]\n")
            targeted_reminder = int(targeted_reminder)
            for num, line in enumerate(readline, 1):
                if num == targeted_reminder:
                    deadline = slicing(line)
                    print(line)
                    print(deadline)
                run = True
            while run:
                os.system("cls")
                if deadline-time.time() > 0:
                    os.system("cls")
                    print("Deadline:", time.ctime(deadline), "\n")
                    curr = time.ctime(time.time())
                    print("Time right now:", curr, "\n")
                    D1 = Deadline(deadline)
                    D1.print()
                    secondsTime = time.mktime(time.gmtime())
                    while True:
                        if secondsTime != time.mktime(time.gmtime()):
                            break
                        if keyboard.is_pressed("esc"):
                           os.system("cls")
                           run = False  
                        else: continue
                else:
                    # Write here what's going to happen once deadline is met.
                    message = "Time's up"
                    print(message)
                    tts(message)
                    break
                
    elif choice == "3":
        os.system("cls")
        f = open("reminders.txt", "r")
        readline = f.readlines()
        print()
        for line in readline:
            print(f"{line}\n")
            
    elif choice.upper() == "END":
        exit()
    else:
        os.system("cls")
        print("Option not available, please type a number from [1-4] or END.\n")
