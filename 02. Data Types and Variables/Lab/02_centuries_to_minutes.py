centuries = int(input())
years = centuries * 100

days_of_tropical_year = 365.2422

days = int(years * days_of_tropical_year)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")