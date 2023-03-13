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