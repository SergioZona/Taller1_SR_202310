import sqlite3
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Issue corrected: https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi
# Create an instance of the FastAPI class
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to the SQLite3 database
#conn = sqlite3.connect('../data/data.db') # Si ejecuto el script desde SRC.
conn = sqlite3.connect('data/data.db')


@app.get("/")
def root():
    return {"message": "Fast API in Python"}

"""----------------"""
"""ENDPOINTS - USER"""
"""----------------"""

# Define a route to get all the rows from the database table
@app.get('/api/user')
async def get_user():
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user')

    # Fetch all the rows and convert them to a list of dictionaries
    rows = cur.fetchall()
    data = [{'user_id': row[0], 'gender': row[1], 'age': row[2], 'country': row[3], 'registered': row[4]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id
@app.get('/api/user/{id}')
async def get_user_by_id(id: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user WHERE user_id = ?', (id,))

    # Fetch the row and convert it to a dictionary
    row = cur.fetchone()
    data = {'user_id': row[0], 'gender': row[1], 'age': row[2], 'country': row[3], 'registered': row[4]}

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

"""-----------------------"""
"""ENDPOINTS - USER_ARTIST"""
"""-----------------------"""

# Define a route to get all the rows from the database table
@app.get('/api/user_artist')
async def get_user_artist():
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user_artist')

    # Fetch all the rows and convert them to a list of dictionaries
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'artist_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id
@app.get('/api/user_artist/{id}')
async def get_user_artist_by_user_id(id: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user_artist WHERE user_id = ?', (id,))

    # Fetch the row and convert it to a dictionary
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'artist_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}


"""----------------------"""
"""ENDPOINTS - USER-TRACK"""
"""----------------------"""
# Define a route to get all the rows from the database table
@app.get('/api/user_track')
async def get_user_track():
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user_track')

    # Fetch all the rows and convert them to a list of dictionaries
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'track_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id
@app.get('/api/user_track/{id}')
async def get_user_track_by_user_id(id: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user_track WHERE user_id = ?', (id,))

    # Fetch the row and convert it to a dictionary
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'track_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Run the app
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)