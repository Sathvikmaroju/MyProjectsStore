import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 630)
cap.set(4, 450)


while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode("utf-8")
        # print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 3)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_COMPLEX, 0.54, (0, 0, 255), 2)

    cv2.imshow("Result", img)
    cv2.waitKey(1)