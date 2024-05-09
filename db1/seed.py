import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="test",
    user="root",
    password="root",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Create a table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        address VARCHAR(255)
    )
""")

# Sample data to insert
data = [
    ("John Doe", "123 Main St"),
    ("Jane Smith", "456 Elm St"),
    ("Bob Johnson", "789 Oak St")
]

# Insert data into the table
for row in data:
    cur.execute("INSERT INTO contacts (name, address) VALUES (%s, %s)", row)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data seeding complete!")