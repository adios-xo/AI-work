import cv2
from deepface import DeepFace

# Open the webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze the frame for emotion
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False,
            silent=False
        )

        # Extract the dominant emotion
        dominant_emotion = result[0]['dominant_emotion']

        # Display the emotion on the frame
        cv2.putText(frame, dominant_emotion, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        print("Detected Emotion:", dominant_emotion)

    except Exception as e:
        print("Error:", e)

    # Show the frame
    cv2.imshow("Real-Time Emotion Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()