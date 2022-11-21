import serial
import time
from collections import Counter

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# i = 0
# moves = list()
# while i<30:
#     move = "grab"
#     moves.append(move)
#     i += 1
# while i<32:
#     move = "release"
#     moves.append(move)
#     i += 1
    
# occurence_count = Counter(moves)
# x = occurence_count.most_common(1)[0][0]

# time.sleep(2)
# value = write_read(x)
# print(value)

while True:
    x = input("Enter move: ")
    time.sleep(2)
    value = write_read(x)
    print(value)
