# FER

FER stands for Facial Emotion Recognition. This folder contains code and resources for detecting and classifying human emotions from facial images or video streams.  It may include scripts, models, or utilities for tasks such as:

* Extracting facial features from images.
* Classifying emotions into categories like anger, disgust, fear, happiness, sadness, surprise, and neutrality.
* Applying pre-trained models or training new models for emotion recognition.

## Installation

**Note:** FER and its dependencies are already installed and readily available within the pre-configured virtual environment (`env`) provided in the main repository.

If you still wish to install FER in a separate environment, you can use the following command:

```bash
pip install fer
```

## fer_image.py

### Purpose

This script uses the fer library and OpenCV to detect emotions in a single image. It loads an image, analyzes it for facial expressions, and outputs the detected emotions with their confidence scores.

### How to Use

1. Ensure you have Python, the fer library, and OpenCV (`cv2`) installed.
2. Place the image you want to analyze in your desired directory.
3. Modify the `img_path` variable in the script to point to your image file.
4. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python fer_image.py
```

## fer_video.py

### Purpose

This script uses the fer library and OpenCV to detect emotions in a video file. It loads a video, analyzes it frame by frame for facial expressions, and can optionally display the video with emotion detection results. It then converts the results to a pandas DataFrame.

### How to Use

1 Ensure you have Python, the fer library, and its dependencies (including OpenCV) installed.
2. Place the image you want to analyze in your desired directory.
3. Modify the `video_filename` variable in the script to point to your image file.
4. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python fer_image.py
```

## fer_camera.py

### Purpose

This script uses the fer library and OpenCV to detect emotions in real-time from your computer's webcam. It captures video frames, analyzes them for facial expressions, and displays the video feed with bounding boxes and emotion labels.

### How to Use

1. Ensure you have Python, the fer library, and OpenCV (`cv2`) installed.
2. Connect your webcam to your computer.
3. Run the script. To run the script, open a terminal or command prompt, navigate to the directory where you saved the script, and run it using the command:

```bash
python fer_camera.py
```

### Notes

* The script initializes the webcam using `cv2.VideoCapture(0)`.  The '0' refers to the default camera.  If you have multiple cameras, you might need to change this to '1', '2', etc.
* Pressing 'q' will close the window and stop the script.
