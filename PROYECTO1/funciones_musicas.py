import manejo_archivos
import transformaciones
def crear_musica():
    print("Nueva musica:")
    code = input("Ingrese un id: ")
    genre = input("Ingrese el género de la canción: ")
    album = input("Ingrese el nombre del álbum de la canción: ")
    artist = input("Ingrese el autor de la canción: ")
    date = input("Ingrese la fecha de publicación de la canción: ")
    description = input("Ingrese una descripción de la canción: ")
    musica = code + ";" + genre + ";" + album + ";" + artist + ";" + date + ";" + description + ';No rescatado'
    manejo_archivos.agregar_a_archivo('./musics.txt', 'a', music)
    
def obtener_lista_musicas():
    archivo_musics = manejo_archivos.leer_archivos('./musics.txt')
    musicas = []
    for cadena in archivo_musics:
        musicas.append(transformaciones.transformar_cadenatexto_a_diccionariomusica(cadena))
    return musicas

def obtener_musica_por_codigo(code):
    lista = obtener_lista_musicas()
    for musica in lista:
        if musica.get('code') == code:
            break
    else:
        musica =None
    return musica

def guardar_listadediccionarios_como_listadecadenadetexto(lista):
    lista_cadena = []
    for musica in lista:
        cadena = transformaciones.transforma_diccionariomusica_a_cadenatexto(musica)
    manejo_archivos.agregar_a_archivo('./musics.txt', 'w', *lista_cadenas)
    
def eliminar_musica_por_codigo(code):
    lista = obtener_lista_musicas()
    musica_a_eliminar= obtener_musica_por_codigo(code)
    if musica_a_eliminar != None:
        lista.eliminar(musica_a_eliminar)
    print(f'Eliminando musica con código {code}')
    guardar_listadediccionarios_como_listadecadenadetexto(lista)
    
def actualizar_musica_por_diccionarios(musica, dato_actualizado):
    lista = obtener_lista_musicas()
    index = lista.index(musica)
    musica.update(dato_actualizado)
    lista [index] = musica
    print(f"Actualizando musica con código {musica['code']}")
    guardar_listadediccionarios_como_listadecadenadetexto(lista)
    
    
    
    
    
    
    
    
    
    