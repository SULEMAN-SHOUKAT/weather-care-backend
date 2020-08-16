import pickle
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

class Prediction:
    
    
#     For flue prediction Flu method will run
    def Flu(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              # Load from file
              # load dataset
                pima = pd.read_csv("Flue.csv")
               #split dataset in features and target variable
                feature_cols = ['WindSpeed', 'MinTemp', 'MaxTemp','Humidity']
                X = pima[feature_cols] # Features
                y = pima.Result # Target variable
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
                #  Create Decision Tree classifer object
                model = DecisionTreeClassifier(criterion="entropy") 
                # Train Decision Tree Classifer
                clf = model.fit(X_train,y_train)
                # #Predict the response for test dataset
                Flu_Probability = clf.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
                return str(Flu_Probability[0])
            
            
            
            
#     for heatstroke prediction  this heatstroke method will run        
    def heatstroke(self,WindSpeed,MinTemp,MaxTemp,Humidity):
               # Load from file
               # load dataset
                pima = pd.read_csv("heatStroke.csv")
               #split dataset in features and target variable
                feature_cols = ['WindSpeed', 'MinTemp', 'MaxTemp','Humidity']
                X = pima[feature_cols] # Features
                y = pima.Result # Target variable
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
                #  Create Decision Tree classifer object
                model = DecisionTreeClassifier(criterion="entropy") 
                # Train Decision Tree Classifer
                clf = model.fit(X_train,y_train)
                # #Predict the response for test dataset
                hs_Probability = clf.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
                return str(hs_Probability[0])
            
            
            
            
            
#     For flue prediction Cold method will run
    def Cold(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              # Load from file
               # load dataset
                pima = pd.read_csv("cold.csv")
               #split dataset in features and target variable
                feature_cols = ['WindSpeed', 'MinTemp', 'MaxTemp','Humidity']
                X = pima[feature_cols] # Features
                y = pima.Result # Target variable
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
                #  Create Decision Tree classifer object
                model = DecisionTreeClassifier(criterion="entropy") 
                # Train Decision Tree Classifer
                clf = model.fit(X_train,y_train)
                # #Predict the response for test dataset
                cold_Probability = clf.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
                return str(cold_Probability[0])
            



#     For flue prediction Cold method will run
    def dangue(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              ## Load from file
               # load dataset
                pima = pd.read_csv("dangue.csv")
               #split dataset in features and target variable
                feature_cols = ['WindSpeed', 'MinTemp', 'MaxTemp','Humidity']
                X = pima[feature_cols] # Features
                y = pima.Result # Target variable
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
                #  Create Decision Tree classifer object
                model = DecisionTreeClassifier(criterion="entropy") 
                # Train Decision Tree Classifer
                clf = model.fit(X_train,y_train)
                # #Predict the response for test dataset
                dangue_Probability = clf.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
                return str(dangue_Probability[0])






#this will handel all the Prediction requests to all methods like flue,hetstroke, 
    def genratePredictions(self,WindSpeed,MinTemp,MaxTemp,Humidity):
        Flu_prediction=self.Flu(WindSpeed,MinTemp,MaxTemp,Humidity)
        heatStroke_prediction=self.heatstroke(WindSpeed,MinTemp,MaxTemp,Humidity)
        Cold_Prediction=self.Cold(WindSpeed,MinTemp,MaxTemp,Humidity)
        dangue_Prediction=self.dangue(WindSpeed,MinTemp,MaxTemp,Humidity)
        return    {'FluProbability':Flu_prediction,
                   'HeatStrokeProbability':heatStroke_prediction,
                   'ColdProbability':Cold_Prediction,
                   'Dangueprobability':dangue_Prediction}