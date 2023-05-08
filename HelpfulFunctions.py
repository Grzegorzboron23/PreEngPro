


def CRC8(data, length):
    poly = 0x31
    crc = 0xFF

    for i in range(length):
        byte = data[i]
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFF

    return crc
