import json
import dateutil.parser as dp
  
f = open('D:\Capstone\Robotic-Arm-Control-using-EEG\Data Collection\Data\Day_1\Subject_1_EPOCFLEX_164574_2022.10.18T14.53.22+05.30.json')
data = json.load(f)

i=0
labels = {
    'rest' : [],
    'grab' : [],
    'elbow_up' :[],
    'elbow_down':[],
    'release':[],
    'shoulder_right':[],
    'shoulder_left':[],
    'wrist_pronation':[],
    'wrist_supination':[]
}
#print(data['Markers'][0]['label'])
while i!=len(data['Markers'])-2:
    labels[data['Markers'][i]['label']].append([dp.parse(data['Markers'][i]['startDatetime']).timestamp(),dp.parse(data['Markers'][i+1]['startDatetime']).timestamp()])
    i=i+1
for i in labels:
    print(i,':',labels[i])
f.close()