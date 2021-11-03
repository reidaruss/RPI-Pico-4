from piuart import ReceiveData
from Transmit import Transmit

class Runner:
    def __init__(self):
        self.receiver = ReceiveData()
        self.transmitter = Transmit()
        
    def start(self):
        # Thread each service
        # Receive Data, Store into Database
        self.receiver.listen()
        
        self.transmitter.sendMessage(10)
        
        