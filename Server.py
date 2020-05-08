from  flask import  Flask,render_template,request,json
import pickle
from Prediction import Prediction
from Precautions import Precautions
from DressingSuggestion import DressingSuggestion
app =Flask(__name__)


#this will only for simple  
@app.route("/")
def home():
    return 'Welcom to weather Care+ Please made request according to Api Discription'

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




if __name__ == '__main__':
    app.run()
