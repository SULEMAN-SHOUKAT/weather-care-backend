import pickle


class Prediction:
    
    
#     For flue prediction Flu method will run
    def Flu(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              # Load from file
              pkl_filename = "./Models/DTflue.pkl"
              with open(pkl_filename, 'rb') as file:
                    pickle_model = pickle.load(file)
              Flu_Probability= pickle_model.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
              return str(Flu_Probability[0])
            
            
            
            
#     for heatstroke prediction  this heatstroke method will run        
    def heatstroke(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              # Load from file
              pkl_filename = "./Models/DTheatStroke.pkl"
              with open(pkl_filename, 'rb') as file:
                    pickle_model = pickle.load(file)
              heatStroke_Probability= pickle_model.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
              return str(heatStroke_Probability[0])
            
            
            
            
            
#     For flue prediction Cold method will run
    def Cold(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              # Load from file
              pkl_filename = "./Models/DTcold.pkl"
              with open(pkl_filename, 'rb') as file:
                    pickle_model = pickle.load(file)
              Cold_Probability= pickle_model.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
              return str(Cold_Probability[0])
            



#     For flue prediction Cold method will run
    def dangue(self,WindSpeed,MinTemp,MaxTemp,Humidity):
              # Load from file
              pkl_filename = "./Models/DTdangue.pkl"
              with open(pkl_filename, 'rb') as file:
                    pickle_model = pickle.load(file)
              dangue_Probability= pickle_model.predict([[WindSpeed,MinTemp,MaxTemp,Humidity]])
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