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
                window.destroy()

        except  Exception as e:
                tkinter.messagebox.showinfo(title='Error', message=str(e))
                window.destroy()
                
        
        finally: 
            conn.commit() 
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
