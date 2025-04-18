# MediaPipe

MediaPipe is a framework for building multimodal applied machine learning pipelines.  This folder contains code and resources for developing applications that process and analyze multimedia data, such as video, audio, and time series data.  It may include scripts, models, or utilities for tasks such as:

* Face detection and landmark tracking.
* Pose estimation.
* Hand tracking.
* Object detection and tracking.
* And other computer vision and machine learning tasks.

## Installation

**Note:** MediaPipe and its dependencies may already be installed and readily available within the pre-configured virtual environment (`env`) provided in the main repository.

If you still wish to install DeepFace in a separate environment, you can use the following command:

```bash
pip install mediapipe
```

## mediapipe_image.py

### Purpose

This script uses the MediaPipe library and OpenCV to detect faces in a single image. It loads an image, processes it with MediaPipe's face detection model, and displays the image with bounding boxes drawn around the detected faces.

### How to Use

1. Ensure you have Python, MediaPipe, and OpenCV (`cv2`) installed.
2. Place the image you want to analyze in your desired directory.
3. Modify the `image_path` variable in the script to point to your image file.
4. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python mediapipe_image.py
```

## mediapipe_video.py

### Purpose

This script uses the MediaPipe library and OpenCV to detect faces in a video file. It loads a video, processes it frame by frame with MediaPipe's face detection model, and displays the video with bounding boxes drawn around the detected faces.

### How to Use

1. Ensure you have Python, MediaPipe, and OpenCV (`cv2`) installed.
2. Place the image you want to analyze in your desired directory.
3. Modify the `video_path` variable in the script to point to your image file.
4. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python mediapipe_video.py
```

### Notes

* The script loads a video using OpenCV's `cv2.VideoCapture()`.

* Pressing 'q' will stop the video playback and the script.

## mediapipe_camera.py

### Purpose

This script uses the MediaPipe library and OpenCV to detect faces in real-time from your computer's webcam. It captures video frames from the webcam, detects faces using MediaPipe's face detection model, and displays the video with bounding boxes around the detected faces.

### How to Use

1. Ensure you have Python, MediaPipe, and OpenCV (`cv2`) installed.
2. Connect your webcam to your computer.
3. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python mediapipe_camera.py
```

### Notes

* The script accesses the default webcam (camera index 0) using OpenCV's `cv2.VideoCapture(0)`. If you have multiple cameras, you may need to change the index (e.g., to 1, 2, etc.).
* Pressing 'q' will close the window and stop the script.
