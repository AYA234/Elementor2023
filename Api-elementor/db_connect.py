
import psycopg2

host = "test-rds-dev.colcjtm9obot.eu-west-1.rds.amazonaws.com"
port = 5432
database = "metrics_dev"
user = "developer"
password = "41b387c1-2cf9-4436-85fa-7c75093b7d14"

# Connect to the metrics_dev database
connection = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
connection.autocommit = True
cursor = connection.cursor()
print(f"Connected to the {database} database!")

# Drop the tables in the correct order
drop_statements = '''
    DROP TABLE IF EXISTS usage_per_site;
    DROP TABLE IF EXISTS metrics;
    DROP TABLE IF EXISTS sites_to_package;
    DROP TABLE IF EXISTS packages_to_users;
    DROP TABLE IF EXISTS sites;
    DROP TABLE IF EXISTS packages;
    DROP TABLE IF EXISTS users;
'''

cursor.execute(drop_statements)
print("Tables dropped successfully!")

# Create the tables in the correct order
create_statements = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        address TEXT,
        phone_number TEXT,
        password INT
    );

    CREATE TABLE IF NOT EXISTS packages (
        package_id INT PRIMARY KEY, 
        cost_per_month INT, 
        storage_gb FLOAT,
        disc_cache FLOAT,
        disc_a_gb FLOAT,
        disc_b_gb FLOAT,
        cpu_percent FLOAT,
        cpu_tic FLOAT
    );

    CREATE TABLE IF NOT EXISTS sites (
        site_id INT PRIMARY KEY,
        user_id INTEGER REFERENCES users(user_id),
        site_name TEXT,
        site_description TEXT,
        date_created DATE DEFAULT CURRENT_DATE
    );

    CREATE TABLE IF NOT EXISTS packages_to_users (
        id INT PRIMARY KEY,
        user_id INTEGER REFERENCES users(user_id),  
        package_id INTEGER REFERENCES packages(package_id)  
    );

    CREATE TABLE IF NOT EXISTS sites_to_package (
        id INT PRIMARY KEY, 
        package_id INTEGER REFERENCES packages(package_id) ,
        site_id INTEGER REFERENCES sites(site_id)
    );

    CREATE TABLE IF NOT EXISTS usage_per_site (
        id INT PRIMARY KEY,
        site_id INTEGER REFERENCES sites(site_id),
        time TIMESTAMPTZ,  
        storage_gb FLOAT,
        disc_cache FLOAT,
        disc_a_gb FLOAT,
        disc_b_gb FLOAT,
        cpu_percent FLOAT,
        cpu_tic FLOAT    
    );

  
'''

cursor.execute(create_statements)
print("Tables created successfully!")

# Close the cursor and connection to the metrics_dev database
cursor.close()
connection.close()
print(f"Disconnected from the {database} database!")