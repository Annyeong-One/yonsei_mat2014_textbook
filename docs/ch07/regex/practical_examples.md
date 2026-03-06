# Practical Examples

## Data Cleaning

### Normalizing Whitespace

```python
import re

raw = "  Hello,\t\tWorld!  \n  Too   many   spaces.  "

# Collapse all whitespace to single space, strip edges
cleaned = re.sub(r'\s+', ' ', raw).strip()
print(cleaned)
# 'Hello, World! Too many spaces.'
```

### Removing Non-ASCII Characters

```python
import re

text = "Café résumé naïve"

# Remove non-ASCII
re.sub(r'[^\x00-\x7F]+', '', text)
# 'Caf rsum nave'

# Keep only alphanumeric and basic punctuation
re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text)
# 'Caf rsum nave'
```

### Cleaning Financial Data

```python
import re

prices = ["\$1,234.56", "€ 2,100.00", "¥10,000", "\$42", "N/A"]

def extract_number(s):
    """Extract numeric value from a price string."""
    cleaned = re.sub(r'[^\d.]', '', s)
    if cleaned:
        return float(cleaned)
    return None

for p in prices:
    print(f"{p:>12} → {extract_number(p)}")
#    \$1,234.56 → 1234.56
#   € 2,100.00 → 2100.0
#      ¥10,000 → 10000.0
#          \$42 → 42.0
#          N/A → None
```

## Validation Patterns

### Email Validation

```python
import re

# Simplified email pattern (covers most common formats)
EMAIL_RE = re.compile(r"""
    ^
    [\w.+-]+          # local part: word chars, dots, plus, hyphen
    @                 # at sign
    [\w-]+            # domain name
    (?:\.[\w-]+)*     # optional subdomains
    \.                # dot before TLD
    [a-zA-Z]{2,}      # TLD (at least 2 letters)
    $
""", re.VERBOSE)

tests = [
    "user@example.com",
    "first.last+tag@sub.domain.co.uk",
    "not-an-email",
    "@missing-local.com",
    "missing-domain@",
    "spaces not@allowed.com",
]

for t in tests:
    valid = "✓" if EMAIL_RE.match(t) else "✗"
    print(f"  {valid} {t}")
#   ✓ user@example.com
#   ✓ first.last+tag@sub.domain.co.uk
#   ✗ not-an-email
#   ✗ @missing-local.com
#   ✗ missing-domain@
#   ✗ spaces not@allowed.com
```

### Date Validation

```python
import re

DATE_RE = re.compile(r"""
    ^
    (?P<year>\d{4})     # year: 4 digits
    [-/]                # separator
    (?P<month>0[1-9]|1[0-2])   # month: 01-12
    [-/]                # separator
    (?P<day>0[1-9]|[12]\d|3[01])  # day: 01-31
    $
""", re.VERBOSE)

tests = ["2024-01-15", "2024/12/31", "2024-13-01", "2024-00-15", "24-01-15"]
for t in tests:
    m = DATE_RE.match(t)
    status = f"✓ {m.groupdict()}" if m else "✗"
    print(f"  {status} ← {t}")
#   ✓ {'year': '2024', 'month': '01', 'day': '15'} ← 2024-01-15
#   ✓ {'year': '2024', 'month': '12', 'day': '31'} ← 2024/12/31
#   ✗ ← 2024-13-01
#   ✗ ← 2024-00-15
#   ✗ ← 24-01-15
```

### IP Address Validation

```python
import re

# Match IPv4 addresses (0.0.0.0 to 255.255.255.255)
IP_RE = re.compile(r"""
    ^
    (?:
        (?:25[0-5]|2[0-4]\d|[01]?\d\d?)   # octet: 0-255
        \.                                   # dot
    ){3}
    (?:25[0-5]|2[0-4]\d|[01]?\d\d?)       # last octet (no trailing dot)
    $
""", re.VERBOSE)

tests = ["192.168.1.1", "255.255.255.255", "0.0.0.0", "256.1.1.1", "1.2.3"]
for t in tests:
    valid = "✓" if IP_RE.match(t) else "✗"
    print(f"  {valid} {t}")
#   ✓ 192.168.1.1
#   ✓ 255.255.255.255
#   ✓ 0.0.0.0
#   ✗ 256.1.1.1
#   ✗ 1.2.3
```

## Log Parsing

### Apache/Nginx Access Log

```python
import re

LOG_RE = re.compile(r"""
    (?P<ip>[\d.]+)              # IP address
    \s+-\s+-\s+                 # identd and user (usually - -)
    \[(?P<date>[^\]]+)\]        # date in brackets
    \s+
    "(?P<method>\w+)            # HTTP method
    \s+(?P<path>\S+)            # request path
    \s+(?P<proto>[^"]+)"        # protocol
    \s+(?P<status>\d{3})        # status code
    \s+(?P<size>\d+|-)          # response size
""", re.VERBOSE)

log_line = '192.168.1.100 - - [15/Jan/2024:10:30:45 +0000] "GET /api/data HTTP/1.1" 200 1234'

match = LOG_RE.match(log_line)
if match:
    info = match.groupdict()
    for k, v in info.items():
        print(f"  {k:>8}: {v}")
#        ip: 192.168.1.100
#      date: 15/Jan/2024:10:30:45 +0000
#    method: GET
#      path: /api/data
#     proto: HTTP/1.1
#    status: 200
#      size: 1234
```

### Python Traceback Extraction

```python
import re

traceback_text = """
Traceback (most recent call last):
  File "main.py", line 42, in process_data
    result = compute(data)
  File "utils.py", line 15, in compute
    return data / 0
ZeroDivisionError: division by zero
"""

# Extract file, line number, and function name
FRAME_RE = re.compile(r'File "(?P<file>[^"]+)", line (?P<line>\d+), in (?P<func>\w+)')

for m in FRAME_RE.finditer(traceback_text):
    print(m.groupdict())
# {'file': 'main.py', 'line': '42', 'func': 'process_data'}
# {'file': 'utils.py', 'line': '15', 'func': 'compute'}

# Extract the exception type and message
exc_match = re.search(r'^(\w+Error): (.+)$', traceback_text, re.M)
if exc_match:
    print(f"Exception: {exc_match.group(1)}")  # ZeroDivisionError
    print(f"Message: {exc_match.group(2)}")     # division by zero
```

## Text Transformation

### Markdown to Plain Text

```python
import re

md = """
# Main Title
This is **bold** and *italic* text.
Here's a [link](https://example.com) and `inline code`.
- List item 1
- List item 2
"""

def md_to_plain(text):
    text = re.sub(r'^#+\s+', '', text, flags=re.M)       # headers
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)         # bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)              # italic
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)      # links
    text = re.sub(r'`(.+?)`', r'\1', text)                # inline code
    text = re.sub(r'^[-*]\s+', '• ', text, flags=re.M)   # list items
    return text.strip()

print(md_to_plain(md))
# Main Title
# This is bold and italic text.
# Here's a link and inline code.
# • List item 1
# • List item 2
```

### CamelCase ↔ snake_case

```python
import re

def camel_to_snake(name):
    """Convert camelCase or PascalCase to snake_case."""
    # Insert underscore before uppercase letters
    s = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', name)
    # Handle consecutive uppercase (e.g., HTTPResponse → http_response)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    return s.lower()

def snake_to_camel(name):
    """Convert snake_case to camelCase."""
    parts = name.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

print(camel_to_snake("myVariableName"))    # my_variable_name
print(camel_to_snake("HTTPResponse"))       # http_response
print(camel_to_snake("getHTTPSUrl"))        # get_https_url

print(snake_to_camel("my_variable_name"))  # myVariableName
print(snake_to_camel("http_response"))      # httpResponse
```

## Financial Data Patterns

### Ticker and Price Extraction

```python
import re

text = """
AAPL closed at \$182.63 (+1.25%)
GOOGL rose to \$141.80 (-0.34%)
MSFT ended at \$378.91 (+0.89%)
"""

STOCK_RE = re.compile(r'(?P<ticker>[A-Z]{1,5})\s+\w+\s+\w+\s+\$(?P<price>[\d.]+)\s+\((?P<change>[+-][\d.]+%)\)')

for m in STOCK_RE.finditer(text):
    d = m.groupdict()
    print(f"  {d['ticker']:>5}: ${d['price']} ({d['change']})")
#    AAPL: \$182.63 (+1.25%)
#   GOOGL: \$141.80 (-0.34%)
#    MSFT: \$378.91 (+0.89%)
```

### CSV Line Parser

```python
import re

def parse_csv_line(line):
    """Parse a CSV line handling quoted fields with commas."""
    pattern = r'(?:"([^"]*(?:""[^"]*)*)"|([^,]*))'
    fields = []
    for quoted, unquoted in re.findall(pattern, line):
        field = quoted.replace('""', '"') if quoted else unquoted
        fields.append(field.strip())
    return [f for f in fields if f or f == '']

line = 'John,"New York, NY",42,"He said ""hi"""'
print(parse_csv_line(line))
# ['John', 'New York, NY', '42', 'He said "hi"']
```

## Common Regex Recipes

| Task | Pattern |
|---|---|
| Integer | `r'[+-]?\d+'` |
| Float | `r'[+-]?\d*\.?\d+'` |
| Scientific notation | `r'[+-]?\d*\.?\d+(?:[eE][+-]?\d+)?'` |
| Hex color | `r'#[0-9a-fA-F]{3,6}\b'` |
| US phone | `r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'` |
| URL | `r'https?://\S+'` |
| Email (simple) | `r'[\w.+-]+@[\w-]+\.[\w.]+'` |
| IP address | `r'\b(?:\d{1,3}\.){3}\d{1,3}\b'` |
| ISO date | `r'\d{4}-\d{2}-\d{2}'` |
| Blank lines | `r'^\s*$'` with `re.M` |
| Duplicate words | `r'\b(\w+)\s+\1\b'` |
| HTML tags | `r'<[^>]+>'` |

!!! tip "Regex Is Not Always the Answer"
    For structured formats like JSON, XML, HTML, or CSV, prefer dedicated parsers (`json`, `xml.etree`, `html.parser`, `csv` modules). Regex is best for semi-structured text, validation, and simple extraction tasks.

## Summary

| Category | Key Takeaway |
|---|---|
| Data cleaning | `re.sub()` for normalization; extract numbers from messy strings |
| Validation | `re.fullmatch()` with verbose patterns for readable validators |
| Log parsing | Named groups + `finditer()` for structured extraction |
| Transformation | Backreferences in `re.sub()` for reordering and reformatting |
| Financial data | Combine named groups with specific numeric patterns |
| When NOT to use | Prefer dedicated parsers for JSON, XML, HTML, CSV |
