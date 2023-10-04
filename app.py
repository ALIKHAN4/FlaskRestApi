from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "NED/0191/16-17",
    "database": "OMS"
}

# Endpoint for user registration
@app.route('/registeruser', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert user data into the 'users' table
        insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (data['username'], data['email'], data['password']))
        connection.commit()

        return jsonify({"message": "User registered successfully"})
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database error"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Endpoint to get all products
@app.route('/getallproducts', methods=['GET'])
def get_all_products():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Query the 'products' table to get all products
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()

        return jsonify(products)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database error"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Add other endpoints for order management (order, allorders, addproduct, updateproduct, deleteproduct)

if __name__ == '__main__':
    app.run(debug=True)
