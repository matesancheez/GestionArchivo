from registro import *
import pickle
import os.path
from datetime import datetime


def add_in_order(vec, reg):
    n = len(vec)
    pos = n
    izq , der = 0, n - 1
    while izq <= der:
        centro = (izq + der) // 2
        if vec[centro].rep == reg.rep:
            pos = centro
            break
        if vec[centro].rep> reg.rep:
            izq = centro + 1
        else:
            der = centro - 1 
    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def load_in_order(archivo, vec):
    primera = True
    omitidos, contados = 0, 0
    m = open(archivo, "rt", encoding="utf-8")    
    for linea in m:
        if primera is True: 
            primera = False
        else:
            proyecto = str_toproyecto(linea)
            if proyecto.lenguaje != "":
                add_in_order(vec, proyecto)
                contados += 1
            else: 
                omitidos += 1
    m.close()

    for i in range(len(vec)):
        print(to_string(vec[i]))

    print()
    print("-"*40)
    print("Proyectos Omitidos: {}".format(omitidos))
    print("Proyectos Contados: {}".format(contados))
    print()


def eliminar_k(vec):
    for i in range(len(vec)):
        l = vec[i].estrellas.replace("k", "")
        vec[i].estrellas = l


def filtrar_tag(vec, tag):
    cant_estrellas = 0
    mensaje = "\nIngrese 1 para generar archivo .csv y visualizar los datos \
             \nIngrese 2 para solamente visualizar los datos:\
             \n >>> "

    op = validar_opcion(mensaje)
    
    if op == 1:
        filtrado = open("filtrado.csv", "w")
        filtrado.write("Nombre|Fecha de actualizacion|estrellas\n")
    
    for i in range(len(vec)):
        if tag in vec[i].tags: 
            eliminar_k(vec)

            if vec[i].estrellas < "10":
                cant_estrellas = "1"
            elif "10" < vec[i].estrellas <= "20":
                cant_estrellas = "2"
            elif "20" < vec[i].estrellas <= "30":
                cant_estrellas = "3"
            elif "30" < vec[i].estrellas <= "40":
                cant_estrellas = "4"
            elif vec[i].estrellas > "40":
                cant_estrellas = "5"


            if op == 1:
                filtrado = open("filtrado.csv", "a")
                filtrado.write(vec[i].nombre)
                filtrado.write("|")
                filtrado.write(vec[i].fecha)
                filtrado.write("|")
                filtrado.write(str(cant_estrellas) + "\n")
                filtrado.close()
                
            elif op == 2:
                print()
                print("Proyecto N*{}".format(i))
                print("Nombre: {}".format(vec[i].nombre))
                print("Fecha de actualizacion: {}".format(vec[i].fecha))
                print("Tiene {} estrellas".format(cant_estrellas))
                print()
        
    
    print()   
    print("Opcion 2 ejecutada con exito.")
    print()   

        
def lenguajes(vec):
    l = []
    #uso diccionarios porque no puede contener repetidos, esto hace mas facil el conteo
    repeticiones = {}

    for i in range(len(vec)):
        l.append(vec[i].lenguaje)

    for lenguaje in l:
        if lenguaje in repeticiones :
            repeticiones[lenguaje] += 1
        else:
            repeticiones[lenguaje] = 0

    return repeticiones


def popularidad(vec):
    filas = 12
    columnas = 5

    matriz = [[0 for x in range(columnas)] for i in range(filas)]

    for i in range(len(vec)):
        token = vec[i].fecha.split("-")
        mes = int(token[1]) - 1
        if vec[i].estrellas < "10":
            matriz[mes][0] += 1
        elif "10" < vec[i].estrellas <= "20":
            matriz[mes][1] += 1
        elif "20" < vec[i].estrellas <= "30":
            matriz[mes][2] += 1
        elif "30" < vec[i].estrellas <= "40":
            matriz[mes][3] += 1
        elif vec[i].estrellas > "40":
            matriz[mes][4] += 1
    
    return matriz


def guardar_populares(matriz, vec2):

    for i in range(len(matriz)):
        mes = i + 1
        suma = 0
        for j in range(len(matriz[i])):
            estrellas = j + 1
            suma = matriz[i][j]

            if suma > 0:
                popular = Populares(mes, estrellas, suma)
                vec2.append(popular)


def validar_opcion(mensaje):
    r = 0
    while r >= 0:
        r = int(input(mensaje))
        if r < 0:
            print("Error! Se ingreso un numero invalido")

        return r


def buscar(vec, rep):
    for i in range(len(vec)):
        if vec[i].rep == rep:
            return i
    return -1


def main():
    op = 0
    vec , vec2 = [], []

    while op != 8:
        print()
        print("Opciones disponibles:\
            \n1. Crear vector con archivo existente.\
            \n2. Filtrar proyectos por su tag.\
            \n3. Mostrar los lenguajes que fueron usados y en que cantidad.\
            \n4. Mostrar popularidad de los proyectos.\
            \n5. Buscar y actualizar proyecto en el archivo.\
            \n6. Guardar los proyectos populares y generar archivo binario.\
            \n7. Leer archivo binario.\
            \n8. Salir")
        print()
        op = validar_opcion('Ingrese una opcion: ')
        print()
        if op == 1:
            load_in_order("proyectos.csv", vec)
            print("Vector creado. Hora de trabajar!!")

        elif op == 2:
            if vec == []:
                print("Error no se generaron datos...")
            else:
                tag = input("Tag por la que desea filtrar: ")
                filtrar_tag(vec, tag)

        elif op == 3:
            l = lenguajes(vec)
            cont = 0
            for lenguaje in l:
                cont += 1
                print()
                print("{}>> {:<20}: {}".format(cont, lenguaje, l[lenguaje]))

        elif op == 4:
            if vec == []:
                print("Error no se generaron datos...")
            else:
                suma = 0
                mensaje1 = "Ingrese el numero de mes que desea saber la cantidad de proyectos: "
                m = validar_opcion(mensaje1)
                matriz = popularidad(vec)

                print()
                print("<<<< Matriz de todos los meses >>>>")
                r = "{} {:>2}|{:>2}|{:>2}|{:>2}|{:>2}".format("Estrellas :", "1", "2", "3", "4", "5") 
                print(r)       
                for k in range(len(matriz)):
                    print("Mes{:<3}:     {}".format(k+1, matriz[k] ))
                    

                for j in range(len(matriz[m-1])):
                    suma+= matriz[m-1][j]
                    
                print()
                print("Total de proyectos en el mes {} es de: ".format(m), suma)
                print()

        elif op == 5:
            if vec == []:
                print("Error no se generaron datos...")
            else:
                rep = input("Repositorio a ser buscado: ")
                print("Buscando repositorio...")
                print()
                
                a = buscar(vec, rep)
                if a == -1:
                    print("No se encontro el proyecto.")
                    print()
                else:
                    print("Proyecto encontrado.")
                    actual = datetime.now()
                    año = actual.year
                    mes = actual.month
                    dia = actual.day
                    
                    url = input("Ingrese el url para actualizarlo: ")
                
                    vec[a].url = url
                    #Se hizo de esta forma porque con datetime.date() formateaba en año-mes-dia
                    vec[a].act = "{}-{}-{}".format(dia, mes, año)
                    
                    ar = open("proyectos.csv", mode="wt", encoding="utf8")
                    ar.write("nombre_usuario|repositorio|descripcion|fecha_actualizacion|lenguaje|estrellas|tags|url\n")
                    for i in range(len(vec)):
                        ar.write(vec[i].nombre)
                        ar.write("|")
                        ar.write(vec[i].rep)
                        ar.write("|")
                        ar.write(vec[i].desc)
                        ar.write("|")
                        ar.write(vec[i].fecha)
                        ar.write("|")
                        ar.write(vec[i].lenguaje)
                        ar.write("|")
                        ar.write(vec[i].estrellas)
                        ar.write("|")
                        ar.write(vec[i].tags)
                        ar.write("|")
                        ar.write(vec[i].url)

                    print("Se ejecuto la opcion con exito...")
                    print("Los datos del achivo cambiaron.")
                    print()

        elif op == 6:
            if vec == []:
                print("Error no se generaron datos...")
            else:
                if matriz == None:
                    print("No se puede ejecutar...")
                    print("Se debe generar una matriz primero (opcion 4).")
                    print()
                else:    
                    guardar_populares(matriz, vec2)
                    nombre = "populares.dat"
                    ar = open(nombre, "wb")
                    for i in range(len(vec2)):
                        pickle.dump(vec2[i], ar)
                    ar.close()

                    print()
                    print("Opcion 6 ejecutada con exito...")
                    print("Archivo '{}' creado correctamente.".format(nombre))
        
        elif op == 7:
            if vec == []:
                print("Error no se generaron datos...")
            else:
                archivo = "populares.dat"
                if not os.path.exists(archivo):
                    print("No exsiste el atchivo...")
                    print("Primero ejecute opcion 6")
                    print()
                    
                else: 
                    m = open(archivo, "rb") 
                    t = os.path.getsize(archivo)
                    
                    print("Datos que contiene el archivo:")
                    
                    while m.tell() < t: 
                        populares = pickle.load(m)
                        display(populares)
                    m.close() 

        elif op == 8:
            print("Muchas gracias por usar el programa.Adios!!")

        else:
            print("Opcion seleccionada inexistente...")

if __name__ == "__main__":
    main()
