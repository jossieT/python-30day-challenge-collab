from datetime import datetime
#Exercises: Day 16
#1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
current_date = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
timestamp = now.timestamp()

print(current_date, current_month, current_year)
print(current_hour,":", current_minute)
print(timestamp)

#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

#3. Today is 5 December, 2019. Change this time string to time.
string_time = "5 December, 2019"
date_object = datetime.strptime(string_time, "%d %B, %Y")
print(date_object)

#4. Calculate the time difference between now and new year.
current_date = datetime.now()
new_year = datetime(2026, 1, 1)
diff = new_year - current_date
print(diff)

#5. Calculate the time difference between 1 January 1970 and now.
current_date = datetime.now()
str_date = "1 January, 1970"
date_object = datetime.strptime(str_date, "%d %B, %Y")
difference = current_date - date_object
print(difference)

#6. Think, what can you use the datetime module for? Examples:
#Time series analysis
#To get a timestamp of any activities in an application
#Adding posts on a blog
"""
Calculating time differences

Scheduling tasks or events

Setting expiration dates

Naming files with timestamps

Calculating age or durations

Converting between time zones

Delaying execution or setting wait times

Sorting records by date

Logging events

Generating reports with dates

Filtering data by date ranges

Measuring code execution time
"""
