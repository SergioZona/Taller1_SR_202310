import sqlite3
import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import hashlib
from datetime import datetime


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
# conn = sqlite3.connect('../data/data.db') # Si ejecuto el script desde SRC.
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

    data = [{'user_id': row[0],
             'gender': row[1],
             'age': row[2],
             'country': row[3],
             'registered': row[4],
             'password_hash': row[5]
             } for row in rows]

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
    data = {'user_id': row[0],
            'gender': row[1],
            'age': row[2],
            'country': row[3],
            'registered': row[4],
            'password_hash': row[5]
            }
    # Close the cursor
    cur.close()
    # Return the data as a JSON response
    return {'data': data}


@app.post("/api/user")
async def create_user(username: str = Body(...), gender: str = Body(...), age: str = Body(...), country: str = Body(...), password: str = Body(...)):
    print("Creating user...")
    newPassword = username+password
    password_hash = hashlib.sha256(
        bytes(newPassword, encoding='utf-8')).hexdigest()

    # Create a cursor object
    cur = conn.cursor()

    cur.execute('INSERT INTO user (user_id, gender, age, country, registered, password_hash) VALUES (?, ?, ?, ?, ?, ?)',
                (username, gender, age, country, datetime.now(), password_hash))
    conn.commit()
    cur.close()
    return {"message": "User created successfully!"}


@app.post("/api/user/login")
async def login(username: str = Body(...), password: str = Body(...)):
    data = await get_user_by_id(username)
    data = data["data"]
    newPassword = data["user_id"]+password
    password_hash = hashlib.sha256(
        bytes(newPassword, encoding='utf-8')).hexdigest()
    if (password_hash == data["password_hash"]):
        return {"message": "LogIn successfully!"}
    return {"message": "Password or account invalid"}

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
    data = [{'id': row[0], 'user_id': row[1],
             'artist_name': row[2], 'rating': row[3]} for row in rows]

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
    data = [{'id': row[0], 'user_id': row[1],
             'artist_name': row[2], 'rating': row[3]} for row in rows]

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
    data = [{'id': row[0], 'user_id': row[1],
             'track_name': row[2], 'rating': row[3]} for row in rows]

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
    data = [{'id': row[0], 'user_id': row[1],
             'track_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

"""---------------------------"""
"""ENDPOINTS - USER-TRACK-RATE"""
"""---------------------------"""
# Define a route to get all the rows from the database table


@app.get('/api/user_track_rate')
async def get_user_track_rate():
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user_track_rate')

    # Fetch all the rows and convert them to a list of dictionaries
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1],
             'track_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id


@app.get('/api/user_track_rate/max/{max}')
async def get_user_track_by_user_id(max: int):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id

    cur.execute(
        'SELECT * FROM user_track_rate ORDER BY rating DESC LIMIT ?', (max,))

    # Fetch the row and convert it to a dictionary
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1],
             'track_name': row[2], 'rating': row[3]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}


@app.get('/api/user_track_rate/{username}/{track_name}')
async def get_rate_from_user_and_track(username: str, track_name: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user_track WHERE user_id = ? AND track_name = ?',
                (username, track_name))

    # Fetch all the rows and convert them to a list of dictionaries
    row = cur.fetchall()
    print("tt", row)
    if (len(row) == 0):
        return {"data": 'the track with this username does not exist'}

    data = {'id': row[0][0], 'user_id': row[0][1],
            'track_name': row[0][2], 'rating': row[0][3]}

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id


@app.put('/api/user_track_rate')
async def get_user_track_by_user_id(username: str = Body(...), track_name: str = Body(...)):
    data = await get_rate_from_user_and_track(username, track_name)
    data = data["data"]

    # Create a cursor object
    cur = conn.cursor()

    if (data == "the track with this username does not exist"):
        cur.execute('INSERT INTO user_track (user_id, track_name, rating) VALUES (?, ?, ?)',
                    (username, track_name, 1))
        conn.commit()
    else:
        rating = int(data["rating"])+1

        # Execute a UPDATE statement to get the row with the specified id

        cur.execute(
            'UPDATE user_track SET rating = ? WHERE user_id = ? AND track_name = ?', (rating, username, track_name))

        # Commit the changes to the database
        conn.commit()

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {"message": "Data updated successfully"}

# Run the app
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
