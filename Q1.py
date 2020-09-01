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
mycursor.execute("SELECT `state`,`date`,`totalTestResults`,`positive`,`death` From `all-states` where `date` = 20200830")
# myresult = mycursor.fetchall()
mytable = from_db_cursor(mycursor)

print(mytable)

'''
Sample Output:

+-------+----------+------------------+----------+-------+
| state |   date   | totalTestResults | positive | death |
+-------+----------+------------------+----------+-------+
|   WY  | 20200830 |      75293       |   3820   |   37  |
|   NE  | 20200830 |      357945      |  33753   |  392  |
|   ND  | 20200830 |      199965      |  11702   |  118  |
|   NC  | 20200830 |     2243273      |  166127  |  2692 |
|   MT  | 20200830 |      246661      |   7340   |  104  |
|   NH  | 20200830 |      209295      |   7254   |  432  |
|   MN  | 20200830 |     1122071      |  75189   |  1865 |
|   MI  | 20200830 |     2744794      |  112526  |  6748 |
|   ME  | 20200830 |      259661      |   4512   |  132  |
|   NJ  | 20200830 |     2836334      |  191611  | 15937 |
|   MD  | 20200830 |     1319238      |  107791  |  3752 |
|   NM  | 20200830 |      752522      |  25178   |  769  |
|   MA  | 20200830 |     1723774      |  128229  |  9049 |
|   NV  | 20200830 |      595685      |  68908   |  1302 |
|   LA  | 20200830 |     1868750      |  147867  |  4931 |
'''