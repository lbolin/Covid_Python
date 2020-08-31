import mysql.connector
import config
import prettytable
from prettytable import from_db_cursor

mydb = mysql.connector.connect(
    host="localhost",
    user=config.user,
    password=config.password,
    database="covid"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT `state`,`date`,`positive`,`death` From `all-states` where `date` = 20200829")
# myresult = mycursor.fetchall()
mytable = from_db_cursor(mycursor)

print(mytable)


