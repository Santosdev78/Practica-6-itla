import os
precio = 0
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
    while opc!='6':
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
            if cantidad<=0:
                print("No se puede ingresar una cantidad negativa, ni tampoco 0")
                input ("Presione enter para volver al menu: ")
            precio_tot = 50 * cantidad
            agregar_al_carrito (id,productos,cantidad,precio_tot)
        elif opc=="2": 
            id=2
            cantidad = int(input("Cuantas lbs de habichuelas quieres: "))
            if cantidad<=0:
                print("No se puede ingresar una cantidad negativa, ni tampoco 0")
                input ("Presione enter para volver al menu: ")
            precio_tot = 80 * cantidad
            agregar_al_carrito (id,productos,cantidad,precio_tot)
        elif opc=="3":
            id=3
            cantidad = int(input("Cuantas lbs de aceite quieres: "))
            if cantidad<=0:
                print("No se puede ingresar una cantidad negativa, ni tampoco 0")
                input ("Presione enter para volver al menu: ")
            precio_tot = 300 * cantidad
            agregar_al_carrito (id,productos,cantidad,precio_tot)
        elif opc=="4":
            id=4
            cantidad = int(input("Cuantas lbs de pollo quieres: "))
            if cantidad<=0:
                print("No se puede ingresar una cantidad negativa, ni tampoco 0")
                input ("Presione enter para volver al menu: ")
            precio_tot = 85 * cantidad
            agregar_al_carrito (id,productos,cantidad,precio_tot)
        elif opc=="5":
            id=5
            cantidad = int(input("Cuantas lbs de lechuga quieres: "))
            if cantidad<=0:
                print("No se puede ingresar una cantidad negativa, ni tampoco 0")
                input ("Presione enter para volver al menu: ")
                precio_tot = 80 * cantidad
            agregar_al_carrito (id,productos,cantidad,precio_tot)
        elif opc=="6":
            print ("Adios")
            print (carrito)

def buscar_producto(id, productos):
    for producto in productos:
        if producto['id']==int(id):
            return producto
    return None

def agregar_al_carrito (id,productos,cantidad,precio_tot):
    producto = buscar_producto(id,productos)
    if producto == None:
        print ("El producto seleccionado no existe")
    elif producto != None:
        if id == 1:
            carrito.append({"id": 1,"producto":"arroz","precio":50,"cantidad":cantidad,"precio total":precio_tot})
        elif id == 2:
            carrito.append({"id": 2,"producto":"habichuelas","precio":80,"cantidad":cantidad,"precio total":precio_tot})
        elif id == 3:
            carrito.append({"id": 3,"producto":"aceite","precio":300,"cantidad":cantidad,"precio total":precio_tot})
        elif id == 4:
            carrito.append({"id": 4,"producto":"pollo","precio":85,"cantidad":cantidad,"precio total":precio_tot})
        elif id == 5:
            carrito.append({"id": 5,"producto":"lechuga","precio":80,"cantidad":cantidad,"precio total":precio_tot })
            
print(menu(productos))