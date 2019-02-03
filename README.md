## CONUHACKS_2019
# Smart=Trash- 

SmarTrash is an automated sorting trash can that analyses the waste thrown into it and disposes of it in the adequate waste collector (Cardboard, Glassm Metal/Plastic, general waste). The analysis is done using IBM Watson’s Visual Recognition API with a custom model trained with roughly 2500 pictures of the different types of waste. A Raspberry Pi is used with a webcam to take a picture of the waste that is then sent to Watson which in return sends its prediction on the category of garbage. The waste is then dropped into the appropriate contained with the use of a mechanical arm controlled by 2 servos. 


Using the Watson API
USe instructions on IBM Watson : 
First of all registe and download cloud, follow the instructions. 
Go on Watson Studio to create a model to train (find Data sets on websites like Kaggle)
Follow the instructions here : 
https://cloud.ibm.com/apidocs/visual-recognition?language=python#classify-images

SmarTrash.py is a merge of every other code for easier implementation on Raspberry Pi.

![alt text](https://github.com/adaamm/Smart-Bin/blob/master/smartBinCircuit.png)
