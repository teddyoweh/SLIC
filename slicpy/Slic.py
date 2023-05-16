import socket
import threading
from .decorators import Logger
import ast
from .util import Util
from .HashMap import HashMap
from .NetworkTrafficMap import NetworkTrafficMap
from .Rate import Rate    
class RateLimiter(object):
    def __init__(self, Network: NetworkTrafficMap, rate: Rate):
        self.network = Network
        self.rate = rate

    def is_allowed(self, addr):
        ip = Util.ipkey(addr)
        if self.network.all.contains(ip):
            if self.network.all.get(ip)['requests'] >= 100:
                return False
            else:
                return self.validate_rate(ip)
        else:
            return True

    def is_allowed_current(self, addr):
        ip = Util.ipkey(addr)
        if self.network.current.contains(ip):
            if self.network.current.get(ip)['requests'] >= 100:
                return False
            else:
                return self.validate_rate(ip)
        else:
            return True

    def validate_rate(self, ip):
        rate_type = self.rate.get_rate()['type']
        rate_value = self.rate.get_rate()['rate']
        if rate_type == 'hourly':
            return self.validate_hourly_rate(ip, rate_value)
        elif rate_type == 'daily':
            return self.validate_daily_rate(ip, rate_value)
        elif rate_type == 'weekly':
            return self.validate_weekly_rate(ip, rate_value)
        elif rate_type == 'monthly':
            return self.validate_monthly_rate(ip, rate_value)
        elif rate_type == 'yearly':
            return self.validate_yearly_rate(ip, rate_value)
        else:
            return True

         

class Slic(socket.socket):
    BUFFER_SIZE = 1024
    logger = Logger("server_logs.log")
    def __init__(self):

        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        #self.logger = Logger("logs/server_logs.log")
        self.resources = HashMap()
        self.network_traffic  = NetworkTrafficMap()
        #self.rate_limiter = RateLimiter(self.network_traffic)
        
    @logger.decorator   
    def start(self,host:str,port:int):
        self.bind((host,port))
        self.listen(5)
        while True:
            conn, addr = self.accept()
            thread = threading.Thread(target=self.handle_conns, args=(conn, addr))
            thread.start()
            self.active_conns(addr,conn)
    @logger.decorator
    def active_conns(self,addr,conn):
        stat = True
        if(self.network_traffic.all.contains(Util.ipkey(addr))):
            self.network_traffic.update_all_request_no()
            stat = False
        if(self.network_traffic.current.contains(Util.ipkey(addr))):
            self.network_traffic.update_current_request_no()
            stat = False
        
        if(stat):
            self.network_traffic.add(addr,conn)

        empty = 0
    @logger.decorator
    def handle_conns(self,conn,addr):

 
        connected = True

        while connected:
            try:
                msg = conn.recv(self.BUFFER_SIZE)
                if msg:
                    buffer = ast.literal_eval(msg.decode('utf-8'))
                    if self.resources.contains(buffer['access']):
                        if (buffer['type'] == 'regular'):

                            self._handle_resource(buffer['access'],buffer['payload'],conn)
                        elif (buffer['type']=='upload'):
                            self._handle_upload_resource(conn,buffer)
                    else:
                        res = {
                            'status':404,
                            'message':'Resource does not exist',
                            'payload':None
                        }
                        conn.send(str(res).encode('utf-8'))
                     
            except ConnectionResetError:
               self.del_conn(conn,addr)
                 
                
                
        conn.close()
         
    
    def link(self,host,port):
        self.connect((host,port))
    @logger.decorator
    def create_resource(self,access:str,resource:object):
        if(self.resources.contains(access)):
            raise Exception("Resource already exists")
        else:
            hashtable = HashMap()
            hashtable.add('access',access)
            hashtable.add('resource',resource)
            hashtable.add('type','regular')
            self.resources.add(access,hashtable)
    @logger.decorator
    def del_conn(self,conn,addr):
        self.network_traffic.remove(addr)
        conn.close

    @logger.decorator
    def _handle_resource(self,access,payload,conn):
        try:
            resource = self.resources.get(access)
        except KeyError as e:
     
            res = {
                'status':404,
                'message':'Resource does not exist',
                'payload':None
            }
            conn.send(str(res).encode('utf-8'))
            return
        else:
            try:

                response =resource.get('resource')(payload)
            except KeyError as e:
     
                res = {
                    'status':400,
                    'message':'Key Error ' + str(e),
                    'payload':None
                }
                conn.send(str(res).encode('utf-8'))
            except Exception as e:
            
                res = {
                    'status':500,
                    'message':'Internal Server Error',
                    'payload':None
                }
                conn.send(str(res).encode('utf-8'))
                
            else:
                res = {
                    'status':200,
                    'message':'OK',
                    'payload':response
                }

                conn.send(str(res).encode('utf-8'))

        #['resource'](payload)
    @logger.decorator
    def _handle_upload_resource(self,conn,buffer):
        self._builtin_upload(f"{self.resources.get(buffer['access']).get('storage')}/{buffer['filename']}",conn)
    @logger.decorator    
    def _builtin_upload(self,path,conn):
        with open(path, "wb") as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
        res = {
        }

        
    def upload_resource(self,access:str,filename:str):
        data = {
            'access':access,
            'filename':filename,
            'type':'upload'
        }
        self.send(str(data).encode('utf-8'))
        with open(filename, "rb") as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.sendall(data)
        pass
    @logger.decorator
    def create_upload_resource(self,access:str,storage:str):
        if(self.resources.contains(access)):
            raise Exception("Resource already exists")
        else:
            hashtable = HashMap()
            hashtable.add('access',access)
            hashtable.add('resource',self._builtin_upload)
            hashtable.add('type','regular')
            hashtable.add('storage',storage)
            self.resources.add(access,hashtable)
            Util.mkdir(storage)



        pass 

    def get_resource(self,access:str,payload):
        data = {
            'access':access,
            'payload':payload,
            'type':'regular'
        }
        
        self.send(str(data).encode('utf-8'))
        
        response =self.recv(self.BUFFER_SIZE).decode('utf-8')


        final = {
            'access':access,


        }
        final['message'] = ast.literal_eval(response)['message']
        final['status'] = ast.literal_eval(response)['status']
        final['payload'] = ast.literal_eval(response)['payload']
        return final
        
    @logger.decorator
    def remove_resource(self,access:str):
        if(self.resources.contains(access)):
            self.resources.remove(access)
        else:
            raise Exception("Resource does not exist")
    @logger.decorator
    def update_resource(self,access:str,resource:object):
        if(self.resources.contains(access)):
            self.resources.update(access,resource)
        else:
            raise Exception("Resource does not exist")
    @logger.decorator
    def clear_resources(self):
        self.resources.clear()


        
        
        

 