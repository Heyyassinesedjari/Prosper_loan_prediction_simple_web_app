import pickle 

modelfilename = 'application/Logistic_Regression.pkl'
scalerfilename = 'application/Scaler.pkl'

model = pickle.load(open(modelfilename, 'rb'))

scaler = pickle.load(open(scalerfilename, 'rb'))
