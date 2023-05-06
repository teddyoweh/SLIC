from Slic import Slic
import pickle
from util import Util
server = Slic()
def add(payload):
    print(payload['a']+1)
    return {'answer':payload['a']+1}
  

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
server.create_resource(":get_server_variable", get_server_variable)
server.create_upload_resource(':pyt','test')
print(globals())
server.start('localhost',9951)



