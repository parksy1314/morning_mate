import cv2
import numpy as np
from keras.models import load_model

# 얼굴 인식기 초기화
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 감정 분석 모델 불러오기
emotion_model = load_model('emotion_model.hdf5')

# 감정 분석 함수 정의
def detect_emotion(image_path):
    # 이미지 파일 불러오기
    image = cv2.imread(image_path)

    # 이미지를 그레이 스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 인식
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 감정 분석을 위한 이미지 전처리
    for (x, y, w, h) in faces:
        # 얼굴 부분만 자르기
        roi_gray = gray[y:y+h, x:x+w]
        #roi_gray = cv2.resize(roi_gray, (64, 64), interpolation=cv2.INTER_AREA)
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        # 이미지를 4차원 텐서로 변환
        image = np.expand_dims(np.expand_dims(roi_gray, axis=-1), axis=0)

        # 감정 분석
        emotion_pred = emotion_model.predict(image)
        emotion_label = np.argmax(emotion_pred)

        # 감정 라벨에 따른 분류
        if emotion_label == 0:
            emotion = 'Angry'
        elif emotion_label == 1:
            emotion = 'Disgust'
        elif emotion_label == 2:
            emotion = 'Fear'
        elif emotion_label == 3:
            emotion = 'Happy'
        elif emotion_label == 4:
            emotion = 'Sad'
        elif emotion_label == 5:
            emotion = 'Surprise'
        else:
            emotion = 'Neutral'

    return emotion

detect_emotion("IMG_1448.JPG")