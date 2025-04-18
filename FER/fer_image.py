from fer import FER 
import cv2

image_path = "../test_image2.jpg" # Insert Your Image path
img = cv2.imread(image_path)

detector = FER()

# detector.top_emotion(img) - returns a tuple containing top detected emotion and the confidence score of the top emotion
# detector.detect_emotions(img) - returns a list of dictionary containing box array and "emotions" which contain deictionary of 7 emotions with their confidence score
result = detector.detect_emotions(img)

print(result)

# You can use json.dumps(result, indent = 4) to display result in a pretty format. Requires "import json" statement to use the function