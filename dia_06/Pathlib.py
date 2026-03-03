from pathlib import Path, PureWindowsPath # Transformar cualquier ruta en una de Windows

# Nos lee lo de dentro del archivo
carpeta = Path('C:/Users/ivan7/Desktop/Cursos/Python_Total/dia_06/alternativo.txt')
print(carpeta.read_text())

# Transformar cualquier ruta en una de Windows
ruta_windows = PureWindowsPath(carpeta)

# El nombre del archivo
print(carpeta.name)
# La extension del archivo
print(carpeta.suffix)
# El nombre sin la extension del archivo
print(carpeta.stem)

# Comprobar si existe
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print('Si existe')


