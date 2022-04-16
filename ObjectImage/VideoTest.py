import time
import sys
import cv2
import numpy as np
from numba import jit

width = 1920
height = 1080


@jit
def FilterColor(img, colors):
    info = img.shape
    height = info[0]
    width = info[1]
    mask = np.zeros((height, width, 1), np.uint8)
    for h in range(0, height):
        for j in range(0, width):
            probeColor = img[h, j]
            for color in colors:
                if(probeColor[0] == color[2] and probeColor[1] == color[1] and probeColor[2] == color[0]):
                    mask[h, j] = 255
                    break
    return mask


def SendingImage():
    cap = cv2.VideoCapture(0)    # 设置成摄像头的ID
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    print("Camera initialized successfully...")
    sum = 0
    count = 0

    SuperMarioBro_RED = (14, 57, 247)  # Red
    SuperMarioBro_GREEN = (45, 145, 27)  # Green
    SuperMarioBro_BLUE = (255, 80, 81)  # Blue
    SuperMarioBro_PINK = (198, 80, 255)  # Pink

    SuperMarioBro3_Body = (178, 217, 255)
    SuperMarioBro3_Rect = (31, 31, 31)

    # Red,(231, 61, 18),(209, 66, 34), (157, 81, 41), (132, 85, 74)(247, 57, 14),
    SuperMarioBro3_RED = ((231, 61, 18))
    #   (209, 66, 34), (157, 81, 41), (132, 85, 74))
    SuperMarioBro3_RED_InWater = (15, 38, 109)  # Red
    SuperMarioBro3_GREEN = (45, 145, 27)  # Green
    SuperMarioBro3_BLUE = (255, 80, 81)  # Blue
    SuperMarioBro3_PINK = (198, 80, 255)  # Pink

    while True:
        ret, frame = cap.read()
        start = cv2.getTickCount()
        result = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25,
                            interpolation=cv2.INTER_NEAREST)
        mask = FilterColor(result, SuperMarioBro3_RED)
        end = cv2.getTickCount()
        during = (end - start) / cv2.getTickFrequency()
        cv2.imshow("Color Filter", mask)
        sum += during
        count += 1
        print(sum/count)
        cv2.imshow("Test Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imwrite(f"{count}.png", frame)
            print("Save Successfully...")


if __name__ == '__main__':
    # client = mqtt.Client(clientID)
    # ClientConnect()
    SendingImage()
