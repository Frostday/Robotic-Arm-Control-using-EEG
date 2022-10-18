import json
import dateutil.parser as dp
  
f = open('D:\Capstone\Robotic-Arm-Control-using-EEG\Data Collection\Data\Subject_1_EPOCFLEX_164574_2022.10.17T20.59.32+05.30.json')
data = json.load(f)

i=0
labels = {
    'rest' : [],
    'grab' : [],
    'elbow_up' :[],
    'elbow_down':[],
    'release':[]
}
#print(data['Markers'][0]['label'])
while i!=len(data['Markers'])-2:
    labels[data['Markers'][i]['label']].append([dp.parse(data['Markers'][i]['startDatetime']).timestamp(),dp.parse(data['Markers'][i+1]['startDatetime']).timestamp()])
    i=i+1
for i in labels:
    print(i,':',labels[i])
f.close()