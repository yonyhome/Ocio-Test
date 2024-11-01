import os
import re  # Importar la librería 're' para trabajar con expresiones regulares

# Define el nombre del archivo de entrada y salida
input_file = "canciones.txt"
output_file = "formato_canciones.txt"

# Leer el archivo de entrada
try:
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        
    # Filtrar y formatear las canciones
    song_list = []
    for line in lines:
        # Eliminar saltos de línea y espacios
        line = line.strip()
        if line:  # Verifica que la línea no esté vacía
            # Eliminar "ft.", "feat." y similares, y luego obtener el nombre de la canción y el artista
            line = re.sub(r'\s*ft\.?\s+.*$', '', line, flags=re.IGNORECASE)  # Quita "ft. algo"
            line = re.sub(r'\s*feat\.?\s+.*$', '', line, flags=re.IGNORECASE)  # Quita "feat. algo"
            line = line.strip()  # Elimina espacios adicionales
            
            # Separar el nombre de la canción y el artista
            parts = line.rsplit(' - ', 1)  # Separar por " - " desde el final
            if len(parts) == 2:
                song_name = parts[0].strip()
                artist_name = parts[1].strip()
                song_list.append(f"{song_name} - {artist_name}")
    
    # Verificar si se encontraron canciones
    if not song_list:
        print("No se encontraron canciones en el archivo.")
    else:
        # Guardar en el archivo de salida
        with open(output_file, "w", encoding="utf-8") as out_file:
            out_file.write("song_list = [\n")
            for song in song_list:
                out_file.write(f'    "{song}",\n')
            out_file.write("]\n")

        print(f"Archivo '{output_file}' creado exitosamente con {len(song_list)} canciones.")

except FileNotFoundError:
    print(f"Error: El archivo '{input_file}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
