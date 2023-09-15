import mysql.connector

def db():
    # Creating connection object
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "dbdemo",
    )

    # Printing the connection object
    print(mydb)

    # Creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
    mycursor = mydb.cursor()

    #display all db names
    mycursor.execute("show databases")
    for x in mycursor:
      print(x)

    # used to execute a SQL statement. create db
    mycursor.execute("create database if not exists dbdemo")     #if not exists use to do not recreate or generate error

    #create table
    mycursor.execute("create table if not exists persons(personid int, lastname varchar(255), firstname varchar(255), address varchar(255), city varchar(255))")

    #insert data
    sql = "insert into persons (personid, lastname, firstname, address, city) values (%s, %s, %s, %s, %s)"  #to avoid duplicate records can apply unique constraints on id
    val = [('1', 'mishra', 'nisha', 'bhosari', 'pune'),
           ('2', 'nene', 'disha', 'pimpri', 'pune'),
           ('3', 'jha', 'mira', 'chinchwad', 'mumbai')]

    #insert many at a time . for single use execute()
    mycursor.executemany(sql, val)
    #commite changes
    mydb.commit()

    # Print the number of rows affected
    print(mycursor.rowcount, "records inserted.")

    #fetch data
    print(mycursor.execute("select * from persons"))

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # disconnecting from server
    #mydb.close()


if __name__ == '__main__':
    db()