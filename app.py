#app.py#Import necessary packages
from flask import Flask
from flask_restful import Resource, reqparse, Api #Instantiate a flask object 
app = Flask(__name__)
#Instantiate Api object
api = Api(app)

#import API from RMPClass
from RMPClass import RateMyProfAPI

class RMP(Resource):
    def get(self, name):    
        rmp = RateMyProfAPI(teacher = name)  
        rmp.retrieve_rmp_info()
        if rmp.get_rmp_info() == "Info currently not available":            
            return -1
        return float(rmp.get_rmp_info().split('/')[0])

api.add_resource(RMP, '/<string:name>')

if __name__=='__main__':        
    #Run the applications
    app.run() 
    