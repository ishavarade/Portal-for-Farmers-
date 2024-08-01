from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import re
import random

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

    def _repr_(self)->str:
         return f"{self.sno} - {self.product_name}"

class Accounts(db.Model):
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    Role = db.Column(db.String(255), nullable=True) 
    # Other columns in the accounts table...

def _repr_(self)->str:
         return f"{self.fid} - {self.email}"

class Earning(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fid = db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
    amount_earned = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

def _repr_(self)->str:
    return f"{self.order_id} - {self.fid} - {self.amount_earned}"

class Cart(db.Model):
    ch_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    bill_id = db.Column(db.Integer, nullable=False)
    sno=db.Column(db.Integer,db.ForeignKey('products.sno'),nullable=False)
    product_name=db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)

def _repr_(self)->str:
    return f"{self.bill_id}"

def genbill():
    bid = random.randint(1, 10000)
    return bid



@app.route('/earn')
def earn():
    return 'this is earning page'

@app.route('/term')
def term():
    # Your view function logic here
    return render_template('terms.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('login.html')
    # Your signup logic here


@app.route('/payment_details')
def paydet(bill_id):
    prods = Cart.query.filter_by(bill_id=bill_id)


    return render_template('addcart.html')
# @app.route('/addfrmr', methods=['GET','POST'])
# def addfrmr():
#     if request.method=='POST':
#         # fid=request.form['farmer_id']  removed because fid is auto-incremented

#         # fid = session.get('fid')
#         # if fid is None:
#         if 'fid' not in session:
#             flash('User not logged in!', 'error')
#             return redirect(url_for('login'))
        
#         fid=session['fid']
#         email=session.get('email')

#         account=Accounts.query.filter_by(email=email).first()
#         if not account:
#             flash('User Email not found!','error')
#             return redirect(url_for('login'))
        
#         if account.fid != fid:
#             flash('Incorrect farmer ID for the logged-in user!', 'error')
#             return redirect(url_for('login'))
        
        

#         product_name=request.form['product_name']
#         price=request.form['price']
#         quantity=request.form['quantity']
#         category=request.form['category']
#         todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
#         db.session.add(todo)
#         db.session.commit()
#         flash('Product added successfully!', 'success')
#         return redirect('addfrmr')
    
#     alltodo=Products.query.all()
#     return render_template('prodt_add_farmer.html',alltodo=alltodo)

@app.route('/ProductDelete/<int:sno>')
def Delete(sno):
    todo=Products.query.filter_by(sno=sno).first()
    fid=todo.fid
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('addfrmr', fid=fid))

@app.route('/ProductUpdate/<int:sno>', methods=['GET','POST'])
def Update(sno):
    if request.method=='POST':
        product_name=request.form['product_name']
        price=request.form['price']
        quantity=request.form['quantity']
        category=request.form['category']
        todo=Products.query.filter_by(sno=sno).first()
        fid = todo.fid
        todo.product_name=product_name
        todo.price=price
        todo.quantity=quantity
        todo.category=category
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('addfrmr', fid=fid))


    todo=Products.query.filter_by(sno=sno).first()
    # fid=todo.fid
    return render_template('ProductUpdate.html',todo=todo)

# def get_prod(sno):
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT * FROM products WHERE sno = %s', (sno,))
#     prod = cursor.fetchone()
#     return prod

@app.route('/ahtml', methods=['GET', 'POST'])
def addcart():
    alltodo = Products.query.all()
    if 'bill_id' not in session:
            session['bill_id'] = genbill()
    if request.method=='POST':
        qty = int(request.form['quantity'])
        todo_sno = request.form['todo_sno']
        bill_id = session.get('bill_id')
        prod = Products.query.filter_by(sno=todo_sno).first()
        if prod is None:
            return 'prod not found'
        else:
            quan = prod.quantity
            product_name=prod.product_name
            price=prod.price
        pq = Products.query.get(todo_sno)
        # if pq:
        #     pq.quantity = quan-qty
        #     if pq.quantity <= 0:
        #         db.session.delete
        if pq:
            updated_quantity = quan - qty
            if updated_quantity <= 0:
               del_prod(todo_sno) # Delete the product from the database
            else:
               pq.quantity = updated_quantity # Add the updated product back to the session for committing 

            # db.session.commit()
        addpro = Cart(bill_id=bill_id, sno=todo_sno,product_name=product_name,price=price,quantity=qty)
        db.session.add(addpro)
        db.session.commit()
        return redirect(url_for('addcart'))
    return render_template('ahtml.html', alltodo=alltodo)

def del_prod(sno):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM products WHERE sno = %s', (sno,))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     msg = ' '
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'fid' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         fid = request.form['fid']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s AND fid= %s', (email, password,fid))
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             session['fid'] = account['fid']
#             session['email'] = account['email']
#             msg = 'Logged in successfully!'
#             return redirect(url_for('frfid'), fid=fid)
#         else:
#             msg = 'Incorrect email / password!'
#     return render_template('login.html', msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ' '
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'fid' in request.form:
        email = request.form['email']
        password = request.form['password']
        fid = request.form['fid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s AND fid= %s', (email, password,fid))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['fid'] = account['fid']
            session['email'] = account['email']
            msg = 'Logged in successfully!'
            return redirect(url_for('frfid', fid=fid))
        else:
            msg = 'Incorrect email / password!'
    return render_template('login.html', msg=msg)



@app.route('/<int:fid>', methods=['GET', 'POST'])
def frfid(fid):
    farmer = Accounts.query.get_or_404(fid)
    return render_template('farmer_details.html', farmer=farmer)

@app.route('/<int:fid>/products', methods=['GET', 'POST'])
def addfrmr(fid):    
    farmer=Products.query.filter_by(fid=fid).all()  
    if request.method=='POST':    
        # fid=request.form['farmer_id']  removed because fid is auto-incremented
   
        #fid = session.get('fid')    
        if fid is None:    
            flash('User not logged in!', 'error')    
            return redirect(url_for('login'))    
   
        product_name=request.form['product_name']    
        price=request.form['price']    
        quantity=request.form['quantity']    
        category=request.form['category']    
        todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
        db.session.add(todo)    
        db.session.commit()    
        flash('Product added successfully!', 'success')    
        return redirect(url_for('addfrmr', fid=fid))    
    return render_template('prodt_add_farmer.html',farmer=farmer) 

# @app.route('/ahtml', methods=['GET', 'POST'])
# def ahtml():
#     return render_template('ahtml.html')
    
# @app.route('/<int:fid>', methods=['GET', 'POST'])
# def frfid(fid):
#     return render_template('farmer_details.html')

# @app.route('/ahtml')
# def display_products():
#     # Assuming alltodo contains product data fetched from the database
#     alltodo = fetch_product_data_from_database()  # Replace this with your actual function to fetch data
#     return render_template('ahtml.html', alltodo=alltodo)

#@app.route('/payment')
#def payment()

# def fetch_product_data_from_database():
#     # Query all products from the Product table
#     products = 
#     return products

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


# @app.route('/login/<int:fid>/addfrmr', methods=['GET','POST'])    
# def addfrmr(fid):    
#     alltodo=Products.query.get(fid)  
#     if request.method=='POST':    
#         # fid=request.form['farmer_id']  removed because fid is auto-incremented
   
#         #fid = session.get('fid')    
#         if fid is None:    
#             flash('User not logged in!', 'error')    
#             return redirect(url_for('login'))    
   
#         product_name=request.form['product_name']    
#         price=request.form['price']    
#         quantity=request.form['quantity']    
#         category=request.form['category']    
#         todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
#         db.session.add(todo)    
#         db.session.commit()    
#         flash('Product added successfully!', 'success')    
#         return redirect('/<int:fid>/addfrmr')    
#     return render_template('prodt_add_farmer.html',alltodo=alltodo) 

@app.route('/list')
def list_products():
    products = Products.query.all()
    product_counts = {}
    for product in products:
        if product.product_name in product_counts:
            product_counts[product.product_name] += 1
        else:
            product_counts[product.product_name] = 1
    return render_template('List.html', product_counts=product_counts)





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
  
if __name__ == "__main__":
    app.run(debug=True)