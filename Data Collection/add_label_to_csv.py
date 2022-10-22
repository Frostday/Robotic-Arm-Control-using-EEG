import pandas as pd
import json
import dateutil.parser as dp


json_file_path = "Subject_1_EPOCFLEX_164574_2022.10.18T14.53.22+05.30.json"
csv_file_path =  "Subject_1_EPOCFLEX_164574_2022.10.18T14.53.22+05.30.csv"
labels_to_index = {'rest':0, 'grab':1, 'elbow_up':2, 'elbow_down':3, 'release':4}

def returnLabel(timestamp): #This code will check which label range does the current timestamp belong to and return the labels name


    with open(json_file_path, 'r') as j:
         contents = json.loads(j.read())
         for i in contents['Markers']:
             startDT = dp.parse(i['startDatetime']).timestamp()
             endDT = dp.parse(i['endDatetime']).timestamp()
             if startDT <= timestamp <= endDT:
                 return i['label']
             else:
                 print("ok")



df = pd.read_csv(csv_file_path,skiprows=1) #skipping first row for original column names

#Next two lines will generated a new column, one will have name of label and other will have index corresponding to label
df['Movement Label Name'] = returnLabel(df['Timestamp'])
df['Movement Label Index'] = labels_to_index[df['Movement Label Name']]
#df.to_csv(csv_file_path)
