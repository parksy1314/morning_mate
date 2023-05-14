# morning_mate

environment : 라즈베리파이4 (라즈베리안,bullseye)
파이썬 버전이나 패키지 정보는 env.yaml에 있음(miniforge 사용)

### google drive
기본적으로 google drive를 마운트해서 사용함

사용법 :
- rclone 설치
- google 계정 연동
- mkdir -p /mnt/gdrive
- gdrive_mount 폴더에 있는 서비스 등록
- systemctl enable rclone-gdrive.service
- systemctl start rclone-gdrive.service

### pi_camera.py
라즈베리파이에 내장된 libcamera-stil 명령어 사용
마운트된 /mnt/gdrive 폴더에 mirror_photo.jpg 이름으로 저장됨

### recog music

pi_camera.py 실행해서 사진을 찍고 그 사진을 input으로 emotion_detection.py 실행하면 어떤 감정인지 나옴
그걸로 youtube_api.py 에 넘겨주면 맵핑되는 제목으로 웹에서 유튜브 실행

### vMakeup
makeup_gan으로 이름 바꿀까하는데 암튼 
똑같이 pi_camera 실행해서 사진 찍고 /mnt/gdrive/makeup 폴더에 있는 사진으로 메이크업해줌
일단 특정 파일로 하드코딩 되어 있는데 makeup사진 파일 이름을 인자로 넘겨주면 그 파일로 메이크업해주게 바꾸려고함
