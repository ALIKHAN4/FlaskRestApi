from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structures to simulate database
users = []
products = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 20.49},
    {"id": 3, "name": "Product C", "price": 15.99},
]
orders = []

# Endpoint for user registration
@app.route('/registeruser', methods=['POST'])
def register_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User registered successfully"})

# Endpoint to get all products
@app.route('/getallproducts', methods=['GET'])
def get_all_products():
    return jsonify(products)

# Endpoint to place an order
@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    orders.append(data)
    return jsonify({"message": "Order placed successfully"})

# Endpoint to retrieve all orders
@app.route('/allorders', methods=['GET'])
def get_all_orders():
    return jsonify(orders)

# Endpoint to add a product
@app.route('/addproduct', methods=['POST'])
def add_product():
    data = request.get_json()
    products.append(data)
    return jsonify({"message": "Product added successfully"})

# Endpoint to update a product
@app.route('/updateproduct/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    if product_id < len(products):
        products[product_id] = data
        return jsonify({"message": "Product updated successfully"})
    else:
        return jsonify({"error": "Product not found"})

# Endpoint to delete a product
@app.route('/deleteproduct/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id < len(products):
        deleted_product = products.pop(product_id)
        return jsonify({"message": "Product deleted successfully", "deleted_product": deleted_product})
    else:
        return jsonify({"error": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True)
