import datetime
def display_current_datetime():
  current_date =  datetime.datetime.now()
  current_date = current_date.strf("%Y - %m - %d %H : %M : %S")
  print ("Current date and time:", current_date)
no_of_days = int(input("Enter the number of days to add to the current date:"))
from datetime import datetime, timedelta
duration = timedelta(days = no_of_days)
def calculate_future_date():
  future_date = current_date + duration
  future_date = future_date.strf("%Y - %m - %d")
  print("Future date:", future_date)
