from datetime import datetime


def EndDay():
    start_hour= '18:59:00'
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == start_hour:
            print ('The work schedule is over. Check the hours')
            DayReport()
            break




def DayReport():
    pass

EndDay()