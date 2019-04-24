import funciones_musicas


def imprimir_encabezado_en_tablamusicas():
    print('%-5s%-12s%-12s%-12s%-20s%-15s%-12s' % ('Cod', 'Genero', 'Album','Autor','Fecha','Estado','Descripción'))
          
def imprimir_fila_en_tablamusica(musica):
    print('%(code)-5s%(genre)-12s%(album)-12s%(artist)-12s%(date)-20s%(state)-15s%(description)-12s' % musica)
    
          
def mostrar_lista_musicas():
    print("Lista de musicas:")
    lista = funciones_musicas.obtener_lista_musicas()
    imprimir_encabezado_en_tablamusicas()
    for musica in lista:
        imprimir_fila_en_tablamusica(musica)
    ordenar = True
    while (ordenar):
       respuesta =input("Desea ordenar la lista (Si/No): ")
       if (True if respuesta == "Si" else False):
           ordenar = True
           respuesta_orden =  input ("Como desea ordenar la lista?(A: ascendente/D: descendente):")
           if (True if respuesta_orden == "A" else False):
              ordenar = False
           else:
               ordenar = True
           print("0) Código")
           print("1) Género")
           print("2) Álbum")
           print("3) Autor")             
           print("4) Fecha de Publicación")
           print("5) Estado")
           print("6) Descripción")
           llave = input('Ingrese una llave a ordenar:')
           def llaves (value):
               try:
                   return {
                       0: 'code',
                       1: 'genre',
                       2: 'album',
                       3: 'artist',
                       4: 'date',
                       5: 'state',
                       6: 'description'
                   }[value]
               except KeyError:
                   print("Opción no definida")
           if (llave.isnumeric()):
               llave = int(llave)
               llave_a_ordennar = llaves(llave)
               def sortBy(elem):
                   return elem[llave_a_ordennar]
               impirmir_encabezado_en_tablamusicas()
               lista.sort(key=sortBy, reverse=ordenar)
               for musica in lista:
                   imprimir_fila_en_tablamusica(musica)
           else:
               ordenar = False
       else:
           ordenar = False
                        
# mostrar interfaz para la búsqueda de datos
def buscar_musica():
    print("Búsqueda de musica:")
    code = input ("Ingrese el código de la canción que desea buscar:")
    musica = funciones_musicas.obtener_musica_por_codigo(code)
    if musica != None:
        imprimir_encabezado_en_tablamusicas()
        imprimir_fila_en_tablamusica(musica)
    else:
        print(f"Musica con código {code} no existe")
                        
# mostrar interfaz para la eliminación de datos
def eliminar_musica():
    print("Elminar musica:")
    code = input ("Ingrese la música que desea eliminar:")
    funciones_musicas.eliminar_musica_por_codigo(code)

# mostrar interfaz para la actualización de datos
def actualizar_musica():
    print("Actualización de musicas:")
    code = input("Ingrese el código de música a actualizar: ")
    musica = funciones_musicas.obtener_musica_por_codigo(code)
    def opciones (value):
        try:
            return {
                0: 'genre',
                1: 'album',
                2: 'artist',
                3: 'date',
                4: 'state',
                5: 'description'
            }[value]
        except KeyError:
            print("Opción no definida")
    if musica != None:
        imprimir_encabezado_en_tablamusicas()
        imprimir_fila_en_tablamusica(musica)
        print("\nOpciones:")
        print("0) Actualizar genero")
        print("1) Actualizar album")
        print("2) Actualizar autor")
        print("3) Actualizar fecha de publicacion")
        print("4) Actualizar estado")
        print("5) Actualizar descripción")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            opcion_actualizar = int(read)
        try:
            llave_a_actualizar = opciones(opcion_actualizar)
            valor = input('Ingrese el nuevo valor: ')
            dato_a_actualizar = {
                llave_a_actualizar: valor
            }                
            funciones_musicas.actualizar_musica_por_diccionario(musica, dato_a_actualizar)
        except TypeError:
            print(f'Option {option}')
    else:
        print(f"Musica con código {code} no existe")           
                        
# seleccionador de acciones principales
def acciones (value):
    try:
        return {
            0: None,
            1: funciones_musicas.crear_musica,
            2: mostrar_lista_musicas,
            3: buscar_musica,
            4: eliminar_musica,
            5: actualizar_musica
        }[value]
    except KeyError:
        print("No existe esta acción")
                 
#función principal
def main(option):
    while option != 0:
        print("\nOpciones:")
        print("1) Ingresar una canción")
        print("2) Obtener lista de canciones")
        print("3) Buscar canción")
        print("4) Eliminar canción")
        print("5) Actualizar canción")
        print("0) Salir")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            option = int(read)
        try:
            acciones(option)()
        except TypeError:
            print(f'Option {option}')

main(-1)
                 
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
    
          
          