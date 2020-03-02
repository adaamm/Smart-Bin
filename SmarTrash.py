from watson_developer_cloud import VisualRecognitionV3
import json
import pprint
from watson_developer_cloud import VisualRecognitionV3
import os
import RPi.GPIO as GPIO
import time

result = 0;
type_garbage = 0 ; 

#Using the IBM API 
visual_recognition = VisualRecognitionV3(
    version='{2018-03-19}', #date of last version
    iam_apikey='56-JCITaJsCJJ9B0aF80K5gliWY9MFcGH1HDGyHeZdcV' #our Key
)

os.system("fswebcam image.jpg") #Triggering the camera

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='56-JCITaJsCJJ9B0aF80K5gliWY9MFcGH1HDGyHeZdcV') #API Key on IBM Watson

#Checking the file
with open('./image.jpg', 'rb') as images_file: 
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
    classifier_ids='DefaultCustomModel_496685283').get_result()
#print(json.dumps(classes, indent=2))

#word to look for
words = ("trash","metal", "plastic", "paper", "cardboard")
with open('waste.txt', 'w') as outfile:
 json.dump(classes, outfile)

with open("waste.txt") as openfile:
    for line in openfile:
        for part in line.split():
            for m in words:
                if m in part:
                  result = m
                  print(result)
                 #just to test what is inside of resut print(result)

if result == "cardboard" or result == "paper":
    type_garbage = 0
elif result == "plastic" or result == "metal":
    type_garbage = 1
elif result == "glass":
    type_garbage = 2
else: type_garbage == 3 #assume trash, has to be


# The issue with 4 and 11 for dumper is that it will hit the ramp if we allow it to go all the way left or right (perpendicular)
# Hence im trying alternative values for left right
#left  ->5
#right ->10

#setting up servos
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
rotator = GPIO.PWM(12, 50)
dumper = GPIO.PWM(16, 50)


#set to middle
rotator.start(7.5) 
dumper.start(7.5)
time.sleep(2)

def smoothRotator(dc): #just to smooth out the first rotator movement
    for i in range(20,-1,-1):
        rotator.ChangeDutyCycle(dc-(i/10.))
        time.sleep(0.07)
        
        
if type_garbage == 0 :
    dumper.ChangeDutyCycle(5) #dump left
    time.sleep(2)
    dumper.ChangeDutyCycle(7.5) #turn middle
    
elif type_garbage == 1:
    dumper.ChangeDutyCycle(10) #dump right
    time.sleep(2)
    dumper.ChangeDutyCycle(7.5) #turn middle
    
elif type_garbage == 2:
    smoothRotator(11) #turn right #11 doesnt work for rotator
    time.sleep(1)
    dumper.ChangeDutyCycle(5) #dump
    time.sleep(2)
    dumper.ChangeDutyCycle(7.5) #back to middle
    time.sleep(1)
    rotator.ChangeDutyCycle(7.5) #back to middle
    
elif type_garbage == 3:
    smoothRotator(11) #turn right
    time.sleep(1)
    dumper.ChangeDutyCycle(10) #dump
    time.sleep(2)
    dumper.ChangeDutyCycle(7.5) #back to middle
    time.sleep(1)
    rotator.ChangeDutyCycle(7.5) #back to middle
    
    
time.sleep(2)
dumper.stop()
rotator.stop()
GPIO.cleanup()





