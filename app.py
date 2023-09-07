from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# A simple data structure to hold our products
products = [
    {'id': '1', 'name': 'Fishing Rod', 'price': 100},
    {'id': '2', 'name': 'Fishing Net', 'price': 50},
    {'id': '3', 'name': 'Fishing Bait', 'price': 20},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/checkout', methods=['POST'])
def checkout():
    # Get the list of product ids from the form submission
    product_ids = request.form.getlist('product')

    # Find the corresponding products
    selected_products = [p for p in products if p['id'] in product_ids]

    # Calculate the total price
    total_price = sum(p['price'] for p in selected_products)
    
    # Store the total price in the session for later use
    session['total_price'] = total_price

    return render_template('checkout.html', products=selected_products, total=total_price)

@app.route('/confirmation', methods=['POST'])
def confirmation():
    # Retrieve total_price from session
    total_price = session.get('total_price', 0) 
    if total_price is None:
        total_price = 0
        
    return render_template('confirmation.html', total=total_price)

if __name__ == '__main__':
    app.run(debug=True)
