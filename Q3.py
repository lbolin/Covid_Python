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
mycursor.execute("SELECT state,totalTestResults,population,((totalTestResults/population)*1000000)TestPerMillion"
                 " From `all-states` INNER JOIN state_pop USING (state) WHERE date = '20200830'")
# myresult = mycursor.fetchall()
mytable = from_db_cursor(mycursor)

print(mytable)
'''
Sample Output:
+-------+------------------+------------+----------------+
| state | totalTestResults | population | TestPerMillion |
+-------+------------------+------------+----------------+
|   WY  |      75293       |   578759   |  130093.8730   |
|   NE  |      357945      |  1934408   |  185041.1080   |
|   ND  |      199965      |   762062   |  262399.9090   |
|   NC  |     2243273      |  10488084  |  213887.7790   |
|   MT  |      246661      |  1068778   |  230787.8710   |
|   NH  |      209295      |  1359711   |  153926.0910   |
|   MN  |     1122071      |  5639632   |  198961.7400   |
|   MI  |     2744794      |  9986857   |  274840.6230   |
|   ME  |      259661      |  1344212   |  193169.6780   |
|   NJ  |     2836334      |  8882190   |  319328.2280   |
|   MD  |     1319238      |  6045680   |  218211.6810   |
'''