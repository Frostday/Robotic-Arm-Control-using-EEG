from cortex import Cortex
import serial
import tensorflow as tf
import numpy as np
from collections import Counter
import time


def write_read(arduino, x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

class Subcribe():
    """
    A class to subscribe data stream.

    Attributes
    ----------
    c : Cortex
        Cortex communicate with Emotiv Cortex Service

    Methods
    -------
    start():
        start data subscribing process.
    sub(streams):
        To subscribe to one or more data streams.
    on_new_data_labels(*args, **kwargs):
        To handle data labels of subscribed data 
    on_new_eeg_data(*args, **kwargs):
        To handle eeg data emitted from Cortex
    on_new_mot_data(*args, **kwargs):
        To handle motion data emitted from Cortex
    on_new_dev_data(*args, **kwargs):
        To handle device information data emitted from Cortex
    on_new_met_data(*args, **kwargs):
        To handle performance metrics data emitted from Cortex
    on_new_pow_data(*args, **kwargs):
        To handle band power data emitted from Cortex
    """
    def __init__(self, app_client_id, app_client_secret, **kwargs):
        """
        Constructs cortex client and bind a function to handle subscribed data streams
        If you do not want to log request and response message , set debug_mode = False. The default is True
        """
        print("Subscribe __init__")
        self.c = Cortex(app_client_id, app_client_secret, debug_mode=True, **kwargs)
        self.c.bind(create_session_done=self.on_create_session_done)
        self.c.bind(new_eeg_data=self.on_new_eeg_data)        
        self.c.bind(inform_error=self.on_inform_error)

    def start(self, streams, headsetId=''):
        """
        To start data subscribing process as below workflow
        (1)check access right -> authorize -> connect headset->create session
        (2) subscribe streams data
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power
        'eq' : EEQ Quality

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']
        headsetId: string , optional
             id of wanted headet which you want to work with it.
             If the headsetId is empty, the first headset in list will be set as wanted headset
        Returns
        -------
        None
        """
        self.streams = streams

        if headsetId != '':
            self.c.set_wanted_headset(headsetId)

        self.c.open()

    def sub(self, streams):
        """
        To subscribe to one or more data streams
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']

        Returns
        -------
        None
        """
        self.c.sub_request(streams)

    def unsub(self, streams):
        """
        To unsubscribe to one or more data streams
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']

        Returns
        -------
        None
        """
        self.c.unsub_request(streams)

    def on_new_eeg_data(self, *args, **kwargs):
        """
        To handle eeg data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array eeg match the labels in the array labels return at on_new_data_labels
        For example:
           {'eeg': [99, 0, 4291.795, 4371.795, 4078.461, 4036.41, 4231.795, 0.0, 0], 'time': 1627457774.5166}
        """
        data = kwargs.get('data')
        batches = 32
        timesteps = 10
        movements = {
                    0:'rest',
                    1:'grab',
                    2:'release',
                    3:'elbow_up',
                    4:'elbow_down',
                    5:'wrist_supination',
                    6:'wrist_pronation',
                    7:'shoulder_right',
                    8:'shoulder_left'
                }
        global X, batch, model, arduino
        new_data = data['eeg'][2:34]
        X.append(new_data)
        if len(X) < timesteps:
            pass
        elif len(X) == timesteps:
            batch.append(X.copy())
            X = list()
            if len(batch) == batches:
                batch_arr = np.array(batch.copy())
                values = model.predict(batch_arr)
                moves = np.argmax(values, axis=1)
                
                occurence_count = Counter(moves)
                x = occurence_count.most_common(1)[0][0]
                move = movements[x]
                value = write_read(arduino, x)
                print(value)
                batch = list()
        else:
            X = []
            batch = []
            print("error")
        # print('eeg data: {}'.format(data))

    # callbacks functions
    def on_create_session_done(self, *args, **kwargs):
        print('on_create_session_done')

        # subribe data 
        self.sub(self.streams)

    def on_inform_error(self, *args, **kwargs):
        error_data = kwargs.get('error_data')
        print(error_data)

# -----------------------------------------------------------
# 
# GETTING STARTED
#   - Please reference to https://emotiv.gitbook.io/cortex-api/ first.
#   - Connect your headset with dongle or bluetooth. You can see the headset via Emotiv Launcher
#   - Please make sure the your_app_client_id and your_app_client_secret are set before starting running.
#   - In the case you borrow license from others, you need to add license = "xxx-yyy-zzz" as init parameter
# RESULT
#   - the data labels will be retrieved at on_new_data_labels
#   - the data will be retreived at on_new_[dataStream]_data
# 
# -----------------------------------------------------------

def main():
    # Please fill your application clientId and clientSecret before running script
    your_app_client_id = 'YhTVuH9KahGPJFaTjaHA3JTWFBJgphPGolgYomZ7'
    your_app_client_secret = 'GGu9BpyH3gRkJq0ZJpdjAPqofgYDctl31Bzbl69o2XCCL0uLjcl5Gfo0RgMGJxEfnBEc7hyEAZFnsKBADBohkEZ4ifAuaH0L7jMWRAgs6K3GYO7CwPbYREsj65NYw7aa'

    s = Subcribe(your_app_client_id, your_app_client_secret)

    # list data streams
    streams = ['eeg']
    s.start(streams)

if __name__ =='__main__':
    X, batch = [], []
    model = tf.keras.models.load_model('../Models/eeg_model_3.h5')
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

    main()

# -----------------------------------------------------------
