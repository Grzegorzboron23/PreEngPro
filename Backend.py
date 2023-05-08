#The idea is to put an array of characters by a command make function,
#then, serialize it to bytes and send through a serial port

import serial
import HelpfulFunctions as HF

#Global variable
serialPort = False

def SerialInit(path:str):
    global serialPort
    try:
        serialPort = serial.Serial(path,115200) #TODO: put more arguments.
        if(serialPort.isOpen()):
            print("SerialInit: Serial is open!")
            return serialPort
        print("SerialInit: Failed to open the port",path)
        return False
    except( BaseException ): #TODO: Distingush the exceptions.
        print("SerialInit: serial.Serial has thrown an exception!")
    return False


def SerialSendCMD(command: bytearray):
    global serialPort
    #append the CRC:
    CRC = HF.CRC8(command)
    command[len(command)-1] = CRC

    #send the command:
    serialPort.write(command)
    return

def SerialGet():
    global serialPort
    return serialPort