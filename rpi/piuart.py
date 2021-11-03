import serial
import time

from mysql_add import DB_Add

class ReceiveData:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #9600 is baud rate(must be same with that of NodeMCU)
        self.ser.flush()

    def listen(self):
        while True:

            line = self.ser.readline().decode('utf-8').rstrip()
            print(line[2:11])
            line = line[2:11]
            s = line.split(',')
            #print(s)
            try:
                db_temp = DB_Add()
                db_temp.insertMeasurement(s[0],s[1],0)
            except:
                print("Error adding to db")
                continue
            time.sleep(5*60)
