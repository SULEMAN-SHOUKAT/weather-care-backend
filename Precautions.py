import sqlite3


class Precautions:
  
  
#this will get the precaution according to the disease  from that specific disease table 
    def getDiseasePrecautions(self,Disease):
        try:
           conn = sqlite3.connect('./Database/weathercare.db')
           Query="SELECT * FROM "+Disease
           cursor = conn.execute(Query)
           Precaution_List=[]
           for precaution in cursor:
               Precaution_List.append({'time':precaution[0],'title':precaution[1],'description':precaution[2]})
           conn.close()
           return Precaution_List
        except:
            return 'there is an error while getting Precautions'
        
        
