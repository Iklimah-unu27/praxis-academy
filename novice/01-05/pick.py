import pickle

nama = { 'indah': 18, 'indi': 19, 'indo': 20 }

serial_nama = pickle.dumps( nama )
print(serial_nama)

received_name = pickle.loads( serial_nama )
print(received_name)