import cv2
import numpy as np

def draw_circles(storage, output):
    circles = np.asarray(storage)
    for circle in circles:
        Radius, x, y = int(circle[0][2]), int(circle[0][0]), int(circle[0][1])
        cv2.Circle(output, (x, y), 1, cv2.CV_RGB(0, 255, 0), -1, 8, 0)
        cv2.Circle(output, (x, y), Radius, cv2.CV_RGB(255, 0, 0), 3, 8, 0)

orig = cv2.LoadImage('images/R/S1001R02.jpg')
processed = cv2.LoadImage('images/R/S1001R02.jpg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
storage = cv2.CreateMat(orig.width, 1, cv2.CV_32FC3)
#use canny, as HoughCircles seems to prefer ring like circles to filled ones.
cv2.Canny(processed, processed, 5, 70, 3)
#smooth to reduce noise a bit more
cv2.Smooth(processed, processed, cv2.CV_GAUSSIAN, 7, 7)

cv2.HoughCircles(processed, storage, cv2.CV_HOUGH_GRADIENT, 2, 100.0, 30, 150, 60, 300)
draw_circles(storage, orig)

cv2.NamedWindow("original with circles")
cv2.ShowImage("original with circles", orig)
cv2.WaitKey(0)
