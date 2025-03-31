from flask import Flask, json, render_template, request
import csv

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
    else:
        data = ['Wrong Source']
    if 'id' in args.keys():
        for ind, x in enumerate(data):
            print("ID")
            print(x['id'])
            print("Requested idx")
            print(args['id'])
            if str(x['id']) == str(args['id']):
                return render_template('product_display.html', products=[data[ind], None])
        return render_template('product_display.html', products=["Product not found"])
    else:
        return render_template('product_display.html', products=data)

def open_csv():
    with open('./products.csv', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        return list(csv_reader)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
