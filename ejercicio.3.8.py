def es_contrasena_segura(contrasena):
    if len(contrasena) >= 8 and "123" not in contrasena:
        return True
    return False

contrasena = input("Introduce una contraseña: ")

if es_contrasena_segura(contrasena):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres y no contener '123'.")