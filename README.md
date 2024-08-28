# Portal-for-Farmers
Portal for farmers to sell their products at better rate
Technologies Used:

# 1.	HTML and CSS:
   
HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets) are fundamental technologies used in web development, playing essential roles in creating visually appealing and interactive user interfaces.
HTML (Hypertext Markup Language):
 
●        HTML serves as the backbone of web pages, defining the structure and content elements.
●        It utilizes tags to denote different elements like headings, paragraphs, images, and forms.
●        Semantic markup ensures accessibility and SEO by organizing content meaningfully.
●        HTML provides the foundation for applying CSS styles to enhance visual presentation.

CSS (Cascading Style Sheets):
●        CSS styles HTML elements, controlling their appearance, layout, and behavior.
●        Developers can customize fonts, colors, spacing, borders, and backgrounds using CSS.
●        Responsive design principles allow websites to adapt to various screen sizes and devices.
●        CSS selectors and rules ensure consistent styling throughout the website.
●        HTML and CSS work in tandem to create visually appealing, accessible, and user-friendly interfaces for web applications. HTML provides the structure and semantics, while CSS adds the aesthetic and stylistic enhancements, resulting in an engaging and immersive user experience. By leveraging the capabilities of HTML and CSS, developers can design interfaces that not only meet functional requirements but also captivate and delight users with their visual appeal and interactivity.

# 2.	MySQL for database management:
   
In the Recipe Generator Project, the MySQL database comprises six interconnected tables: cuisine, Recipe, userlogin, bookmark, and ingredient_recipe. Each table serves a specific purpose and is linked to others through relationships to facilitate data management and retrieval. Here's an overview of the tables and their interconnections:
A)Products Table:
●        Stores information about products listed by farmers.
●        Columns include sno (primary key), fid (foreign key referencing Accounts table), product_name, price, quantity, category, and date_created.
●        Enables farmers to add and manage their products for sale.
B)Accounts Table:
●        Manages user authentication and login information. Columns include fid (primary key), username, password, email, and Role.
●        Supports user registration, login, and role-based access control.
 C)Earning Table:
●        Tracks earnings generated from sales transactions.
●        Columns include ch_id (primary key), bill_id (foreign key referencing Cart table), fid (foreign key referencing Accounts table), amount_earned, and order_date.
●        Facilitates the calculation and recording of earnings for farmers.
D)Cart Table:
●        Records items added to customers' carts.
●        Columns include ch_id (primary key), bill_id, fid (foreign key referencing Accounts table), sno (foreign key referencing Products table),,product_name,price and quantity.
●        Supports the management of customer orders and facilitates the checkout process.
E) Primary Key & Foreign Key:
Primary Key:
●        ‘sno’ in the Products table serves as the primary key, uniquely identifying each product.
Foreign Key:
●        ‘Fid’ in the ‘Products’, ‘Earning’, and ‘Cart’ tables establishes relationships with the Accounts table, linking each record to the respective farmer.

These tables are interconnected through foreign key constraints, enabling efficient data retrieval and manipulation. The database structure supports the functionalities of the web platform, including product management, user authentication, earnings tracking, and cart management, contributing to a seamless user experience.

# 3.	Python flask connectivity:
In the portal for farmer, Flask is essential to establishing communication between the database, server-side logic, and frontend interface. This is how Flask makes this connectivity possible:
1.	Routing and URL handling: In Flask, routes are defined using the @app.route() decorator, which associates specific URLs with Python functions. For example, @app.route('/') defines the root URL, and @app.route('/signup') defines the URL for signing up. These routes handle incoming HTTP requests and direct them to the appropriate Python functions for processing. By defining routes, developers can create endpoints for various functionalities like user authentication, product management, and more.
2.	Template Rendering: Flask integrates with Jinja2, a powerful templating engine, to dynamically generate HTML content. Templates are HTML files that include placeholders for dynamic data. In the Flask application, these templates are rendered with context variables, which are passed from the backend Python code to the HTML template. For example, render_template('index.html', data=data) would render the index.html template with the provided data. This allows developers to create dynamic web pages that display information retrieved from the backend database.
3.	Database Interaction: Flask applications can interact with databases using various libraries such as Flask-SQLAlchemy and Flask-MySQLdb. In the provided code, SQLAlchemy is used to define database models and interact with the MySQL database. Database models are Python classes that represent tables in the database, and SQLAlchemy provides an ORM (Object-Relational Mapper) for querying and manipulating data. For example, the Products class represents a table of products, and methods like query.filter_by() are used to retrieve data from the database based on specified criteria.
Farmer Authentication: Authentication functionality is implemented in the Flask application to ensure that only authenticated users (in this case, farmers) can access certain parts of the application. When a user attempts to log in, their credentials are verified against records stored in the database. If the credentials are valid, a session is created to keep the user logged in across requests. Routes are protected by checking whether a user is logged in (session['loggedin']) before granting access. This ensures that only authenticated farmers can access functionalities like adding products or viewing earnings

Index Page:

![image](https://github.com/user-attachments/assets/6b00af03-2912-46e4-a1c4-a0d367c398fd)

Farmer Product Management:

![image](https://github.com/user-attachments/assets/5e8311f1-d7da-46c0-833b-dd83da2535bd)

User Login and Registration:

![image](https://github.com/user-attachments/assets/68fb6d46-fdff-4bf4-af4c-55c73babe413)

![image](https://github.com/user-attachments/assets/2ac39b0f-b4a1-4c72-991e-cb00149fd7b9)

Customer Product Viewing and Cart Functionality:

![image](https://github.com/user-attachments/assets/def99c2c-51de-4c77-982e-aa1359b14e08)

Earning Page:

![image](https://github.com/user-attachments/assets/8fa498b8-b2d6-405b-af44-289fe919c1c1)





