from django.shortcuts import render
from joblib import load
import pickle

model = pickle.load(open("model.pkl",'rb'))


def Landingpage(req):
    return render(req,"Landingpage.html")

def Prediction(req):
    rain=int(req.POST['rain'])
    maxtemp=int(req.POST['tmax'])
    mintemp=int(req.POST['tmin'])
    mintempg=int(req.POST['tming'])
    year=int(req.POST['year'])
    month=int(req.POST['month'])
    day=int(req.POST['day'])
    input=[[0,rain,0,0,maxtemp,mintemp,mintempg,year,month,day]]
    print(input)
    prediction=model.predict(input)
    print(prediction)
    return render(req,'Result1.html',{'predicted':prediction})

