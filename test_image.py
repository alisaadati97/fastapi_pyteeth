import cv2
from urllib.request import urlopen
import numpy as np
image_url = "https://raw.githubusercontent.com/alisaadati97/Pyteeth/master/examples/test_images/IMG_6031.JPG"

req = urlopen(image_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'

cv2.imshow('image', img)
if cv2.waitKey() & 0xff == 27: quit()