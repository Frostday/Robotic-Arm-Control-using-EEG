import pandas as pd
import json
import dateutil.parser as dp


json_file_path = "Data/Day_1/Subject_1_EPOCFLEX_164574_2022.10.18T14.53.22+05.30.json"
csv_file_path =  "Data/Day_1/Subject_1_EPOCFLEX_164574_2022.10.18T14.53.22+05.30.csv"
labels_to_index = {'rest':1, 'grab':2, 'elbow_up':3, 'elbow_down':4, 'release':5, 'shoulder_right':6, 'shoulder_left':6,'wrist_pronation':7,'wrist_pronation':8,'None': 0}


def labelsToIndex(label):
    return labels_to_index[label]

def returnLabel(timestamp): #This code will check which label range does the current timestamp belong to and return the labels name


    with open(json_file_path, 'r') as j:
        i=0
        data = json.loads(j.read())
        while i!=len(data['Markers'])-2:
           startDT = dp.parse(data['Markers'][i]['startDatetime']).timestamp()
           endDT = dp.parse(data['Markers'][i+1]['startDatetime']).timestamp()
           print(startDT,endDT,timestamp)
           if startDT <= timestamp <= endDT:
               return data['Markers'][i]['label']
           i=i+1
    return "None"



df = pd.read_csv(csv_file_path,skiprows=1) #skipping first row for original column names

#Next two lines will generated a new column, one will have name of label and other will have index corresponding to label
df['Movement Label Name'] = df.apply(lambda row: returnLabel(row['Timestamp']), axis=1)
df['Movement Label Index'] = df.apply(lambda row: labelsToIndex(row['Movement Label Name']), axis=1)
