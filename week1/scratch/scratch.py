
from datetime import datetime


current_time = datetime.now()
print(f"Current time: {current_time}")
day_of_week = current_time.weekday()
print(f"Day of the week (0=Monday, 6=Sunday): {day_of_week}")