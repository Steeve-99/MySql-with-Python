import mysql.connector

try:                            
    mydb = mysql.connector.connect(
            host = "localhost",
            user ="xxxxxx",
            password = "********",
            database = "myDataBase"
            ) # Connecting with MySql database 
    
    if mydb:
        print("Connected with Mysql database")
    
except Exception as e:
    print("Cannot connect with database, {} " .format(e))
    
cursor = mydb.cursor()

def execute(query):
    try:
        cursor.execute(query)
    except Exception as e:
        print("ERROR, {}".format(e))
        
def executeQuery(query, value):
    
    try:
        if isinstance(value, list):
            cursor.executemany(query, value) # Executes many statements together
        else:
            cursor.execute(query, value) # Executes single query at a time
        
    except Exception as e:
        print("ERROR, {}".format(e))
   
query1 = "CREATE TABLE StudentData4(Id int,fname varchar(10),lname varchar(10),department varchar(30),marks float,result varchar(4))"
execute(query1) # This Query should be executed only once , After executing comment it.

query2 = "INSERT INTO StudentData4 values (%s, %s, %s, %s, %s, %s)"

rec1 = (1, "MS", "Dhoni", "Mechanical", 56.3, "P")
rec2 = (2 ,"Virat", "Kohli", "Electronics and comm", 63.1, "P")
rec3 = (3, "yuzi", "Chahal", "Information and sci", 23.3 ,"F")
rec4 = (4, "B", "Kumar", "Electrical",33.3, "F")

values = [
        (5, "Rohit", "Sharma", "Mechanical", 71, "P"),
        (6, "Shikar", "Dhavan", "Electrical", 31.3, "F"),
        (7, "R", "Ashwin", "civil", 45, "P")
        ]

executeQuery(query2, rec1)
executeQuery(query2, rec2)
executeQuery(query2, rec3)
executeQuery(query2, rec4)
executeQuery(query2, values)

def displayData():
    query3 = "SELECT * FROM StudentData4"
    execute(query3)
    results = cursor.fetchall()
    for data in results:
        print(data)

displayData()
print()

query4 = "UPDATE StudentData4 SET marks = marks - 10 WHERE marks > 60"
execute(query4)

displayData()
print()

query5 = "DELETE FROM StudentData4 WHERE id = 7"
execute(query5)

displayData()

mydb.commit() # Save all changes made