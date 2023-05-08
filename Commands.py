#Here is a list of functions, when called they return the array of bytes.
# CRC needs to be added, and they can be send
CMD_SIZE = 10

#Exemplary command:
def CMD_PING(arg0,arg1):
    arg0 = 0xaa5555aa
    arg1 = 0xaa5555aa

    data = bytearray([0])

    data.extend(arg0.to_bytes(4,'little'))
    data.extend(arg1.to_bytes(4, 'little'))
    data.append(0)
    assert (len(data) == CMD_SIZE)
    return data

if __name__ == "__main__":
    print(CMD_PING(1,1))