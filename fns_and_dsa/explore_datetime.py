from datetime import datetime, timedelta

def display_current_datetime():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current  date and time: {current_date}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.now() + timedelta(days = number_of_days)
    chosen_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {chosen_date}")

calculate_future_date()
