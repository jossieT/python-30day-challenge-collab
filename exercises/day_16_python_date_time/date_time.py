from datetime import datetime, date
# Exercises: Day 16
#1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)
year  = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
time_stamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', time_stamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time)
#3. Today is 5 December, 2019. Change this time string to time.
date_string = " 5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
#4. Calculate the time difference between now and new year.
today_= date(year=2025, month=7, day=20)
new_year = date(year=2026, month=1, day=1)
time_left_for_newyear = new_year - today_

print('Time left for new year: ', time_left_for_newyear)
t1 = now
t2 = datetime(year = 2026, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
#5. Calculate the time difference between 1 January 1970 and now.
t11 = datetime(year=1970, month=1,day=1, hour=0, minute=0, second=0)
t22 = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
time_difference = t22-t11
print(f"The time difference betwen 1 January 1970 and now is {time_difference}")
#6. Think, what can you use the datetime module for? Examples:
#. Time series analysis
#. To get a timestamp of any activities in an application
#. Adding posts on a blog
#. Scheduling tasks
#. Logging events with timestamps
#. To calculate age from birthdate
#. To calculate the time difference between two events
#. To create timelines for projects
#. To schedule reminders or events
#. To track user activity in applications
#. To analyze user behavior over time
#. To generate reports based on time intervals
#. To create time-based visualizations
#. To manage time zones in applications
#. To handle recurring events or tasks
#. To calculate deadlines for tasks or projects
#. To record login information
#. To track changes in data over time
#. To create time-based notifications
#. To manage time-sensitive data in databases
#. To implement time-based access control
#. To create time-based filters in data analysis
#. To analyze trends over time
