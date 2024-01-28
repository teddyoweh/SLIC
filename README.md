# SLIC - (Swift Low-latency Intercommunication)

SLIC (Swift Low-latency Intercommunication) simplifies client-server communication using tcp / p2p protocols while focusing on latency reduction through low-latency intercommunication techniques. By optimizing network protocols, minimizing data processing overhead, with optimized algorithms for data serialization and deserialization, reducing processing overhead and improving efficiency, while offering built-in capabilities like rate limiting and network traffic management for enhanced network efficiency and seamless data exchange to ensure faster response times, reduced communication delays, and enhanced overall performance in latency-sensitive applications.

## Table of Contents
- [Introduction](./#Introduction)
- [Quick Start](./#quick-start)
- [Features](./#Features)
- [Usage](./#Usage)
- [Examples](./#Examples)


## Introduction
SLIC is designed to simplify client-server communication in Python applications. It enables the creation of resources and handles incoming client requests, allowing for efficient data transfer between the client and server. The library incorporates features such as rate limiting to prevent abuse and network traffic management for tracking and monitoring client connections.

## Quick Start
To quickly get started with SLIC, follow these steps:

1. Install SLIC library:
```sh
$ pip install slicpy
```
2. Import the necessary modules and classes:
```py
from slicpy import Slic, RateLimiter, Rate, NetworkTrafficMap
```

3. Create a server instance and define your resources:
```py
server = Slic()

def my_resource(payload):
    # Handle the client request and return a response
    return {'message': 'Hello, World!'}

server.create_resource(':my_resource', my_resource)

# Add more resources as needed

```

4. Start the server and listen for incoming connections:
```py
server.start('localhost', 9999)
```


5. Create a client instance and connect to the server:
```py
client = Slic()
client.link('localhost', 9999)

```

6. Send a request to the server and receive the response:
```py
response = client.get_resource(':my_resource', {})
print(response['message'])
```

For more detailed information on the SLIC library and its usage, refer to the Usage section.

## Features
SLIC provides the following key features:

- Resource Creation: Create and manage resources on the server for handling specific client requests.
- Request Handling: Handle incoming client requests and execute the associated resource logic.
- Upload Resources: Enable clients to upload files or data to the server.
- Rate Limiting: Apply rate limits to control the number of requests from a client within a given time frame.
- Network Traffic Management: Track and manage client connections and their request counts.

## Usage
The SLIC library can be used to build client-server applications with ease. Below is a more detailed explanation of the library's usage and its main components.

### Resource Creation
To create a resource on the server, use the create_resource method. This method takes two parameters: the access path and the resource function.

Example:

```py
server.create_resource(':my_resource', my_resource_function)
```

### Request Handling
SLIC handles incoming client requests through the handle_conns method. This method is executed in a separate thread for each client connection.

Example:

```py
def handle_conns(conn, addr):
    # Handle the client connection and request here
    pass

    # Inside the Slic class
    thread = threading.Thread(target=handle_conns, args=(conn, addr))
    thread.start()
```
### Upload Resources
SLIC allows clients to upload files or data to the server by creating upload resources using the create_upload_resource method. This method takes two parameters: the access path and the storage location.

server.py
```py
from slicpy import Slic

# Create a SLIC server instance
server = Slic()

# Define an upload resource for handling file uploads
def handle_upload(payload):
    file_content = payload['file'].read()
    # Process the uploaded file content
    return {'success': True}

# Create an upload resource and assign it a unique access key
server.create_upload_resource(':upload', '/path/to/storage')

# Start the server on a specific host and port
server.start('localhost', 9999)

```

client.py
```py
from slicpy import Slic

# Create a SLIC client instance
client = Slic()

# Connect to the SLIC server
client.connect('localhost', 9999)

# Upload a file to the server
with open('path/to/file.txt', 'rb') as file:
    response = client.upload_resource(':upload', 'path/to/file.txt')

print(response)  # {'success': True}

# Close the client connection
client.close()
```

### Example Server

server.py
```py
from slic import Slic

# Create a SLIC server instance
server = Slic()

# Define your resources (functions to handle client requests)
def add(payload):
    return {'answer': payload['a'] + 1}

def login(payload):
    return {'login': True}

# Create resources and assign them unique access keys
server.create_resource(':add', add)
server.create_resource(':login', login)

# Start the server on a specific host and port
server.start('localhost', 9999)
```

### Example Client
To make requests to the SLIC server, you can use the SLIC client:
```py
from slicpy import Slic

# Create a SLIC client instance
client = Slic()

# Connect to the SLIC server
client.connect('localhost', 9999)

# Send a request to the server
response = client.get_resource(':add', {'a': 10})
print(response)  # {'answer': 11}

# Close the client connection
client.close()
```


## Examples
 Example Sources frontend/client and server code are located in [./examples](./examples)
