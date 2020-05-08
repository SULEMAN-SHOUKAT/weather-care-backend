import pickle
import sqlite3



class DressingSuggestion:

        
#  this method return us the current weather perdiction   
    def get_WeatherPerdiction(self,MinTemp,MaxTemp):
        # Load from file
              pkl_filename = "./Models/Temperature_Classification.pkl"
              with open(pkl_filename, 'rb') as file:
                    pickle_model = pickle.load(file)
              WeatherPerdiction= pickle_model.predict([[MinTemp,MaxTemp]])
              return str(WeatherPerdiction[0])
       
       
       
            
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