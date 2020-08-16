from  flask import  Flask,render_template,request,json
import pickle
from Prediction import Prediction
from Precautions import Precautions
from Medicen import Medicine
from DressingSuggestion import DressingSuggestion
from flask_cors import CORS,cross_origin
app =Flask(__name__)
CORS(app)

#this will only for simple  
@app.route("/")
def home():
    return {'Discription':'Welcom to weather Care+ Please made request according to Api Discription you can change variable values',
            'ApiRequests/urls':['/Prediction?MinTemp=5&MaxTemp=(valid temperature value)&WindSpeed=(valid wind speed value)&Humidity=(valid Humidity value)',
                                 '/Dressing?MinTemp=(valid temperature value)&MaxTemp=(valid temperature value)',
                                 '/Precaution?Disease=(flu)or(dangue)or(heatStroke)or(cold)','/dressingDiscription?Weather=(Very hot)or(Hot)or(Warm)or(Mild)or(Cold)or(Cool)']}

#this request it contains some parameters wind,maxtemp,mintemp,humidity  will used for the prediction of a disease  
@app.route("/Prediction", methods=['GET','POST'])
def prediction():
    if request.method == "GET" or request.method == "POST" :
              WindSpeed=request.args.get('WindSpeed')
              MinTemp=request.args.get('MinTemp')
              MaxTemp=request.args.get('MaxTemp')
              Humidity=request.args.get('Humidity')
              Predict=Prediction()
              Probability=Predict.genratePredictions(WindSpeed,MinTemp,MaxTemp,Humidity)
              return json.dumps({'results':Probability})
    return json.dumps({'Message':"Oops there is a problem in your request try later"})





#this will used for getting the precautions  of the disease that user request for  
@app.route("/Precaution", methods=['GET','POST'])
def precaution():
    if request.method == "GET" or request.method == "POST" :
              Disease=request.args.get('Disease')
              Precaution=Precautions()
              Precautions_List=Precaution.getDiseasePrecautions(Disease)
              return json.dumps({'Precautions':Precautions_List })
    return json.dumps({'Message':"Oops there is a problem in your request try later"})





#this will used for getting the Dressing Suggestions accrding to the Current Temperature 
@app.route("/Dressing", methods=['GET','POST'])
def Dressing():
    if request.method == "GET" or request.method == "POST" :
              MinTemp=request.args.get('MinTemp')
              MaxTemp=request.args.get('MaxTemp')
              dressing=DressingSuggestion()
              dressingSuggestion_data=dressing.get_DressingSuggestion(MinTemp,MaxTemp)
              return json.dumps({'urls':dressingSuggestion_data })
    return json.dumps({'Message':"Oops there is a problem in your request try later"})
        



#this will used for getting the precautions  of the disease that user request for  
@app.route("/dressingDiscription", methods=['GET','POST'])
def dressingDiscription():
    if request.method == "GET" or request.method == "POST" :
              weather=request.args.get('Weather')
              dressing=DressingSuggestion()
              DressingDiscription_List=dressing.getDressingDiscription(weather)
              return json.dumps({'Precautions':DressingDiscription_List})
    return json.dumps({'Message':"Oops there is a problem in your request try later"})


#this request it contains some parameters wind,maxtemp,mintemp,humidity  will used for the gettig the medicens 
@app.route("/Medicine", methods=['GET','POST'])
def medicine():
    if request.method == "GET" or request.method == "POST" :
              WindSpeed=request.args.get('WindSpeed')
              MinTemp=request.args.get('MinTemp')
              MaxTemp=request.args.get('MaxTemp')
              Humidity=request.args.get('Humidity')
              Predict=Prediction()
              Disease_Probability=Predict.genratePredictions(WindSpeed,MinTemp,MaxTemp,Humidity)
              GenerateMedicine=Medicine()
              medicines_List=GenerateMedicine.Generate_Medicine(Disease_Probability)
              return json.dumps({'results':medicines_List})
    return json.dumps({'Message':"Oops there is a problem in your request try later"})








if __name__ == '__main__':
    app.run()
