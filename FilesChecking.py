import os
import time
from TimeTrack import FilesInterpreter


directoryPath = r'C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Python\Leasons\MainProject\MainProject\Entries'
def FirstTry():
    if  not os.listdir(directoryPath):
        print('There are no files. Auto-Checking after 1 min ')
        TimeCheck()
    else:
        print('Files were found in the folder. Uploading the data.')
        FilesInterpreter()

def TimeCheck():
    timetocheck=0
    while timetocheck < 10:   #change with how many second you want
        time.sleep(1)
        timetocheck+=1
    
    timetocheck=0
    CheckingFileExist()
        
        
def CheckingFileExist (): 
    if  not os.listdir(directoryPath):
        print('There are no files. Auto-Checking after 1 min ')
        TimeCheck()
    else:
        print('Files were found in the folder. Uploading the data.')
        FilesInterpreter()


FirstTry()



        

