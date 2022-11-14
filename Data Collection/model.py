import tensorflow as tf
import numpy as np
import concurrent.futures as cf
from cf import ThreadPoolExecutor

X, batch = [], []
batches = 32
timesteps = 10

def send_to_model(data):
    global X, batch
    model = tf.keras.models.load_model('eeg_model.h5')
    new_data = data['eeg'][2:34]
    X.append(new_data)
    if len(X) < timesteps:
        return
    elif len(X) == timesteps:
        batch.append(X)
        X = []
        if len(batch) == batches:
            with ThreadPoolExecutor(max_workers=1) as ex:
                batches = np.array(batches)
                future = ex.submit(model.predict(batches))
                #movements = model.predict(batches)
                future.result()
                # call function to move arm
    else:
        print("error")
        return
