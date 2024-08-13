import os 
import csv
import shutil


directoryPath = r'C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Python\Leasons\MainProject\MainProject\Entries' + '\\'
BackupEntries=r'C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Python\Leasons\MainProject\MainProject\Backup_Entries' + '\\'

def FilesInterpreter():
    dir_list = os.listdir(directoryPath)
    for file in dir_list:
        extension = os.path.splitext(file)[1]
        if extension == '.txt':
            with open (directoryPath + file, 'r') as EntryTextJournal:
               for line in EntryTextJournal:
                   print(line)
            shutil.move(directoryPath + file, BackupEntries + file)
        elif extension == '.csv':
            with open(directoryPath + file, 'r')as EntryCSVJournal:
                csvFile = csv.reader(EntryCSVJournal)
                for line in csvFile:
                    print(line)
            shutil.move(directoryPath + file, BackupEntries + file)
    
        else:
            print(f'The file {file} is not save under the right format. Supports only ".csv" and ".txt".')
            os.remove(directoryPath + file)


print(FilesInterpreter())
