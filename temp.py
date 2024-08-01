# # welcome login page code which runs perfectly-------------------------------------------------------------------------------->

from flask import Flask , render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:22210531$viit@localhost:3306/Info'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)

app.app_context().push()


class Login(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(200),nullable=False)
    password=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
         return f"{self.sno} - {self.email}"

@app.route('/' , methods=['GET','POST'])
def hell_world():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        view=Login(email=email,password=password)
        db.session.add(view)
        db.session.commit()
    Alogin=Login.query.all()
    return render_template('login.html',Alogin=Alogin)

@app.route('/Update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        view=Login.query.filter_by(sno=sno).first()
        view.email=email
        view.password=password
        db.session.add(view)
        db.session.commit()
        return redirect("/")

    view=Login.query.filter_by(sno=sno).first()
    return render_template('update.html',view=view)
    

@app.route('/Delete/<int:sno>')
def delete(sno):
    view=Login.query.filter_by(sno=sno).first()
    db.session.delete(view)
    db.session.commit()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True ,port=5000)


# ----------------------------------------------------------------------------------------------------------------------------------------------
























# example code

# from flask import Flask, render_template,request,redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:22210531$viit@localhost:3306/todo'
# app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
# db=SQLAlchemy(app)

# app.app_context().push()

# class Todo(db.Model):
#     sno=db.Column(db.Integer,primary_key=True)
#     tittle=db.Column(db.String(200),nullable=False)
#     desc=db.Column(db.String(500),nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self)->str:
#         return f"{self.sno} - {self.tittle}"

# @app.route('/', methods=['GET','POST'])
# def hello_world():
#     if request.method=="POST":
#      tittle=request.form['tittle']
#      desc=request.form['desc']

#      todo=Todo(tittle=tittle, desc=desc)
#      db.session.add(todo)
#      db.session.commit()
#     allTodo=Todo.query.all()
#     return render_template('index.html',allTodo=allTodo)

# @app.route('/show')
# def products():
#     allTodo=Todo.query.all()
#     print(allTodo)
#     return 'This is product page'

# @app.route('/update/<int:sno>')
# def update(sno):
#     todo=Todo.query.filter_by(sno=sno).first()
#     return render_template('update.html',todo=todo)



# @app.route('/delete/<int:sno>')
# def delete(sno):
#     todo=Todo.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect("/")


    

# if __name__=="__main__":
#     app.run(debug=True ,port=8000) 



# ==============================================================================================================================================





# main code

# # from flask import Flask, render_template,request,redirect,url_for
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime
# # from sqlalchemy.sql import func
# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:22210531$viit@localhost:3306/Farmer'
# # app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
# # db=SQLAlchemy(app)

# # app.app_context().push()

# # class Details(db.Model):
# #     app = Flask(__name__)
# #     app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:22210531$viit@localhost:3306/Farmer'
# #     app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
# #     db=SQLAlchemy(app)
# #     # _tablename_ = 'details'
# #     email = db.Column(db.String(100))
# #     name = db.Column(db.String(100))
# #     phone_no = db.Column(db.String(15))   
# #     farmer_id = db.Column(db.Integer, primary_key=True, unique=True)
# #     address = db.Column(db.String(100))
# #     date_created=db.Column(db.DateTime,default=datetime.utcnow)

# #     def __repr__(data)->str:
# #         return f"{data.email} - {data.name} - {data.phone_no} - {data.farmer_id} - {data.address}"
    
# # class Earning(db.Model):
# #     _tablename_ = 'earning'
# #     tranc_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
# #     order_id = db.Column(db.Integer, unique=True, nullable=False)
# #     order_date = db.Column(db.Date)
# #     farmer_id = db.Column(db.Integer, db.ForeignKey('details.farmer_id'))

# # class Products(db.Model):
# #     _tablename_ = 'products'
# #     product_id = db.Column(db.Integer, primary_key=True, unique=True)
# #     farmer_id = db.Column(db.Integer, db.ForeignKey('details.farmer_id'))
# #     category = db.Column(db.String(50))
# #     price = db.Column(db.Float)
# #     product_name = db.Column(db.String(100))
# #     quantity = db.Column(db.Integer)

# # class customer(db.Model):
# #     _tablename_ = 'customers'
# #     cfirstname = db.Column(db.String(100), nullable=False)
# #     clastname = db.Column(db.String(100), nullable=False)
# #     cemail = db.Column(db.String(90), unique=True, nullable=False, primary_key=True)
# #     addr = db.Column(db.String(90), nullable=False)

# #     def _repr(self):
# #         return f'<Customer {self.cfirstname}>'




# # @app.route('/signup', methods=['GET'])
# # def signup():
# #     return redirect(url_for('signup_farmer'))

# # @app.route('/', methods=['GET','POST'])
# # def signup_farmer():
# #     if request.method == 'POST':
# #         # Handle form submission here
# #         email = request.form['email']
# #         name = request.form['name']
# #         phone = request.form['phone']
# #         farmer_id = request.form['farmer_id']
# #         address = request.form['address']
# #         farmer = Details(email=email, name=name, phone_no=phone, farmer_id=farmer_id, address=address)
# #         db.session.add(farmer)
# #         db.session.commit()
        

# #         signup_farmer()
# #         # Perform any necessary processing or database operations
# #         return redirect(url_for('index'))
# #     return render_template('signinfarmer.html')

# # @app.route('/signin.html', methods=['GET', 'POST'])
# # def index():
# #     return render_template('signin.html')

    

# # if __name__=="__main__":
# #     app.run(debug=True ,port=5000) 








# {% extends 'ProductBase.html' %}
# {% block body %}
#     <style>
#         /* Add your CSS styles here */
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         .container {
#             max-width: 600px;
#             margin: 50px auto;
#             background-color: #fff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
#         }

#         h1 {
#             text-align: center;
#             color: #4CAF50;
#             margin-bottom: 20px;
#         }

#         label {
#             display: block;
#             margin-bottom: 5px;
#         }

#         input[type="text"],
#         input[type="number"] {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             box-sizing: border-box;
#         }

#         select {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             box-sizing: border-box;
#         }

#         input[type="submit"] {
#             width: 100%;
#             padding: 10px;
#             background-color: #4CAF50;
#             color: #fff;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#             text-align: center;
#         }

#         input[type="submit"]:hover {
#             background-color: #45a049;
#         }

#         .file-upload {
#             position: relative;
#             overflow: hidden;
#             margin-bottom: 20px;
#         }

#         .file-upload input[type=file] {
#             position: absolute;
#             top: 0;
#             right: 0;
#             margin: 0;
#             padding: 0;
#             font-size: 20px;
#             cursor: pointer;
#             opacity: 0;
#         }

#         .file-select {
#             display: inline-block;
#             padding: 10px 20px;
#             background-color: #4CAF50;
#             color: #fff;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }
#     </style>
# </head>

# <body>
#     <div class="container my-3">
#         <h1>Product Entry Portal</h1>
#         <form action="/" method="POST">
      
#         <label for="product_name">Product Name:</label>
#         <input type="text" id="product_name" name="product_name" placeholder="Enter Product Name" required>

#         <!-- <label for="productImage">Product Image:</label>
#         <div class="file-upload">
#             <input type="file" id="productImage" name="productImage" accept="image/*" required>
#             <label for="productImage" class="file-select">Choose File</label>
#         </div> -->

#         <label for="price">Price:</label>
#         <input type="number" id="price" name="price" placeholder="Enter Price" required>

#         <label for="quantity">Quantity:</label>
#         <input type="number" id="quantity" name="quantity" placeholder="Enter Quantity" required>

#         <label for="category">Select category:</label>
#         <select id="category" name="category" required>
#             <option value="" disabled selected>Select Category</option>
#             <option value="Vegetable">Vegetable</option>
#             <option value="Spices">Spices</option>
#             <option value="Fruit">Fruit</option>
#             <option value="Dairy">Dairy</option>
#         </select>

#         <input type="submit" value="Submit" href="./ahtml.html">
#     </form>
        
#     </div>
#     <div class="container-fluid my-3">
#         <h2>Products</h2>
        
#         <table class="table table-green table-striped-columns">
#             <thead>
#                 <tr>
#                     <th scope="col">S.No</th>
#                     <th scope="col">ProductName</th>
#                     <th scope="col">Price</th>
#                     <th scope="col">Quantity</th>
#                     <th scope="col">Category</th>
#                     <th scope="col">Time</th>
#                     <th scope="col">Actions</th>
#                 </tr>
#             </thead>
#             <tbody>
#                 {% if alltodo|length==0 %}
#                         no record
#                     {% else %}      
                
#                 {% for todo in alltodo %}
#                 <tr>
#                     <th scope="row">{{loop.index}}</th>
#                     <td>{{todo.product_name}}</td>
#                     <td>{{todo.price}}</td>
#                     <td>{{todo.quantity}}</td>
#                     <td>{{todo.category}}</td>
#                     <td>{{todo.date_created}}</td>
#                     <td>
#                         <a href="/ProductDelete/{{todo.sno}}" type="button" class="btn btn-danger btn-sm mx-1">Delete</button>
#                         <a href="/ProductUpdate/{{todo.sno}}" type="button" class="btn btn-success btn-sm mx-1">Update</button>
                
#                     </td>
#                 </tr>
#                 {% endfor %}
#                 {% endif %}
                
#             </tbody>
#         </table>
#     </div>

#     {% endblock body %} 



# ===========================================
# prodt_add_farmer
# ===========================================
# {% extends 'ProductBase.html' %}
# {% block body %}
#     <style>
#         /* Add your CSS styles here */
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         .container {
#             max-width: 600px;
#             margin: 50px auto;
#             background-color: #fff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
#         }

#         h1 {
#             text-align: center;
#             color: #4CAF50;
#             margin-bottom: 20px;
#         }

#         label {
#             display: block;
#             margin-bottom: 5px;
#         }

#         input[type="text"],
#         input[type="number"] {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             box-sizing: border-box;
#         }

#         select {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             box-sizing: border-box;
#         }

#         input[type="submit"] {
#             width: 100%;
#             padding: 10px;
#             background-color: #4CAF50;
#             color: #fff;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#             text-align: center;
#         }

#         input[type="submit"]:hover {
#             background-color: #45a049;
#         }

#         .file-upload {
#             position: relative;
#             overflow: hidden;
#             margin-bottom: 20px;
#         }

#         .file-upload input[type=file] {
#             position: absolute;
#             top: 0;
#             right: 0;
#             margin: 0;
#             padding: 0;
#             font-size: 20px;
#             cursor: pointer;
#             opacity: 0;
#         }

#         .file-select {
#             display: inline-block;
#             padding: 10px 20px;
#             background-color: #4CAF50;
#             color: #fff;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }
#     </style>
# </head>

# <body>
#     <div class="container my-3">
#         <h1>Product Entry Portal</h1>
#         <form action="/addfrmr" method="POST">

#         <!-- <label for="fid">Farmer ID:</label>
#         <input type="" -->
      
#         <label for="product_name">Product Name:</label>
#         <input type="text" id="product_name" name="product_name" placeholder="Enter Product Name" required>

#         <!-- <label for="productImage">Product Image:</label>
#         <div class="file-upload">
#             <input type="file" id="productImage" name="productImage" accept="image/*" required>
#             <label for="productImage" class="file-select">Choose File</label>
#         </div> -->

#         <label for="price">Price:</label>
#         <input type="number" id="price" name="price" placeholder="Enter Price" required>

#         <label for="quantity">Quantity:</label>
#         <input type="number" id="quantity" name="quantity" placeholder="Enter Quantity" required>

#         <label for="category">Select category:</label>
#         <select id="category" name="category" required>
#             <option value="" disabled selected>Select Category</option>
#             <option value="Vegetable">Vegetable</option>
#             <option value="Spices">Spices</option>
#             <option value="Fruit">Fruit</option>
#             <option value="Dairy">Dairy</option>
#         </select>

#         <input type="submit" value="Submit" href="/addfrmr">
#         <a href="/ahtml" class="btn btn-primary">Next</a>
#     </form>
        
#     </div>
#     <div class="container-fluid my-3">
#         <h2>Products</h2>
        
#         <table class="table table-green table-striped-columns">
#             <thead>
#                 <tr>
#                     <th scope="col">S.No</th>
#                     <th scope="col">Farmer ID</th>
#                     <th scope="col">ProductName</th>
#                     <th scope="col">Price</th>
#                     <th scope="col">Quantity</th>
#                     <th scope="col">Category</th>
#                     <th scope="col">Time</th>
#                     <th scope="col">Actions</th>
#                 </tr>
#             </thead>
#             <tbody>
                
#                 {% if alltodo|length==0 %}
#                         no record
#                     {% else %}      
                
#                 {% for todo in alltodo %}
#                 <tr>
#                     <th scope="row">{{loop.index}}</th>

#                     <th>{{loop.fid}}</th>
#                     <td>{{todo.product_name}}</td>
#                     <td>{{todo.price}}</td>
#                     <td>{{todo.quantity}}</td>
#                     <td>{{todo.category}}</td>
#                     <td>{{todo.date_created}}</td>
#                     <td>
#                         <a href="/ProductDelete/{{todo.sno}}" type="button" class="btn btn-danger btn-sm mx-1">Delete</button>
#                         <a href="/ProductUpdate/{{todo.sno}}" type="button" class="btn btn-success btn-sm mx-1">Update</button>
                
#                     </td>
#                 </tr>
#                 {% endfor %}
#                 {% endif %}
                
#             </tbody>
#         </table>
#     </div>

#     {% endblock body %} 

# ========================================
# ProductUpdate.htl
# ==================================



    


#     {% extends 'ProductBase.html' %}
# {% block body %}
#     <style>
#         /* Add your CSS styles here */
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         .container {
#             max-width: 600px;
#             margin: 50px auto;
#             background-color: #fff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
#         }

#         h1 {
#             text-align: center;
#             color: #4CAF50;
#             margin-bottom: 20px;
#         }

#         label {
#             display: block;
#             margin-bottom: 5px;
#         }

#         input[type="text"],
#         input[type="number"] {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             box-sizing: border-box;
#         }

#         select {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#             box-sizing: border-box;
#         }

#         input[type="submit"] {
#             width: 100%;
#             padding: 10px;
#             background-color: #4CAF50;
#             color: #fff;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#             text-align: center;
#         }

#         input[type="submit"]:hover {
#             background-color: #45a049;
#         }

#         .file-upload {
#             position: relative;
#             overflow: hidden;
#             margin-bottom: 20px;
#         }

#         .file-upload input[type=file] {
#             position: absolute;
#             top: 0;
#             right: 0;
#             margin: 0;
#             padding: 0;
#             font-size: 20px;
#             cursor: pointer;
#             opacity: 0;
#         }

#         .file-select {
#             display: inline-block;
#             padding: 10px 20px;
#             background-color: #4CAF50;
#             color: #fff;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }
#     </style>
# </head>

# <body>
#     <div class="container my-3">
#         <h1>Update Your Product </h1>
#         <h3>Product id:{{fid}}</h3>
#         <form action="/ProductUpdate/{{todo.sno}}" method="POST">
#         <!-- <form id="productForm" method="post" action="/submit_product.php"> -->
#         <label for="product_name">Product Name:</label>
#     <input type="text" id="product_name" name="product_name" value="{{todo.product_name}}" placeholder="Enter Product Name" required>

#         <!-- <label for="productImage">Product Image:</label>
#         <div class="file-upload">
#             <input type="file" id="productImage" name="productImage" accept="image/*" required>
#             <label for="productImage" class="file-select">Choose File</label>
#         </div> -->

#         <label for="price">Price:</label>
#         <input type="number" id="price" name="price" value="{{todo.price}}" placeholder="Enter Price" required>

#         <label for="quantity">Quantity:</label>
#         <input type="number" id="quantity" name="quantity" placeholder="Enter Quantity" value="{{todo.quantity}}" required>

#         <label for="category">Select category:</label>
#         <select id="category" name="category"  value="{{todo.category}}" required>
#             <option value="" disabled selected>Select Category</option>
#             <option value="Vegetable">Vegetable</option>
#             <option value="Spices">Spices</option>
#             <option value="Fruit">Fruit</option>
#             <option value="Dairy">Dairy</option>
#         </select>

#         <input type="submit" value="Update">
#     </form>
#         <!-- </form> -->
#     </div>
    

#     {% endblock body %}