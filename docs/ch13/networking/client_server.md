# Client-Server Model

## What is Client-Server?

The **client-server model** divides computing between service requesters (clients) and service providers (servers):

```
Client-Server Architecture

┌──────────┐                         ┌──────────┐
│  Client  │ ──── Request ─────────▶ │  Server  │
│          │                         │          │
│ (browser)│ ◀─── Response ───────── │ (web app)│
└──────────┘                         └──────────┘

Client: Initiates requests, displays results
Server: Waits for requests, processes, responds
```

## Characteristics

### Client

- Initiates communication
- Sends requests
- Waits for responses
- Usually many clients per server
- Examples: web browser, mobile app, API client

### Server

- Listens for connections
- Processes requests
- Returns responses
- Serves many clients simultaneously
- Examples: web server, database, API endpoint

## Request-Response Cycle

```
1. Client establishes connection
   ┌────────┐                    ┌────────┐
   │ Client │ ═══ Connect ═════▶ │ Server │
   └────────┘                    └────────┘

2. Client sends request
   ┌────────┐                    ┌────────┐
   │ Client │ ──── Request ────▶ │ Server │
   │        │    (GET /page)     │        │
   └────────┘                    └────────┘

3. Server processes request
   ┌────────┐                    ┌────────┐
   │ Client │                    │ Server │
   │(waiting)                    │[Process]│
   └────────┘                    └────────┘

4. Server sends response
   ┌────────┐                    ┌────────┐
   │ Client │ ◀─── Response ──── │ Server │
   │        │   (HTML content)   │        │
   └────────┘                    └────────┘

5. Connection closes (or stays open for more)
```

## Python Client Example

```python
import socket

def simple_client(host, port, message):
    """Send a message to server and get response."""
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        # Send data
        client_socket.send(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Receive response
        response = client_socket.recv(4096).decode('utf-8')
        print(f"Received: {response}")
        
        return response
    finally:
        client_socket.close()

# Usage
# simple_client('localhost', 8080, 'Hello, Server!')
```

## Python Server Example

```python
import socket

def simple_server(host, port):
    """Simple echo server."""
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to address
    server_socket.bind((host, port))
    
    # Listen for connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        try:
            # Receive data
            data = client_socket.recv(4096).decode('utf-8')
            print(f"Received: {data}")
            
            # Process and respond (echo with modification)
            response = f"Server received: {data}"
            client_socket.send(response.encode('utf-8'))
        finally:
            client_socket.close()

# Usage
# simple_server('localhost', 8080)
```

## Handling Multiple Clients

### Sequential (Blocking)

```python
# One client at a time - doesn't scale!
while True:
    client = server.accept()
    handle_client(client)  # Blocks until complete
```

### Threading

```python
import socket
import threading

def handle_client(client_socket, address):
    """Handle a single client in its own thread."""
    try:
        data = client_socket.recv(4096)
        response = process(data)
        client_socket.send(response)
    finally:
        client_socket.close()

def threaded_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(100)
    
    while True:
        client, address = server.accept()
        # Handle each client in separate thread
        thread = threading.Thread(target=handle_client, 
                                  args=(client, address))
        thread.start()
```

### Async I/O

```python
import asyncio

async def handle_client(reader, writer):
    """Handle client with async I/O."""
    data = await reader.read(4096)
    message = data.decode()
    
    response = f"Received: {message}"
    writer.write(response.encode())
    await writer.drain()
    
    writer.close()
    await writer.wait_closed()

async def async_server(host, port):
    server = await asyncio.start_server(
        handle_client, host, port
    )
    
    async with server:
        await server.serve_forever()

# asyncio.run(async_server('localhost', 8080))
```

## Common Client-Server Patterns

### Web Server (HTTP)

```
Browser                              Web Server
   │                                      │
   │──── GET /index.html ───────────────▶│
   │                                      │
   │◀──── 200 OK + HTML ──────────────────│
   │                                      │
```

### Database

```
Application                          Database
   │                                      │
   │──── SELECT * FROM users ───────────▶│
   │                                      │
   │◀──── [user1, user2, ...] ────────────│
   │                                      │
```

### API Server

```
Client App                           API Server
   │                                      │
   │──── POST /api/process ─────────────▶│
   │     {"data": [...]}                  │
   │                                      │
   │◀──── {"result": "done"} ─────────────│
   │                                      │
```

## Stateless vs Stateful

### Stateless

Server doesn't remember previous requests:

```python
# Stateless: each request is independent
@app.route('/add')
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))

# Client must send all info every time
# GET /add?a=5&b=3 → 8
```

### Stateful

Server maintains state between requests:

```python
# Stateful: server remembers session
sessions = {}

@app.route('/login')
def login():
    session_id = create_session(request.user)
    sessions[session_id] = {'user': request.user}
    return session_id

@app.route('/profile')
def profile():
    session_id = request.cookies.get('session')
    user_data = sessions.get(session_id)  # Retrieved from memory
    return user_data
```

## Load Balancing

Distributing requests across multiple servers:

```
                    ┌────────────────┐
                    │ Load Balancer  │
                    └───────┬────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
    ┌──────────┐      ┌──────────┐      ┌──────────┐
    │ Server 1 │      │ Server 2 │      │ Server 3 │
    └──────────┘      └──────────┘      └──────────┘

Strategies:
  - Round Robin: Rotate through servers
  - Least Connections: Send to least busy
  - IP Hash: Same client → same server
```

## Using HTTP Libraries

### Client with Requests

```python
import requests

# Simple GET
response = requests.get('https://api.example.com/data')
data = response.json()

# POST with data
response = requests.post(
    'https://api.example.com/process',
    json={'input': [1, 2, 3]}
)
result = response.json()
```

### Server with Flask

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    result = sum(data['input'])
    return jsonify({'result': result})

# app.run(host='0.0.0.0', port=5000)
```

## Summary

| Concept | Description |
|---------|-------------|
| **Client** | Initiates requests, consumes services |
| **Server** | Listens, processes, responds |
| **Request** | Client message to server |
| **Response** | Server reply to client |
| **Stateless** | No memory between requests |
| **Stateful** | Server maintains session state |
| **Load Balancing** | Distributing load across servers |

Key points:

- Client-server is the foundation of web and distributed systems
- Servers must handle concurrent clients (threading, async)
- HTTP is the dominant client-server protocol for web
- Stateless designs scale better
- Python's `socket` for low-level, `requests`/`flask` for HTTP
