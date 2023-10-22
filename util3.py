# generar la tabla para las imagenes
import os
N_COLS = 3


# Definir una función de clave personalizada para ordenar por los números
def ordenar_por_numero(nombre_archivo):
    # Extraer el número después de 'IA_'
    numero = int(nombre_archivo.split('_')[1].split('.')[0])
    return numero

def create_gallery_md(folder_path, output_md='gallery.md'):
    # Obtiene la lista de todos los archivos en la carpeta especificada
    all_files = os.listdir(folder_path)
    # Filtra solo las imágenes (por simplicidad, vamos a suponer que son .jpg y .png)
    image_files = [f for f in all_files if f.lower().endswith(('.jpg', '.png'))]
    
    image_files.sort(key=ordenar_por_numero)

    # Comienza a escribir el archivo .md con codificación UTF-8
    with open(output_md, 'w', encoding='utf-8') as md_file:
        # Encabezado del archivo
        md_file.write("# Colección de USACHINES IA\n\n")

        # Comienza la tabla
        for index, image in enumerate(image_files):
            # Header para renderizar la tabla
            if index == N_COLS:
                md_file.write("| --------- | --------- | -------- | -------- |\n")
            # Ruta relativa para Markdown
            relative_path = os.path.join(folder_path, image)
            
            # Si es el inicio de una fila
            if index % N_COLS == 0:
                md_file.write(f'| {index+1} |')

            # Añade la imagen
            md_file.write(f'![{image}]({relative_path}) | ')

            # Si es el final de una fila o es la última imagen
            if (index + 1) % N_COLS == 0 or (index + 1) == len(image_files):
                md_file.write('\n')

if __name__ == '__main__':
    # Cambia 'ruta_de_tu_carpeta' por la ruta de tu carpeta de imágenes
    create_gallery_md('./IA/')
