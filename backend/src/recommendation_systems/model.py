"""Librería Surprise"""
# Importación de librerias
seed = 161
import pandas as pd
import numpy as np
import hashlib

# Se importa la librería de tiempo para medir cuánto se demora en encontrar los hiperparámetros con cada modelo.
import time
import math

# Librerias CUDA
# import cudf
# cudf.set_option("spill", True)

# Database
import sqlite3

# Gráficos
import matplotlib.pyplot as plt

# Importamos la librería del SR
import os
from surprise import Reader
from surprise import Dataset
from surprise.model_selection import train_test_split
from surprise import KNNBasic, KNNWithZScore
from surprise import accuracy


#Para garantizar reproducibilidad en resultados
import random
seed = 2023
#random.seed(seed) 
#np.random.seed(seed)

# Importar/Exportar modelos
from joblib import dump, load

async def creation(df, user_based):
    reader = Reader( rating_scale = ( 1, 5 ) )
    #Se crea el dataset a partir del dataframe
    surprise_dataset = Dataset.load_from_df( df[['user_id', 'track_artist', 'rating']], reader )

    train_set, test_set=  train_test_split(surprise_dataset, test_size=.2)

    sim_options = {'name': 'pearson_baseline',
               'user_based': user_based # calcule similitud user-user
               }

    algo = KNNWithZScore(k=15, min_k=2, sim_options=sim_options)

    algo.fit(train_set)

    return algo

async def prediction(table, id, model):
    songs = table['track_artist'].unique()
    predictions = []
    escuchadas = table.loc[table['user_id'] == id]['track_artist'].to_list()
    for i in songs:
        if i not in escuchadas:
            predictions.append(model.predict(id, i))
    predictions.sort(key=lambda x : x.est, reverse=True)
    #Se convierte a dataframe
    labels = ['track_artist', 'estimation']
    df_predictions = pd.DataFrame.from_records(list(map(lambda x: (x.iid, x.est) , predictions)), columns=labels)
 
    # Lo unimos con el dataframe de películas PENDIENTE
    df_predictions[['track_name', 'artist_name']] = df_predictions['track_artist'].str.split('-/-', n=1, expand=True)
    
    df_predictions.index.name='id'

    # Drop the original column
    df_predictions.drop('track_artist', axis=1, inplace=True)

    return df_predictions