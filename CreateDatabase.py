from faker import *
import sqlite3
import random
import tkinter as tk
import tkinter.messagebox

database=r"C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Project_ITSchool_SQL_05.06\AccessGate.db"
window = tkinter.Tk()
window.wm_withdraw()


Managers={"10":"cristian.mirea.mc@gmail.com",
          "11": "cristian.mirea.mc@gmail.com",
          "12": "cristian.mirea.mc@gmail.com"
        }

def TodayEmployees ():
    
    try:
        conn=sqlite3.connect(database)
        cursor=conn.cursor()
        
        for i in range(int(first_answer)):
            fake = Faker(['ro_RO'])
            employeefullname=fake.name()
            employeee=employeefullname.split(" ")
            idlist=list(Managers.keys())
            idManager=random.choice(idlist)
            cursor.execute(f'INSERT INTO Employees ( ID,First_Name, Last_Name, Company, ID_Manager, Time) VALUES ({i+1},"{employeee[0]}","{employeee[1]}","{second_answer}","{idManager}","00:00:00");')
        
        conn.commit()
        
        tkinter.messagebox.showinfo(title='Success', message="Employees were added in today's database!")
        window.destroy()
        
    except sqlite3.OperationalError as error:
        tkinter.messagebox.showinfo(title='Alert', message=error)
        window.destroy()
    finally:
        if conn in locals():
            conn.close() 
        
        
# Variable to hold the second input
second_input = None

def firstquestion():
    global first_answer  
    first_answer = entry.get()  
    
    # Close the current window
    root.destroy()

    # Open a new window
    secondquestion()

def secondquestion():
    new_window = tk.Tk()
    new_window.title('Company time tracker')

   
    question_label = tk.Label(new_window, text="Please add the company name:")
    question_label.pack(pady=(10, 5))  

    
    new_entry = tk.Entry(new_window)
    new_entry.pack(pady=10)

    
    def submit_second_answer():
        global second_answer  
        second_answer = new_entry.get()  
        new_window.destroy()  
        TodayEmployees()
        
        

   
    submit_button = tk.Button(new_window, text="Submit", command=submit_second_answer, width=50, height=10)
    submit_button.pack(pady=20)

    # Start the new application's main loop
    new_window.mainloop()
if __name__ == "__main__":
# Create the main application window
    root = tk.Tk()
    root.title("Company time tracker")

# Create a label for asking a question above the entry widget
    question_label = tk.Label(root, text="Hello. How many employees are today in the office?")
    question_label.pack(pady=(10, 5))  # Adding some padding

# Create an entry widget for user input
    entry = tk.Entry(root)
    entry.pack(pady=20)

# Create a button that will call the store_input function when clicked
    submit_button = tk.Button(root, text="Submit", command=firstquestion, width=50, height=10)
    submit_button.pack(pady=10)

# Start the application
    root.mainloop()



