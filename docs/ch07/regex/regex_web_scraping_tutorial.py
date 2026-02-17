"""
Topic 7.10 - Regex for Web Scraping and Data Extraction Tutorial

Real-world regex patterns for extracting structured data from
semi-structured web content (HTML, JSON-in-HTML, API responses).

When APIs aren't available, web scraping often requires parsing raw HTML
or embedded JSON to extract the data you need. Regex is the tool for this:
find patterns in messy text and pull out clean, structured fields.

This tutorial builds a complete pipeline:
  raw text → regex extraction → deduplication → pandas DataFrame → CSV

Inspired by a Starbucks store location scraper that parses store data
(ID, name, latitude, longitude, city, state, zip) from web responses.

Learning Objectives:
- Writing multi-group regex patterns for structured data extraction
- Extracting repeated records from large text blocks
- Non-greedy matching (.*?) to avoid over-matching
- Named groups for readability
- Deduplication patterns for scraped data
- Building DataFrames from extracted data
- Combining regex with pandas for data pipelines

Prerequisites:
- ch07/regex (regex basics, groups, quantifiers)
- ch10/core (pandas DataFrame basics)
- ch15/networking (HTTP requests, web scraping)

Author: Python Educator
Date: 2024
"""

import re
import csv
import json
from typing import Any


# ============================================================================
# PART 1: BEGINNER - Extracting Fields from Structured Text
# ============================================================================

def demonstrate_basic_field_extraction():
    """
    Extract key-value pairs from semi-structured text using regex groups.

    Web APIs and HTML pages often embed data in predictable formats.
    Regex groups let you extract specific fields from these patterns.
    """
    print("=" * 70)
    print("BEGINNER: Extracting Fields from Structured Text")
    print("=" * 70)

    # --- Extracting from JSON-like text ---
    print("\n1. Extracting from JSON-like text in HTML")
    print("-" * 50)

    # Simulate text embedded in a web page (common in store locators)
    html_fragment = '''
    <script>var storeData = {"storeNumber":"12345","name":"Downtown Plaza",
    "coordinates":{"latitude":34.0522,"longitude":-118.2437},
    "address":{"city":"Los Angeles","state":"CA","postalCode":"90012"}};
    </script>
    '''

    # Extract store number
    store_num = re.search(r'"storeNumber":"(\d+)"', html_fragment)
    if store_num:
        print(f"   Store number: {store_num.group(1)}")

    # Extract store name
    store_name = re.search(r'"name":"([^"]+)"', html_fragment)
    if store_name:
        print(f"   Store name  : {store_name.group(1)}")

    # Extract latitude and longitude
    lat = re.search(r'"latitude":([-\d.]+)', html_fragment)
    lon = re.search(r'"longitude":([-\d.]+)', html_fragment)
    if lat and lon:
        print(f"   Latitude    : {lat.group(1)}")
        print(f"   Longitude   : {lon.group(1)}")

    # Extract city
    city = re.search(r'"city":"([^"]+)"', html_fragment)
    if city:
        print(f"   City        : {city.group(1)}")

    # --- Non-greedy vs greedy matching ---
    print(f"\n2. Non-greedy matching: .*? vs .*")
    print("-" * 50)

    text = '"name":"First Store","other":"data","name":"Second Store"'

    # Greedy: .* grabs as much as possible
    greedy = re.search(r'"name":"(.*)"', text)
    print(f"   Greedy  .*  : {greedy.group(1) if greedy else 'None'}")
    # Gets: First Store","other":"data","name":"Second Store

    # Non-greedy: .*? grabs as little as possible
    nongreedy = re.search(r'"name":"(.*?)"', text)
    print(f"   Non-greedy .*? : {nongreedy.group(1) if nongreedy else 'None'}")
    # Gets: First Store

    print("\n   Key insight: Use .*? when extracting from quoted values")
    print("   to stop at the FIRST closing quote, not the last one.")

    # --- Named groups for readability ---
    print(f"\n3. Named groups (?P<name>...) for readability")
    print("-" * 50)

    log_line = '2024-03-15 14:30:45 [ERROR] Server: Connection refused (port 5432)'

    pattern = (
        r'(?P<date>\d{4}-\d{2}-\d{2}) '
        r'(?P<time>\d{2}:\d{2}:\d{2}) '
        r'\[(?P<level>\w+)\] '
        r'(?P<source>\w+): '
        r'(?P<message>.+)'
    )

    match = re.search(pattern, log_line)
    if match:
        print(f"   date    = {match.group('date')}")
        print(f"   time    = {match.group('time')}")
        print(f"   level   = {match.group('level')}")
        print(f"   source  = {match.group('source')}")
        print(f"   message = {match.group('message')}")
        print(f"\n   As dict: {match.groupdict()}")

    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 2: INTERMEDIATE - Multi-Record Extraction from Web Content
# ============================================================================

def demonstrate_multi_record_extraction():
    """
    Extract multiple records from a block of text using regex.

    Web pages often contain many similar data records (store listings,
    product cards, search results). The strategy:
    1. Use re.findall() or re.finditer() to find all record boundaries
    2. Extract fields from each record with groups
    """
    print("=" * 70)
    print("INTERMEDIATE: Extracting Multiple Records")
    print("=" * 70)

    # Simulate a web response with multiple store records
    # This mimics what a store locator API might return embedded in HTML
    response_text = '''
    {"stores":[
        {"storeNumber":"10234","name":"Main St & 5th","coordinates":
         {"latitude":34.0522,"longitude":-118.2437},"address":
         {"city":"Los Angeles","countrySubdivisionCode":"CA","postalCode":"90012"},"slug":"main-st"},
        {"storeNumber":"10567","name":"Hollywood & Vine","coordinates":
         {"latitude":34.1017,"longitude":-118.3267},"address":
         {"city":"Hollywood","countrySubdivisionCode":"CA","postalCode":"90028"},"slug":"hollywood"},
        {"storeNumber":"10891","name":"Venice Boardwalk","coordinates":
         {"latitude":33.9850,"longitude":-118.4695},"address":
         {"city":"Venice","countrySubdivisionCode":"CA","postalCode":"90291"},"slug":"venice"},
        {"storeNumber":"10234","name":"Main St & 5th","coordinates":
         {"latitude":34.0522,"longitude":-118.2437},"address":
         {"city":"Los Angeles","countrySubdivisionCode":"CA","postalCode":"90012"},"slug":"duplicate"}
    ]}
    '''

    # --- Step 1: Split into individual records ---
    print("\n1. Finding individual records with re.findall()")
    print("-" * 50)

    # Each record runs from "storeNumber" to "slug"
    record_pattern = r'"storeNumber":.*?"slug"'
    records = re.findall(record_pattern, response_text, re.DOTALL)
    print(f"   Found {len(records)} records")

    # --- Step 2: Extract fields from each record ---
    print(f"\n2. Extracting fields with multi-group pattern")
    print("-" * 50)

    # This pattern uses 7 capturing groups to extract all fields at once
    field_pattern = (
        r'"storeNumber":"(.*?)"'       # Group 1: store ID
        r'.*?"name":"(.*?)"'           # Group 2: store name
        r'.*?"latitude":([\d.-]+)'     # Group 3: latitude
        r'.*?"longitude":([\d.-]+)'    # Group 4: longitude
        r'.*?"city":"(.*?)"'           # Group 5: city
        r'.*?"countrySubdivisionCode":"(.*?)"'  # Group 6: state
        r'.*?"postalCode":"(.*?)"'     # Group 7: zip code
    )

    extracted = []
    for record in records:
        match = re.search(field_pattern, record, re.DOTALL)
        if match:
            extracted.append(match.groups())
            store_id, name, lat, lon, city, state, zip_code = match.groups()
            print(f"   Store {store_id}: {name}")
            print(f"     Location: ({lat}, {lon})")
            print(f"     Address:  {city}, {state} {zip_code}")
            print()

    # --- Alternative: re.findall with groups returns list of tuples ---
    print("3. Shortcut: re.findall() with groups")
    print("-" * 50)

    # When the pattern has groups, findall returns list of tuples
    all_matches = re.findall(field_pattern, response_text, re.DOTALL)
    print(f"   re.findall returned {len(all_matches)} tuples")
    for m in all_matches:
        print(f"   {m[0]}: {m[1]} in {m[4]}, {m[5]}")

    print("\n" + "=" * 70 + "\n")
    return all_matches


# ============================================================================
# PART 3: INTERMEDIATE - Deduplication Patterns
# ============================================================================

def demonstrate_deduplication(records: list[tuple]) -> list[tuple]:
    """
    Deduplicate scraped records.

    Web scraping often produces duplicates because:
    - The same item appears on multiple pages
    - Search regions overlap (nearby zip codes)
    - Pagination issues

    Args:
        records: List of tuples (store_id, name, lat, lon, city, state, zip)

    Returns:
        Deduplicated list
    """
    print("=" * 70)
    print("INTERMEDIATE: Deduplication Patterns for Scraped Data")
    print("=" * 70)

    print(f"\n   Records before dedup: {len(records)}")

    # --- Method 1: Track seen IDs ---
    print(f"\n1. Method 1: Track seen IDs with a set")
    print("-" * 50)

    seen_ids = set()
    unique_records = []
    duplicates = 0

    for record in records:
        store_id = record[0]
        if store_id not in seen_ids:
            seen_ids.add(store_id)
            unique_records.append(record)
        else:
            duplicates += 1
            print(f"   Duplicate found: store {store_id} ({record[1]})")

    print(f"   After dedup: {len(unique_records)} unique, {duplicates} removed")

    # --- Method 2: dict.fromkeys() preserves order ---
    print(f"\n2. Method 2: dict keyed by ID (preserves insertion order)")
    print("-" * 50)

    store_dict = {}
    for record in records:
        store_id = record[0]
        if store_id not in store_dict:
            store_dict[store_id] = record

    unique_via_dict = list(store_dict.values())
    print(f"   Result: {len(unique_via_dict)} unique records")

    # --- Method 3: Using pandas (for large datasets) ---
    print(f"\n3. Method 3: pandas drop_duplicates (best for large data)")
    print("-" * 50)
    print("   import pandas as pd")
    print("   df = pd.DataFrame(records, columns=[...])")
    print("   df = df.drop_duplicates(subset=['store_id'])")
    print("   # Handles thousands of records efficiently")

    # --- Why sets work well here ---
    print(f"\n4. Why set-based dedup is O(n)")
    print("-" * 50)
    print("   set.add() and 'in set' are both O(1) average case")
    print("   Looping through n records: n × O(1) = O(n)")
    print("   vs. list-based 'if id in seen_list': O(n) per check → O(n²)")
    print("   For 10,000 records: set is ~10,000x faster than list!")

    print("\n" + "=" * 70 + "\n")
    return unique_records


# ============================================================================
# PART 4: INTERMEDIATE - Building a DataFrame from Scraped Data
# ============================================================================

def demonstrate_dataframe_construction(records: list[tuple]):
    """
    Convert extracted records into a structured pandas DataFrame.

    This is the typical final step in a scraping pipeline:
    raw text → regex → tuples → DataFrame → CSV/analysis
    """
    print("=" * 70)
    print("INTERMEDIATE: Building a DataFrame from Scraped Data")
    print("=" * 70)

    columns = ["store_id", "name", "latitude", "longitude",
               "city", "state", "zip_code"]

    # --- Method 1: From list of tuples ---
    print(f"\n1. DataFrame from list of tuples")
    print("-" * 50)

    # We'll use a simulated dataset here (real scraping would use actual data)
    sample_records = [
        ("10234", "Main St & 5th",       "34.0522", "-118.2437", "Los Angeles", "CA", "90012"),
        ("10567", "Hollywood & Vine",     "34.1017", "-118.3267", "Hollywood",   "CA", "90028"),
        ("10891", "Venice Boardwalk",     "33.9850", "-118.4695", "Venice",      "CA", "90291"),
        ("11023", "Pasadena Old Town",    "34.1478", "-118.1445", "Pasadena",    "CA", "91101"),
        ("11156", "Santa Monica Pier",    "34.0094", "-118.4973", "Santa Monica","CA", "90401"),
        ("11289", "Beverly Hills Plaza",  "34.0736", "-118.4004", "Beverly Hills","CA","90210"),
        ("11422", "Downtown Arts Dist",   "34.0402", "-118.2351", "Los Angeles", "CA", "90013"),
        ("11555", "Glendale Galleria",    "34.1456", "-118.2551", "Glendale",    "CA", "91210"),
        ("11688", "Burbank Media Dist",   "34.1808", "-118.3090", "Burbank",     "CA", "91502"),
        ("11821", "Long Beach Pike",      "33.7675", "-118.1924", "Long Beach",  "CA", "90802"),
    ]

    # Direct construction — most common approach
    # (importing pandas only if available, since this is a regex tutorial)
    try:
        import pandas as pd

        df = pd.DataFrame(sample_records, columns=columns)

        # Convert numeric columns from strings
        df["latitude"] = df["latitude"].astype(float)
        df["longitude"] = df["longitude"].astype(float)

        print(f"   Shape: {df.shape}")
        print(f"   Dtypes:\n{df.dtypes}")
        print(f"\n   Preview:")
        print(df[["store_id", "name", "city", "zip_code"]].to_string(index=False))

        # --- Quick analysis ---
        print(f"\n2. Quick analysis of scraped data")
        print("-" * 50)

        print(f"   Total stores    : {len(df)}")
        print(f"   Unique cities   : {df['city'].nunique()}")
        print(f"   Stores per city :")
        city_counts = df["city"].value_counts()
        for city, count in city_counts.items():
            print(f"     {city}: {count}")

        print(f"\n   Geographic bounds:")
        print(f"     Lat range : {df['latitude'].min():.4f} to {df['latitude'].max():.4f}")
        print(f"     Lon range : {df['longitude'].min():.4f} to {df['longitude'].max():.4f}")

        # --- Save to CSV ---
        print(f"\n3. Saving to CSV")
        print("-" * 50)

        csv_path = "/tmp/scraped_stores.csv"
        df.to_csv(csv_path, index=False)
        print(f"   Saved {len(df)} records to {csv_path}")

        # Verify by reading back
        df_check = pd.read_csv(csv_path)
        print(f"   Verified: read back {len(df_check)} records")

    except ImportError:
        print("   (pandas not available — showing CSV approach instead)")

        # Fallback: pure csv module
        csv_path = "/tmp/scraped_stores.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(sample_records)
        print(f"   Wrote {len(sample_records)} records to {csv_path}")

    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 5: ADVANCED - Complete Regex Scraping Pipeline
# ============================================================================

def demonstrate_complete_pipeline():
    """
    A complete pipeline that combines all the patterns:
    1. Simulate fetching a web response
    2. Extract records with regex
    3. Clean and normalize fields
    4. Deduplicate
    5. Build DataFrame
    6. Export to CSV

    This mirrors how real web scrapers work.
    """
    print("=" * 70)
    print("ADVANCED: Complete Regex Scraping Pipeline")
    print("=" * 70)

    # --- Step 1: Simulated web response ---
    # In practice, this comes from requests.get(url).text
    print("\n--- Step 1: Receive web response ---")

    response_text = '''
    window.__INITIAL_STATE__ = {"stores":{"items":[
    {"storeNumber":"10234","name":"Main St \\u0026 5th Ave","coordinates":
     {"latitude":34.0522,"longitude":-118.2437},"address":
     {"city":"Los Angeles","countrySubdivisionCode":"CA",
      "postalCode":"90012-1234"},"slug":"main-st"},
    {"storeNumber":"10567","name":"Hollywood \\u0026 Vine","coordinates":
     {"latitude":34.1017,"longitude":-118.3267},"address":
     {"city":"Hollywood ","countrySubdivisionCode":"CA",
      "postalCode":"90028"},"slug":"hw-vine"},
    {"storeNumber":"10891","name":"Venice  Boardwalk","coordinates":
     {"latitude":33.9850,"longitude":-118.4695},"address":
     {"city":"Venice","countrySubdivisionCode":"CA",
      "postalCode":"90291"},"slug":"venice-bw"},
    {"storeNumber":"10234","name":"Main St \\u0026 5th Ave","coordinates":
     {"latitude":34.0522,"longitude":-118.2437},"address":
     {"city":"Los Angeles","countrySubdivisionCode":"CA",
      "postalCode":"90012-1234"},"slug":"main-st-dup"}
    ]}};
    '''

    print(f"   Response length: {len(response_text)} chars")

    # --- Step 2: Extract records ---
    print("\n--- Step 2: Extract records with regex ---")

    record_pattern = r'"storeNumber":.*?"slug"'
    raw_records = re.findall(record_pattern, response_text, re.DOTALL)
    print(f"   Found {len(raw_records)} raw records")

    field_pattern = (
        r'"storeNumber":"(?P<id>.*?)"'
        r'.*?"name":"(?P<name>.*?)"'
        r'.*?"latitude":(?P<lat>[\d.-]+)'
        r'.*?"longitude":(?P<lon>[\d.-]+)'
        r'.*?"city":"(?P<city>.*?)"'
        r'.*?"countrySubdivisionCode":"(?P<state>.*?)"'
        r'.*?"postalCode":"(?P<zip>.*?)"'
    )

    extracted = []
    for record in raw_records:
        match = re.search(field_pattern, record, re.DOTALL)
        if match:
            extracted.append(match.groupdict())

    print(f"   Extracted {len(extracted)} records")
    for rec in extracted:
        print(f"   {rec['id']}: {rec['name']} — {rec['city']}, {rec['state']}")

    # --- Step 3: Clean and normalize ---
    print("\n--- Step 3: Clean and normalize fields ---")

    def clean_record(record: dict) -> dict:
        """
        Clean a single scraped record.

        Common cleaning tasks:
        - Decode unicode escapes (\\u0026 → &)
        - Strip whitespace
        - Normalize zip codes (take first 5 digits)
        - Collapse multiple spaces
        """
        cleaned = {}
        cleaned["store_id"] = record["id"].strip()
        # Decode unicode escapes like \u0026
        cleaned["name"] = (
            record["name"]
            .encode("utf-8")
            .decode("unicode_escape")
            .strip()
        )
        # Collapse multiple spaces
        cleaned["name"] = re.sub(r"\s+", " ", cleaned["name"])
        cleaned["latitude"] = float(record["lat"])
        cleaned["longitude"] = float(record["lon"])
        cleaned["city"] = record["city"].strip()
        cleaned["state"] = record["state"].strip()
        # Normalize zip to 5 digits
        cleaned["zip_code"] = record["zip"][:5]
        return cleaned

    cleaned_records = [clean_record(r) for r in extracted]
    print(f"   Cleaned {len(cleaned_records)} records")
    for rec in cleaned_records:
        print(f"   {rec['store_id']}: {rec['name']} — {rec['city']}, "
              f"{rec['state']} {rec['zip_code']}")

    # --- Step 4: Deduplicate ---
    print("\n--- Step 4: Deduplicate ---")

    seen = set()
    unique = []
    for rec in cleaned_records:
        if rec["store_id"] not in seen:
            seen.add(rec["store_id"])
            unique.append(rec)
        else:
            print(f"   Removed duplicate: {rec['store_id']} ({rec['name']})")

    print(f"   {len(cleaned_records)} → {len(unique)} after dedup")

    # --- Step 5: Build DataFrame ---
    print("\n--- Step 5: Build DataFrame ---")

    try:
        import pandas as pd
        df = pd.DataFrame(unique)
        print(df.to_string(index=False))
    except ImportError:
        for rec in unique:
            print(f"   {rec}")

    # --- Step 6: Save to CSV ---
    print("\n--- Step 6: Save to CSV ---")

    csv_path = "/tmp/scraped_stores_pipeline.csv"
    fieldnames = ["store_id", "name", "latitude", "longitude",
                   "city", "state", "zip_code"]

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique)

    print(f"   Saved {len(unique)} records to {csv_path}")

    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 6: ADVANCED - Regex Patterns for Common Web Formats
# ============================================================================

def demonstrate_common_web_patterns():
    """
    A reference of regex patterns commonly needed in web scraping.
    """
    print("=" * 70)
    print("ADVANCED: Common Regex Patterns for Web Scraping")
    print("=" * 70)

    # --- JSON embedded in HTML (window.__DATA__) ---
    print("\n1. Extracting embedded JSON from HTML <script> tags")
    print("-" * 50)

    html = '''
    <html><head>
    <script>window.__INITIAL_DATA__ = {"user":"alice","count":42};</script>
    </head></html>
    '''

    pattern = r'window\.__INITIAL_DATA__\s*=\s*({.*?});'
    match = re.search(pattern, html)
    if match:
        data = json.loads(match.group(1))
        print(f"   Extracted: {data}")
        print(f"   user={data['user']}, count={data['count']}")

    # --- HTML table rows ---
    print(f"\n2. Extracting data from HTML tables")
    print("-" * 50)

    table_html = '''
    <table>
    <tr><td>Apple</td><td>$1.20</td><td>In Stock</td></tr>
    <tr><td>Banana</td><td>$0.50</td><td>Low Stock</td></tr>
    <tr><td>Cherry</td><td>$3.00</td><td>Out of Stock</td></tr>
    </table>
    '''

    row_pattern = r'<tr><td>(.*?)</td><td>\$([\d.]+)</td><td>(.*?)</td></tr>'
    rows = re.findall(row_pattern, table_html)
    print(f"   Found {len(rows)} rows:")
    for name, price, status in rows:
        print(f"   {name}: ${price} ({status})")

    # --- Coordinates from various formats ---
    print(f"\n3. Extracting coordinates from various formats")
    print("-" * 50)

    texts = [
        'Located at lat: 34.0522, lng: -118.2437',
        'GPS: (40.7128, -74.0060)',
        '"latitude":51.5074,"longitude":-0.1278',
        'position="48.8566,2.3522"',
    ]

    coord_patterns = [
        (r'lat:\s*([\d.-]+),\s*lng:\s*([\d.-]+)', "lat/lng format"),
        (r'\(([\d.-]+),\s*([\d.-]+)\)', "parenthesized format"),
        (r'"latitude":([\d.-]+).*?"longitude":([\d.-]+)', "JSON format"),
        (r'position="([\d.-]+),([\d.-]+)"', "attribute format"),
    ]

    for text, (pattern, fmt) in zip(texts, coord_patterns):
        match = re.search(pattern, text)
        if match:
            print(f"   {fmt}: ({match.group(1)}, {match.group(2)})")

    # --- Meta tags and Open Graph ---
    print(f"\n4. Extracting meta tags from HTML")
    print("-" * 50)

    html_head = '''
    <meta name="description" content="Best coffee shop in LA">
    <meta property="og:title" content="Starbucks - Main St">
    <meta property="og:image" content="https://example.com/store.jpg">
    '''

    meta_pattern = r'<meta\s+(?:name|property)="([^"]+)"\s+content="([^"]+)"'
    metas = re.findall(meta_pattern, html_head)
    for name, content in metas:
        print(f"   {name}: {content}")

    # --- Pagination links ---
    print(f"\n5. Extracting pagination info")
    print("-" * 50)

    pagination_html = '''
    <a href="/stores?page=1">1</a>
    <a href="/stores?page=2">2</a>
    <a href="/stores?page=3" class="current">3</a>
    <a href="/stores?page=4">4</a>
    <a href="/stores?page=5">Next</a>
    '''

    page_pattern = r'href="/stores\?page=(\d+)"'
    pages = re.findall(page_pattern, pagination_html)
    print(f"   Available pages: {pages}")
    print(f"   Last page: {max(int(p) for p in pages)}")

    print("\n" + "=" * 70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print(" " * 8 + "REGEX FOR WEB SCRAPING AND DATA EXTRACTION")
    print(" " * 20 + "Complete Tutorial")
    print("=" * 70 + "\n")

    # Beginner
    demonstrate_basic_field_extraction()

    # Intermediate
    records = demonstrate_multi_record_extraction()
    unique_records = demonstrate_deduplication(records)
    demonstrate_dataframe_construction(unique_records)

    # Advanced
    demonstrate_complete_pipeline()
    demonstrate_common_web_patterns()

    print("\n" + "=" * 70)
    print("Tutorial Complete!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Use .*? (non-greedy) to extract quoted values")
    print("2. Multi-group patterns extract several fields at once")
    print("3. re.findall() with groups returns list of tuples")
    print("4. Named groups (?P<name>...) improve readability")
    print("5. Always deduplicate scraped data (use sets for O(n))")
    print("6. Clean data before analysis: strip, normalize, convert types")
    print("7. Pipeline: fetch → regex → clean → dedup → DataFrame → CSV")
    print("8. re.DOTALL flag lets . match newlines in multi-line content")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
