#!/usr/bin/env python3
import argparse
from Audio import Audio
import rsa
from Steganographer import Steganographer


parser = argparse.ArgumentParser(description='Encryptor parser')
parser.add_argument('-i', type=str, default=r'mozart_after.wav')
parser.add_argument('-enc', type=str, default="utf-8")

with open("private_key.txt", "r") as pr:
    private_str = pr.read().split(" ")
    private = rsa.PrivateKey(int(private_str[0]), int(private_str[1]), int(private_str[2]), int(private_str[3]), int(private_str[4]))

args = parser.parse_args()
audio = Audio(filename=args.i)
decoder = Steganographer(audio=audio)
res = decoder.decode(private)
print(res.replace("*", "\n"))
