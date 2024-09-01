from datetime import datetime, date
import tkinter
import tkinter.messagebox
import sqlite3
import smtplib, ssl
from CreateDatabase import Managers


database=r"C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Project_ITSchool_SQL_05.06\AccessGate.db"
conn=sqlite3.connect(database, timeout=10.0)
cursor=conn.cursor()
window = tkinter.Tk()
window.wm_withdraw()

def EndDay():
    start_hour= '20:49:00'
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == start_hour:
            tkinter.messagebox.showinfo(title='Important message', message='The work schedule is over. An email will be sent if there are any employees that have not complete 8 hours')
            window.destroy()
            DayReport()
            break




def DayReport():
    try:
        cursor.execute('SELECT First_Name, Last_Name, ID_Manager, Time FROM Employees;')
        rezultat=cursor.fetchall()
        for lista in rezultat:
            hour=lista[3].split(":")
            real_hour=int(hour[0])
            if real_hour < 8:
                manager_ID=str(lista[2])
                receiver_email=Managers[manager_ID]
                # print(receiver_email)

                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "cristian.mirea.mc@gmail.com"  # Enter your address
                password='auio rool jpii xpjn' #email password


                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, 'cristian.mirea.mc@gmailcom', f'Hello, \n The employee {lista[0]} {lista[1]} has not completed 8 hours of work on {date.today()}. ')

            

    except  OverflowError as error:
            tkinter.messagebox.showinfo(title='Alert', message=error)
            window.destroy()

# EndDay()
DayReport()