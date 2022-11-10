from django.shortcuts import render
import pickle
import pandas as pd
# Create your views here.
def index(request):
    return render(request,'home/index.html')

def YesOrNo(query):
    if int(query)==1:
        return 'YES'
    return 'NO'

def result(request):
    rfr = pickle.load(open("RandomForestRegressor.pkl","rb"))
    if request.method == 'POST':
        temp={}
        temp['Age'] = request.POST.get('Age')
        temp['Diabetes'] = request.POST.get('Diabetes')
        temp['BloodPressureProblems'] = request.POST.get('BloodPressureProblems')
        temp['AnyTransplants'] = request.POST.get('AnyTransplants')
        temp['AnyChronicDiseases'] = request.POST.get('AnyChronicDiseases')
        temp['Height'] = request.POST.get('Height')
        temp['Weight'] = request.POST.get('Weight')
        temp['KnownAllergies'] = request.POST.get('KnownAllergies')
        temp['HistoryOfCancerInFamily'] = request.POST.get('HistoryOfCancerInFamily')
        temp['NumberOfMajorSurgeries'] = request.POST.get('NumberOfMajorSurgeries')

        testdata = pd.DataFrame({'x':temp}).transpose()
        predictedData = rfr.predict(testdata)

    context={
        'name' : request.POST.get('Name'),
        'age': temp['Age'],
        'diabetes':YesOrNo(temp['Diabetes']),
        'bloodPressureProblems':YesOrNo(temp['BloodPressureProblems']),
        'transplants':YesOrNo(temp['AnyTransplants']),
        'chronicDiseases':YesOrNo(temp['AnyChronicDiseases']),
        'height': temp['Height'],
        'weight': temp['Weight'],
        'allergies':YesOrNo(temp['KnownAllergies']),
        'cancerInFamily':YesOrNo(temp['HistoryOfCancerInFamily']),
        'surgeries': temp['NumberOfMajorSurgeries'],
        'premium': round(predictedData[0])
        }
    return render(request,'home/result.html',context)