import cv2 #import pip install opencv-python for this project
"""this piece of code will open the camera from your desktop"""
'''video_cap=cv2.VideoCapture(0)
while True:
    ret,video=video_cap.read()
    cv2.imshow("video_live",video)
    if cv2.waitKey(10)==ord("a"):
            break
video_cap.realease()'''
"""this piece of code will detect the face in the camera"""
face_cap=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")#this line helps the program to detect the face muscel 
video_cap=cv2.VideoCapture(0)
while True:
    ret,video=video_cap.read()
    col=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)#this line convert the image in camera into balck and white beacuse muscel are more visible in black and white color
    faces=face_cap.detectMultiScale(      
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h)in faces:
          cv2.rectangle(video,(x,y),(x+w,y+h),(0,255,0),2)#it provide the grid to the image which gives us the position of the face
    cv2.imshow("video_live",video)
    if cv2.waitKey(10)==ord("a"):# "a" button the keybord is use to stop the program
            break
video_cap.realease() #closing function

