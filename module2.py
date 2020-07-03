#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:     photo debuging
#
# Author:      Даниил Чугай
#
# Created:     20.06.2020
# Copyright:   (c) Даниил Чугай 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import cv2
import os

#Фото!
def face_detection():   #Проверка на лица
    import cv2
    imagePath = "image.jpg"
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    os.remove("image.jpg")
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)

    )
    return(len(faces))

