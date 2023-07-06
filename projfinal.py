import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

df=pd.read_csv('diabetes_pred.csv')

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])


feat = ['gender','age','hypertension','heart_disease','smoking_history','bmi','HbA1c_level','blood_glucose_level','diabetes']

X = df[feat]

def data_split(data,ratio):
    np.random.seed(222)
    shuffle=np.random.permutation(len(data))
    testsize=int(len(data)*ratio)
    train_ind=shuffle[testsize:]
    test_ind=shuffle[:testsize]
    return data.iloc[train_ind],data.iloc[test_ind]
train,test=data_split(df,0.99)

X_train=train[['gender','age','hypertension','heart_disease','smoking_history','bmi','HbA1c_level','blood_glucose_level']].to_numpy()
Y_train=train[['diabetes']].to_numpy()
X_test=test[['gender','age','hypertension','heart_disease','smoking_history','bmi','HbA1c_level','blood_glucose_level']].to_numpy()
Y_test=test[['diabetes']].to_numpy()

model1=LinearRegression()
model1.fit(X_train,Y_train)
def answ():
    g=input('Gender(M/F):')
    if g.lower()=='m':
        gen=1
    elif g.lower()=='f':
        gen=0
    else:
        gen=1
    age=int(input('Enter your age:'))
    hyp=input('Do you have hypertension(y/n):')
    if hyp.lower()=='y':
        ten=1
    elif hyp.lower()=='n':
        ten=0
    else:
        ten=0
    hyp = input('Do you have any heart disease(y/n):')
    if hyp.lower() == 'y':
        hea = 1
    elif hyp.lower() == 'n':
        hea = 0
    else:
        hea = 0
    print('Are you a smoker(y/n/f):')
    smk=input('')
    if smk.lower()=='y':
        smkq=1
    elif smk.lower()=='f':
        smkq=2
    elif smk.lower()=='n':
        smkq=0
    else:
        smkq=0
    bmi=float(input('Enter your BMI:'))
    hb=float(input('HbA1c_level:'))
    glc=float(input('Blood glucose level:'))
    p1 = model1.predict(np.array([gen,age,ten,hea,smkq,bmi,hb,glc]).reshape(1, -1))
    print('Chances of Diabetes', abs(p1[0][0] * 100),'%')
    if abs(p1[0][0])<=0.05:
        print('Eat Well!! You do not have diabetes')
    elif 0.051<= abs(p1[0][0]) <= 0.20:
        print('Low chance Take care')
    elif 0.201 <= abs(p1[0][0]) <= 0.40:
        print('Start Lowering sugar content in your diet')
    elif 0.401 <= abs(p1[0][0]) <= 0.60:
        print('Go Sugar Free for a healthy life and Take the sugar test as soon as possible')
    elif 0.601 <= abs(p1[0][0]):
        print('Take the sugar test as soon as possible')

while 1==1:
    answ()

