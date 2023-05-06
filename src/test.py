from Slic import Slic

client = Slic()
client.link('localhost',9951)
a =client.get_resource(':test',{
    'a':99
})
b =client.get_resource(':login',{
 
    'password':99

})
# client.upload_resource(':pyt','README.md')
client.close()
print(b)