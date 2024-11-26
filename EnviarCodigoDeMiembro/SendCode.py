import pandas as pd
import pywhatkit as kit
import time

# Configuración
codigo_pais = "+52"  # Cambia esto según el país
archivo_excel = "list.xlsx"

# Cargar datos del archivo Excel
datos = pd.read_excel(archivo_excel)

# Iterar sobre cada fila del archivo
for index, fila in datos.iterrows():
    nombre = fila['Nombre'].strip()  # Nombre de la persona
    numero = str(fila['Número de teléfono']).strip()  # Número de teléfono
    codigo = fila['Código único']  # Código único

    # Agregar código de país si no está presente
    if not numero.startswith("+"):
        numero = f"{codigo_pais}{numero}"

    # Crear el mensaje personalizado
    mensaje = f"Hola {nombre}, Gracias por formar parte de la SCJ sede Puebla. Tu código único de miembro es: {codigo}."

    try:
        # Enviar mensaje de WhatsApp
        kit.sendwhatmsg_instantly(numero, mensaje)
        print(f"Mensaje enviado a {nombre} ({numero})")
        time.sleep(10)  # Pausa entre mensajes para evitar bloqueos
    except Exception as e:
        print(f"Error enviando mensaje a {nombre} ({numero}): {e}")
