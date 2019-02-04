## CONUHACKS 2019
# SmartTrash 

SmarTrash is an automated sorting trash can that analyses the waste thrown into it and disposes of it in the adequate waste collector (Cardboard, Glassm Metal/Plastic, general waste). The analysis is done using IBM Watson’s Visual Recognition API with a custom model trained with roughly 2500 pictures of the different types of waste. A Raspberry Pi is used with a webcam to take a picture of the waste that is then sent to Watson which in return sends its prediction on the category of garbage. The waste is then dropped into the appropriate contained with the use of a mechanical arm controlled by 2 servos. 

Files Description: 

--------------------------------MAIN PROGRAM-------------------------------------------------
- Smart Trash - Main Program Ready to use once your custom model has been trained on WATSON

--------------------------------SUB PARTS PROGRAMS-------------------------------------------

- Trigger.py - Take a screenshoot from the webcam.
- WatsonAPI.py - Type your API for usage.
- WatsonAPIusa.py - Used to call the API and print the prediction on screen. 
- Setup.py - Used to install all required packages.


Using the Watson API
USe instructions on IBM Watson : 
First of all register in IBM Watson cloud, follow the instructions. 
Go on Watson Studio -> Find Visual Processing -> Create a Custom model (find Data sets on websites like Kaggle)

Follow the instructions here : 
https://cloud.ibm.com/apidocs/visual-recognition?language=python#classify-images


The motion 

![alt text](https://github.com/adaamm/Smart-Bin/blob/master/smartBinCircuit.png)

[![IMAGE ALT TEXT HERE](https://github.com/adaamm/Smart-Bin/blob/master/smartBinCircuit.png)](https://www.youtube.com/watch?v=2YGlFAdJA10&feature=youtu.be)
