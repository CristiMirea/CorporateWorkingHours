import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime
from CreateDatabase import database




app= Flask(__name__)


def Complete_data(id, date, action):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO Attendace ( ID, Time_Stamp, Action ) VALUES ({id}, "{date}", "{action}");')
        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        raise Exception(f"Database error: {str(error)}")
    

@app.route('/add-gate', methods=['POST'])

def Add_Gate():
    data_json = request.get_json()

    # Check if data_json is None (in case of invalid JSON)
    if data_json is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    # Check if the data is a list
    if not isinstance(data_json, list):
        return jsonify({"error": "Request must contain a list of records"}), 400

    

    for record in data_json:
        try:
           
            id = record['idPersoana']
            date = datetime.fromisoformat(record['data'].replace('Z', '')).strftime('%H:%M:%S')
            action = record['sens']

            
            Complete_data(id, date, action)

            
        
        except ValueError as e:
            # Handle error for date parsing
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
     
    return jsonify({"responses": "Attendace table was updated"}), 201


if __name__ == '__main__':
    app.run(debug=True)
        
     






