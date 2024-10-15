"""
This file contains the logic to:

1. Create an user
2. Update user information
4. Get user information
"""
import user_repository
from users import users



def check_credentials(username, password):
    # Comprobar si el usuario existe y la contraseña coincide
    if username in users and users[username]['password'] == password:
        return True
    else:
        return False
def create_user(username, password):
    """
    Crea un nuevo usuario y guarda la información en el archivo.
    """
    # Verificar si el usuario ya existe
    if username in users:
        raise Exception(f"El usuario {username} ya existe")

    # Verificar que se proporcionen los campos obligatorios
    if not password:
        raise Exception("La contraseña es obligatoria")

    # Agregar el nuevo usuario al diccionario
    users[username] = {"password": password}

    # Guardar los usuarios actualizados en el archivo JSON
    user_repository.save_users(users)

    return True

def update_user(username, **kwargs):
    """
    Actualiza la información de un usuario existente.
    """
    if username not in users:
        raise Exception(f"El usuario {username} no está registrado")

    # Aseguramos que la información contenga las claves necesarias
    password = kwargs.get("password")
    
    if password is None:
        raise Exception("La contraseña es obligatoria")

    # Actualiza solo el username y password en el diccionario de usuarios
    users[username]["password"] = password  # Actualiza la contraseña

    # Si se desea cambiar el username, se puede manejar aquí
    new_username = kwargs.get("new_username")
    if new_username and new_username != username:
        users[new_username] = users.pop(username)  # Cambia el nombre de usuario
        username = new_username  # Actualiza el username

    user_repository.save_users(users)  # Guarda los cambios en el archivo

    print(f"Usuario actualizado: {username}, nueva contraseña: {password}")


