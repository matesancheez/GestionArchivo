
class Proyectos:
    def __init__(self, nombre, rep, desc, fecha, lenguaje, estrellas, tags, url):
        self.nombre = nombre
        self.rep = rep
        self.desc = desc
        self.fecha = fecha
        self.lenguaje = lenguaje
        self.estrellas = estrellas
        self.tags = tags
        self.url = url

def to_string(proy):
    res = ''
    res += 'Nombre de usuario: {:<10}'.format(str(proy.nombre))
    res += '\nRepositorio: {:<10}'.format(str(proy.rep))
    res += '\nDescripcion : {:<100}'.format(str(proy.desc))
    res += '\nFecha de actualizacion: {:<10}'.format(str(proy.fecha))
    res += '\nLenguaje: {:<10}'.format(str(proy.lenguaje))
    res += '\nEstrellas: {:<8}'.format(str(proy.estrellas))
    res += '\nTags: {:<400}'.format(str(proy.tags))
    res += '\nUrl: {:<70}'.format(str(proy.url))
    return res


def str_toproyecto(linea):
    token = linea.split('|')
    nombre = token[0]
    rep = token[1]
    desc = token[2]
    fecha = token[3]
    lenguaje = token[4]
    estrellas = token[5]
    tags = token[6]
    url = token[7]
    proyecto = Proyectos(nombre, rep, desc, fecha, lenguaje, estrellas, tags, url)
    return proyecto
        
class Populares: 
    def __init__(self, mes, estrellas, suma): 
        self.mes = mes 
        self.estrellas = estrellas 
        self.suma = suma 


def display(populares): 
    print(' - Mes: {:<5}'.format(populares.mes)) 
    print(' - Estrellas: {:<5}'.format(populares.estrellas)) 
    print(' - Suma: {:<5}'.format(populares.suma))


class Lenguajes:
    def __init__(self, lenguaje, cantidad):
        self.lenguaje = lenguaje
        self.cantidad = cantidad


    def __str__(self):
        r = 'Lenguaje: {} Veces usado: {}'.format(self.lenguaje, self.cantidad)
        return r