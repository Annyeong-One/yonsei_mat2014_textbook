# Protocols (TCP/IP, HTTP)

## What is a Protocol?

A **protocol** is a set of rules for communication. Like languages for computers—both sides must follow the same rules to understand each other.

```
Without Protocol:          With Protocol (HTTP):
                          
"gimme page"              GET /page HTTP/1.1
"here stuff"              Host: example.com
                          
   ???                    HTTP/1.1 200 OK
                          Content-Type: text/html
                          <html>...
```

## TCP/IP Protocol Suite

The foundation of internet communication:

```
TCP/IP Layers

┌─────────────────────────────────────────────────┐
│ Application Layer                               │
│   HTTP, FTP, SMTP, DNS, SSH                     │
├─────────────────────────────────────────────────┤
│ Transport Layer                                 │
│   TCP (reliable) / UDP (fast)                   │
├─────────────────────────────────────────────────┤
│ Internet Layer                                  │
│   IP (addressing and routing)                   │
├─────────────────────────────────────────────────┤
│ Network Access Layer                            │
│   Ethernet, WiFi, physical transmission         │
└─────────────────────────────────────────────────┘
```

## IP: Internet Protocol

**IP** handles addressing and routing packets across networks.

### IP Packet Structure

```
IP Packet:
┌──────────────────────────────────────────────────┐
│                   IP Header                      │
│  ┌──────────┬──────────┬────────────────────┐   │
│  │ Version  │  Length  │  Type of Service   │   │
│  ├──────────┴──────────┼────────────────────┤   │
│  │   Source IP Address │  Dest IP Address   │   │
│  └─────────────────────┴────────────────────┘   │
├──────────────────────────────────────────────────┤
│                     Data                         │
│              (TCP/UDP segment)                   │
└──────────────────────────────────────────────────┘
```

### IP Characteristics

- **Connectionless**: Each packet independent
- **Best-effort**: No delivery guarantee
- **Unreliable**: Packets can be lost, duplicated, reordered

## TCP: Transmission Control Protocol

**TCP** provides reliable, ordered delivery over unreliable IP.

### TCP Features

| Feature | Description |
|---------|-------------|
| **Connection-oriented** | Establishes connection before data |
| **Reliable** | Guarantees delivery (retransmits lost) |
| **Ordered** | Data arrives in sequence |
| **Flow control** | Prevents overwhelming receiver |
| **Error checking** | Checksums detect corruption |

### TCP Three-Way Handshake

```
Connection Establishment:

Client                           Server
   │                                │
   │ ──────── SYN ────────────────▶ │  1. Client: "Want to connect"
   │                                │
   │ ◀─────── SYN-ACK ───────────── │  2. Server: "OK, I'm ready"
   │                                │
   │ ──────── ACK ────────────────▶ │  3. Client: "Let's go!"
   │                                │
   │ ════ Connection Established ═══│
```

### TCP Data Transfer

```
Reliable Delivery:

Client                           Server
   │ ──── Data [Seq=1] ──────────▶ │
   │ ◀─── ACK [Ack=2] ───────────  │  "Got it"
   │                                │
   │ ──── Data [Seq=2] ──────────▶ │
   │         (lost!)                │
   │                                │
   │ ...timeout...                  │
   │                                │
   │ ──── Data [Seq=2] ──────────▶ │  Retransmit
   │ ◀─── ACK [Ack=3] ───────────  │
```

### Python TCP Socket

```python
import socket

# TCP Client
def tcp_client(host, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM = TCP
    sock.connect((host, port))
    sock.send(message.encode())
    response = sock.recv(4096)
    sock.close()
    return response.decode()

# TCP Server
def tcp_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    
    while True:
        client, addr = sock.accept()  # Blocks until connection
        data = client.recv(4096)
        client.send(b"Received: " + data)
        client.close()
```

## UDP: User Datagram Protocol

**UDP** provides fast, connectionless communication without guarantees.

### UDP vs TCP

| Aspect | TCP | UDP |
|--------|-----|-----|
| Connection | Required | None |
| Reliability | Guaranteed | Best-effort |
| Order | Preserved | Not guaranteed |
| Speed | Slower (overhead) | Faster |
| Use case | Web, email, files | Streaming, gaming, DNS |

### Python UDP Socket

```python
import socket

# UDP Client
def udp_client(host, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM = UDP
    sock.sendto(message.encode(), (host, port))
    response, addr = sock.recvfrom(4096)
    return response.decode()

# UDP Server
def udp_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    
    while True:
        data, addr = sock.recvfrom(4096)  # No accept needed
        sock.sendto(b"Received: " + data, addr)
```

## HTTP: HyperText Transfer Protocol

**HTTP** is the application protocol for the web.

### HTTP Request

```
GET /api/data?id=123 HTTP/1.1
Host: api.example.com
User-Agent: Python/3.10
Accept: application/json
Authorization: Bearer token123

[optional body for POST/PUT]
```

### HTTP Response

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 42
Date: Mon, 01 Jan 2024 12:00:00 GMT

{"id": 123, "name": "Example", "value": 42}
```

### HTTP Methods

| Method | Purpose | Body |
|--------|---------|------|
| **GET** | Retrieve resource | No |
| **POST** | Create resource | Yes |
| **PUT** | Update resource | Yes |
| **DELETE** | Remove resource | Optional |
| **PATCH** | Partial update | Yes |
| **HEAD** | Get headers only | No |

### HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| **2xx** | Success | 200 OK, 201 Created |
| **3xx** | Redirect | 301 Moved, 304 Not Modified |
| **4xx** | Client Error | 400 Bad Request, 404 Not Found |
| **5xx** | Server Error | 500 Internal, 503 Unavailable |

### Python HTTP Client

```python
import requests

# GET request
response = requests.get('https://api.example.com/data')
print(response.status_code)  # 200
print(response.json())       # {'key': 'value'}

# POST request
response = requests.post(
    'https://api.example.com/create',
    json={'name': 'test'},
    headers={'Authorization': 'Bearer token123'}
)

# Error handling
response = requests.get('https://api.example.com/data')
response.raise_for_status()  # Raises exception for 4xx/5xx
```

### Python HTTP Server

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'ok'}).encode())
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        
        self.send_response(201)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'received': data}).encode())

# server = HTTPServer(('localhost', 8080), SimpleHandler)
# server.serve_forever()
```

## HTTPS: Secure HTTP

**HTTPS** = HTTP + TLS encryption:

```
HTTPS Connection:

Client                           Server
   │                                │
   │ ──── ClientHello ────────────▶ │  Supported ciphers
   │ ◀─── ServerHello ───────────── │  Chosen cipher + certificate
   │                                │
   │   [Certificate validation]     │
   │                                │
   │ ──── Key Exchange ───────────▶ │  Establish shared secret
   │ ◀───────────────────────────── │
   │                                │
   │ ═══ Encrypted HTTP Traffic ═══ │
```

## Protocol Comparison

```
┌─────────────┬─────────────────────────────────────────┐
│  Protocol   │  Characteristics                        │
├─────────────┼─────────────────────────────────────────┤
│  IP         │  Addressing, routing, unreliable        │
│  TCP        │  Reliable, ordered, connection-oriented │
│  UDP        │  Fast, unreliable, connectionless       │
│  HTTP       │  Web requests, text-based, stateless    │
│  HTTPS      │  HTTP + encryption                      │
│  WebSocket  │  Full-duplex, persistent connection     │
└─────────────┴─────────────────────────────────────────┘
```

## Summary

| Protocol | Layer | Purpose |
|----------|-------|---------|
| **IP** | Internet | Addressing and routing |
| **TCP** | Transport | Reliable delivery |
| **UDP** | Transport | Fast, unreliable delivery |
| **HTTP** | Application | Web communication |
| **HTTPS** | Application | Secure web communication |

Key points for Python:

- Use `socket` for TCP/UDP low-level communication
- Use `requests` for HTTP client operations
- Use `flask`/`fastapi` for HTTP servers
- TCP for reliability, UDP for speed
- HTTPS for any sensitive data
- Understand status codes for proper error handling
