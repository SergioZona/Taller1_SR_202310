"""Aditional libraries"""
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import MinMaxScaler
from .recommendation_systems import model
from surprise import dump



"""Backend dependencies"""
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

# Sample for testing
df_ut_sample = pd.read_csv('data/df_ut_sample.csv', sep=',', index_col='id')

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
    newPassword = password
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
    newPassword = password
    password_hash = hashlib.sha256(
        bytes(newPassword, encoding='utf-8')).hexdigest()
    if (password_hash == data["password_hash"]):     
        return {"message": "LogIn successfully!"}
    return {"message": "Password or account invalid"}


"""-----------------------------"""
"""ENDPOINTS - USER-TRACK-ARTIST"""
"""-----------------------------"""
# Define a route to get all the rows from the database table


@app.get('/api/user_track_artist')
async def get_user_track_artist():
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user_track_artist')

    # Fetch all the rows and convert them to a list of dictionaries
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'track_name': row[2], 'artist_name': row[3], 'track_artist': row[4],
             'reproductions': row[5], 'rating': row[6]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

@app.get('/api/user_track_artist/{id}')
async def get_user_track_artist_by_user_id(id: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user_track_artist WHERE user_id = ?', (id,))

    # Fetch the row and convert it to a dictionary
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'track_name': row[2], 'artist_name': row[3], 'track_artist': row[4],
             'reproductions': row[5], 'rating': row[6]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

@app.get('/api/user_track_artist/{id}/{max}')
async def get_top_songs_by_user_id(id: str, max: int):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user_track_artist WHERE user_id = ? ORDER BY reproductions DESC LIMIT ?;', (id, max))

    # Fetch the row and convert it to a dictionary
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'track_name': row[2], 'artist_name': row[3], 'track_artist': row[4],
             'reproductions': row[5], 'rating': row[6]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}


@app.get('/api/user_track_artist/songs/top/{max}')
async def get_top_songs(max: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get the row with the specified id
    cur.execute('SELECT * FROM user_track_artist ORDER BY rating DESC LIMIT ?;', (max,))

    # Fetch the row and convert it to a dictionary
    rows = cur.fetchall()
    data = [{'id': row[0], 'user_id': row[1], 'track_name': row[2], 'artist_name': row[3], 'track_artist': row[4],
             'reproductions': row[5], 'rating': row[6]} for row in rows]

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}


@app.get('/api/user_track_artist/{username}/{track_name}/{artist_name}')
async def get_rate_from_user_track_artist(username: str, track_name: str, artist_name: str):
    # Create a cursor object
    cur = conn.cursor()

    # Execute a SELECT statement to get all the rows from the table
    cur.execute('SELECT * FROM user_track_artist WHERE user_id = ? AND track_name = ? AND artist_name = ?',
                (username, track_name, artist_name))

    # Fetch all the rows and convert them to a list of dictionaries
    row = cur.fetchall()
    if (len(row) == 0):
        return {"data": 'the track with this username does not exist'}

    data = {'id': row[0][1], 'user_id': row[0][1], 'track_name': row[0][2], 'artist_name': row[0][3], 'track_artist': row[0][4],
             'reproductions': row[0][5], 'rating': row[0][6]}

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {'data': data}

# Define a route to get a single row from the database table by id

@app.put('/api/user_track_artist/play_song')
async def play_song(username: str = Body(...), track_name: str = Body(...), artist_name: str=Body(...)):
    data = await get_rate_from_user_track_artist(username, track_name, artist_name)
    data = data["data"]

    track_artist = track_name+"-/-"+artist_name

    # Create a cursor object
    cur = conn.cursor()

    if (data == "the track with this username does not exist"):
        cur.execute('INSERT INTO user_track_artist (user_id, track_name, artist_name, track_artist, reproductions, rating) VALUES (?, ?, ?, ?, ?, ?)',
                    (username, track_name, artist_name, track_artist, 1, 5.0))
        
        # We update all the ratings in the database.
        rating_query_update = await recalculate_rating(username)
        # file = open("output.txt", "w", encoding="utf-8")
        # file.write(rating_query_update)
        # file.close()

        cur.execute(rating_query_update)
        
        conn.commit()
    else:
        reproductions = int(data["reproductions"])+1

        # Execute a UPDATE statement to get the row with the specified id
        cur.execute(
            'UPDATE user_track_artist SET reproductions = ? WHERE user_id = ? AND track_name = ? AND artist_name = ?', (reproductions, username, track_name, artist_name))

        # We update all the ratings in the database.
        rating_query_update = await recalculate_rating(username)
        # file = open("output.txt", "w", encoding="utf-8")
        # file.write(rating_query_update)
        # file.close()

        cur.execute(rating_query_update)

        # Commit the changes to the database
        conn.commit()

    # Close the cursor
    cur.close()

    # Return the data as a JSON response
    return {"message": "Data updated successfully"}


async def recalculate_rating(username: str):
    df_user = await get_user_track_artist_by_user_id(username)
    df_user = df_user["data"]

    scaler = MinMaxScaler(feature_range=(1, 5))
    df_user = pd.DataFrame(df_user)
    df_user[['track_name', 'artist_name']] = df_user[['track_name', 'artist_name']].applymap(lambda x: x.encode('utf-8').decode('utf-8'))
    df_user = df_user.loc[df_user['user_id'] == username]

    if df_user[['reproductions']].max()[0] != df_user[['reproductions']].min()[0]:
        df_user.loc[df_user['user_id'] == username, 'rating'] = scaler.fit_transform(df_user[['reproductions']])
    else:
        df_user.loc[df_user['user_id'] == username, 'rating'] = 5.0

    # We create the Query to execute
    sql_query = """UPDATE user_track_artist SET rating =
                CASE \n"""
    # Iterate over the rows of the DF 
    for index, row in df_user.iterrows():
        track = row['track_name']
        artist = row['artist_name']
        rating = row['rating']

        sql_query += f"""WHEN track_name = "{track}" AND artist_name = "{artist}" THEN {rating} \n"""


    sql_query += f"""ELSE rating
                END 
                WHERE user_id = "{username}";"""    
    
    return sql_query


@app.get('/api/user_track_artist/recommendation/{user_id}/{top_songs}/{user_based}')
async def get_recommendations(user_id: str, top_songs: int, user_based: bool):
    user_based = bool(user_based)
    df_data = await get_user_track_artist()
    df_data = df_data["data"]
    df_data = pd.DataFrame(df_data)

    df_songs = await get_top_songs_by_user_id(user_id,1)
    df_songs = df_songs["data"]  

    if user_based and len(df_songs)>0:    
        algo = await model.creation(df_data, user_based)

        print("Model created")
        print("Waiting for predictions...")
        prediction = await model.prediction(df_data, user_id, algo)

        prediction = prediction[:top_songs].to_dict(orient='records')

        return {'data': prediction}
    elif not user_based and len(df_songs)>0:
        algo = dump.load('data/models/ii_pearson.pkl')[1]

        print("Model created")
        print("Waiting for predictions...")        
        prediction = await model.prediction(df_data, user_id, algo)

        prediction = prediction[:top_songs].to_dict(orient='records')

        return {'data': prediction}
    else:
        return {'data': []}


"""------"""
""" MAIN """
"""------"""
# Run the app
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
