import time
import os


time_unit_names = ["year", "month", "day", "hour", "minute", "second"]

year_min = time.localtime().tm_year
year_max = 2999
month_min = time.localtime().tm_mon
month_max = 12
day_min = time.localtime().tm_mday
day_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
hour_min = time.localtime().tm_hour
hour_max = 23
minute_min = time.localtime().tm_min
minute_max = 59
second_min = time.localtime().tm_sec
second_max = 59

leap_year = False
msg2 = ""

class Definer:
    def __init__(self, name, unit):
        self.name = name
        self.unit = time_unit_names[unit]
    def Checker(self, min_num, max_num, msg1, unit):
        global year_min, month_min, day_min, hour_min, minute_min, second_min
        while True:
            os.system("cls")
            self.name = self.unit
            msg2 = f"Please enter the {self.unit}. Number must be between {min_num}-{max_num}"
            print(f"{msg2}\n\n{msg1}\n")
            self.name = input(f"{self.name}: ")

            if self.name.isnumeric() and int(self.name) <= max_num and int(self.name) >= min_num:
                self.name = int(self.name)
                break
        if unit == 0 and self.name > year_min:
            month_min = 1
            day_min = 1
            hour_min = 0
            minute_min = 0
            second_min = 0
        elif unit == 1 and self.name > month_min:
            day_min = 1
            hour_min = 0
            minute_min = 0
            second_min = 0
        elif unit == 2 and self.name > day_min:
            hour_min = 0
            minute_min = 0
            second_min = 0
        elif unit == 3 and self.name > hour_min:
            minute_min = 0
            second_min = 0
        elif unit == 4 and self.name > minute_min:
            second_min = 0

                
os.system("cls")          

name = input("Deadline name: ")


year = Definer("year", 0)
year.Checker(year_min, year_max, f"{name.upper()}: YYYY/MM/DD HH:MM:SS", 0)

if year.name % 4 == 0:
    if year.name % 400 == 0:
        leap_year = True
    elif year.name % 100 == 0:
        pass
    else:
        leap_year = True

month = Definer("month", 1)
month.Checker(month_min, month_max, f"{name.upper()}: {year.name}/MM/DD HH:MM:SS", 1)

if leap_year == True and month.name == 2:
    day_max[1] = 29

day = Definer("day", 2)
day.Checker(day_min, day_max[month.name-1], f"{name.upper()}: {year.name}/{month.name}/DD HH:MM:SS", 2)


hour = Definer("hour", 3)
hour.Checker(hour_min, hour_max, f"{name.upper()}: {year.name}/{month.name}/{day.name} HH:MM:SS", 3)


minute = Definer("minute", 4)
minute.Checker(minute_min, minute_max, f"{name.upper()}: {year.name}/{month.name}/{day.name} {hour.name}:MM:SS", 4)


second = Definer("second", 5)
second.Checker(second_min, second_max, f"{name.upper()}: {year.name}/{month.name}/{day.name} {hour.name}:{minute.name}:SS", 5)

os.system("cls")

from datetime import datetime

# Create a datetime object from the extracted elements
dt = datetime(year.name, month.name, day.name, hour.name, minute.name, second.name)

# Convert the datetime object to epoch time
epoch_time = int(dt.timestamp())

f = open("reminders.txt", "a")
f.write(f"\n{name}: {epoch_time}")
f.close()
