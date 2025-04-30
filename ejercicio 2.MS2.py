#asistente virtual
from datetime import datetime

# Obtener fecha y hora actual
ahora = datetime.now()
hora = ahora.hour
dia_semana = ahora.weekday()  # 0 = lunes, 6 = domingo

# Verificar si es fin de semana
if dia_semana >= 5:
    # Es sábado o domingo
    if 6 <= hora < 9:
        actividad = "hacer ejercicio"
    elif 9 <= hora < 20:
        actividad = "descansar"
    else:
        actividad = "descansar"
else:
    # Es día laboral (lunes a viernes)
    if 6 <= hora < 9:
        actividad = "hacer ejercicio"
    elif 9 <= hora < 12:
        actividad = "trabajar"
    elif 12 <= hora < 13:
        actividad = "descansar"
    elif 13 <= hora < 18:
        actividad = "trabajar"
    elif 18 <= hora < 20:
        actividad = "hacer ejercicio"
    else:
        actividad = "descansar"

print(f" Sugerencia actual: {actividad}")
