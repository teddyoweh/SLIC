from .util import Util
from .HashMap import HashMap
class NetworkTrafficMap(object):
    def __init__(self):
        self.all = HashMap()
        self.current = HashMap()
        

    @property
    def requests_no_all(self):
        return self.all.size
    @property
    def requests_no_current(self):
        return self.current.size
    def add(self, addr,conn):
        ip = Util.ipkey(addr)

        data = {
            'key':ip,
            'ip':addr[0],
            'port':addr[1],
            'requests':0,
            'addr':addr,
            'conn':conn,
            'date':Util.timestamp(),

        }
        self.all.add(ip, data)
        self.current.add(ip, data)
    def remove(self,addr):
        ip = Util.ipkey(addr)
        self.current.remove(ip)
    def update_all_request_no(self,addr):
        ip = Util.ipkey(addr)
        self.all.get(ip)['requests'] += 1
    def update_current_request_no(self,addr):
        ip = Util.ipkey(addr)
        self.current.get(ip)['requests'] += 1
    
