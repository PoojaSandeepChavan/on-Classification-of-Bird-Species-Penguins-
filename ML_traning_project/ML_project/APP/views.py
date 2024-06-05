from django.shortcuts import render
import pickle
import os
from django.conf import settings
# Create your views here.
def home(request):
    return render(request,'home.html')

def showresult(request):
    if request.method=='POST':
        Island=(request.POST['Island'])
        culmen_length_mm= float(request.POST['P'])
        culmen_depth_mm=float(request.POST['K'])

        flipper_length_mm=float(request.POST['T'])
        body_mass_g	=float(request.POST['H'])
        Sex=int(request.POST['Sex'])
       
        with open(os.path.join(settings.BASE_DIR,'Penguin_svl'),'rb') as f:
            model=pickle.load(f)
            print("model loaded ")
            result=model.predict([[Island,culmen_length_mm,culmen_depth_mm,flipper_length_mm,body_mass_g,Sex]])[0]
            if int(result) == 0:
                result = "Adelie"
            elif int(result) == 1:
                result = "Chinstrap"
            else:
                result = "Gentoo"

            print("value predicted")

    
    return render(request,'result.html',{'result':result})