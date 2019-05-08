import manejo_archivos_artistas
import transformaciones_artistas
def crear_artista():
    print("Nuevo Artista:")
    code = input("Ingrese un id: ")
    nombre = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del album del artista: ")
    edad = input("Ingrese la edad del artista: ")
    sexo = input("Ingrese el sexo del artista: ")
    description = input("Ingrese una descripción sobre el artista: ")
    artist = code + ";" + nombre + ";" + album + ";" + edad + ";" + sexo + ";" + description + ';No registrado'
    manejo_archivos_artistas.agregar_a_archivo('./artists.txt', 'a', artist)
    
def obtener_lista_artistas():
    archivo_artists = manejo_archivos_artistas.leer_archivos('./artists.txt')
    artistas = []
    for cadena in archivo_artists:
        artistas.append(transformaciones_artistas.transformar_cadenatexto_a_diccionarioartista(cadena))
    return artistas

def obtener_artista_por_codigo(code):
    lista = obtener_lista_artistas()
    for artista in lista:
        if artista.get('code') == code:
            break
    else:
        artista =None
    return artista

def guardar_listadediccionarios_como_listadecadenadetexto(lista):
    lista_cadenas = []
    for artista in lista:
        cadena = transformaciones_artistas.transformar_diccionarioartista_a_cadenatexto(artista)
    lista_cadenas.append(cadena)
    manejo_archivos_artistas.agregar_a_archivo('./artists.txt', 'w', *lista_cadenas)
    
def eliminar_artista_por_codigo(code):
    lista = obtener_lista_artistas()
    artista_a_eliminar= obtener_artista_por_codigo(code)
    if artista_a_eliminar != None:
        lista.remove(artista_a_eliminar)
    print(f'Eliminando artista con código {code}')
    guardar_listadediccionarios_como_listadecadenadetexto(lista)
    
"""def actualizar_musica_por_diccionario(musica, dato_actualizado):
    lista = obtener_lista_musicas()
    index = lista.index(musica)
    musica.update(dato_actualizado)
    lista [index] = musica
    print(f"Actualizando musica con código {musica['code']}")
    guardar_listadediccionarios_como_listadecadenadetexto(lista)"""
    