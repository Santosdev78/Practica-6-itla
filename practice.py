import os

productos = [
{"id": 1,"producto":"arroz","precio":50 },
{"id": 2,"producto":"habichuelas","precio":80 },
{"id": 3,"producto":"aceite","precio":300 },
{"id": 4,"producto":"pollo","precio":85 },
{"id": 5,"producto":"lechuga","precio":80 }
]
carrito=[]
def menu(productos):
    opc=''
    vol_agregar="si"
    while opc!="6":
        os.system("cls")
        print('''
            ---Menú---
            1. Arroz -> RD$50
            2. Habichuelas -> RD$80
            3. Aceite -> RD$300
            4. Pollo -> RD$85
            5. Lechuga -> RD$80
            6. Salir
            ''')
        opc=input("Elige una de las opciones: ")
        if opc=="1":
            id=1
            cantidad = int(input("Cuantas lbs de arroz quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
                menu(productos)
            else:
                precio_tot = 50 * cantidad
                agregar_al_carrito (id,productos,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                while vol_agregar == "si":
                    menu(productos)
                if vol_agregar != "si":
                    opc="6"
                    mostrar_carrito(carrito)
                    print ("Adios")
                    input()
        elif opc=="2": 
            id=2
            cantidad = int(input("Cuantas lbs de habichuelas quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
                menu(productos)
            else:
                precio_tot = 80 * cantidad
                agregar_al_carrito (id,productos,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                while vol_agregar == "si":
                    menu(productos)
                if vol_agregar != "si":
                    opc="6"
                    mostrar_carrito(carrito)
                    print ("Adios")
                    input()
        elif opc=="3":  
            id=3
            cantidad = int(input("Cuantas lbs de aceite quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
                menu(productos)
            else:
                precio_tot = 300 * cantidad
                agregar_al_carrito (id,productos,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                while vol_agregar == "si":
                    menu(productos)
                if vol_agregar != "si":
                    opc="6"
                    mostrar_carrito(carrito)
                    print ("Adios")
                    input()
        elif opc=="4":
            id=4
            cantidad = int(input("Cuantas lbs de pollo quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
                menu(productos)
            else:
                precio_tot = 85 * cantidad
                agregar_al_carrito (id,productos,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                while vol_agregar == "si":
                    menu(productos)
                if vol_agregar != "si":
                    opc="6"
                    mostrar_carrito(carrito)
                    print ("Adios")
                    input()
        elif opc=="5":
            id=5
            cantidad = int(input("Cuantas lbs de lechuga quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
                menu(productos)
            else:
                precio_tot = 80 * cantidad
                agregar_al_carrito (id,productos,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                while vol_agregar == "si":
                    menu(productos)
                if vol_agregar != "si":
                    opc="6"
                    mostrar_carrito(carrito)
                    print ("Adios")
                    input()
        elif opc=="6":
            mostrar_carrito(carrito)
            print ("Adios")
            input()
        else:
            id=int(opc)
            producto=buscar_producto(id,productos)
            if producto == None:
                print("El producto seleccionado no existe")
                input ("Presione ENTER para volver al menu:")

def buscar_producto(id, productos):
    for producto in productos:
        if producto['id']==int(id):
            return producto
    return None

def agregar_al_carrito (id,productos,cantidad,precio_tot):
    if id == 1:
            carrito.append({"id": 1,"producto":"arroz","precio":50,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 2:
            carrito.append({"id": 2,"producto":"habichuelas","precio":80,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 3:
            carrito.append({"id": 3,"producto":"aceite","precio":300,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 4:
            carrito.append({"id": 4,"producto":"pollo","precio":85,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 5:
            carrito.append({"id": 5,"producto":"lechuga","precio":80,"cantidad":cantidad,"precio total":precio_tot})

def mostrar_carrito (carrito):
    for producto in carrito:
        print("----------------------------") 
        print("ID:", producto['id'])   
        print("Producto:", producto['producto'])
        print("Precio Unidad:",producto['precio'])
        print("Cantidad:",producto['cantidad'])
        print("Precio Total:",producto["precio total"])
        print("----------------------------") 
    subtotal = sum([producto['precio'] * producto['cantidad'] for producto in carrito])
    impuesto = subtotal*0.18
    total=subtotal+impuesto
    print("----------------------------") 
    print ("Su subtotal fue de:",subtotal)
    print ("El precio final fue de:",total," con: ",impuesto," de impuesto")
    print("----------------------------") 
print(menu(productos))
