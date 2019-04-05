# -*- coding: utf-8 -*
import serial
import time

def showPacket_(packet):
    print([hex(byte) for byte in packet])

class SCS215():
    def __init__(self,devName="ttyAMA0",baudRate=1000000):
        self.devName = "/dev/"+devName
        self.baudRate = baudRate

    def open(self):
        self.ser = serial.Serial(self.devName,self.baudRate,timeout=0.5)

    def close(self):
        self.ser.close()
    
    def checksum(self,packet):
        sum = 0
        for byte in packet:
            sum += byte
        sum = ~sum & 0xFF
        return sum

    def ping(self,id):
        txPacket = [0xFF,0xFF] + [id] + [0x02,0x01]
        txPacket = txPacket + [self.checksum(txPacket[2:])]
        self.ser.write(txPacket)
        rxPacket = self.ser.read(6)
        return ord(rxPacket[4]) if len(rxPacket)==6 else None

    def read(self,id,addr,size):    
        txPacket = [0xFF,0xFF] + [id] + [0x04,0x02] + [addr,size]
        txPacket = txPacket + [self.checksum(txPacket[2:])]
        self.ser.write(txPacket)
        rxPacket = self.ser.read(6+size)
        return [ord(byte) for byte in rxPacket[-(size+1):-1]]

    def writeSync(self,idList,addr,dataList):
        txPacket = [0xFF,0xFF,0xFE,(len(dataList[0])+1)*len(dataList)+4,0x83,addr,len(dataList[0])]
        for id,data in zip(idList,dataList):
            txPacket = txPacket + [id] + data
        txPacket = txPacket + [self.checksum(txPacket[2:])]
        #showPacket_(txPacket)
        self.ser.write(txPacket)



if __name__ == '__main__':
    servo = SCS215()
    servo.open()
    #print(servo.read(3,0x2A,4))
    #servo.writeSync(idList=[2],addr=0x28,dataList=[[0x01]])
    #servo.writeSync(idList=[2],addr=0x2A,dataList=[[0x02,0x40,0x00,0x00,0x00,0x00]])
    servo.writeSync(idList=[11],addr=0x2A,dataList=[[0x02,0x40]])
    #print(servo.read(3,0x2A,4))
    time.sleep(3)
    servo.close()


