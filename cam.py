import pyvirtualcam as pvc
import cv2 as cv
import numpy as np


WIDTH = 1280
HEIGHT = 720


if __name__ == '__main__':

    cap = cv.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)

    fmt = pvc.PixelFormat.BGR

    with pvc.Camera(width=WIDTH, height=HEIGHT, fps=24, fmt=fmt) as cam:
        while True:
            _, frame = cap.read()

            thresh, output_frame = cv.threshold(frame, 127, 255, cv.THRESH_BINARY)

            # virtual cam output
            cam.send(output_frame)
            cam.sleep_until_next_frame()

            # DEBUG: real cam output
            frame = cv.flip(frame, 1)
            cv.imshow('out', frame)

            if cv.waitKey(1) == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()
