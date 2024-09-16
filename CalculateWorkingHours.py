import sqlite3
from datetime import *
from CreateDatabase import database





def Calculate_work_time():
    conn=sqlite3.connect(database, timeout=10.0)
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Attendace')
    rezultat =cursor.fetchall()

    work_time = {}
    last_in_time = {}
    try:
        for emp_id, time_str, state in rezultat:
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
    
    # Convert work time from seconds to a readable format 
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
            cursor.execute(f'UPDATE Employees SET TIME = "{timp}" WHERE ID={id};')
            conn.commit()
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except  sqlite3.OperationalError as error:
            print(error)



Calculate_work_time()
