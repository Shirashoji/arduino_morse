import serial
import time

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
            time.sleep(0.5)
            ser.write("0".encode())
        elif i == "－":
            print("－", end="")
            ser.write("1".encode())
            time.sleep(0.2)
            ser.write("0".encode())
        elif i == " ":
            print("　", end="")
            ser.write("0".encode())
            time.sleep(0.2)
        time.sleep(0.2)
    print()

def text2morse(text):
    return [Morse[i] for i in list(text)]


text = input("TEXT: ").upper()
[light(i) for i in list(text2morse(text))]