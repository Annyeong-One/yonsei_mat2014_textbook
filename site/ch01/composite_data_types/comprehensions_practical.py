"""
Practical Examples: Python Comprehensions in Real-World Scenarios
This file demonstrates how comprehensions are used in actual programming tasks
"""

# ============================================================================
# Example 1: E-Commerce Product Filtering

if __name__ == "__main__":
    print("="*60)
    print("Example 1: E-Commerce Product Filtering")
    print("="*60)

    products = [
        {'name': 'Laptop', 'price': 1200, 'category': 'Electronics', 'stock': 5},
        {'name': 'Mouse', 'price': 25, 'category': 'Electronics', 'stock': 50},
        {'name': 'Desk', 'price': 300, 'category': 'Furniture', 'stock': 10},
        {'name': 'Chair', 'price': 150, 'category': 'Furniture', 'stock': 15},
        {'name': 'Monitor', 'price': 400, 'category': 'Electronics', 'stock': 8},
        {'name': 'Keyboard', 'price': 75, 'category': 'Electronics', 'stock': 30}
    ]

    # Get all electronics
    electronics = [p for p in products if p['category'] == 'Electronics']
    print(f"\nElectronics ({len(electronics)} items):")
    for item in electronics:
        print(f"  {item['name']}: ${item['price']}")

    # Products under $100
    affordable = [p['name'] for p in products if p['price'] < 100]
    print(f"\nAffordable products (< $100): {', '.join(affordable)}")

    # Low stock alert (stock < 10)
    low_stock = {p['name']: p['stock'] for p in products if p['stock'] < 10}
    print(f"\nLow Stock Alert:")
    for name, stock in low_stock.items():
        print(f"  {name}: Only {stock} left!")

    # Calculate total inventory value
    total_value = sum(p['price'] * p['stock'] for p in products)
    print(f"\nTotal Inventory Value: ${total_value:,}")

    # ============================================================================
    # Example 2: Text Analysis & Processing
    print("\n" + "="*60)
    print("Example 2: Text Analysis & Processing")
    print("="*60)

    text = """
    Python is a versatile programming language. It's used for web development,
    data science, artificial intelligence, and more. Python's simplicity makes
    it perfect for beginners, while its power satisfies experts.
    """

    # Clean and split into words
    words = [w.strip('.,!?').lower() for w in text.split() if w.strip('.,!?')]

    # Word statistics
    word_stats = {
        'total_words': len(words),
        'unique_words': len(set(words)),
        'avg_length': sum(len(w) for w in words) / len(words)
    }

    print(f"\nText Statistics:")
    for key, value in word_stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value:.2f}" if isinstance(value, float) else f"  {key.replace('_', ' ').title()}: {value}")

    # Find all words containing 'th'
    th_words = {w for w in words if 'th' in w}
    print(f"\nWords containing 'th': {', '.join(sorted(th_words))}")

    # Word frequency (top 5)
    word_freq = {word: words.count(word) for word in set(words)}
    top_5 = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"\nTop 5 Most Common Words:")
    for word, count in top_5:
        print(f"  '{word}': {count} times")

    # ============================================================================
    # Example 3: Student Grade Management System
    print("\n" + "="*60)
    print("Example 3: Student Grade Management System")
    print("="*60)

    students = {
        'Alice': [85, 92, 88, 90, 87],
        'Bob': [78, 85, 80, 82, 79],
        'Charlie': [92, 95, 90, 94, 96],
        'Diana': [88, 86, 84, 85, 87],
        'Eve': [70, 75, 72, 71, 74]
    }

    # Calculate averages
    averages = {name: sum(grades)/len(grades) for name, grades in students.items()}

    # Assign letter grades
    def get_letter_grade(avg):
        if avg >= 90: return 'A'
        elif avg >= 80: return 'B'
        elif avg >= 70: return 'C'
        else: return 'F'

    letter_grades = {name: get_letter_grade(avg) for name, avg in averages.items()}

    # Generate report card
    print("\nClass Report Card:")
    print(f"{'Student':<12} {'Average':<10} {'Grade':<8} {'Lowest':<10} {'Highest'}")
    print("-" * 60)
    for name, grades in students.items():
        avg = averages[name]
        letter = letter_grades[name]
        print(f"{name:<12} {avg:<10.2f} {letter:<8} {min(grades):<10} {max(grades)}")

    # Honor roll (average >= 90)
    honor_roll = [name for name, avg in averages.items() if avg >= 90]
    print(f"\n🏆 Honor Roll: {', '.join(honor_roll)}")

    # Students needing improvement (average < 75)
    needs_help = [name for name, avg in averages.items() if avg < 75]
    if needs_help:
        print(f"⚠️  Needs Support: {', '.join(needs_help)}")

    # Class statistics
    class_avg = sum(averages.values()) / len(averages)
    print(f"\nClass Average: {class_avg:.2f}")

    # ============================================================================
    # Example 4: Data Transformation & API Response Processing
    print("\n" + "="*60)
    print("Example 4: API Response Processing")
    print("="*60)

    # Simulated API response
    api_response = [
        {'user_id': 101, 'username': 'alice', 'email': 'ALICE@EMAIL.COM', 'age': 28, 'active': True},
        {'user_id': 102, 'username': 'bob', 'email': 'BOB@EMAIL.COM', 'age': 32, 'active': True},
        {'user_id': 103, 'username': 'charlie', 'email': 'CHARLIE@EMAIL.COM', 'age': 25, 'active': False},
        {'user_id': 104, 'username': 'diana', 'email': 'DIANA@EMAIL.COM', 'age': 30, 'active': True}
    ]

    # Clean and transform data
    cleaned_users = [
        {
            'id': user['user_id'],
            'name': user['username'].title(),
            'email': user['email'].lower(),
            'age': user['age']
        }
        for user in api_response if user['active']
    ]

    print("\nCleaned Active Users:")
    for user in cleaned_users:
        print(f"  {user['id']}: {user['name']} ({user['email']})")

    # Create lookup dictionary
    user_lookup = {user['id']: user['name'] for user in cleaned_users}
    print(f"\nUser Lookup: {user_lookup}")

    # Age groups
    age_groups = {
        '20-29': [u['name'] for u in cleaned_users if 20 <= u['age'] < 30],
        '30-39': [u['name'] for u in cleaned_users if 30 <= u['age'] < 40]
    }
    print(f"\nAge Distribution:")
    for group, users in age_groups.items():
        print(f"  {group}: {', '.join(users)}")

    # ============================================================================
    # Example 5: File System Operations
    print("\n" + "="*60)
    print("Example 5: File System Processing")
    print("="*60)

    # Simulated file listing
    files = [
        'report.pdf', 'data.csv', 'script.py', 'notes.txt',
        'image1.jpg', 'image2.png', 'backup.zip', 'config.json',
        'test.py', 'main.py', 'README.md', 'requirements.txt'
    ]

    # Group by extension
    from collections import defaultdict
    by_extension = defaultdict(list)
    for file in files:
        ext = file.split('.')[-1]
        by_extension[ext].append(file)

    print("\nFiles by Type:")
    for ext, file_list in sorted(by_extension.items()):
        print(f"  .{ext}: {len(file_list)} files")

    # Python files only
    py_files = [f for f in files if f.endswith('.py')]
    print(f"\nPython files: {', '.join(py_files)}")

    # Image files
    image_files = [f for f in files if f.endswith(('.jpg', '.png', '.gif'))]
    print(f"Image files: {', '.join(image_files)}")

    # Generate file info dictionary
    file_info = {
        f: {
            'name': f.split('.')[0],
            'extension': f.split('.')[-1],
            'is_code': f.endswith(('.py', '.js', '.java'))
        }
        for f in files
    }

    code_files = [name for name, info in file_info.items() if info['is_code']]
    print(f"\nCode files: {', '.join(code_files)}")

    # ============================================================================
    # Example 6: Sales Data Analysis
    print("\n" + "="*60)
    print("Example 6: Sales Data Analysis")
    print("="*60)

    sales_data = [
        {'product': 'Laptop', 'region': 'North', 'quarter': 'Q1', 'sales': 45000},
        {'product': 'Laptop', 'region': 'South', 'quarter': 'Q1', 'sales': 38000},
        {'product': 'Mouse', 'region': 'North', 'quarter': 'Q1', 'sales': 5000},
        {'product': 'Mouse', 'region': 'South', 'quarter': 'Q1', 'sales': 4500},
        {'product': 'Laptop', 'region': 'North', 'quarter': 'Q2', 'sales': 50000},
        {'product': 'Laptop', 'region': 'South', 'quarter': 'Q2', 'sales': 42000},
    ]

    # Total sales by product
    product_totals = {}
    for record in sales_data:
        product = record['product']
        product_totals[product] = product_totals.get(product, 0) + record['sales']

    print("\nSales by Product:")
    for product, total in sorted(product_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {product}: ${total:,}")

    # Sales by region (using comprehension)
    regions = {record['region'] for record in sales_data}
    region_totals = {
        region: sum(r['sales'] for r in sales_data if r['region'] == region)
        for region in regions
    }

    print("\nSales by Region:")
    for region, total in region_totals.items():
        print(f"  {region}: ${total:,}")

    # Top performing product-region combination
    best_combo = max(sales_data, key=lambda x: x['sales'])
    print(f"\nBest Performance: {best_combo['product']} in {best_combo['region']} (${best_combo['sales']:,})")

    # Average sales per transaction
    avg_sale = sum(r['sales'] for r in sales_data) / len(sales_data)
    print(f"Average Transaction: ${avg_sale:,.2f}")

    # High-value transactions (> average)
    high_value = [
        f"{r['product']} ({r['region']})" 
        for r in sales_data 
        if r['sales'] > avg_sale
    ]
    print(f"\nAbove Average Transactions: {', '.join(high_value)}")

    # ============================================================================
    # Example 7: URL Parameter Builder
    print("\n" + "="*60)
    print("Example 7: URL Parameter Building")
    print("="*60)

    # Build query strings from dictionaries
    search_params = {
        'query': 'python programming',
        'category': 'books',
        'min_price': 10,
        'max_price': 50,
        'sort': 'relevance'
    }

    # Build URL query string
    query_string = '&'.join(f"{k}={v}" for k, v in search_params.items() if v is not None)
    url = f"https://api.example.com/search?{query_string}"
    print(f"\nGenerated URL:\n{url}")

    # Filter out None values
    params_with_none = {'a': 1, 'b': None, 'c': 3, 'd': None}
    clean_params = {k: v for k, v in params_with_none.items() if v is not None}
    print(f"\nCleaned Parameters: {clean_params}")

    # ============================================================================
    # Example 8: Matrix Operations
    print("\n" + "="*60)
    print("Example 8: Matrix Operations")
    print("="*60)

    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    print("\nMatrix A:")
    for row in matrix_a:
        print(f"  {row}")

    print("\nMatrix B:")
    for row in matrix_b:
        print(f"  {row}")

    # Transpose
    transpose = [[row[i] for row in matrix_a] for i in range(len(matrix_a[0]))]
    print("\nTranspose of A:")
    for row in transpose:
        print(f"  {row}")

    # Element-wise addition
    matrix_sum = [[a + b for a, b in zip(row_a, row_b)] 
                  for row_a, row_b in zip(matrix_a, matrix_b)]
    print("\nA + B:")
    for row in matrix_sum:
        print(f"  {row}")

    # Get diagonal
    diagonal = [matrix_a[i][i] for i in range(len(matrix_a))]
    print(f"\nDiagonal of A: {diagonal}")

    # Flatten
    flat = [num for row in matrix_a for num in row]
    print(f"Flattened A: {flat}")

    # ============================================================================
    # Example 9: Contact List Management
    print("\n" + "="*60)
    print("Example 9: Contact List Management")
    print("="*60)

    contacts = [
        {'name': 'Alice Johnson', 'email': 'alice@email.com', 'phone': '555-0101', 'city': 'NYC'},
        {'name': 'Bob Smith', 'email': 'bob@email.com', 'phone': '555-0102', 'city': 'LA'},
        {'name': 'Charlie Brown', 'email': 'charlie@email.com', 'phone': '555-0103', 'city': 'NYC'},
        {'name': 'Diana Prince', 'email': 'diana@email.com', 'phone': '555-0104', 'city': 'Chicago'},
    ]

    # Extract emails for newsletter
    emails = [c['email'] for c in contacts]
    print(f"\nNewsletter Recipients: {', '.join(emails)}")

    # NYC contacts
    nyc_contacts = [c['name'] for c in contacts if c['city'] == 'NYC']
    print(f"NYC Contacts: {', '.join(nyc_contacts)}")

    # Create phone directory
    phone_book = {c['name']: c['phone'] for c in contacts}
    print(f"\nPhone Directory:")
    for name, phone in phone_book.items():
        print(f"  {name}: {phone}")

    # Group by city
    cities = {c['city'] for c in contacts}
    by_city = {city: [c['name'] for c in contacts if c['city'] == city] for city in cities}
    print(f"\nContacts by City:")
    for city, names in by_city.items():
        print(f"  {city}: {', '.join(names)}")

    print("\n" + "="*60)
    print("Examples Complete!")
    print("="*60)
