from unittest import result
import paho.mqtt.client as mqtt
import time
import sys
import cv2
import numpy as np

width = 1920
height = 1080


def SendingImage():
    cap = cv2.VideoCapture(0)    # 设置成摄像头的ID
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    print("Camera initialized successfully...")
    sum = 0
    count = 0

    # set the lower and upper bounds for the green hue
    lower_green = np.array([10, 43, 46])
    upper_green = np.array([11, 255, 255])

    while True:
        ret, frame = cap.read()
        start = cv2.getTickCount()
        result = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25,
                            interpolation=cv2.INTER_NEAREST)

        hsvImage = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvImage, lower_green, upper_green)

        end = cv2.getTickCount()
        during = (end - start) / cv2.getTickFrequency()
        cv2.imshow("Color Filter", mask)
        sum += during
        count += 1
        print(sum/count)
        cv2.imshow("Test Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imwrite(f"{count}.png", result)
            print("Save Successfully...")


if __name__ == '__main__':
    # client = mqtt.Client(clientID)
    # ClientConnect()
    SendingImage()
