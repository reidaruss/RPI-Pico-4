import mysql.connector
import datetime

class DB_Add:
    def __init__(self):
        # establishing the connection
        self.conn = mysql.connector.connect(
            user='root', password='password', host='127.0.0.1', database='pico')

        # Creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

    def insertMeasurement(self,temp,humidity,soil_moisture):


        # Preparing SQL query to INSERT a record into the database.
        insert_stmt = (
            "INSERT INTO MEASUREMENTS(TEMP, HUMIDITY, SOIL_MOISTURE, TIME)"
            "VALUES (%s, %s, %s, %s)"
        )
        data = (temp,humidity,0,datetime.datetime.now())

        try:
            # Executing the SQL command
            self.cursor.execute(insert_stmt, data)

            # Commit your changes in the database
            self.conn.commit()

        except:
            # Rolling back in case of error
            self.conn.rollback()

        print("Data inserted")

        # Closing the connection
        self.conn.close()