from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    ProductsFound = [product for product in products if product['name'] == product_name]
    if (len(ProductsFound) > 0):
        return jsonify({"product": ProductsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)