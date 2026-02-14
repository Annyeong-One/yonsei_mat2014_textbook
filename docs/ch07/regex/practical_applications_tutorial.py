"""
Python Regular Expressions - Tutorial 07: Practical Applications
================================================================

This tutorial demonstrates real-world applications of regex patterns.

DIFFICULTY: ADVANCED
"""

import re

print("="*70)
print("REAL-WORLD REGEX PATTERNS")
print("="*70)

# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = ["user@example.com", "invalid@", "test@test.co.uk"]
print("\nEmail Validation:")
for email in emails:
    valid = bool(re.match(email_pattern, email))
    print(f"  {'✓' if valid else '✗'} {email}")

# URL validation
url_pattern = r"^https?://(?:www\.)?[\w.-]+\.\w+(?:/[\w./?%&=-]*)?$"
urls = ["https://example.com", "http://www.test.org/page", "invalid"]
print("\nURL Validation:")
for url in urls:
    valid = bool(re.match(url_pattern, url))
    print(f"  {'✓' if valid else '✗'} {url}")

# Phone number formatting
phone_text = "Call 5551234567 or 8005551234"
phone_pattern = r"(\d{3})(\d{3})(\d{4})"
formatted = re.sub(phone_pattern, r"() -", phone_text)
print(f"\nPhone Formatting:\n  Before: {phone_text}\n  After: {formatted}")

# Extract all links from HTML
html = '<a href="http://example.com">Link</a> <a href="http://test.org">Test</a>'
link_pattern = r'href="(https?://[^"]+)"'
links = re.findall(link_pattern, html)
print(f"\nExtracted Links: {links}")

# Data extraction from logs
log = "2024-03-15 14:30:45 ERROR Connection failed"
log_pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
match = re.search(log_pattern, log)
if match:
    print(f"\nLog Parsing:")
    print(f"  Date: {match.group(1)}")
    print(f"  Time: {match.group(2)}")
    print(f"  Level: {match.group(3)}")
    print(f"  Message: {match.group(4)}")

# Text cleaning
text = "Hello!!!  How are   you???  "
cleaned = re.sub(r'\s+', ' ', text).strip()
cleaned = re.sub(r'([!?]){2,}', r'', cleaned)
print(f"\nText Cleaning:\n  Before: '{text}'\n  After: '{cleaned}'")

# IP address validation
ip_pattern = r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
ips = ["192.168.1.1", "256.1.1.1", "10.0.0.1"]
print("\nIP Address Validation:")
for ip in ips:
    valid = bool(re.match(ip_pattern, ip))
    print(f"  {'✓' if valid else '✗'} {ip}")

print("\n" + "="*70)
print("END OF TUTORIAL - All concepts completed!")
print("="*70)
