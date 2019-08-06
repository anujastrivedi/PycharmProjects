# Create a Time class and initialize it with hours and minutes.
# 1. Make a method addTime which should take two time object and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method displayTime which should print the time.
# 3. Make a method DisplayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def display_time(self):
        time = f"{self.hours} hours and {self.minutes} minutes"
        return time

    def __str__(self):
        return self.display_time()


t1 = Time(3, 15)
t2 = Time(5, 55)


def add_time(time1, time2):
    minutes = time1.minutes + time2.minutes
    total_minutes = minutes % 60
    total_hours = (time1.hours + time2.hours) + int(minutes / 60)

    total_time = f"{total_hours} hours and {total_minutes} minutes"

    print(f"{time1} + {time2} is {total_time}")


def display_minute(time1):
    minutes = (time1.hours * 60) + time1.minutes
    print(f"{time1} is {minutes} minutes")


add_time(t1, t2)
display_minute(t1)
