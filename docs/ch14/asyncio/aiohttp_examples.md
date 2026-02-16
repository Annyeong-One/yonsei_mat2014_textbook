# Async HTTP with aiohttp

`aiohttp` is the standard library for async HTTP in Python, supporting both client and server functionality.

## Installation

```bash
pip install aiohttp
```

## Basic Client Usage

### Simple GET Request

```python
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Status: {response.status}")
            return await response.text()

async def main():
    html = await fetch("https://example.com")
    print(html[:200])

asyncio.run(main())
```

### Session Best Practices

```python
# WRONG: Creating session per request (slow)
async def fetch_bad(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# CORRECT: Reuse session for multiple requests
async def fetch_many(urls):
    async with aiohttp.ClientSession() as session:
        results = []
        for url in urls:
            async with session.get(url) as response:
                results.append(await response.text())
        return results

# BEST: Pass session as parameter
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://example.com"] * 10
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
```

## Request Methods

```python
async def http_methods_example():
    async with aiohttp.ClientSession() as session:
        # GET
        async with session.get('https://api.example.com/items') as r:
            data = await r.json()
        
        # POST
        async with session.post('https://api.example.com/items', 
                                json={'name': 'item'}) as r:
            result = await r.json()
        
        # PUT
        async with session.put('https://api.example.com/items/1',
                               json={'name': 'updated'}) as r:
            result = await r.json()
        
        # DELETE
        async with session.delete('https://api.example.com/items/1') as r:
            print(r.status)
        
        # PATCH
        async with session.patch('https://api.example.com/items/1',
                                 json={'name': 'patched'}) as r:
            result = await r.json()
```

## Request Parameters

### Query Parameters

```python
async def with_params():
    async with aiohttp.ClientSession() as session:
        params = {'key': 'value', 'page': 1}
        async with session.get('https://api.example.com/search', 
                               params=params) as r:
            # URL becomes: https://api.example.com/search?key=value&page=1
            return await r.json()
```

### Headers

```python
async def with_headers():
    async with aiohttp.ClientSession() as session:
        headers = {
            'Authorization': 'Bearer token123',
            'Accept': 'application/json'
        }
        async with session.get('https://api.example.com', 
                               headers=headers) as r:
            return await r.json()

# Or set default headers for session
async def with_default_headers():
    headers = {'Authorization': 'Bearer token123'}
    async with aiohttp.ClientSession(headers=headers) as session:
        # All requests use these headers
        async with session.get('https://api.example.com') as r:
            return await r.json()
```

### POST Data

```python
async def post_data():
    async with aiohttp.ClientSession() as session:
        # JSON data
        async with session.post('https://api.example.com',
                                json={'key': 'value'}) as r:
            return await r.json()
        
        # Form data
        async with session.post('https://api.example.com',
                                data={'key': 'value'}) as r:
            return await r.text()
        
        # Form data with file
        data = aiohttp.FormData()
        data.add_field('file', open('file.txt', 'rb'),
                       filename='file.txt',
                       content_type='text/plain')
        async with session.post('https://api.example.com/upload',
                                data=data) as r:
            return await r.json()
```

## Response Handling

```python
async def handle_response():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com') as r:
            # Status
            print(r.status)        # 200
            print(r.reason)        # 'OK'
            
            # Headers
            print(r.headers)
            print(r.headers['Content-Type'])
            
            # URL (after redirects)
            print(r.url)
            
            # Response body
            text = await r.text()          # As string
            data = await r.json()          # As JSON
            binary = await r.read()        # As bytes
            
            # Streaming
            async for chunk in r.content.iter_chunked(1024):
                process_chunk(chunk)
```

## Timeouts

```python
async def with_timeout():
    # Per-request timeout
    timeout = aiohttp.ClientTimeout(total=30)
    
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.get('https://slow-api.example.com') as r:
                return await r.json()
        except asyncio.TimeoutError:
            print("Request timed out")

# More granular timeouts
timeout = aiohttp.ClientTimeout(
    total=60,        # Total timeout
    connect=10,      # Connection timeout
    sock_read=30,    # Read timeout
    sock_connect=10  # Socket connect timeout
)
```

## Error Handling

```python
async def safe_fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise on 4xx/5xx
                return await response.json()
                
        except aiohttp.ClientConnectionError:
            print("Connection failed")
        except aiohttp.ClientResponseError as e:
            print(f"HTTP error: {e.status}")
        except aiohttp.ClientError as e:
            print(f"Client error: {e}")
        except asyncio.TimeoutError:
            print("Request timed out")
```

## Concurrent Requests

### Using gather()

```python
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        async def fetch_one(url):
            async with session.get(url) as r:
                return await r.json()
        
        tasks = [fetch_one(url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)

async def main():
    urls = [f"https://api.example.com/item/{i}" for i in range(100)]
    results = await fetch_all(urls)
```

### Rate Limiting with Semaphore

```python
async def fetch_with_rate_limit(urls, max_concurrent=10):
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def fetch_one(session, url):
        async with semaphore:
            async with session.get(url) as r:
                return await r.json()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

### With Retry Logic

```python
async def fetch_with_retry(session, url, max_retries=3, backoff=1.0):
    for attempt in range(max_retries):
        try:
            async with session.get(url) as r:
                r.raise_for_status()
                return await r.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            if attempt == max_retries - 1:
                raise
            
            wait = backoff * (2 ** attempt)
            print(f"Retry {attempt + 1} in {wait}s: {e}")
            await asyncio.sleep(wait)
```

## Practical Examples

### 1. API Client Class

```python
class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        return self
    
    async def __aexit__(self, *args):
        await self.session.close()
    
    async def get(self, endpoint, **params):
        url = f"{self.base_url}/{endpoint}"
        async with self.session.get(url, params=params) as r:
            r.raise_for_status()
            return await r.json()
    
    async def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        async with self.session.post(url, json=data) as r:
            r.raise_for_status()
            return await r.json()

# Usage
async def main():
    async with APIClient("https://api.example.com", "secret") as client:
        users = await client.get("users", page=1)
        new_user = await client.post("users", {"name": "Alice"})
```

### 2. Parallel API Fetcher

```python
async def parallel_api_fetch(endpoints, base_url, max_concurrent=5):
    semaphore = asyncio.Semaphore(max_concurrent)
    results = {}
    
    async def fetch_endpoint(session, endpoint):
        async with semaphore:
            try:
                async with session.get(f"{base_url}/{endpoint}") as r:
                    results[endpoint] = await r.json()
            except Exception as e:
                results[endpoint] = {"error": str(e)}
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_endpoint(session, ep) for ep in endpoints]
        await asyncio.gather(*tasks)
    
    return results

# Usage
async def main():
    endpoints = ["users", "posts", "comments", "todos"]
    data = await parallel_api_fetch(endpoints, "https://jsonplaceholder.typicode.com")
    print(data)
```

### 3. Streaming Download

```python
async def download_file(url, filepath, chunk_size=8192):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(filepath, 'wb') as f:
                async for chunk in response.content.iter_chunked(chunk_size):
                    f.write(chunk)

# With progress
async def download_with_progress(url, filepath):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            total = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(filepath, 'wb') as f:
                async for chunk in response.content.iter_chunked(8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress = (downloaded / total * 100) if total else 0
                    print(f"\rProgress: {progress:.1f}%", end='')
```

### 4. WebSocket Client

```python
async def websocket_client():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('wss://echo.websocket.org') as ws:
            # Send message
            await ws.send_str('Hello!')
            
            # Receive messages
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(f"Received: {msg.data}")
                    if msg.data == 'close':
                        await ws.close()
                        break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break
```

## Connection Pooling

```python
# Configure connector for connection pooling
connector = aiohttp.TCPConnector(
    limit=100,           # Total connection limit
    limit_per_host=10,   # Per-host limit
    ttl_dns_cache=300,   # DNS cache TTL
    keepalive_timeout=30 # Keep-alive timeout
)

async with aiohttp.ClientSession(connector=connector) as session:
    # All requests share the connection pool
    pass
```

## Key Takeaways

- Always use `async with` for sessions and responses
- Reuse sessions across multiple requests
- Use semaphores for rate limiting
- Implement retry logic for reliability
- Handle timeouts and errors gracefully
- Use connection pooling for high-throughput applications
- Stream large responses with `iter_chunked()`
