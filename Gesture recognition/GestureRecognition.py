import cv2

webcam = cv2.VideoCapture(0)

while True:
    boolean, image = webcam.read()
    cv2.imshow("the TITLE", image)
    key = cv2.waitKey(10)

    if key == 27:       # ascii of 'Esc' key
        break
webcam.release()
cv2.destroyAllWindows()