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
mycursor.execute(
    'SELECT state,totalTestResults,population,FORMAT(((totalTestResults/population)*1000000),2)TestPerMillion'
    ' From `all-states` INNER JOIN state_pop USING (state) WHERE date = \'20200830\'')
# myresult = mycursor.fetchall()
mytable = from_db_cursor(mycursor)

print(mytable)
'''
Sample Output:
+-------+------------------+------------+----------------+
| state | totalTestResults | population | TestPerMillion |
+-------+------------------+------------+----------------+
|   WY  |      75293       |   578759   |   130,093.87   |
|   NE  |      357945      |  1934408   |   185,041.11   |
|   ND  |      199965      |   762062   |   262,399.91   |
|   NC  |     2243273      |  10488084  |   213,887.78   |
|   MT  |      246661      |  1068778   |   230,787.87   |
|   NH  |      209295      |  1359711   |   153,926.09   |
|   MN  |     1122071      |  5639632   |   198,961.74   |
|   MI  |     2744794      |  9986857   |   274,840.62   |
|   ME  |      259661      |  1344212   |   193,169.68   |
'''