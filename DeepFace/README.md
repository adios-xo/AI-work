# DeepFace

DeepFace is a powerful and user-friendly Python framework for facial recognition and facial attribute analysis. Built on top of popular deep learning models like VGG-Face, Google FaceNet, OpenFace, and others, it provides a high-level interface for performing tasks such as:

* **Face Recognition:** Identifying individuals in images or videos by comparing their facial features against a database of known faces.
* **Facial Attribute Analysis:** Estimating attributes like age, gender, emotion (e.g., happy, sad, angry, surprised), and race/ethnicity from facial images.

This framework simplifies the process of applying complex deep learning models to real-world applications, making facial analysis accessible to a wider range of developers and researchers.

## Installation

**Note:** DeepFace and its dependencies are already installed and readily available within the pre-configured virtual environment (`env`) provided in the main repository.

If you still wish to install DeepFace in a separate environment, you can use the following command:

```bash
pip install deepface
```

## deepface_image.py

### Purpose

This script uses the DeepFace library to analyze a single image. It takes the path to an image file as input and performs facial attribute analysis, such as detecting emotion, age, gender, and race. The analysis results are then printed to the console.

### How to Use

1. Ensure you have Python and the DeepFace library installed.
2. Place the image you want to analyze in your desired directory.
3. Modify the `img_path` variable in the script to point to your image file.
4. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python deepface_image.py
```

## deepface_video.py

### Purpose

This script uses the DeepFace library and OpenCV to detect emotions in a video file.  It processes the video frame by frame, analyzes the facial emotion in each frame (or a subset of frames), and can optionally display the video with the detected emotion overlaid.

### How to Use

1. Ensure you have Python, the DeepFace library, and OpenCV (`cv2`) installed.
2. Place the video you want to analyze in your desired directory.
3. Modify the `video_path` variable in the script to point to your video file.
4. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python deepface_video.py
```

### Notes

* The script analyzes every 10th frame by default. You can adjust this by changing the value in the line `if frame_num % 10 == 0:`.  A lower value will increase processing time but may improve accuracy.
* Press 'q' to quit the video playback and stop the analysis.

## deepface_camera.py

### Purpose

This script uses the DeepFace library and OpenCV to detect emotions in real-time from your computer's webcam. It captures video frames from the webcam, analyzes the facial emotion in each frame, and displays the video with the detected emotion overlaid.

### How to Use

1. Ensure you have Python, the DeepFace library, and OpenCV (`cv2`) installed.
2. Connect your webcam to your computer.
3. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python deepface_camera.py
```

### Notes

* The script uses the default webcam (camera index 0). If you have multiple cameras, you may need to change the camera index in the `cv2.VideoCapture(0)` line.
* Press 'q' to quit the application and stop the emotion detection.
