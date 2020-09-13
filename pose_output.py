"""
Created on Sat Sept 13 13:07:23 2020
@author: gauravsinha7
"""


import cv2
import math
import numpy as np
from pose_estimator import face_orientation  #importing from pose_estimator.py

f = open('/home/gauravsinha7/Documents/face_estimation/test/landmark.txt','r')
for line in iter(f):
    img_info = line.split(' ')
    img_path = img_info[0]
    frame = cv2.imread(img_path)
    landmarks =  map(int, img_info[1:])
    
    print img_path
    imgpts, modelpts, rotate_degree, nose = face_orientation(frame, landmarks)
    
    cv2.line(frame, nose, tuple(imgpts[1].ravel()), (0,255,0), 3) #GREEN
    cv2.line(frame, nose, tuple(imgpts[0].ravel()), (255,0,), 3) #BLUE
    cv2.line(frame, nose, tuple(imgpts[2].ravel()), (0,0,255), 3) #RED
    
    remapping = [2,3,0,4,5,1]
    for index in range(len(landmarks)/2):
        random_color = tuple(np.random.random_integers(0,255,size=3))
 
        cv2.circle(frame, (landmarks[index*2], landmarks[index*2+1]), 5, random_color, -1)  
        cv2.circle(frame,  tuple(modelpts[remapping[index]].ravel().astype(int)), 2, random_color, -1)  
        
            
#    cv2.putText(frame, rotate_degree[0]+' '+rotate_degree[1]+' '+rotate_degree[2], (10, 30),
#                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
#                thickness=2, lineType=2)
                
    for j in xrange(len(rotate_degree)):
                cv2.putText(frame, ('{:05.2f}').format(float(rotate_degree[j])), (10, 30 + (50 * j)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2, lineType=2)

    cv2.imwrite(img_path.split('/')[1], frame)

f.close()
