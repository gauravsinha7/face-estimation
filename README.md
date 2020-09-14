# face-estimation
Project to predict face landmarks and poses using openCV.

## Description
Pose estimation(yaw, pitch and roll)using by Face landmarks(left eye, right eye, nose, left mouth, right mouth and chin).
Roll:+90°：-90°/Pitch:+90°：-90°/Yaw:+90°：-90°

![Roll Pitch Yaw.png](https://raw.githubusercontent.com/gauravsinha7/face-estimation/master/roll_pitch_yaw.png)

## Outputs

The order of numbers is ***ROLL***, ***PITCH***, ***YAW*** :
<br/>

![Sample_1.png](https://raw.githubusercontent.com/gauravsinha7/face-estimation/master/sample_1.jpg)
![Sample_2.png](https://raw.githubusercontent.com/gauravsinha7/face-estimation/master/sample_2.JPEG)
![Sample_3.png](https://raw.githubusercontent.com/gauravsinha7/face-estimation/master/sample_3.JPEG)

# Preprocessing
* I fine-tune the MTCNN into the output of 6 landmark feature points, reference and make some adjustments in this article 'Head Pose Estimation using OpenCV and Dlib'.
* Because the MTCNN's eyes are the middle of the position rather than the corner of the eye, so we modify the world coordinate(model point) from original to (-150.0, -150.0, -125.0)# Left Mouth corner/(150.0, -150.0, -125.0)# Right mouth corner
* Modify the camera matrix's focal_length from original to img_size[1]/2 / np.tan(60/2 * np.pi / 180).
