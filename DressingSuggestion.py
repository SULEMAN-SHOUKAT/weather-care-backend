import pickle
import sqlite3
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


class DressingSuggestion:

        
#  this method return us the current weather perdiction   
    def get_WeatherPerdiction(self,MinTemp,MaxTemp):
        # Load from file
               # load dataset
                pima = pd.read_csv("Temperature_Classification.csv")
               #split dataset in features and target variable
                feature_cols = ['MinTemp', 'MaxTemp']
                X = pima[feature_cols] # Features
                y = pima.Weather # Target variable
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
                #  Create Decision Tree classifer object
                model = DecisionTreeClassifier(criterion="entropy") 
                # Train Decision Tree Classifer
                clf = model.fit(X_train,y_train)
                # #Predict the response for test dataset
                weathear_Probability = clf.predict([[MinTemp,MaxTemp]])
                return str(weathear_Probability[0])
       
       
       
            
#this method will get the url of clothing images according to the perdiction
    def get_dressUrl(self,Weather):
        try:
           conn = sqlite3.connect('./Database/weathercare.db')
           cursor = conn.execute("SELECT %s,%s,%s FROM DressUrl where %s=?" % ('weather', 'gender','url','weather'), (Weather,))
           Url_List=[]
           for url in cursor:
               Url_List.append({'weather':url[0],'gender':url[1],'url':url[2]})
           conn.close()
           return Url_List
        except:
            return 'there is an error while getting Urls of clothing images'
        
        
        
        
#this method will get the dressing discription according to the request     
    def getDressingDiscription(self,weather):
        if(weather=='Very hot'):
            weather='Veryhot'
        if(weather=='Cold'):
            weather='Coold'
        try:
           conn = sqlite3.connect('./Database/weathercare.db')
           Query="SELECT * FROM "+weather
           cursor = conn.execute(Query)
           discription_List=[]
           for discription in cursor:
               discription_List.append({'time':discription[0],'title':discription[1],'description':discription[2]})
           conn.close()
           return discription_List
        except:
            return 'There is an error while getting you Dressing Discriptions'




#this method will used to get the dressing  data and return it
    def get_DressingSuggestion(self,MinTemp,MaxTemp):
            Weather_Perdiction=self.get_WeatherPerdiction(MinTemp,MaxTemp)
            DressingUrls=self.get_dressUrl(Weather_Perdiction)
            return DressingUrls