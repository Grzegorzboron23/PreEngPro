import Frontend
import Backend
import HelpfulFunctions
import BackendConnect
import Commands
import threading
import time

import time

FinishFlag = True

def main():
    #make a thread for the frontend
    global FinishFlag
    BackendThread = threading.Thread(target=SerialReception)
    BackendThread.start()
    Frontend.FrontInit()
    #kill should be send to the backend #todo
    FinishFlag = False

    BackendThread.join()
    exit(0)


def SerialReception():
    global FinishFlag
    time.sleep(0.1)
    #try to autoconnect:
    serialPort = BackendConnect.SerialAutoConnect()
    if(serialPort == False):
        print("main: Unable to automatically open the port")
        Frontend.FrontSetPort(0)
    else:
        print("Port", serialPort.name, "is open")
        Frontend.FrontSetPort(serialPort.name)

    while(FinishFlag):


        time.sleep(0.1)

    #for now just wait

if __name__ == "__main__":
    main()



