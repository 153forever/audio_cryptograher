#!/usr/bin/env python3
from Audio import Audio
from Steganographer import Steganographer
from BBS import BBS
import numpy as np
import rsa
from Crypto.Random import get_random_bytes

public, private = rsa.newkeys(512)
alg = BBS()
audio = Audio(filename=r'source.wav')
crypter = Steganographer(audio=audio, algorithm=alg)
crypter.encrypt("Hello world!"*100, filename=r'source_new.wav', publicKey=public)
audio2 = Audio(filename=r'source_new.wav')
session_key = rsa.decrypt(bytes(audio2.getkey(512)), private)
session_key = session_key.decode('utf-8')
crypter2 = Steganographer(audio=audio2, key=session_key)
print(crypter2.decode())
