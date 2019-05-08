def transformar_cadenatexto_a_diccionarioartista(linea):
    partes_linea = (linea + "").replace("\n", "").split(';')
    artista = {
        'code': partes_linea[0],
        'nombre': partes_linea[1],
        'album': partes_linea[2],
        'edad': partes_linea[3],
        'sexo': partes_linea[4],
        'state': partes_linea[6],
        'description': partes_linea[5]
    }
    return artista

def transformar_diccionarioartista_a_cadenatexto(artista):
    return f"{artista['code']};{artista['nombre']};{artista['album']};{artista['edad']};{artista['sexo']};{artista['description']};{artista['state']}"