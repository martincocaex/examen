productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}








def agregar_precio(stock:str):
    stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
            'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
            'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}
stock['123FHD','fgdxFHD','GF75HD','2175HD','123FHD', 'UWU131HD','JjfFHD', '342FHD','FS1230HD'].append()




def validador_entero_positivo(msg_input:str):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("No se pueden ingresar numeros negativos")
                continue
        except ValueError:
            print("Solo se pueden ingresar numeros enteros")




def validar_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto



        

def validador_opciones():
    while True:
        try:
            opcion = (int(input("Ingrese una opcion 1 - 4: ")))
            if opcion < 1 or opcion >4:
                print("Error debe ingresar un numero en el rango del 1 - 4. ")
                continue
            return opcion
        except ValueError:
            print("Error opcion no esta en el rango de numeros (1 - 4)" )
            continue




def p_min(mensaje_input:str):
    while True:
        try:
            numero_min = int(input(mensaje_input))
            if numero_min <= 0:
                print("No puede ingresar numeros negativos o menor que 0")
                continue
        except ValueError:
            print("Solo se pueden ingresar numeros enteros ")
            continue


def p_max(msg_input:str):
    while True:
        try:
            numero_max = int(input(msg_input))
            if numero_max <= 1000000:
                print("No hay notebooks en ese rango de precios")
                continue
        except ValueError:
            print("Solo se pueden ingresar numeros enteros.")
            continue

nuevo_precio = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
                'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
                'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}
                   



def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("[1] - Stock marca")
        print("[2] - Busqueda por precio")
        print("[3] - Actualizar Precio")
        print("[4] - Salir.")


        opcion = validador_opciones()

        if opcion == 1:
            marca = str(input("Ingrese marca a consultar: "))
            if marca == 'HP':
                print(f"{stock['8475HD']}, {stock['fgdxFHD']}")
            
            elif marca == 'lenovo':
                print(f"{stock['2175HD']}, {stock['123FHD']}, {stock['342FHD']}")
            

            elif marca == 'Asus':
                print(f"{stock['JjfFHD']}, {stock['GF75HD']}")
            
            elif marca == 'Dell':
                print(f"{stock['UWU131HD']}")
        

        
        if opcion == 2:
            precio_min = p_min("Ingrese precio minimo: ")
            precio_max =  p_max("Ingrese precio maximo: ")
            
            if precio_min and precio_max == 0 and 249980:
                print("No se encuentran notebooks en ese rango de precio.")
                

            elif precio_min and precio_max == 0 and 749990:
                print(f"{productos['123FHD'], productos['2175HD'], productos['342FHD'], productos['8475HD',productos['fgdxFHD'], productos['GF75HD'],productos ['JjfFHD'], productos['UWU131HD']]}")

            
        






        if opcion == 3:
            modelos_actualizar = str(input("Ingrese el modelo a actulizar: "))
            if modelos_actualizar == '8475HD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")

            elif modelos_actualizar == 'fgdxFHD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")
            
            elif modelos_actualizar == 'GF75HD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")
            elif modelos_actualizar == '2175HD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")
            elif modelos_actualizar == '123FHD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")
            
            elif modelos_actualizar == 'JjfFHD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")


            elif modelos_actualizar == '342FHD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")

            elif modelos_actualizar == 'FS1230HD':
                nuevo_precio = agregar_precio("Ingrese nuevo precio")
                print("Precio actualizado")

            else:
                print("No se a podido modificar el precio del producto.")
                continue
    


        if opcion == 4:
            print("Programa finalizado.")
            break



























menu()