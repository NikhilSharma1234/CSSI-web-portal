import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Uncomment any part of this to help create and or popualte your db

conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'))

cur = conn.cursor()

# Execute a command: this creates a new table
# cur.execute('DROP TABLE IF EXISTS users;')
# cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
#                                  'name varchar (150) NOT NULL,'
#                                  'email varchar (50) NOT NULL,'
#                                  'password varchar NOT NULL,'
#                                  'created_at date DEFAULT CURRENT_TIMESTAMP,'
#                                  'updated_at date DEFAULT CURRENT_TIMESTAMP,'
#                                  'deleted_at date);'
#                                  )

# # This adds a row to the table
# cur.execute('INSERT INTO users (name, email, password)'
#             'VALUES (%s, %s, %s)',
#             ('Eren Yeager',
#              'titanhunter@gmail.com',
#              'Memories@2024')
#             )
# conn.commit()
cur.close()
conn.close()