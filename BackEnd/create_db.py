"""
Creates the database if it doesn't exist
"""
import mariadb

try:
    # Connect without specifying a database
    conn = mariadb.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )
    cursor = conn.cursor()
    
    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS cit_curriculum")
    print("✓ Database 'cit_curriculum' created or already exists")
    
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    print(f"✗ Error: {e}")
