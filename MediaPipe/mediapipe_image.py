import cv2
import mediapipe as mp

# Load your image
image_path = 'your_image.jpg'  # Insert your image path
image = cv2.imread(image_path)

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces
    results = face_detection.process(image_rgb)

    # Draw detections
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

    # Show the result
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()