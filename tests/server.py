from slicpy import Slic
from beardb import Beardb,Bucket


server = Slic()

project = Beardb('teddyoweh.net')
project.load_database('app')
views = Bucket(project=project, bucket_name='views')
contact = Bucket(project=project,bucket_name='contact')

def add_contact(data):
    contact.insert(data)
    return 'Inserted'

def get_contact(payload):
    return contact.fetchData()

def get_contact_query(payload):
    return contact.fetchData(payload)

def add_views(data):
    views.insert(data)
    return 'Inserted'

def get_views(payload):
    return views.fetchData()

def get_views_query(payload):
    return views.fetchData(payload)


server.create_resource(':add_views',add_views)
server.create_resource(':get_views',get_views)
server.create_resource(':get_views_query',get_views_query)
server.create_resource(':add_contact',add_contact)
server.create_resource(':get_contact',get_contact)
server.create_resource(':get_contact_query',get_contact_query)
server.start('localhost',9999)