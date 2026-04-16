import psycopg2
from psycopg2 import sql

# Connection parameters
conn_params = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'tg6xctg6x',
    'port': '5432'
}

# Database name
db_name = 'btredb'

try:
    # Connect to PostgreSQL server
    conn = psycopg2.connect(**conn_params)
    conn.autocommit = True
    cursor = conn.cursor()

    # Terminate active connections to the database
    cursor.execute("""
        SELECT pg_terminate_backend(pid)
        FROM pg_stat_activity
        WHERE datname = %s AND pid <> pg_backend_pid();
    """, (db_name,))

    # Drop the database if it exists
    cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(db_name)))
    print(f"Database '{db_name}' dropped successfully.")

    # Create the database
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    print(f"Database '{db_name}' created successfully.")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")