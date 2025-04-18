import cv2
import mediapipe as mp

# Initialize MediaPipe face detection and drawing modules
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Access the webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

# Load the face detection model
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # If webcam frame not captured correctly

        # Convert BGR to RGB (MediaPipe uses RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        results = face_detection.process(frame_rgb)

        # Draw face detections
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)

        # Show the output frame
        cv2.imshow("Webcam Face Detection", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release webcam and close window
cap.release()
cv2.destroyAllWindows()