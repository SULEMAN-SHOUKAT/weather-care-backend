import sqlite3


class Medicine:
    
      Medi=[]
      
    #this method will get the url of Medicine images according to the perdiction
      def get_MedicineUrl(self,Disease):
        try:
           conn = sqlite3.connect('./Database/weathercare.db')
           cursor = conn.execute("SELECT %s,%s FROM MedicineUrl where %s=?" % ('disease', 'mediUrl','disease'), (Disease,))
           
           for url in cursor:
                self.Medi.append({'disease':url[0],'mediUrl':url[1]})
           conn.close()
           
        except:
            self.Medi.append({'NoMedi':'DataBaseErrorr'})  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
#     Get the Medicine according to Disease Perdiction
      def Generate_Medicine(self,Predictions):
         self.Medi=[]
#        Getting the Medicen if Prediction has value > 0
         if(Predictions["FluProbability"]!='0'):
                if(Predictions["FluProbability"]=='1'):
                     print('as flue is one so do nothing')    
                else:
                     self.get_MedicineUrl('Flu')
         if(Predictions["ColdProbability"]!='0'):
            self.get_MedicineUrl('Cold')
         if(Predictions[ "HeatStrokeProbability"]!='0'):
            self.get_MedicineUrl('H-S')
         if(Predictions[ "Dangueprobability"]!='0'):
            self.get_MedicineUrl('Dengue')
         if((Predictions["FluProbability"]=='0' or Predictions["FluProbability"]=='1') and Predictions["ColdProbability"]=='0' and Predictions[ "HeatStrokeProbability"]=='0' and Predictions[ "Dangueprobability"]=='0'):
            return None
         print(self.Medi)   
         return self.Medi