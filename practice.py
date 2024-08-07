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
            