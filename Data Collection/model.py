import tensorflow as tf
import numpy as np

X, batch = [], []
batches = 32
timesteps = 10

def send_to_model(data):
    global X, batch
    new_data = data['eeg'][2:34]
    X.append(new_data)
    if len(X) < timesteps:
        return
    elif len(X) == timesteps:
        batch.append(X)
        X = []
        if len(batch) == batches:
            model = tf.keras.models.load_model('eeg_model.h5')
            batches = np.array(batches)
            movements = model.predict(batches)
            print(movements)
            # call function to move arm
    else:
        print("error")
        return
