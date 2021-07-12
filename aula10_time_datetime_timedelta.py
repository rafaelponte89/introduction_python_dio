from datetime import date, time, datetime, timedelta

def working_with_datetime():
    current_date = datetime.now()
    print(current_date)
    print(current_date.strftime('%d/%m/%Y %H:%M:%S'))
    print(current_date.strftime('%c'))
    print(current_date.year)
    print(current_date.microsecond)
    print(current_date.weekday())
    print(current_date.month)
    tuple_week = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tuple_week[current_date.weekday()])
    date_created = datetime(2018, 6, 20,15,30,20)
    print(date_created)
    print(date_created.strftime('%c'))
    date_str = '01/01/2019 12:20:22'
    date_converted = datetime.strptime(date_str,'%d/%m/%Y %H:%M:%S')
    print(date_converted)
    print(date_converted.weekday())
    # using timedelta
    date_new = date_converted - timedelta(days=365, hours=2, minutes=15)
    print(date_new)

    
def working_with_date():
    current_date = date.today()
    current_date_str = current_date.strftime('%A %B %Y')
    print(type(current_date))
    print(current_date_str)
    print(type(current_date_str))

def working_with_time():
    schedule = time(hour=15, minute=18, second=30)
    print(schedule)
    schedule_str = schedule.strftime('%H:%M:%S')
    print(schedule_str)

if __name__ == '__main__':
    #working_with_date()
    #working_with_time()
    working_with_datetime()