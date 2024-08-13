from faker import *
import sqlite3
import random



conn = sqlite3.connect(r"C:\Users\CristianMirea\OneDrive - RightClick Solutions, B.V\Desktop\SQL\Project_ITSchool_SQL_05.06\Access.db")


def AdaugareAngajati ():
    Managers={"10":"John Doe",
          "11": "Sam Sample",
          "12": "Marie Michelle"
        }
    TodaysEmployees=int(input('How many employees are today in the office? '))
    CompanyName=str(input("Cum se numeste compania? "))
    for i in range(TodaysEmployees):
        fake = Faker(['ro_RO'])
        employeefullname=fake.name()
        employeee=employeefullname.split(" ")
        idlist=list(Managers.keys())
        idManager=random.choice(idlist)
        cursor=conn.cursor()
        function=(f'INSERT INTO Access VALUES (NULL,"{employeee[0]}","{employeee[1]}","{CompanyName}","{idManager}"); ')
        cursor.execute(function)
        conn.commit()





AdaugareAngajati()
