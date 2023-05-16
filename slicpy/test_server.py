from Slic import Slic
import pickle
from util import Util
from beardb import Beardb,Bucket
server = Slic()
project = Beardb('teddyoweh.net')
project.load_database('app')
views = Bucket(project=project, bucket_name='views')
def add(payload):
    print(payload['a']+1)
    return {'answer':payload['a']+1}
  
 



def add_views(data):
 
    views.insert(data)

def get_views(payload):
   return views.fetchData()

def login(payload):
    print(payload['username'])
    print(payload['password'])
    return {'login':True}
name = 'teddy'
 
 
   
def get_server_variable(payload):
    var = payload["variable_name"]
    print(payload)
    var = var.split('.')
    if var[0] in globals():
        
    
     
       if var[0] in globals():
        obj = globals()[var[0]]
        nested_attr = Util.get_nested_attribute(var,obj, var[1:])
        print(nested_attr)
        bits = f"{nested_attr}"
        
     

        
        return str(bits)
    else:
        return f"Variable '{var[0]}' not found in server globals"
        #raise Exception(f"Variable '{var[0]}' not found in server globals")

server.create_resource(':test',add)
server.create_resource(':login',login)
server.create_resource(':add_views',add_views)
server.create_resource(':get_views',get_views)
server.create_resource(":get_server_variable", get_server_variable)
server.create_upload_resource(':pyt','test')
 
server.start('localhost',9999)



