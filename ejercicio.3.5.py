# Solicitar protocolo y puerto al usuario
protocolo = input("Introduce el protocolo (http o https): ").strip().lower()
puerto = input("Introduce el puerto (80 o 443): ").strip()

# Verificar si la conexión es segura
if protocolo == "https" and puerto == "443":
    print("La conexión es segura.")
else:
    print("La conexión no es segura.")