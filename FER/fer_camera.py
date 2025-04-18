import cv2
from fer import FER

# Initialize webcam
cap = cv2.VideoCapture(0) # 0 - uses default webcam. Use 1, 2, ... for other available camera

# Initialize the emotion detector
detector = FER()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions in the current frame
    result = detector.detect_emotions(frame)

    # Loop through all detected faces
    for face in result:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)

        # Draw bounding box and emotion label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        label = f"{dominant_emotion}: {emotions[dominant_emotion]:.2f}"
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Emotion Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()