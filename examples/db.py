from beardb import Beardb,Bucket

project = Beardb('teddyoweh.net')
project.load_database('app')
views = Bucket(project=project, bucket_name='views')

def add_views(data):
    views.insert(data)

print(views.fetchData())
