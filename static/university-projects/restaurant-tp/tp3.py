import menus
import random


def validar(inf):
    n = int(input("Cantidad de comidas(mayor a " + str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error. Se pidio mayor a " + str(inf) + "Cargue de nuevo"))
    return n


def comidas(v):
    n = len(v)
    for i in range(n):
        nom = input("Ingrese el nombre de la comida " + str(i) + ": ")
        tipo = int(input("Ingrese el tipo de la comida: "))
        clas = int(input("Ingrese la clase de la comida: "))
        tiem = round(float(input("Ingrese el tiempo de coccion(en min): ")), 2)
        pre = round(float(input("Ingrese el precio de la comida: ")), 2)
        v[i] = menus.Menu(tipo, nom, clas, tiem, pre)
        print()


def manual():
    n = validar(0)
    v = n * [None]

    comidas(v)
    return v


def auto_comidas(v):

    n = len(v)
    entradas = ('Empanada', 'Tabla de fiambres', 'Dips variados', 'Buffet')
    principal = ('Pollo al Grill con verduras salteadas', 'Tira de Asado', 'Ravioles de verdura', 'Canelones con salsa Bolognesa', 'Matambre de cerdo asado')
    postre = ('Frutillas a la crema', 'Flan con dulce de leche', 'Torta tentación', 'Lemon Pie', 'Helado de frutilla y chocolate')

    for i in range(n):
        tipo = random.randint(0, 2)

        if tipo == 0:
            nom = random.choice(entradas)
        elif tipo == 1:
            nom = random.choice(principal)
        elif tipo == 2:
            nom = random.choice(postre)

        clas = random.randint(0, 3)
        tiem = round(random.random() * 90, 2)
        pre = round(random.random() * 200, 2)

        v[i] = menus.Menu(tipo, nom, clas, tiem, pre)

    print()


def automatica():
    n = random.randint(15, 20)
    v = n * [None]

    auto_comidas(v)
    return v


def carga():
    print('Carga de menú para el dueño...')

    op = 1
    while op != 3:
        print("1) Ingresar menús de forma manual")
        print("2) Ingresar menús de forma automatica")
        print("3) Dejar menú vacio")
        op = int(input("Ingrese la opcion deseada: "))

        if op == 1:
            v = manual()
        elif op == 2:
            v = automatica()
        elif op == 3:
            return None

        return v


def op1(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].nombre > v[j].nombre:
                v[i], v[j] = v[j], v[i]

    for i in v:
        print(menus.to_string(i))


def op2(v):

    tipo_comida = int(input("Ingrese el tipo de comida a analizar (Entrada=0, Principal=1, Postre=2): "))
    suma_precio = cantidad_comidas = 0

    for comida in v:
        if comida.tipo == tipo_comida:
            suma_precio += comida.precio
            cantidad_comidas += 1

    promedio_precio = suma_precio / cantidad_comidas

    if promedio_precio < 100:
        for comida in v:
            if comida.tipo == tipo_comida:
                comida.precio = round(comida.precio * 1.1, 2)

    print('El precio promedio es: $', promedio_precio)

    for comida in v:
        if comida.tipo == tipo_comida:
            print(menus.to_string(comida))


    print()


def op3(v):
    menor_tiempo = 1000

    for comida in v:
        if comida.tiempo < menor_tiempo:
            menor_tiempo = comida.tiempo

    for comida in v:
        if comida.tiempo == menor_tiempo:
            print(menus.to_string(comida))

    print()


def op4(v):
    clasif = 4 * [0]
    for i in range(4):
        print('Cantidad de comidas en la clasificación ' + str(i), end=': ')
        for comida in v:
            if comida.clasificacion == i:
                clasif[i] += 1
        print(clasif[i])
    print()


def buscar_comida(v, nombre):
    for comida in v:
        if comida.nombre == nombre and comida.tipo == 1:
            return comida
    return False


def sugerencias(v, buscada, i):
    for comida in v:
        if comida.clasificacion == buscada.clasificacion and comida.tipo == i:
            return comida
    return 'No existe una comida de clasificación ' + str(buscada.clasificacion) + ' y tipo ' + str(i)



def op5(v):
    nombre = input('ingrese el nombre de la comida que desea buscar: ')
    sug = 3 * [0]
    sug[1] = buscar_comida(v, nombre)
    if sug[1]:
        print('La comida si existe: \n' + menus.to_string(sug[1]))
        print('Sugerencias:')
        sug[0] = sugerencias(v, sug[1], 0)
        sug[2] = sugerencias(v, sug[1], 2)
        print(menus.to_string(sug[0]))
        print(menus.to_string(sug[2]))
    else:
        print('No existe dicho plato principal')


def comidadeldia(v, clasif, i):
    for comida in v:
        if comida.clasificacion == clasif and comida.tipo == i:
            return comida


def op6(v):
    clasif = int(input('ingrese la clasificación que desea (0: Estandar / 1: Sin TACC / 2: Vegetariano / 3: Light): '))
    print('El menú del día es: ')

    preciototal = 0
    tiempototal = 0
    for i in range(3):
        comida = comidadeldia(v, clasif, i)
        print(menus.to_string(comida))
        preciototal += comida.precio
        tiempototal += comida.tiempo
    print('Tiempo total: ', tiempototal)
    print('Precio total: ', preciototal)






def test():

    v = carga()


    op = 1

    while op != 7:
        print('Opciones para el comensal: ')
        print("1) Consultar carta")
        print("2) Precio promedio")
        print("3) Menor tiempo de coccion")
        print("4) Comidas por tipo")
        print("5) Buscar y sugerir")
        print("6) Menu del dia")
        print("7) Salir")
        op = int(input("Ingrese el numero de la opcion deseada: "))

        if op == 1:
            op1(v)

        elif op == 2:
            op2(v)

        elif op == 3:
            op3(v)

        elif op == 4:
            op4(v)

        elif op == 5:
            op5(v)

        elif op == 6:
            op6(v)

        elif op == 7:
            print("Programa terminado. I will back...")


if __name__ == "__main__":
    test()
