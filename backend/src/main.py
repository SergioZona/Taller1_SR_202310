import sqlite3
import uvicorn;
from fastapi import FastAPI, Body   
from fastapi.middleware.cors import CORSMiddleware;
import hashlib
import uuid


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
    data = [{'user_id': row[0], 'password_hash': row[1], 'email': row[2]} for row in rows]

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
    data = {'user_id': row[0], 'password_hash': row[1], 'email': row[2]}

    # Close the cursor
    cur.close()
    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id
@app.get('/api/user/{email}')
async def get_user_by_email(email: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user WHERE email = ?', (email,))

    # Fetch the row and convert it to a dictionary
    row = cur.fetchone()
    data = {'user_id': row[0], 'password_hash': row[1], 'email': row[2]}

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}


@app.post("/api/user")
async def create_user(email: str = Body(...), password: str = Body(...)):
    print("Creating user...")
    id_user=str(uuid.uuid4())
    newPassword=str(id_user)+password
    password_hash= hashlib.sha256(bytes(newPassword, encoding='utf-8')).hexdigest()
    # Create a cursor object
    cur = conn.cursor()

    cur.execute('INSERT INTO user (user_id, email, password_hash) VALUES (?, ?, ?)',
              (id_user, email , password_hash))
    conn.commit()
    cur.close()
    return {"message": "User created successfully!"}

@app.post("/api/user/login")
async def login(email: str = Body(...), password: str = Body(...)):
    data=await get_user_by_email(email)
    data=data["data"]
    print(data)
    newPassword=data["user_id"]+password   
    password_hash= hashlib.sha256(bytes(newPassword, encoding='utf-8')).hexdigest()
    if (password_hash==data["password_hash"]):
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