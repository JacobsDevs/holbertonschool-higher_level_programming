from flask import Flask, json, render_template, request
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items = json.load(open('./items.json'))
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    args = request.args
    data = []
    if args['source'] == 'json':
        data = json.load(open('./products.json'))
    elif args['source'] == 'csv':
        data = open_csv()
    elif args['source'] == 'db':
        data = read_db()
    else:
        data = ['Wrong source']
    if 'id' in args.keys():
        for ind, x in enumerate(data):
            if str(x['id']) == str(args['id']):
                return render_template('product_display.html', products=[data[ind], None])
        return render_template('product_display.html', products=["Product not found"])
    else:
        return render_template('product_display.html', products=data)

def open_csv():
    with open('./products.csv', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        return list(csv_reader)

def read_db():
    conn = sqlite3.connect('products.db')

    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('select * from Products')
    rows = cursor.fetchall()
    return [dict(x) for x in rows]

def create_database():
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT OR IGNORE INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)

