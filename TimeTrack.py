import os 
import csv
import shutil
import tkinter as tk
import tkinter.messagebox
import sqlite3
from datetime import *

database=r"C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Project_ITSchool_SQL_05.06\AccessGate.db"
directoryPath = r'C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Python\Leasons\MainProject\MainProject\Entries' + '\\'
BackupEntries=r'C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Python\Leasons\MainProject\MainProject\Backup_Entries' + '\\'


def FilesInterpreter():
    window = tkinter.Tk()
    window.wm_withdraw()

    dir_list = os.listdir(directoryPath)
    for file in dir_list:
        extension = os.path.splitext(file)[1]
        try:
            conn=sqlite3.connect(database, timeout=10.0)
            cursor=conn.cursor()
            if extension == '.txt':
                with open (directoryPath + file, 'r') as EntryTextJournal:
                    for line in EntryTextJournal:
                        info=line.split(",")
                        time = info[1][11:19]
                        if 'in' in line:
                            cursor.execute(f'INSERT INTO Attendace ( ID, Time_Stamp, Action) VALUES ({info[0]},"{time}","in");')
                        else:
                            cursor.execute(f'INSERT INTO Attendace ( ID, Time_Stamp, Action) VALUES ({info[0]},"{time}","out");')
                         
                shutil.move(directoryPath + file, BackupEntries + file)
            
       
            elif extension == '.csv': 
                with open(directoryPath + file, 'r') as EntryCSVJournal:
                    csvFile = csv.reader(EntryCSVJournal)
                    for line in csvFile:
                        if 'Data' not in line:
                            time=line[1]
                            time_convert = time[11:19]
                            if 'in' in line:
                                cursor.execute(f'INSERT INTO Attendace ( ID, Time_Stamp, Action) VALUES ({line[0]},"{time_convert}","in");')
                            else:
                                cursor.execute(f'INSERT INTO Attendace ( ID, Time_Stamp, Action) VALUES ({line[0]},"{time_convert}","out");')
                           
                shutil.move(directoryPath + file, BackupEntries + file)
    
            else:
                tkinter.messagebox.showinfo(title='Alert', message=(f'The file {file} is not save under the right format. Supports only ".csv" and ".txt".'))
                window.destroy()
                os.remove(directoryPath + file)

        except  sqlite3.OperationalError as error:
                tkinter.messagebox.showinfo(title='DataBase error', message=error)

        except  Exception as e:
                tkinter.messagebox.showinfo(title='Error', message=str(e))
                
        
        finally: 
            conn.commit() 
            cursor.execute('SELECT * FROM Attendace')
            global rezultat
            rezultat =cursor.fetchall()
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    calculate_work_time(rezultat)
    window.destroy() 




def calculate_work_time(x):
    work_time = {}
    last_in_time = {}
    try:
        for emp_id, time_str, state in x:
            current_time = datetime.strptime(time_str, '%H:%M:%S')
        
            if state == 'in':
                last_in_time[emp_id] = current_time
            elif state == 'out' and emp_id in last_in_time:
                if emp_id not in work_time:
                    work_time[emp_id] = 0
            
            # Calculate the duration between in and out
                duration = (current_time - last_in_time[emp_id]).total_seconds()
                if duration > 0:  # Only add if the duration is positive
                    work_time[emp_id] += duration
            
            # Clean up the last in time for this employee
                del last_in_time[emp_id]
    
    # Convert work time from seconds to a readable format (HH:MM:SS)
        for emp_id in work_time:
            total_seconds = work_time[emp_id]
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            work_time[emp_id] = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    except  Exception as error:
            print(error)


    conn=sqlite3.connect(database, timeout=10.0)
    cursor=conn.cursor()
    try:
        for id, timp in work_time.items():
            # print(type(id),type(timp))
            cursor.execute(f'UPDATE Employees SET TIME = "{timp}" WHERE ID={id};')
            conn.commit()
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except  sqlite3.OperationalError as error:
            print(error)
