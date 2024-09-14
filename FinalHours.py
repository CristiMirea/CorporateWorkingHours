from datetime import datetime, date
import tkinter
import tkinter.messagebox
import sqlite3
import smtplib, ssl
import csv
from CreateDatabase import Managers
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Help_File import *


BackupEntries=r'C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Python\Leasons\MainProject\MainProject\Backup_Entries' + '\\'
database=r"C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Project_ITSchool_SQL_05.06\AccessGate.db"
conn=sqlite3.connect(database, timeout=10.0)
cursor=conn.cursor()
window = tkinter.Tk()
window.wm_withdraw()



def EndDay():
    start_hour= '16:45:00'
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == start_hour:
            tkinter.messagebox.showinfo(title='Important message', message='The work schedule is over. An email will be sent if there are any employees that have not complete 8 hours')
            window.destroy()
            DayReport()
            break




def DayReport():
    today =date.today()
    with open(BackupEntries +  str(today) +'_Chiulangii.csv', "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header) #
    try:
        cursor.execute('SELECT First_Name, Last_Name, ID_Manager, Time FROM Employees;')
        rezultat=cursor.fetchall()
        for lista in rezultat:
            hour=lista[3].split(":")
            real_hour=int(hour[0])
            if real_hour < 8:
                with open(BackupEntries +  str(today) +'_Chiulangii.txt', "a") as file: 
                        file.write(f'{lista[0]} {lista[1]} {lista[3]} '"\n")
                with open(BackupEntries +  str(today) +'_Chiulangii.csv', "a", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    row=[lista[0], lista[1], lista[3]] 
                    writer.writerow(row) 

                manager_ID=str(lista[2])
                receiver_email=Managers[manager_ID]
                first_name=lista[0]
                last_name=lista[1]
                to_email = receiver_email
                body = f"""Hello, \nThe employee {first_name} {last_name} has not completed 8 hours of work on {today}."""
                msg = MIMEMultipart()
                msg['From'] = from_email
                msg['To'] = to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()  # Secure the connection
                server.login(from_email, smtp_password)

            # Send the email
                server.sendmail(from_email, to_email, msg.as_string())
                server.quit()

        # Create_backup_files()
               

    except OverflowError as error:
            tkinter.messagebox.showinfo(title='Alert', message=error)
            window.destroy()





    
     




EndDay()

