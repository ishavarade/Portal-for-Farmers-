# +=======================app.py=====================my code
from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import re
import sqlite3


app = Flask(__name__)

app.secret_key = 'your_secret_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '22210531$viit'
app.config['MYSQL_DB']='Farmer'
app.config['PORT']='3306'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:22210531$viit@localhost:3306/Farmer'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

mysql = MySQL(app)
db=SQLAlchemy(app)

app.app_context().push()

class Products(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    fid=db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
    product_name=db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(50),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
         return f"{self.sno} - {self.product_name}"

class Accounts(db.Model):
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    Role = db.Column(db.String(255), nullable=True) 
    # Other columns in the accounts table...

def __repr__(self)->str:
         return f"{self.fid} - {self.email}"

class Earning(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fid = db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
    amount_earned = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self)->str:
    return f"{self.order_id} - {self.fid} - {self.amount_earned}"

@app.route('/earn')
def earn():
    return 'this is earning page'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('login.html')
    # Your signup logic here


@app.route('/addfrmr', methods=['GET','POST'])
def addfrmr():
    if request.method=='POST':
        # fid=request.form['farmer_id']  removed because fid is auto-incremented

        # fid = session.get('fid')
        # if fid is None:
        if 'fid' not in session:
            flash('User not logged in!', 'error')
            return redirect(url_for('login'))
        
        fid=session['fid']
        email=session.get('email')

        account=Accounts.query.filter_by(email=email).first()
        if not account:
            flash('User Email not found!','error')
            return redirect(url_for('login'))
        
        if account.fid != fid:
            flash('Incorrect farmer ID for the logged-in user!', 'error')
            return redirect(url_for('login'))
        
        

        product_name=request.form['product_name']
        price=request.form['price']
        quantity=request.form['quantity']
        category=request.form['category']
        todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
        db.session.add(todo)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect('addfrmr')
    
    alltodo=Products.query.all()
    return render_template('prodt_add_farmer.html',alltodo=alltodo)

@app.route('/ProductDelete/<int:sno>')
def Delete(sno):
    todo=Products.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/addfrmr")

@app.route('/ProductUpdate/<int:sno>', methods=['GET','POST'])
def Update(sno):
    if request.method=='POST':
        product_name=request.form['product_name']
        price=request.form['price']
        quantity=request.form['quantity']
        category=request.form['category']
        todo=Products.query.filter_by(sno=sno).first()
        todo.product_name=product_name
        todo.price=price
        todo.quantity=quantity
        todo.category=category
        db.session.add(todo)
        db.session.commit()
        return redirect("/addfrmr")


    todo=Products.query.filter_by(sno=sno).first()
    # fid=todo.fid
    return render_template('ProductUpdate.html',todo=todo)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ' '
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['fid'] = account['fid']
            session['email'] = account['email']
            msg = 'Logged in successfully!'
            return redirect('/addfrmr')
        else:
            msg = 'Incorrect email / password!'
    return render_template('login.html', msg=msg)
   


@app.route('/ahtml')
def display_products():
    # Assuming `alltodo` contains product data fetched from the database
    alltodo = fetch_product_data_from_database()  # Replace this with your actual function to fetch data
    return render_template('ahtml.html', alltodo=alltodo)

def fetch_product_data_from_database():
    # Query all products from the Product table
    products = Products.query.all()
    return products

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        Role=request.form['Role']

         # Check if the email is already registered
        existing_user = Accounts.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already exists!', 'error')
            return redirect(url_for('login'))

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!', 'error')
            return redirect(url_for('signup'))
        
        if Role == 'Farmer':
            cursor.execute('SELECT fid FROM accounts WHERE email = %s', (email,))
            farmer = cursor.fetchone()
            if farmer:
                farmer_id = farmer['fid']

       

        # Create a new Accounts object and add it to the database
        new_user = Accounts(username=username, password=password, email=email,Role=Role)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')

        
        if Role=="Buyer":
            return redirect(url_for('display_products'))
        elif Role=='Farmer':
            return redirect(url_for('login'))
    
    


    last_user = Accounts.query.order_by(Accounts.fid.desc()).first()
    if last_user:
        farmer_id = last_user.fid + 1  # Assuming fid is auto-incremented
    else:
        farmer_id = 1  # Initial value for farmer_id

    
    return render_template('register.html',msg=msg , farmer_id=farmer_id)



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'product-image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['product-image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Here you would typically save the filename to a database along with other product details
            return 'File uploaded successfully'
    return render_template('index.html')


# Function to fetch product details from the database
def get_product_details(fid):

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='22210531$viit',
        database='Farmer'
    )
    # Connect to your database
    conn = sqlite3.connect('Farmer.db')
    cursor = conn.cursor()
    
    # Query the database to fetch product details
    cursor.execute("SELECT * FROM products WHERE id=?", (fid,))
    product_details = cursor.fetchone()
    
    conn.close()
    
    return product_details

# Route to display the add to cart page
@app.route('/addcart')
def add_to_cart():
    # Retrieve product details from the request query parameters
    fid = request.args.get('fid')
    
    # Fetch product details from the database
    product_details = get_product_details(fid)
    
    # Pass product details to the addcart.html template
    return render_template('addcart.html', product_details=product_details)
  
if __name__ == "__main__":
    app.run(debug=True)
