# import the necessary package
from __future__ import print_function
from imutil import WebCamVideoStream
from imutil import FPS
import cv2
print("aaa")

if __name__ == "__main__":
    # grab a pointer to the video stream and initialize the FPS counter
    print("[INFO] sampling frames from webcam")
    stream = cv2.VideoCapture(0)
    fps = FPS().start()

    # loop over some frames
    while(True):
        # grab the frame from the stream and resize it to have a maximum
        # width of 400 pixels
        (grabbed, frame) = stream.read()
        frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25,
                           interpolation=cv2.INTER_NEAREST)
        # check to see if the frame should be displayed on screen

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xff

        # update the fps counter
        fps.update()

        print("[INFO] elapsed time : {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # stop the timer and display the information

    # do a bit of cleanup
    stream.release()
    cv2.destroyAllWindows()
