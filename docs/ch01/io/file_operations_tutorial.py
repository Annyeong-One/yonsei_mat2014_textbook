"""
PYTHON FILE OPERATIONS - COMPLETE TUTORIAL
===========================================

Learn how to read, write, and manipulate files in Python.
"""

import os
from pathlib import Path

# =============================================================================
# 1. OPENING AND CLOSING FILES (BASIC WAY)
# =============================================================================

print("=" * 60)
print("1. OPENING AND CLOSING FILES")
print("=" * 60)

# Basic way (NOT recommended - might not close file if error occurs)
# file = open('example.txt', 'r')
# content = file.read()
# file.close()

# This approach has problems:
# - If an error occurs, file might not be closed
# - Easy to forget to close the file
# - More verbose

print("Use context managers instead (see next section)!")
print()

# =============================================================================
# 2. CONTEXT MANAGERS (with statement) - RECOMMENDED
# =============================================================================

print("=" * 60)
print("2. CONTEXT MANAGERS - THE RIGHT WAY")
print("=" * 60)

# Create a sample file first
with open('sample.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('This is a sample file.\n')
    f.write('Python file operations are easy!\n')

# Reading with context manager (RECOMMENDED)
with open('sample.txt', 'r') as f:
    content = f.read()
    print(f"File content:\n{content}")

# Benefits of 'with' statement:
# - Automatically closes file when block exits
# - Even if an error occurs, file is closed
# - Cleaner, more readable code
# - Pythonic way to handle files

print("File is automatically closed after 'with' block")
print()

# =============================================================================
# 3. FILE MODES
# =============================================================================

print("=" * 60)
print("3. FILE MODES")
print("=" * 60)

modes_explanation = """
Mode | Description
-----|------------
'r'  | Read (default) - file must exist
'w'  | Write - creates new file or OVERWRITES existing
'a'  | Append - adds to end of file
'x'  | Exclusive creation - fails if file exists
'b'  | Binary mode
't'  | Text mode (default)
'+'  | Read and write

Combinations:
'rb'  | Read binary
'wb'  | Write binary
'r+'  | Read and write
'w+'  | Write and read (overwrites)
'a+'  | Append and read
"""

print(modes_explanation)

# Examples
# Read mode (file must exist)
with open('sample.txt', 'r') as f:
    content = f.read()

# Write mode (overwrites file!)
with open('output.txt', 'w') as f:
    f.write('This will overwrite existing content!\n')

# Append mode (adds to end)
with open('output.txt', 'a') as f:
    f.write('This is appended to the end.\n')

print("Modes demonstrated above")
print()

# =============================================================================
# 4. READING FILES
# =============================================================================

print("=" * 60)
print("4. READING FILES")
print("=" * 60)

# Create sample file
with open('read_demo.txt', 'w') as f:
    f.write('Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n')

# Method 1: read() - reads entire file as string
with open('read_demo.txt', 'r') as f:
    content = f.read()
    print(f"read() - entire file:\n{content}")

# Method 2: read(size) - reads specified number of characters
with open('read_demo.txt', 'r') as f:
    chunk = f.read(10)
    print(f"read(10): '{chunk}'")

# Method 3: readline() - reads one line at a time
with open('read_demo.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"readline() x2:\n{line1}{line2}")

# Method 4: readlines() - reads all lines into a list
with open('read_demo.txt', 'r') as f:
    lines = f.readlines()
    print(f"readlines(): {lines}")

# Method 5: Iterate through file (MOST EFFICIENT)
print("Iterating through file:")
with open('read_demo.txt', 'r') as f:
    for line in f:
        print(f"  {line.strip()}")  # strip() removes \n

print()

# =============================================================================
# 5. WRITING FILES
# =============================================================================

print("=" * 60)
print("5. WRITING FILES")
print("=" * 60)

# Method 1: write() - writes a string
with open('write_demo.txt', 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')
    # Returns number of characters written
    chars_written = f.write('Third line\n')
    print(f"Wrote {chars_written} characters")

# Method 2: writelines() - writes a list of strings
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('write_demo2.txt', 'w') as f:
    f.writelines(lines)

# Method 3: print() to file
with open('write_demo3.txt', 'w') as f:
    print('Using print function', file=f)
    print('This is line 2', file=f)

# Appending to file
with open('write_demo.txt', 'a') as f:
    f.write('This is appended\n')

print("Files written successfully")
print()

# =============================================================================
# 6. WORKING WITH PATHS (pathlib)
# =============================================================================

print("=" * 60)
print("6. WORKING WITH PATHS (pathlib - RECOMMENDED)")
print("=" * 60)

# pathlib provides object-oriented way to work with paths
from pathlib import Path

# Create path objects
current_file = Path('sample.txt')
nested_path = Path('data') / 'files' / 'example.txt'

print(f"Current file: {current_file}")
print(f"Nested path: {nested_path}")

# Path properties
print(f"\nPath properties:")
print(f"  Name: {current_file.name}")
print(f"  Suffix: {current_file.suffix}")
print(f"  Stem: {current_file.stem}")
print(f"  Parent: {current_file.parent}")
print(f"  Absolute: {current_file.absolute()}")

# Check existence
print(f"\nExists? {current_file.exists()}")
print(f"Is file? {current_file.is_file()}")
print(f"Is directory? {current_file.is_dir()}")

# Reading/writing with Path
content = current_file.read_text()
print(f"\nFile content (first 50 chars): {content[:50]}")

# Write using Path
output = Path('path_demo.txt')
output.write_text('Written using Path.write_text()\n')

print()

# =============================================================================
# 7. DIRECTORY OPERATIONS
# =============================================================================

print("=" * 60)
print("7. DIRECTORY OPERATIONS")
print("=" * 60)

from pathlib import Path

# Create directory
demo_dir = Path('demo_folder')
demo_dir.mkdir(exist_ok=True)  # exist_ok=True prevents error if exists
print(f"Created directory: {demo_dir}")

# Create nested directories
nested_dir = Path('demo_folder/sub1/sub2')
nested_dir.mkdir(parents=True, exist_ok=True)
print(f"Created nested: {nested_dir}")

# List directory contents
print(f"\nContents of current directory:")
for item in Path('.').iterdir():
    if item.is_file():
        print(f"  [FILE] {item.name}")
    elif item.is_dir():
        print(f"  [DIR]  {item.name}")

# Glob patterns (find files matching pattern)
txt_files = list(Path('.').glob('*.txt'))
print(f"\nAll .txt files: {[f.name for f in txt_files]}")

# Recursive glob
all_txt = list(Path('.').rglob('*.txt'))  # Searches subdirectories too
print(f"All .txt (recursive): {len(all_txt)} files")

# Get current working directory
cwd = Path.cwd()
print(f"\nCurrent directory: {cwd}")

print()

# =============================================================================
# 8. CSV FILES
# =============================================================================

print("=" * 60)
print("8. CSV FILES")
print("=" * 60)

import csv

# Writing CSV
csv_data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
print("CSV file created")

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    print("\nReading CSV:")
    for row in reader:
        print(f"  {row}")

# Using DictReader (more convenient)
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("\nReading with DictReader:")
    for row in reader:
        print(f"  {row['Name']} is {row['Age']} years old")

# Writing with DictWriter
data = [
    {'name': 'Diana', 'age': 28, 'city': 'Boston'},
    {'name': 'Eve', 'age': 32, 'city': 'Seattle'}
]

with open('data2.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
print("CSV with headers created")

print()

# =============================================================================
# 9. JSON FILES
# =============================================================================

print("=" * 60)
print("9. JSON FILES")
print("=" * 60)

import json

# Python data to JSON
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'coding', 'gaming'],
    'active': True
}

# Writing JSON
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
print("JSON file created")

# Reading JSON
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(f"\nLoaded JSON: {loaded_data}")
    print(f"Name: {loaded_data['name']}")
    print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")

# JSON to string and back
json_string = json.dumps(data, indent=2)
print(f"\nJSON as string:\n{json_string}")

parsed = json.loads(json_string)
print(f"Parsed from string: {parsed['name']}")

# Pretty printing JSON
print("\nPretty JSON:")
print(json.dumps(data, indent=2, sort_keys=True))

print()

# =============================================================================
# 10. BINARY FILES
# =============================================================================

print("=" * 60)
print("10. BINARY FILES")
print("=" * 60)

# Writing binary data
binary_data = b'Hello in binary!\x00\x01\x02'
with open('binary.bin', 'wb') as f:
    f.write(binary_data)
print("Binary file written")

# Reading binary data
with open('binary.bin', 'rb') as f:
    data = f.read()
    print(f"Binary data: {data}")
    print(f"As hex: {data.hex()}")

# Working with bytes
text = "Hello, World!"
encoded = text.encode('utf-8')  # String to bytes
print(f"\nEncoded: {encoded}")

decoded = encoded.decode('utf-8')  # Bytes to string
print(f"Decoded: {decoded}")

print()

# =============================================================================
# 11. ERROR HANDLING
# =============================================================================

print("=" * 60)
print("11. ERROR HANDLING")
print("=" * 60)

# File not found
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found!")

# Permission error
try:
    with open('/root/protected.txt', 'w') as f:
        f.write('test')
except PermissionError:
    print("Error: Permission denied!")

# General error handling
try:
    with open('sample.txt', 'r') as f:
        content = f.read()
        print("File read successfully")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Cleanup code (always runs)")

print()

# =============================================================================
# 12. FILE INFORMATION
# =============================================================================

print("=" * 60)
print("12. FILE INFORMATION")
print("=" * 60)

import os
from pathlib import Path
from datetime import datetime

file_path = Path('sample.txt')

if file_path.exists():
    # Using pathlib
    stats = file_path.stat()
    
    print(f"File: {file_path.name}")
    print(f"Size: {stats.st_size} bytes")
    print(f"Created: {datetime.fromtimestamp(stats.st_ctime)}")
    print(f"Modified: {datetime.fromtimestamp(stats.st_mtime)}")
    print(f"Accessed: {datetime.fromtimestamp(stats.st_atime)}")
    
    # Using os module (older way)
    print(f"\nUsing os.path:")
    print(f"Absolute path: {os.path.abspath('sample.txt')}")
    print(f"Size: {os.path.getsize('sample.txt')} bytes")
    print(f"Is file: {os.path.isfile('sample.txt')}")

print()

# =============================================================================
# 13. COMMON PATTERNS AND BEST PRACTICES
# =============================================================================

print("=" * 60)
print("13. COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Read file line by line (memory efficient)
def process_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            # Process line
            pass

# Pattern 2: Read file if exists, else create
def read_or_create(filename):
    path = Path(filename)
    if path.exists():
        return path.read_text()
    else:
        path.write_text('Default content')
        return 'Default content'

# Pattern 3: Atomic write (write to temp, then rename)
def atomic_write(filename, content):
    temp_file = Path(f"{filename}.tmp")
    temp_file.write_text(content)
    temp_file.replace(filename)

# Pattern 4: Backup before overwrite
def safe_write(filename, content):
    path = Path(filename)
    if path.exists():
        backup = Path(f"{filename}.bak")
        path.replace(backup)
    path.write_text(content)

# Pattern 5: Process CSV without loading all into memory
def process_csv_streaming(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Process row
            pass

print("Common patterns defined above")
print()

# =============================================================================
# 14. ENCODING
# =============================================================================

print("=" * 60)
print("14. ENCODING")
print("=" * 60)

# Always specify encoding for text files!
with open('utf8.txt', 'w', encoding='utf-8') as f:
    f.write('Hello 世界 🌍\n')  # Unicode characters

# Reading with encoding
with open('utf8.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"UTF-8 content: {content}")

# Different encodings
encodings = ['utf-8', 'ascii', 'latin-1']
for encoding in encodings:
    try:
        with open('utf8.txt', 'r', encoding=encoding) as f:
            content = f.read()
            print(f"{encoding}: Success")
    except UnicodeDecodeError:
        print(f"{encoding}: Failed to decode")

print()

# =============================================================================
# 15. TEMPORARY FILES
# =============================================================================

print("=" * 60)
print("15. TEMPORARY FILES")
print("=" * 60)

import tempfile

# Create temporary file
with tempfile.TemporaryFile(mode='w+') as f:
    f.write('Temporary data')
    f.seek(0)
    content = f.read()
    print(f"Temp file content: {content}")
# File automatically deleted when closed

# Named temporary file
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
    f.write('Named temp file')
    temp_name = f.name
    print(f"Temp file name: {temp_name}")

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temp directory: {temp_dir}")
    # Use temp directory
# Directory automatically deleted

print()

# =============================================================================
# SUMMARY
# =============================================================================

print("=" * 60)
print("FILE OPERATIONS SUMMARY")
print("=" * 60)

summary = """
ALWAYS USE:
✓ Context managers (with statement)
✓ pathlib for path operations
✓ Specify encoding for text files
✓ Handle exceptions properly

FILE MODES:
  'r'  - Read (default)
  'w'  - Write (overwrites!)
  'a'  - Append
  'x'  - Exclusive creation

READING:
  read()      - Entire file
  readline()  - One line
  readlines() - All lines as list
  for line    - Iterate (best for large files)

WRITING:
  write(str)       - Write string
  writelines(list) - Write list of strings
  print(..., file=f) - Use print

CSV:
  csv.reader / csv.writer
  csv.DictReader / csv.DictWriter

JSON:
  json.load / json.dump
  json.loads / json.dumps

PATHS (pathlib):
  Path('file.txt')
  .exists() .is_file() .is_dir()
  .read_text() .write_text()
  .mkdir() .iterdir() .glob()
"""

print(summary)
print("=" * 60)
print("TUTORIAL COMPLETE!")
print("=" * 60)
