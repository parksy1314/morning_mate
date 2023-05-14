import emotion_detection
import youtube_api
import webbrowser
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
import pi_camera

if __name__ == '__main__':
    mapping_url = {"Angry":"화날 때 듣는 노래",
                   "Disgusting":"불안할때 듣는 노래",
                   "Fearful":"악몽 꿨을때 노래",
                   "Happy":"행복할 때 듣는 노래",
                   "Sad":"슬플 때 듣는 노래",
                   "Surpring":"마음이 안정되는 노래",
                   "Neutral":"심심할 때 듣는 노래"}

    emotion = emotion_detection.detect_emotion("/mnt/gdrive/mirror_photo.jpg")
    print("지금 감정은? :", emotion) 
    print(mapping_url[emotion])
    get_url = youtube_api.get_top_video_link("AIzaSyCCNIK0pJsKEKAoqnUWYAZuW7v_8vr23ZE",mapping_url[emotion])
    print(get_url)
    webbrowser.open(get_url)




