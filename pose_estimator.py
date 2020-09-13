
"""
Created on Sat Sept 12 20:58:14 2020
@author: gauravsinha7
"""


import cv2
import math
import numpy as np


def face_orientation(frame, landmarks):
    size = frame.shape #(height, width, color_channel)

    image_points = np.array([
                            (landmarks[4], landmarks[5]),     # Nose tip
                            (landmarks[10], landmarks[11]),   # Chin
                            (landmarks[0], landmarks[1]),     # Left eye left corner
                            (landmarks[2], landmarks[3]),     # Right eye right corne
                            (landmarks[6], landmarks[7]),     # Left Mouth corner
                            (landmarks[8], landmarks[9])      # Right mouth corner
                        ], dtype="double")

    

                        
    model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-165.0, 170.0, -135.0),     # Left eye left corner
                            (165.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner                         
                        ])
