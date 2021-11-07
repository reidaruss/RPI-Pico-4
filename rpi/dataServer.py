from flask import Flask, send_from_directory, render_template
import mysql.connector
import datetime

app = Flask(__name__, template_folder='./templates')

def getData():

    # establishing the connection
    conn = mysql.connector.connect(user='root', password='butter', host='127.0.0.1', database='pico')
    cursor = conn.cursor()
    # Preparing SQL query to INSERT a record into the database.
    request = (
        "SELECT * FROM measurements;"
    )
    try:
        # Executing the SQL command
        cursor.execute(request)
        print("Data retrieved.")

    except:
        # Rolling back in case of error
        print("Error retrieving data from sql server")

    # Closing the connection
    conn.close()



@app.route('/')
def hello_world():
    print("hello")

@app.route('/get-data')
def getDataRoute():
    return getData()




if __name__ == '__main__':
    app.run(host="0.0.0.0",port="2000")
