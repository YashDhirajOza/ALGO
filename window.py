import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Function to detect hand sweep gesture
def detect_hand_sweep(landmarks, img_width):
    x_coords = [landmark.x * img_width for landmark in landmarks.landmark]
    x_min = min(x_coords)
    x_max = max(x_coords)
    sweep_threshold = 0.8 * img_width  # Define sweep threshold as 80% of image width
    if x_max - x_min > sweep_threshold:
        return True
    return False

previous_sweep = None

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and find hands
    results = hands.process(image)

    # Convert back to BGR for OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get image dimensions
            h, w, _ = image.shape
            
            # Detect hand sweep gesture
            if detect_hand_sweep(hand_landmarks, w):
                current_sweep = 'right' if hand_landmarks.landmark[0].x > 0.5 else 'left'
                if current_sweep != previous_sweep:
                    if current_sweep == 'right':
                        # Simulate Alt+Tab for switching windows to the right
                        pyautogui.hotkey('alt', 'tab')
                    previous_sweep = current_sweep
            
            # Display the current sweep gesture on the image
            cv2.putText(image, f'Sweep: {previous_sweep}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Display the image
    cv2.imshow('Hand Sweep Gesture Control', image)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
