from pathlib import Path

# Construyen objetos al formato de directorios
guia = Path('Barcelona', 'Sagrada_Familia')
print(guia)

# Instancia Path de la raiz principal
base = Path.home()
guia = Path(base, 'Barcelona', 'Sagrada_Familia.txt')  # C:\Users\ivan7\Barcelona\Sagrada_Familia.txt

# Lo que tambien se puede hacer
guia = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada_Familia.txt'))

# Llegando a la misma ruta pero cambiando el archivo de destino
base = Path.home()
guia = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada_Familia.txt'))
guia2 = guia.with_name("La_Pedrera.txt")

print(guia)
print(guia2)

# El antecesor mas inmediato de una ruta de archivos determinada
print(guia.parent)  # C:\Users\ivan7\Europa\España\Barcelona
print(guia.parent.parent)  # C:\Users\ivan7\Europa\España

# Imagina que tenemos una carpeta Europa, con dos archivos, y dos carpetas, y dentro de una de
# esas dos carpetas, hay una con otras dos carpetas y cada una de ellas un archivo, luego hay otra carpeta aparte

# Con ese for ejecuta SOLO los archivos de la carpeta Europa
guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("*.txt"):
    print(txt)

    # Con esto sacamos tambien todos los .txt de las subcarpetas de Europa
guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

# Y si queremos ver todo lo relacionado con unas rutas en especifico
guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")

en_europa = guia.relative_to(Path("Europa"))
en_espana = guia.relative_to(Path("Europa", "Espana"))

print(en_europa)
print(en_espana)