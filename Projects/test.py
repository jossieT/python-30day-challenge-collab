from datetime import datetime, date
today = date.today()
registration_year = today.strftime("%Y-%m-%d")

print(registration_year.split("-")[0][2:])