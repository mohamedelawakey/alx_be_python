from datetime import datetime, timedelta

def display_current_datetime ():
    current_date = datetime.now()
    print(current_date)
    
def calculate_future_date():
    current_date = datetime.now()
    num_of_days = int(input('Enter the number of days to add to the current date: '))
    
    tdelta = timedelta(days = num_of_days)
    future_date = current_date  + tdelta  
    
    print('Future date: ', future_date.date())
    
display_current_datetime()
calculate_future_date()