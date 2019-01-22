#coding:utf-8

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
import numpy as np
import cv2

cv2.namedWindow('Video')

video_capture = cv2.VideoCapture(0)

video_writer = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc('M','J','P','G'),
							   video_capture.get(cv2.CAP_PROP_FPS),
							   (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
								int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))))

face_cascade = cv2.CascadeClassifier('E:/baiduyunApi/AI/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('E:/baiduyunApi/AI/Lib/site-packages/cv2/data/haarcascade_eye.xml')

while video_capture.isOpened():
	succes, frame = video_capture.read()
	if succes:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	
		faces = face_cascade.detectMultiScale(gray, 1.1, 3)	
		for (x,y,w,h) in faces:
			img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			#eyes = eye_cascade.detectMultiScale(roi_gray)
			#for (ex,ey,ew,eh) in eyes:
				#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)			
			
		#高斯模糊
		#blur_frame = cv2.GaussianBlur(frame,(3,3),0)
		#video_writer.write(blur_frame)
		#水平翻转			
		flip_frame = cv2.flip(frame,2)
		#添加文字
		font = cv2.FONT_HERSHEY_SIMPLEX	
		cv2.putText(flip_frame,'FaceDetected',(10,25),font,1,(255,255,255),2,cv2.LINE_AA)
		video_writer.write(flip_frame)
		cv2.imshow('Video',flip_frame)
		if cv2.waitKey(1) == 27:
			break
	else:
		break

cv2.destroyWindow('Video')
video_capture.release()
