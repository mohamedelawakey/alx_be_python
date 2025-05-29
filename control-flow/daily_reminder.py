task = input('Enter your task: ')
Priority = input('Priority (high/medium/low): ')
time_bound = input('Is it time-bound? (yes/no): ')

match Priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Remember: '{task}' is a high priority task. Try to complete it soon.")
    case 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a medium priority task that still needs to be done today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Plan it into your schedule.")
    case 'low':
        if time_bound == 'yes':
            print(f"'{task}' is a low priority task, but it's time-sensitive. Try to do it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    