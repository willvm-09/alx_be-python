task = input("Enter your task:")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority"
    case "medium":
        reminder = f"The task '{task}' is of medium priority"
    case "low":
        reminder = f"The task '{task}' is of low priority"
    case _:
        print("Invalid priority. PLease enter 'high', or 'low'.")
        exit()

if time_bound == 'yes':
    Reminder: += "It requires immediate attention today!."
    print('Reminder:')
    input{"Press Enter to continue...")
    print("Task completed!")
