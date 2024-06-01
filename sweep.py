import cv2
import mediapipe as mp
import pyautogui

# Function to switch the window based on hand position
def switch_window(hand_landmarks):
    if hand_landmarks is not None:
        # Extract x-coordinate of the tip of the index finger
        index_tip_x = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x
        screen_width, _ = pyautogui.size()
        # If tip of index finger is on the left side
        if index_tip_x < 0.5:
            pyautogui.hotkey('alt', 'tab')  # Switch to the next window
        # If tip of index finger is on the right side
        else:
            pyautogui.hotkey('alt', 'shift', 'tab')  # Switch to the previous window

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Hands
    results = hands.process(image)

    # Convert the RGB image back to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Switch window based on hand position
            switch_window(hand_landmarks)

    # Display the resulting image
    cv2.imshow('Hand Tracking', image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy any OpenCV windows
cap.release()
cv2.destroyAllWindows()
