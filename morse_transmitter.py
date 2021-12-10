import serial
import time
import sys

ser = serial.Serial("/dev/cu.usbmodem14101", 9600)

Morse = {
    "A": "・－",
    "B": "－・・・",
    "C": "－・－・",
    "D": "－・・",
    "E": "・",
    "F": "・・－・",
    "G": "－－・",
    "H": "・・・・",
    "I": "・・",
    "J": "・－－－",
    "K": "－・－",
    "L": "・－・・",
    "M": "－－",
    "N": "－・",
    "O": "－－－",
    "P": "・－－・",
    "Q": "－－・－",
    "R": "・－・",
    "S": "・・・",
    "T": "－",
    "U": "・・－",
    "V": "・・・－",
    "W": "・－－",
    "X": "－・・－",
    "Y": "－・－－",
    "Z": "－－・・",
    "1": "・－－－－",
    "2": "・・－－－",
    "3": "・・・－－",
    "4": "・・・・－",
    "5": "・・・・・",
    "6": "－・・・・",
    "7": "－－・・・",
    "8": "－－－・・",
    "9": "－－－－・",
    "0": "－－－－－",
    ".": "・－・－・－",
    ",": "－－・・－－",
    ":": "－－－・・・",
    ";": "－・－・－・",
    "?": "・・－－・・",
    "_": "・・－－・－",
    "+": "・－・－・",
    "－": "－・・・・－",
    "'": "・－－－－・",
    "!": "－・－・－－",
    "/": "－・・－・",
    "(": "－・－－・",
    " ": "　"
}


def light(signal):
    for i in list(signal):
        if i == "・":
            print("・", end="")
            ser.write("1".encode())
            time.sleep(0.2)
            ser.write("0".encode())
        elif i == "－":
            print("－", end="")
            ser.write("1".encode())
            time.sleep(0.5)
            ser.write("0".encode())
        elif i == " ":
            print("　", end="")
            ser.write("0".encode())
            time.sleep(0.2)
        time.sleep(0.2)
    print()

def text2morse(text):
    return [Morse[i] for i in list(text)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, mode='r') as f:
            lines = f.readlines()
            for text in lines:
                [light(i) for i in list(text2morse(text.replace('\r', '').replace('\n', ' ').replace('-', '').upper()))]
    else:
        text = input("TEXT: ").upper()
        [light(i) for i in list(text2morse(text))]
