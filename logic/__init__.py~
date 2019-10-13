import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

class QR:
    def Scan(string = None):
        if string != None:
            cap = cv2.VideoCapture(0)
            Z = True
            while Z:
                _, frame = cap.read()

                decodedObjects = pyzbar.decode(frame)
                for obj in decodedObjects:

                    a = obj.data
                    print(obj.data)
                    if a != '':
                        Z = False
                cv2.imshow("QRCode reader", frame)

                key = cv2.waitKey(1)
                if key == 27:
                    break

        if string == None:
            cap = cv2.VideoCapture(0)
            Z = True
            while Z:
                _, frame = cap.read()

                decodedObjects = pyzbar.decode(frame)
                for obj in decodedObjects:

                    a = obj.data
                    if a != '':
                        Z = False
                        
        return a