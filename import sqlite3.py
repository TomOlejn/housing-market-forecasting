import sqlite3
import pandas as pd

# Connect to database file and load the table
conn = sqlite3.connect('C:\Projekt\HousePriceML\HousePriceML.db')
df = pd.read_sql_query("SELECT * FROM Housing", conn)
conn.close()

# View the imported data
print(df.head())