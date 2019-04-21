def transformar_cadenatexto_a_diccionariomusica(linea):
    partes_linea = (linea + "").replace("\n", "").split(';')
    musica = {
        'code': partes_linea[0],
        'genre': partes_linea[1],
        'album': partes_linea[2],
        'artist': partes_linea[3],
        'date': partes_linea[4],
        'description': partes_linea[5]
    }
    return musica

def transformar_diccioanriomusica_a_cadenatexto(musica):
    return f"{musica['code']};{musica['genre']};{musica['album']};{musica['artist']};{musica['date']};{mascota['description']}"