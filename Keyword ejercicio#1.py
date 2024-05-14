def add_keyword():
    
    try: 
        with open( fichero , 'a') as file:
            file.write( '\n'.  join( nueva_keyword ) + '\n')
            print("Agregada correctamente")
    except:
        print(f"Error: {e}")
        
    menu()
    

def show_ketwords():
    
        fichero = open('keywords.txt', 'r')
        #secuencia para imprimir de a 20 palabras
        menu()
    

def menu():
    
    opcion = int(input(("KEYWORD\n[1] - IMPLEMETAR PALABRAS CLAVE\n[2] - MOTRAR PALABRAS CLAVE \n[3] - SALIR\nINGRESE LA ACCION QUE DESEA REALIZAR: ")))
    
    while opcion != 3:
        
        if opcion == 1:
            fichero = 'keywords.txt'
            nueva_keyword = input("INGRESE LA PALABRA QUE DESEA IMPLEMENTAR")
            add_keyword(fichero , nueva_keyword)
          
        if opcion == 2:
            fichero = 'keywords.txt'
            show_ketwords()

        break
    
menu()