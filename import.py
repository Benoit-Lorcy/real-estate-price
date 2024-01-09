import sqlite3
import csv
import math
from collections import defaultdict

# Connect to SQLite database
conn = sqlite3.connect('data/real_estate_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS real_estate (
                    Ville TEXT,
                    Quartier TEXT,
                    Prix_au_m2 REAL)''')

# Function to calculate mean
def calculate_mean(values):
    return math.floor(sum(values) / len(values))

# Read the CSV file and calculate mean prices
data = defaultdict(list)
with open('data/prix_immobilier_fictif.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        key = (row['Ville'], row['Quartier'])
        data[key].append(float(row['Prix au m²']))

# Prepare data for insertion (calculate mean for each Ville and Quartier)
data_for_insertion = [(ville, quartier, calculate_mean(prices)) for (ville, quartier), prices in data.items()]

# Insert the data into the SQLite table
cursor.executemany('INSERT INTO real_estate (Ville, Quartier, Prix_au_m2) VALUES (?, ?, ?)', data_for_insertion)

# Commit and close
conn.commit()
conn.close()

