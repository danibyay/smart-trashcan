# Requires Adafruit_Python_PN532
# Authors: Daniela Becerra, Adair Ibarra
# Date: April 2018
import binascii
import sys
import struct

import Adafruit_PN532 as PN532
# spi configuration for raspberry pi model 3
CS   = 8 # GPIO 24, BCM 8
MOSI = 10 # GPIO 19, BCM 10
MISO = 9 # GPIO 21, BCM 9
SCLK = 11 # GPIO 23, BCM 11

# This works with the white card
CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
HEADER = b'BG'

# Determine value to write
dec_value = 3 # invalid object
my_file = open("BrandIndex.txt", "r")
# coca, heineken, tecate, nada = 0 , 1, 2, 3
hex_string = my_file.read(1)
my_file.close()


# Create and initialize an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()
print('Place the card to be written on the PN532...')
# read uid
uid = pn532.read_passive_target()
while uid is None:
    uid = pn532.read_passive_target()
print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
# Authenticate block 4
if not pn532.mifare_classic_authenticate_block(uid, 4, PN532.MIFARE_CMD_AUTH_B,
                                               CARD_KEY):
    print('Error! Failed to authenticate block 4 with the card.')
    sys.exit(-1)
# build data frame
data = bytearray(16)
data = bytearray(b'\x00\x00\x03\x0b\xd1\x01\x07\x54\x02\x65\x73\x30\x30\x30\x33\xfe')
# hardcoded the way it worked when writing plain text from NXP tag write app
data[14] = hex_string

#data[0:2] = HEADER
#hex_string = format(dec_value, 'x')
#while (6 > len(hex_string)): # padding of zeros to have always 6 chars
#    hex_string = '0' + hex_string
#data[2:8] = hex_string
# write to the card
# Finally write the card.
if not pn532.mifare_classic_write_block(4, data):
    print('Error! Failed to write to the card.')
    sys.exit(-1)
print('Wrote card successfully! You may now remove the card from the PN532.')
print('wrote value {}'.format(hex_string))

"""
16 bytes of -plain text- containing hola in ascii
0-0-3-b-d1-1-7-54-2-65-73-68-6f-6c-61-fe
x-x-x-x-xx-x-x-xx-x-xx-xx-h -o -l -a -xx
"""
data = bytearray(b'\x00\x00\x03\x0b\xd1\x01\x07\x54\x02\x65\x73\x30\x30\x30\x33\xfe')
