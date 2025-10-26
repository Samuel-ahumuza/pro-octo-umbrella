# app.py (Modified)

# import psycopg2 # <-- REMOVE THIS LINE
import mysql.connector # <-- ADD THIS LINE

# --- Database Connection Setup ---
DB_CONFIG = {
    "host": "127.0.0.1", # Matches HeidiSQL Hostname / IP
    "user": "root",      # Matches HeidiSQL User
    "password": "root", # Matches HeidiSQL Password
    "port": 3306,        # Matches HeidiSQL Port
    "database": "bank_system" # IMPORTANT: You must create this database in HeidiSQL first!
}

def get_db_connection():
    """Establishes a connection to the MariaDB/MySQL database."""
    # Use mysql.connector.connect instead of psycopg2.connect
    conn = mysql.connector.connect(**DB_CONFIG) 
    return conn

