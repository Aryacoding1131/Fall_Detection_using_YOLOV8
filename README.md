# Fall_Detection_using_YOLOV8

#### Dataset used:
https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset

#### dependencies 
1. python, Vs code
2. webcam / integrated webcam
3. Ultralytics
4. opencv

#### steps

1. create a virtual environment 'python -m venv venv'
2. activate the virtual environment by directing into scripts and activate.ps1
3. create .yaml file and write down the path of dataset
4. create train.py file for where we import yolov8 model from ultralytics then we train the model by giving the path of .yaml file and epoches of 20 since the dataset is about ~50mb, also it comes with email alerting system and buzzer 
5. we evaluate the model, we use metrices such as Recall (R), Precission (P), mAP 50, mAP 50-100
6. we test the model with video.mp4 file and also with live streaming data ie webcam for better results



#### Logic behind the code 

1. conf >= 0.40 and aspect_ratio > 1.0 and area > 15000.
Confidence ≥ 0.40 → YOLO is confident about the detection.
Aspect ratio > 1.0 → Person appears wider than tall (likely lying down).
Area > 15000 → Detection is large enough to be a person.


2. for normal person, hight > width & aspect ratio < 1
3. for fallen person, width > height & aspect ratio > 1

here aspect ratio = width / height


#### Results

1. Evaluation metrices

   <img width="1138" height="226" alt="image" src="https://github.com/user-attachments/assets/1d9a717e-c7d2-4402-837b-407430787c98" />

2. validation metrics

i. Confusion matrix

<img width="3000" height="2250" alt="image" src="https://github.com/user-attachments/assets/2a4f9fa5-5851-47c1-a6cb-4fd3586e639f" />

ii. validation

<img width="1920" height="1280" alt="image" src="https://github.com/user-attachments/assets/b1336b5a-910b-4ca7-8fb7-3987c792f60c" />


2. test 1

<img width="712" height="552" alt="image" src="https://github.com/user-attachments/assets/e1c5e642-ae3c-45fc-8dbc-bef8671b14c6" />

3. test 2

<img width="982" height="120" alt="image" src="https://github.com/user-attachments/assets/377c662f-6911-420e-ac58-dc95336354e8" />


<img width="1386" height="947" alt="image" src="https://github.com/user-attachments/assets/0498c9bb-7c34-46f8-8bf0-92cfa178236a" />


