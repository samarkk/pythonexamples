# download world database from
# https://downloads.mysql.com/docs/world-db.zip
# unzip it
# and in mysql execute
# source <world.sql location>

# pip3 install mysql-connector-python to get the mysql package
# with just mysql-connector will get  Authentication plugin 'caching_sha2_password' is not supported

import mysql.connector
from mysql.connector import errors, errorcode
from collections import OrderedDict
from datetime import datetime, timedelta
import pprint

pp = pprint.PrettyPrinter(indent=4)
'''
connect specifying parameters
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='abcD123$'
)
'''

mycursor = mydb.cursor()

# create a new database

mycursor.execute('create database if not exists ntestdb')

# connect using configuration file
mysql_conf_file_location = 'D:/localmts/pycodes/my.conf'
mydb = mysql.connector.connect(option_files=mysql_conf_file_location)
mycursor = mydb.cursor()


# create a table in the database
mycursor.execute(
    '''
        create table if not exists ntestdb.utable(
        id int primary key auto_increment, 
        fname varchar(50), 
        lname varchar(50), gender varchar(5),       
        height decimal)      
''')

# insert a row into the table
mycursor.execute(
    '''
        insert into ntestdb.utable(fname, lname, gender, height)
        values ('user1', 'ln1', 'm', 181.2)
    ''')

# get the table rows
mycursor.execute('select * from ntestdb.utable')
myres = mycursor.fetchall()

mycursor.close()

'''
In the case of an unbuffered cursor, trying to close the cursor object or executing a new query before reading the result set from the old one will result in InternalError: Unread result found exception
'''

# Cursor Attributes

cursor = mydb.cursor()

cursor.execute("""select * from ntestdb.utable""")

print("rowcount (initial):", cursor.rowcount, end='\n\n')

# reading rows but not displaying
for row in cursor: pass

print("column_names:", cursor.column_names, end='\n\n')
print("with_rows:", cursor.with_rows, end='\n\n')

print("description: ", end="")
pp.pprint(cursor.description)

print("\nstatement:", cursor.statement, end='\n\n')

print("lastrowid:", cursor.lastrowid, end='\n\n')

print("rowcount (final):", cursor.rowcount, end='\n\n')

cursor.close()

# create multiple tables
cursor = mydb.cursor()

db_name = 'blog'

tables = OrderedDict()

tables['category'] = '''
create table category
(
  id int not null auto_increment primary key,
  name varchar(50) not null
)
'''

tables['post'] = '''
create table post
(
  id int not null auto_increment PRIMARY KEY,
  title varchar(200) not null,
  content text not null,
  date TIMESTAMP not null,
  category_id int not null,
  FOREIGN key (category_id) REFERENCES category(id)
)
'''


def create_db(cursor):
    try:
        cursor.execute("create database {}".format(db_name))
        print("Database created.")
    except mysql.connector.Error as err:
        print("Database creation failed:", err)
        exit(1)

try:
    mydb.database = db_name
    print('Database {} already exist.'.format(db_name))
except mysql.connector.Error as err:
    # database doesn't exist, create one
    if errorcode.ER_BAD_DB_ERROR == err.errno:
        create_db(cursor)
        mydb.database = db_name

for k, v in tables.items():
    try:
        cursor.execute(v)
        print('Table {} created.'.format(k))
    except mysql.connector.Error as err:
        if errorcode.ER_TABLE_EXISTS_ERROR == err.errno:
            print('Table {} already exists.'.format(k))

cursor.close()

# bulk inserts
cursor = mydb.cursor(buffered=True)

insert_many_category_sql = "insert into category(name) value(%s)"

insert_many_category_data = [
    ('css',),
    ('java',),
    ('design',),
    ('ui',),
    ('php',),
]

cursor.executemany(insert_many_category_sql, insert_many_category_data)  # insert categories into the category table

insert_many_potst_sql = "insert into post(title, content, category_id) value(%s, %s, %s, %s)"

insert_many_potst_data = [
    ('title 2', 'content 2', datetime.now().date(), 1),
    ('title 3', 'content 3', datetime.now().date(), 1),
    ('title 4', 'content 4', datetime.now().date(), 1),
    ('title 5', 'content 5', datetime.now().date(), 1),
    ('title 6', 'content 6', datetime.now().date(), 1),
]

cursor.executemany(insert_many_potst_sql, insert_many_potst_data)
mydb.commit()  # commit the changes

# update a single row
cursor = mydb.cursor(buffered=True)

update_one_sql = "update category set name=%s WHERE ID=2"

update_one_data = ('CSS',)

cursor.execute(update_one_sql, update_one_data)

mydb.commit()  # commit the changes

print("Rows affected:", cursor.rowcount)

cursor.close()

# update multiple rows
cursor = mydb.cursor(buffered=True)

update_many_sql = "update post set date=%s"

update_many_data = [
            (datetime.now().date() + timedelta(days=10),), 
        ]

cursor.executemany(update_many_sql, update_many_data)

mydb.commit()  # commit the changes

print("Rows affected:", cursor.rowcount)

cursor.close()

# delete one row
cursor = mydb.cursor(buffered=True)

delete_one_sql = "delete from category where name=%s limit 1"

delete_one_data = ('php',)

cursor.execute(delete_one_sql, delete_one_data)

mydb.commit()  # commit the changes

print("Rows affected:", cursor.rowcount)

cursor.close()

# delete multiple rows
cursor = mydb.cursor(prepared=True)

delete_multiple_sql = "delete from post where id=%s"

delete_multiple_data = [
            (3,), (4,), (5,), (6,)
        ]

cursor.executemany(delete_multiple_sql, delete_multiple_data)

mydb.commit()  # commit the changes

print("Rows affected:", cursor.rowcount)

cursor.close()

mydb.close()

'''
transactions
check the mysql autocmooit level in the shell, issue
select @@autocommit
1 would mean that it is enaabled

By default mysql python connector has autocommit disabled
That is the reason why commit has to be called
The rollback() method of the connection object can be used to rollback the transaction
To enable the autocommit mode set autocommit argument of the connection object to True.

'''
mydb.close()

try:

    db = mysql.connector.connect(option_files=mysql_conf_file_location, autocommit=True)

    cursor = db.cursor()

    sql1 = """
    create table employees(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary INT NOT NULL
    )
    """

    cursor.execute(sql1)

    sql2 = """
    insert into employees(name, salary) value('John', 15000)
    """

    cursor.execute(sql2)

    sql2 = """
    insert into employees(name, salary) value('Bob', 20000)
    """

    cursor.execute(sql2)

    # db.commit()  # we don't need to call commit() because autocommit=True

    print('Table created successfully.')

except errors.Error as e:
    print(e)

finally:
    cursor.close()
    db.close()

# start_transaction() method
'''
If autocommit is enabled (i.e autocommit=True) and you want to execute a set of statements as a single unit, then you must explicitly start the transaction using the start_transaction() method of the connection object
'''
try:

    db = mysql.connector.connect(option_files=mysql_conf_file_location, autocommit=True)

    cursor = db.cursor()

    db.start_transaction()

    # these two INSERT statements are executed as a single unit

    start_transaction_sql1 = """
    insert into employees(name, salary) value('Tom', 19000)
    """

    start_transaction_sql2 = """
    insert into employees(name, salary) value('Leo', 21000)
    """

    cursor.execute(start_transaction_sql1)
    cursor.execute(start_transaction_sql2)

    db.commit()  # commit changes

    print('Transaction committed.')

except errors.Error as e:
    db.rollback()  # rollback changes
    print("Rolling back ...")
    print(e)

finally:
    cursor.close()
    db.close()

# rollback the entire transaction on error - all or nothing
try:

    db = mysql.connector.connect(option_files=mysql_conf_file_location, autocommit=True)

    cursor = db.cursor()

    db.start_transaction()

    # these two INSERT statements are executed as a single unit

    start_transaction_sql11 = """
    insert into employees(name, salary) value('Tom', 19000)
    """

    start_transaction_sql21 = """
    insert into employees(name, salarys) value('Leo', 21000)
    """

    cursor.execute(start_transaction_sql11)
    cursor.execute(start_transaction_sql21)

    db.commit()  # commit changes

    print('Transaction committed.')

except errors.Error as e:
    db.rollback()  # rollback changes
    print("Rolling back ...")
    print(e)

finally:
    cursor.close()
    db.close()
    
'''
Rolling back ...
1054 (42S22): Unknown column 'salarys' in 'field list'
'''
