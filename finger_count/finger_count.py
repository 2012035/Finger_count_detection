import cv2
import mediapipe as mp
import hand_tracking as ht
import os
import math
path=os.listdir('image')
layer=[]
for i in path:
    image=cv2.imread(f'image/{i}')
    image=cv2.resize(image,(150,200))
    layer.append(image)
video=cv2.VideoCapture(0)
detect=ht.handDetector()
while True:
    s,images=video.read()
    h,w,s=layer[0].shape
    hand=detect.handDetection(images,draw=False)
    position=detect.findPosition(hand,draw=False)
    if len(position)!=0:
        x,y=position[0][1],position[0][2]
        a, b = position[9][1], position[9][2]
        x1,y1=position[4][1],position[4][2] #thumb
        x2,y2=position[8][1],position[8][2] #index
        x3,y3=position[12][1],position[12][2] #middle
        x4,y4=position[16][1],position[16][2] #ring
        x5,y5=position[20][1],position[20][2] #small
        mx,my=(a+x)/2,(b+y)/2;
        distance1 = math.sqrt((mx - x1) ** 2 + (my - y1) ** 2)
        distance2 = math.sqrt((mx - x2) ** 2 + (my - y2) ** 2)
        distance3 = math.sqrt((mx - x3) ** 2 + (my - y3) ** 2)
        distance4 = math.sqrt((mx - x4) ** 2 + (my - y4) ** 2)
        distance5 = math.sqrt((mx - x5) ** 2 + (my - y5) ** 2)
        if(distance1>=100 or distance2>=120 or distance3>=110 or distance4>=100 or distance5>=100):
            if(distance1<=60 and distance3<=60 and distance4<=60 and distance5<=60):
                hand[:h, :w] = layer[1]
                cv2.putText(hand,'1',(10,400),cv2.FONT_HERSHEY_DUPLEX,3.0,(0,0,0),3)
            elif(distance1<=30 and distance4<=30 and distance5<=30):
                hand[:h, :w] = layer[2]
                cv2.putText(hand, '2', (10, 400), cv2.FONT_HERSHEY_DUPLEX, 3.0, (0, 0, 0), 3)
            elif(distance1<=40 and distance5<=40):
                hand[:h, :w] = layer[3]
                cv2.putText(hand, '3', (10,400), cv2.FONT_HERSHEY_DUPLEX, 3.0, (0, 0, 0), 3)
            elif(distance1<=40):
                hand[:h, :w] = layer[4]
                cv2.putText(hand, '4', (10, 400), cv2.FONT_HERSHEY_DUPLEX, 3.0, (0, 0, 0), 3)
            else:
                hand[:h, :w] = layer[5]
                cv2.putText(hand, '5', (10, 400), cv2.FONT_HERSHEY_DUPLEX, 3.0, (0, 0, 0), 3)
        else:
            hand[:h, :w] = layer[0]
            cv2.putText(hand, '0', (10, 400), cv2.FONT_HERSHEY_DUPLEX, 3.0, (0, 0, 0), 3)
    cv2.imshow('Finger_count',hand)
    if(cv2.waitKey(1) & 0xff==ord('z')):
        break

