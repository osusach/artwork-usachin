import os

# Ruta de la carpeta donde se encuentran las imágenes
carpeta = "./"

# Prefijo que debe tener el nombre de las imágenes
prefijo = "IA_"

# Obtener una lista de todos los archivos en la carpeta
archivos = os.listdir(carpeta)

# Inicializar el número para el siguiente archivo
ultimo_numero = 0

# Encontrar el último número en los nombres de archivo existentes
for archivo in archivos:
    if archivo.startswith(prefijo):
        try:
            numero = int(archivo[len(prefijo):-4])  # -4 para eliminar la extensión ".png"
            ultimo_numero = max(ultimo_numero, numero)
        except ValueError:
            pass

# Cambiar el nombre de los archivos que no siguen el formato
for archivo in archivos:
    if not archivo.startswith(prefijo) and not archivo.endswith(".py"):
        nuevo_nombre = f"{prefijo}{ultimo_numero + 1}.png"
        nuevo_nombre_path = os.path.join(carpeta, nuevo_nombre)
        archivo_path = os.path.join(carpeta, archivo)
        os.rename(archivo_path, nuevo_nombre_path)
        ultimo_numero += 1

print("Proceso completado.")
