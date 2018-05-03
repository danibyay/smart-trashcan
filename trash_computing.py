import os
import sys
import argparse

# Authors: Daniela Becerra, Adair Ibarra
# Date: May 2018
# dependencies: openCV and AdafruitPN532 libraries


#argparse
img_str="photos/vaso.jpg"
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=False, help='image to process')
args = vars(ap.parse_args())
if args["image"] is not None:
    img_str = args["image"]


script1 = "ProcessImage.py"
os.system("python {} -i {}".format(script1, img_str))

script2 = "pite_nfc_write.py"
os.system("python {}".format(script2))
