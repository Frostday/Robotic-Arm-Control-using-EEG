columns = ['COUNTER', 'INTERPOLATED', 'Cz', 'Fz', 'Fp1', 'F7', 'F3', 
           'FC1', 'C3', 'FC5', 'FT9', 'T7', 'CP5', 'CP1', 'P3', 'P7', 
           'PO9', 'O1', 'Pz', 'Oz', 'O2', 'PO10', 'P8', 'P4', 'CP2', 
           'CP6', 'T8', 'FT10', 'FC6', 'C4', 'FC2', 'F4', 'F8', 'Fp2', 
           'HighBitFlex', 'SaturationFlag', 'RAW_CQ', 'MARKER_HARDWARE']
format = ['Cz', 'Fz', 'Fp1', 'F7', 'F3', 'FC1', 'C3', 'FC5','FT9', 'T7', 
          'CP5', 'CP1', 'P3', 'P7', 'PO9', 'O1', 'Pz', 'Oz', 'O2', 'PO10', 
          'P8', 'P4', 'CP2', 'CP6', 'T8', 'FT10', 'FC6', 'C4', 'FC2', 'F4', 
          'F8', 'Fp2']

def send_to_model(data):
    print(data['eeg'][2:34])
