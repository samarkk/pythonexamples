import sqlite3

sqlite3_db_location='D:/tmp/learndb.db'
conn = sqlite3.connect(sqlite3_db_location)
conn.execute('DROP TABLE PRODUCTS')
conn.execute("""CREATE TABLE IF NOT EXISTS products (
         productID    INTEGER PRIMARY KEY AUTOINCREMENT,
         productCode  CHAR(3)       NOT NULL DEFAULT '',
         name         VARCHAR(30)   NOT NULL DEFAULT '',
         quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
         price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99
       );""")

# Insert a row with all the column values
cur = conn.execute("INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);")

# Insert multiple rows in one command
# Inserting NULL to the auto_increment column results in max_value + 1
cur = conn.execute("""
                   INSERT INTO products VALUES
         (NULL, 'PEN', 'Pen Blue',  8000, 1.25),
         (NULL, 'PEN', 'Pen Black', 2000, 1.25);
         """)

# Insert value to selected columns
# Missing value for the auto_increment column also results in max_value + 1
conn.execute("""INSERT INTO products (productCode, name, quantity, price) VALUES
         ('PEC', 'Pencil 2B', 10000, 0.48),
         ('PEC', 'Pencil 2H', 8000, 0.49)""")


# Missing columns get their default values
conn.execute("""
             INSERT INTO products (productCode, name) VALUES ('PEC', 'Pencil HB')""")

# Remove the last row
conn.execute('DELETE FROM products WHERE productID = 1006')

cur = conn.execute('Select * from products')
print(cur.fetchall())

cur_lim = conn.execute('Select * from products where price < 1000')
print(cur_lim.fetchall())

 # String values are quoted
print(conn.execute("SELECT name, price FROM products WHERE productCode = 'PEN'").fetchall())

# String Pattern Matching - LIKE and NOT LIKE
# Display the first two rows
print(conn.execute(" SELECT name, price FROM products WHERE name LIKE 'PENCIL%'").fetchall())

# logical operaotrs
print(conn.execute("""SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'Pen %' """).fetchall())

print(conn.execute("""SELECT * FROM products WHERE NOT (quantity >= 5000 AND name LIKE 'Pen %')""").fetchall())

# IN, NOT IN
print(conn.execute("""SELECT * FROM products WHERE name IN ('Pen Red', 'Pen Black');""").fetchall())

# BETWEEN, NOT BETWEEN
print(conn.execute("""SELECT * FROM products 
       WHERE (price BETWEEN 1.0 AND 2.0) AND (quantity BETWEEN 1000 AND 2000)""").fetchall())

# IS NULL, IS NOT NULL
print(conn.execute("""SELECT * FROM products WHERE productCode IS NULL""").fetchall())

# ORDER BY
print(conn.execute("""SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC""").fetchall())

# LIMIT CLAUSE  

print(conn.execute("""SELECT * FROM products ORDER BY price LIMIT 2""").fetchall())
# Skip the first two rows and display the next 1 row
print(conn.execute("""SELECT * FROM products ORDER BY price LIMIT 2, 1""").fetchall())

# ALIAS, AS
print(conn.execute(""" SELECT productID AS ID, productCode AS Code,
              name AS Description, price AS `Unit Price`  -- Define aliases to be used as display names
       FROM products
       ORDER BY ID;  -- Use alias ID as reference """).fetchall())

# DISTINCT AND GROUPING - SUMMARY REPORTS

print(conn.execute(""" SELECT DISTINCT price, name FROM products""").fetchall())

# Only first record in each group is shown
print(conn.execute(""" SELECT * FROM products GROUP BY productCode """).fetchall())

# Group By Aggregate Functions: COUNT, MAX, MIN, AVG, SUM

# Function COUNT(*) returns the number of rows selected
print(conn.execute(""" SELECT COUNT(*) AS `Count` FROM products  """).fetchall())

print(conn.execute(""" SELECT productCode, COUNT(*) AS count 
       FROM products 
       GROUP BY productCode
       ORDER BY count DESC  """).fetchall())

print(conn.execute("""SELECT MAX(price), MIN(price), AVG(price), SUM(quantity)
       FROM products  """).fetchall())

# HAVING CLAUSE
print(conn.execute(""" SELECT
          productCode AS `Product Code`,
          COUNT(*) AS `Count`,
          CAST(AVG(price) AS DECIMAL(7,2)) AS `Average`
       FROM products 
       GROUP BY productCode
       HAVING Count >=3  """).fetchall())

# Modifying data - Update
print(conn.execute(""" UPDATE products SET price = price * 1.1; """).fetchall())
print(conn.execute(""" SELECT * FROM PRODUCTS """).fetchall())

# modify selected rows
conn.execute("""
             UPDATE products SET quantity = quantity - 100 WHERE name = 'Pen Red'
             """)
print(conn.execute(""" SELECT * FROM PRODUCTS """).fetchall())

# modify more than one value
conn.execute("""
             UPDATE products SET quantity = quantity + 50, price = 1.23 WHERE name = 'Pen Red
             """)
print(conn.execute(""" SELECT * FROM PRODUCTS """).fetchall())

# Deleting Rows
conn.execute("""
             DELETE FROM products WHERE name LIKE 'Pencil%'
             """)
print(conn.execute(""" SELECT * FROM PRODUCTS """).fetchall())


# Multiple tables
conn.execute("""
             CREATE TABLE IF NOT EXISTS suppliers (
         supplierID  INTEGER PRIMARY KEY AUTOINCREMENT, 
         name        VARCHAR(30)   NOT NULL DEFAULT '', 
         phone       CHAR(8)       NOT NULL DEFAULT ''
       )""")

conn.execute("""
             INSERT INTO suppliers VALUES
          (501, 'ABC Traders', '88881111'), 
          (502, 'XYZ Company', '88882222'), 
          (503, 'QQ Corp', '88883333');
             """)
print(conn.execute(""" SELECT * FROM SUPPLIERS """).fetchall())


conn.execute("""
             Alter table products 
             add column supplierID int
             """)

conn.execute("""
             Update Products 
             set SupplierID = 501
             """)

print(conn.execute(""" SELECT * FROM PRODUCTS  """).fetchall())

# need to enable foreign keys on the connection
# this should be executed immediately

conn.execute('PRAGMA foreign_keys=1')

conn.execute("""CREATE TABLE IF NOT EXISTS productsn (
         productID    INTEGER PRIMARY KEY AUTOINCREMENT,
         productCode  CHAR(3)       NOT NULL DEFAULT '',
         name         VARCHAR(30)   NOT NULL DEFAULT '',
         quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
         price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
         supplierID   INTEGER foreigh key references products(supplierID)
       );""")

print(conn.execute(""" select productid, productcode, p.name,
                   quantity, price, s.supplierid 
                   from products p 
                   inner join suppliers s
                   on p.supplierid = s.supplierid 
                   """).fetchall())

conn.execute("""
             Insert into productsn
             select productid, productcode, p.name,
             quantity, price, s.supplierid 
             from products p 
             inner join suppliers s
             on p.supplierid = s.supplierid 
            """)

# select with join
print(conn.execute(""" 
                   select productid, productcode, p.name,
                   quantity, price, s.supplierid 
                   from productsn p 
                   inner join suppliers s
                   on p.supplierid = s.supplierid 
                   """).fetchall())

# Join via WHERE clause (lagacy and not recommended)
print(conn.execute("""
                   SELECT products.name, price, suppliers.name 
       FROM products, suppliers 
       WHERE products.supplierID = suppliers.supplierID
          AND price < 0.6
                   """).fetchall())

# Use aliases for column names for display
print(conn.execute("""
                   SELECT products.name AS `Product Name`, price, suppliers.name AS `Supplier Name` 
       FROM products 
          JOIN suppliers ON products.supplierID = suppliers.supplierID
       WHERE price < 0.6
       """).fetchall())

# use aliases for table names too
print(conn.execute(""" 
                   SELECT p.name AS `Product Name`, p.price, s.name AS `Supplier Name` 
       FROM products AS p 
          JOIN suppliers AS s ON p.supplierID = s.supplierID
       WHERE p.price < 0.6;                   
               """).fetchall())

# many to many relationship
conn.execute("""
             CREATE TABLE products_suppliers (
         productID   INT UNSIGNED  NOT NULL,
         supplierID  INT UNSIGNED  NOT NULL,
                     -- Same data types as the parent tables
         PRIMARY KEY (productID, supplierID),
                     -- uniqueness
         FOREIGN KEY (productID)  REFERENCES products  (productID),
         FOREIGN KEY (supplierID) REFERENCES suppliers (supplierID)
       )""")

# conn.execute('drop table products_suppliers')
conn.execute("""
             INSERT INTO products_suppliers VALUES (1001, 501), (1002, 501),
       (1003, 501), (1004, 502), (1001, 503)
       """)


print(conn.execute(""" 
                   select * from products_suppliers
                   """).fetchall())

print(conn.execute("""
                   SELECT products.name AS `Product Name`, price, suppliers.name AS `Supplier Name`
       FROM products_suppliers 
          JOIN products  ON products_suppliers.productID = products.productID
          JOIN suppliers ON products_suppliers.supplierID = suppliers.supplierID
       WHERE price < 0.6
                   """).fetchall())

# one to one relationship
conn.execute("""
             CREATE TABLE product_details (
          productID  INT UNSIGNED   NOT NULL,
                     -- same data type as the parent table
          comment    TEXT  NULL,
                     -- up to 64KB
          PRIMARY KEY (productID),
          FOREIGN KEY (productID) REFERENCES products (productID)
       )
        """)

conn.execute(""" 
                   insert into product_details values
                   (1001, 'a red pen to reflect 
                   the passion you put into your words
                   ')
                   """)
                   
print(conn.execute(""" 
                   select *
                   from products p
                   inner join product_details pd
                   on p.productid = pd.productid
                   """).fetchall())

print(conn.execute("""  """).fetchall())
print(conn.execute("""  """).fetchall())
print(conn.execute("""  """).fetchall())



conn.close()