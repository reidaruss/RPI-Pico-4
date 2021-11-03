import mysql.connector
import datetime

class DB_Add:
    def __init__(self):
        # establishing the connection
        self.conn = mysql.connector.connect(
            user='root', password='butter', host='127.0.0.1', database='pico')

        # Creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

    def insertMeasurement(self,temp,humidity,soil_moisture):


        # Preparing SQL query to INSERT a record into the database.
        insert_stmt = (
            "INSERT INTO measurements(TEMP, HUMIDITY, SOIL_MOISTURE, TIME)"
            "VALUES (%s, %s, %s, %s);"
        )
        data = (float(temp),float(humidity),11.1,datetime.datetime.now())
        try:
            # Executing the SQL command
            self.cursor.execute(insert_stmt, data)
            

            # Commit your changes in the database
            self.conn.commit()
            print("Data inserted")

        except:
            # Rolling back in case of error
            self.conn.rollback()


        # Closing the connection
        self.conn.close()