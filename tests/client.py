from slicpy import Slic

client = Slic()
client.link('localhost',9999)
a =client.get_resource(':add_views',{
    'name':'amake',
    'who':'keka'
})
a =client.get_resource(':get_views',{
    'a':99
})
b =client.get_resource(':login',{
    'username':'teddy',
    'password':'password'

})
# client.upload_resource(':pyt','README.md')
client.close()
print(a['payload'])