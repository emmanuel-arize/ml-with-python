"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from xgboost import XGBClassifier
import numpy as np
from xgboost import XGBClassifier
import joblib
import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# loading the saved model
model=joblib.load(os.path.join(BASE_DIR,'app/models/iris_model.pkl'))

def home(request):
    return render(request,'app/index.html',{'title':'Home Page','year':datetime.now().year,})

def SpeciesPrediction(request):
    if request.method=='POST':
        sepal_l=request.POST['sepal_length']
        sepal_w=request.POST['sepal_width']
        petal_l=request.POST['petal_length']
        petal_w=request.POST['petal_width']
        data=[sepal_l,sepal_w,petal_l,petal_w]
        data=np.array(data).reshape(-1,4)
        result=model.predict(data)
        print(result)
        species = ['Setosa', 'versicolor', 'virginica']
        result = species[result[0]]
        context={"result":result}
        return render(request, 'app/irispredict.html', context)
        
    


