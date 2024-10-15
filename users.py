"""
Lee informacion de usuarios desde archivos Json y los almacena en un diccionario 
"""
import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) # ruta
JSON_PATH = os.path.join(BASE_PATH, "user.json") # direccion exacta

users = {} # Almanezara los datos

def load_users():
    with open(JSON_PATH, "r") as j:
        data = json.load(j) #leer el contenido del archivo JSON y convertirlo en un objeto de Python
        
        j.close()
    return data 
    
users = load_users() # contendra la informacion leida del archivo user.json