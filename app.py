# Importing Libraries
from flask import Flask, render_template, request
import os
import webbrowser
import threading

# Flask App Initialization
app = Flask(__name__)
app.secret_key = 'billing_app_secret_key'

# Folder where bills will be stored
BILL_FOLDER = 'bills'
os.makedirs(BILL_FOLDER, exist_ok=True)

# File to keep track of the last bill number
BILL_NUMBER_FILE = 'last_bill_number.txt'

# Product list with prices
products = {
    'Chicken Biriyani 1kg': 200,
    'Chicken Biriyani 1/2kg': 100,
    'Chicken Biriyani 1/4kg': 50,
    'Kushka 1kg': 160,
    'Kushka 1/2kg': 80,
    'Kushka 1/4kg': 40,
    'Egg Biriyani 1kg': 180,
    'Egg Biriyani 1/2kg': 90,
    'Egg Biriyani 1/4kg': 45,
    'Mutton Biriyani 1kg': 300,
    'Mutton Biriyani 1/2kg': 150,
    'Mutton Biriyani 1/4kg': 75
}

# Initialize bill number if file does not exist
if not os.path.exists(BILL_NUMBER_FILE):
    with open(BILL_NUMBER_FILE, 'w') as f:
        f.write('0000')

# Main Route (/):
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        phone = request.form['phone']
        
        # Read the last bill number and generate a new one
        with open(BILL_NUMBER_FILE, 'r') as f:
            last_bill_number = int(f.read())
        bill_number = str(last_bill_number + 1).zfill(4)  # Pad bill number with zeros (Only 4 Digits)
        
        # Save the new bill number for the next request
        with open(BILL_NUMBER_FILE, 'w') as f:
            f.write(str(last_bill_number + 1))
        
        # Capture quantities
        quantities = {item: int(request.form.get(item, 0)) for item in products.keys()}
        
        total = 0
        bill_content = f"""Welcome to Dolly's Biriyani
Bill Number   : {bill_number}
Customer Name : {customer_name}
Phone Number  : {phone}
-------------------------------------
Product                Qty      Price
-------------------------------------
"""
        # Generate bill content based on quantities
        for item, qty in quantities.items():
            if qty > 0:
                price = products[item] * qty
                total += price
                bill_content += f"{item:<22} {qty:<8} {price:<5}\n"

        bill_content += f"-------------------------------------\nTotal: {total} Rupees Only\n"

        # Save bill to file
        bill_file = os.path.join(BILL_FOLDER, f'BN-{bill_number}.txt')
        with open(bill_file, 'w') as file:
            file.write(bill_content)

        return render_template('index.html', products=products, bill_content=bill_content, bill_number=bill_number, total=total)

    else:
        # For GET request, read the last bill number and generate a new one
        with open(BILL_NUMBER_FILE, 'r') as f:
            last_bill_number = int(f.read())
        bill_number = str(last_bill_number + 1).zfill(4)  # Pad bill number with zeros (Only 4 Digits)

        # Render template with initial values
        return render_template('index.html', products=products, bill_number=bill_number, total=0)
    
def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')
threading.Timer(1, open_browser).start()

if __name__ == '__main__':
    app.run(debug=False)
