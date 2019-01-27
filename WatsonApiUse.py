import json
import pprint
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='enterapihere') #API Key on IBM Watson

with open('./image.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='DefaultCustomModel_117701744').get_result()
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
                  print(part)
                 #just to test what is inside of resut print(result)

