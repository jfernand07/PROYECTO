#Acceso exclusivo al evento
edad=int(input("¿Cuántos años tienes? "))
invita= input("¿Tienes invitación? (si/no) ")
if invita == "si":
    print("Puedes entrar al evento")
if edad >= 18:
    print("Puedes entrar al evento")