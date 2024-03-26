#importing vital libraries
import csv
import sqlite3
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Data Extraction

# Extract data from a CSV file
def get_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Scrape data from a given HTML page
def get_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find_all()
    # extract data from HTML using BeautifulSoup methods
    return data

#  Parse an XML file
def parse_XML(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    # parse XML data into usable format
    
    data = []
    for item in root.findall('item'):  # Assuming 'item' is the XML tag containing the data
        item_data = {}
        for child in item:
            item_data[child.tag] = child.text
        data.append(item_data)
    return data
  

#  Read data from a JSON file
def get_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

#  Database Operations

#  Create a SQLite database and define the schema
def create_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    # define schema
    cursor.execute('''CREATE TABLE IF NOT EXISTS data_table (
                        id INTEGER PRIMARY KEY,
                        item_id INTEGER,
                        column_name TEXT,
                        column_value TEXT
                    )''')
    conn.commit()
    conn.close()

#  Insert the extracted data into the SQLite database
def insert_into_database(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''INSERT INTO data_table (column1, column2, ...) 
                          VALUES (?, ?, ...)''', (row['column1'], row['column2'], ...))
    conn.commit()
    conn.close()

#  Implement parameterized queries to search for specific data within the database
def search_database(query):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_table WHERE column1 = ?", (query,))
    result = cursor.fetchall()
    conn.close()
    return result

#  Data Interface

def main():
    
    # Step 2: Extract data from various sources



    csv_data = get_csv('Air_condition.csv')
    xml_data = parse_XML('Air_condition.xml')
    json_data = get_json('Air_condition.json')
    html_data = get_html( 'Air_condition.web.htm')  # Assuming you have the HTML content

    # Step 3: Insert extracted data into the database
    insert_into_database(csv_data)
    insert_into_database(xml_data)
    insert_into_database(json_data)
    insert_into_database(html_data)




 # Step 4: Query the database
    search_query = input("Enter search query: ")
    search_result = search_database(search_query)

    print("Search Result:", search_result)


if __name__ == "__main__":
    main()
