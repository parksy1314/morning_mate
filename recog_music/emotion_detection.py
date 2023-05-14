import cv2
import numpy as np
#from tensorflow.keras.preprocessing.utils import img_to_array
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

def detect_emotion(img):
    # Face detection XML load and trained model loading
    face_detection = cv2.CascadeClassifier('model_files/haarcascade_frontalface_default.xml')
    emotion_classifier = load_model('model_files/emotion_model.hdf5', compile=False)
    EMOTIONS = ["Angry", "Disgusting", "Fearful", "Happy", "Sad", "Surpring", "Neutral"]

    image = cv2.imread(img)
    # Convert color to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Face detection
    faces = face_detection.detectMultiScale(gray,
                                            scaleFactor=1.1,
                                            minNeighbors=5,
                                            minSize=(30, 30))

    # Create empty image
    canvas = np.zeros((250, 300, 3), dtype="uint8")

    # Perform emotion recognition only when face is detected
    if len(faces) > 0:
        # For the largest image
        face = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = face
        # Resize the image to 64x64 for neural network
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        # Emotion predict
        preds = emotion_classifier.predict(roi)[0]
        label = EMOTIONS[preds.argmax()]

    return label
