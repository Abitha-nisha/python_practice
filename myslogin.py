# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import mysql.connector

# def fech_data():
#     db_connection={
#         'host':'sagasoft',
#         'user':'root',
#         'password':'Abii@321',
#         'database':'abitha'
#     }
#     conn=mysql.connector.connect(**db_connection)
#     cur=conn.cursor()
#     data= "SELECT username,password FROM automation limit 1"
#     cur.execute(data)
#     result=cur.fetchone()
#     cur.close()
#     conn.close()

#     if result:
#         return{'username':result[0],'password':result[1]}
#     else:
#         raise Exception("no data found a database")


# database=fech_data()
# email=database['username']
# passw=database['password']

# driver=webdriver.Chrome()
# driver.get("https://dash.sagasoft.io/sagasuite/signin")
# driver.maximize_window()

# login_email=WebDriverWait(driver,30).until(
#     EC.presence_of_element_located((By.XPATH,"//*[@id='email']"))
# )
# login_email.send_keys(email)
# login_password=WebDriverWait(driver,30).until(
#     EC.presence_of_element_located((By.XPATH,"//*[@id='password']"))
# )
# login_password.send_keys(passw)
# print("Successully enter the email and password.")

# time.sleep(5)
# driver.quit()


# #get multiple values

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import mysql.connector



# def fetch_data():
#     db_connection = {
#         'host': 'sagasoft',
#         'user': 'root',
#         'password': 'Abii@321',
#         'database': 'abitha'
#     }
#     conn = mysql.connector.connect(**db_connection)
#     cur = conn.cursor()
#     data = "SELECT username, password FROM automation"
#     cur.execute(data)
#     results = cur.fetchall()  
#     cur.close()
#     conn.close()
    
#     if results:
#         data = []
#         for result in results:
#             user_name = result[0]
#             password = result[1]
#             data.append({'username': user_name, 'password': password})
#         return data
#     else:
#         raise Exception("No data found in the database")

# database = fetch_data()

# for user in database:

#     email = user['username'] 
#     passw = user['password']
    
#     driver = webdriver.Chrome()
#     driver.get("https://dash.sagasoft.io/sagasuite/signin")
#     driver.maximize_window()

#     login_email = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
#     )
#     login_email.send_keys(email)
#     login_password = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='password']"))
#     )
#     login_password.send_keys(passw)

#     time.sleep(5)
#     driver.quit()


from flask import Flask, request, jsonify


app = Flask(__name__)

# Sample data (acting as a database)
users = [
    {"id": 1, 
     "name": "John Doe",
    "email": "john@example.com"},
    {"id": 2, 
     "name": "Jane Doe", 
     "email": "jane@example.com"},
     {"id":3,
      "name":"abitha",
      "email":"abitha@gmail.com"},
      {"name":"sakthi",
       "id":4,
       "email":"sathiabi23@gmail.com"}
]

# 🟢 READ (Get all users)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# 🟢 READ (Get single user by ID)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 🔵 CREATE (Add a new user)
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    user.update(data)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)










































# from flask import Flask, request, jsonify
# import csv
# import io

# app = Flask(__name__)

# # Sample data (acting as a database)
# users = [
#     {"id": 1, "name": "John Doe", "role": "Admin", "age": 30},
#     {"id": 2, "name": "Jane Doe", "role": "Manager", "age": 28}
# ]

# # 🔵 CREATE / UPDATE Users from CSV File
# @app.route('/upload_csv', methods=['POST'])
# def upload_csv():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if not file.filename.endswith('.csv'):
#         return jsonify({"error": "Invalid file format"}), 400

#     stream = io.StringIO(file.stream.read().decode("UTF8"))
#     reader = csv.DictReader(stream)

#     new_users = []
#     new_id = max([u["id"] for u in users], default=0) + 1

#     for row in reader:
#         new_user = {
#             "id": new_id,
#             "name": row["name"],
#             "role": row["role"],
#             "age": int(row["age"])
#         }
#         new_users.append(new_user)
#         users.append(new_user)
#         new_id += 1

#     return jsonify({"message": "Users added/updated successfully", "users": new_users}), 201

# if __name__ == '__main__':
#     app.run(debug=True)
