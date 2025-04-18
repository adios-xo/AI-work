import cv2
from deepface import DeepFace

# Load your video
video_path = "your_video.mp4"  # change this to your video file
cap = cv2.VideoCapture(video_path)

# Frame counter
frame_num = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Analyze every Nth frame to reduce processing time
    if frame_num % 10 == 0:  # adjust this value as needed
        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False,
                silent=True  # suppress verbose output
            )

            # Extract and print dominant emotion
            dominant_emotion = result[0]['dominant_emotion']
            print(f"Frame {frame_num}: {dominant_emotion}")

            # Draw the emotion on the frame (optional)
            cv2.putText(frame, dominant_emotion, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error on frame {frame_num}: {e}")

    # Show the frame (optional)
    cv2.imshow("Emotion Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_num += 1

# Release resources
cap.release()
cv2.destroyAllWindows()