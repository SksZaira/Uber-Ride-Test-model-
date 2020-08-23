from django.shortcuts import render
import pickle
import os

# Create your views here.
def index(request):
    return render(request,'index.html')

def test(request):
    ppw = int(request.POST['ppw'])
    pn = int(request.POST['pn'])
    mi = int(request.POST['mi'])
    appm = int(request.POST['appm'])
    modulepath = os.path.dirname(__file__)             # for absolute path
    filepath = os.path.join(modulepath,'taxi.pkl')
    model = pickle.load(open(filepath,'rb'))
    res =str(model.predict([[ppw,pn,mi,appm]])[0].round(2))
    return render(request,'index.html',{'res':res})

