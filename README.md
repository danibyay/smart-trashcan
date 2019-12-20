# smart-trashcan

As a user, by introducing empty aluminum cans to the smart trash can, you will get digital points to redeem in online stores.
Get your points from the trashcan to your NFC card. Then, read the NFC card with your smartphone and get the points into your account.

This project includes the software that would run on the trash can. 
The android app is not included in this repo.

With computer vision, the trash can will identify the brand of the can.
This information will be valuable to stakeholders to know the consumer's patterns.

This **prototype** uses a simple color filter to _identify_ the brand. This is the central part of the idea, and it needs to be further improved.


## Demo video
Watch the [Video](https://www.youtube.com/watch?v=TDKvSwTfk3g&t=1s)

## Dependencies:
* Adafruit_PN532 [library](https://github.com/adafruit/Adafruit-PN532)
* OpenCV3
* Android companion App, developed with app inventor.

## Physical devices:
* NXP NFC chip [PN532 breakout board](https://www.amazon.com.mx/gp/product/B00NQRVQIO/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1), using SPI interface
* Raspberry pi 3
* Raspberry pi camera module v2
* MiFare NFC tag
* Android Smartphone with companion app

## Usage
Enter the virtual env of opencv

`bash`

`source ~/.profile` 

`workon cv`

Filter the image and detect the brand

`python ProcessImage.py -i photos/<image.png>`

A number associated with the brand will be written to BrandIndex.txt

`exit`

Exit the virtual env of opencv

Place the user's NFC card over the module.

`python pite_nfc_write.py`

Now, your card will have a value written. 

Read your card with your phone app and the points will be transfered to your account.


