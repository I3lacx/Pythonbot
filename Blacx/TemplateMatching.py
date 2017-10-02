import numpy as np
import cv2

#You can add your own Template.png and this code will use
#your webcam and look after this template with a threshold

#my template
template_color = cv2.imread('Template.png')
#dont need this but good for troubleshooting of the wrong template
cv2.imshow('template', template_color)

#caputre web cam
cap = cv2.VideoCapture(0)
_,frame = cap.read()

#you will need height and width from the template to draw a box
h,w,_ = template_color.shape


while True:
        #rea webcam
        _,frame = cap.read()

        #for all px start points give the match quality
        res = cv2.matchTemplate(template_color, frame, cv2.TM_CCOEFF_NORMED)

        #set limit and look for high enough matches
        threshold = 0.7
        loc = np.where(res >= threshold)

        #every matches cords draw a rectangle
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255))

        #show image with boxes
        cv2.imshow('Detected', frame)

        #stop the loop
        if cv2.waitKey(1) == ord('q'):
            break

#set your webcam free
cap.release()
