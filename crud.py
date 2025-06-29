


from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='sagasoft',  
        user='root',    
        password='Abii@321',  
        database='abitha' 
 
    )
    return conn

@app.route('/users', methods=['POST'])
def create_user():
    try:
        
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

  
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO login (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()

   
        cursor.close()
        conn.close()

        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getusers', methods=['GET'])
def get_users():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM login")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(users)

@app.route('/putusers/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json() 
    username = data['username']
    password = data['password']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE login SET username = %s, password = %s WHERE id = %s", (username, password,id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "User updated successfully!"})



@app.route('/delusers/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM login WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "User deleted successfully!"})


if __name__ == '__main__':
    app.run(debug=True)
