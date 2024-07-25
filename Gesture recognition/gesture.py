import cv2
import mediapipe as mp

# Initialize webcam and mediapipe solutions
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    boolean, image = webcam.read()
    if not boolean:
        continue
##1 ------- Detecting Hand(s)-----------------------

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, f_depth = image.shape

    # Detect hand(s)
    detect = my_hands.process(image_rgb)
    hands = detect.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw only landmarks (without connections)
            drawing_utils.draw_landmarks(image, hand)

##2 ------- Detecting Fingers/Landmarks-------------
            
            landmarks = hand.landmark
            for idx, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if idx == 8:
                    cv2.circle(img=image, center=(x,y), radius=8, color=(200,100,100), thickness=5)
                    x1, y1 = x, y
                if idx == 4:
                    cv2.circle(img=image, center=(x,y), radius=8, color=(200,100,100), thickness=5)
                    x2, y2 = x, y

##3 --------- Distance in-between ---------------------
            cv2.line(image, (x1,y1), (x2,y2), (0,255,0), 3)
            distance = ( (x1-x2)**2 + (y1-y2)**2)**(0.5) //2
            print(distance)

    cv2.imshow("Hand Tracking", image)
    key = cv2.waitKey(10)

    if key == 27:  # Esc key to exit
        break

webcam.release()
cv2.destroyAllWindows()
