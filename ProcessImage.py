# Authors: Daniela Becerra, Adair Ibarra
# Date: May 2018

import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='image to process')
args = vars(ap.parse_args())
img_str = args["image"]

img = cv2.imread(img_str, 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

brands = ['Coca', 'Heineken', 'Tecate']
colors = [[169,189],[55,75],[101,121]]
match = [0, 0, 0] # pixels that match filter
Threshold = [1.5, 1.5, 1.5] 
per = [0,0,0] # percentaje of match
masks = []

for i in range(3):
    lower_range = np.array([colors[i][0], 100, 100], dtype=np.uint8)
    upper_range = np.array([colors[i][1], 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    masks.append(mask)
    #MEASURE PIXELS
    totPix = mask.size # total pixels
    #print(totPix)
    n_white_pix = np.sum(mask == 255)
    match[i] = n_white_pix
    per[i] = (match[i]*100)/totPix
    #print('Number of {} pixels: {} Percentage: {}'.format(brands[i], match[i], per[i]))
    #cv2.imshow('mask', mask)

#Return index of grartes value in match
#Identify the brand of the bottle

Max = match[0]
MaxI = 0
for i in range(len(match)):
    if Max < match[i]:
        MaxI = i
        Max = match[i]
print(MaxI)

#Define Threshold
#Create a file with the info
my_string = ""
if per[MaxI] > Threshold[MaxI]:
    file = open("BrandIndex.txt", "w")
    file.write(str(MaxI))
    file.close()
    my_string = brands[MaxI]
else:
    file = open("BrandIndex.txt", "w")
    file.write('3')
    file.close()
    my_string = "None"


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(mask, my_string, (10,500), font, 300, (255,255,255),10)
cv2.imwrite('outputs/mask.jpg', masks[MaxI])

"""

while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break
 
cv2.destroyAllWindows()
"""
