class Menu:
    def __init__(self, tipo=0, nom='', clas=0, tiem=0.0, pre=0.0):
        self.tipo = tipo
        self.nombre = nom
        self.clasificacion = clas
        self.tiempo = tiem
        self.precio = pre


def to_string(menu):
    r = ''
    r += '{:<10}'.format('Tipo: ' + str(menu.tipo))
    r += '{:<50}'.format('Nombre: ' + menu.nombre)
    r += '{:<10}'.format('Clase: ' + str(menu.clasificacion))
    r += '{:<15}'.format('Tiempo: ' + str(menu.tiempo))
    r += '{:<15}'.format('Precio: $' + str(menu.precio))
    return r




