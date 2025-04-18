from deepface import DeepFace

# Path to your image
img_path = "../test_image2.jpg"  # Insert your image path

# Analyze the image
result = DeepFace.analyze(img_path=img_path) # actions=["emotion", "age", "gender", "race"]

# Print full result
print(result)