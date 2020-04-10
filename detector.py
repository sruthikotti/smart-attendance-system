import cv2
import numpy as np
import sqlite3
conn=sqlite3.connect('test.db')
c=conn.cursor()
recognizer= cv2.createLBPHFaceRecognizer()
fname="recognizer/trainner.yml"
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load(fname)
fontFace=cv2.FONT_HERSHEY_SIMPLEX
fontScale=1
fontColor=(0,255,0)
while True:
    ret, img =cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
       
        if(ids==1):
                ids="pravalika"
                sql_command="""update stu_attendance set status="present" where name="sruthi";"""
                c.execute(sql_command)
                conn.commit()
                cv2.putText(img,str(ids),(x,y),fontFace,fontScale,fontColor)
        if(ids==2):
                ids="sruthi"
                sql_command="""update stu_attendance set status="present" where name="sruthi";"""
                c.execute(sql_command)
                conn.commit()
                cv2.putText(img,str(ids),(x,y),fontFace,fontScale,fontColor)
    cv2.imshow('Face Recognizer',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     
      
    
cap.release()
cv2.destroyAllWindows()
