import graphviz
import os
from dataclasses import dataclass



@dataclass
class Casilla():
    color: chr
    fila: int
    colum: int
    nextCasilla: 'Casilla'


class Tablero():
    largo = int
    primerCasilla = Casilla
        

    def __init__(self):
        self.largo = 0
        self.primerCasilla = None


    def llenar(self, filas, columnas):
        # if self.primerCasilla is not None:
        #     raise Exception("El tablero ya está lleno.")        
               
        # num = 1
        for fila in range(0, columnas):
            for columna in range(0, filas):
                nueva_casilla = Casilla(" ", fila, columna, None)
                if self.primerCasilla is None:
                    self.primerCasilla = nueva_casilla
                    casilla_actual = self.primerCasilla
                else:
                    casilla_actual.nextCasilla = nueva_casilla
                    casilla_actual = nueva_casilla   
                #print(fila, columna,"")
                # num = num + 1             
 

    def imprimir(self, ancho: int):
        tempCasilla = self.primerCasilla
        cont = 1       
        while tempCasilla != None:
            print(f"[ {tempCasilla.color} ]", end="")
            tempCasilla = tempCasilla.nextCasilla
            if cont == ancho:            
                print("\n",end="")
                cont = 0        
            cont = cont + 1
        print("")    

    
    def pintar(self, fila, colum, color):
            current = self.primerCasilla                      
            
            while current is not None:
                if current.fila == fila and current.colum == colum:
                    current.color = color
                    print("Se ha modificado el color de la casilla", end="\n\n")
                    return  # Salir del bucle una vez que se haya encontrado y modificado la casilla
                current = current.nextCasilla  # Avanzar al siguiente nodo                 
        

    def grafica(self, filas, columnas):
        dot = graphviz.Digraph('Arbol', format='png', node_attr={'shape': 'circle', 'width': '0.9'})        # 'fixedsize': 'true' 

        tempCasilla = self.primerCasilla
        dot.node('100', label='Colorealo\nGuatematel', width='1.0')
        n = 0
        r = 0        

        for j in range(0, filas):     
            for i in range(0, columnas):
                color = tempCasilla.color
                if color == "A" or color == "a":
                    color = "lightblue"
                elif color == "R" or color == "r":
                    color = "red" 
                elif color == "V" or color == "v":
                    color = "green"
                elif color == "N" or color == "n":
                    color = "orange"
                elif color == "P" or color == "p":
                    color = "purple"
                else:
                    color = "lightgrey"               

                if j == 0:
                    orden = 100
                else:
                    orden = i + r

                dot.node(f'{i+n}', style='filled', fillcolor=f'{color}',color=f'{color}', fontcolor=f'{color}')  # f'{i}' es el nombre del nodo
                dot.edge(f'{orden}', f'{i+n}', )  # f'{i}' es el nombre del nodo
                tempCasilla = tempCasilla.nextCasilla               
                # print(orden, end=" ")
                # print(i+n, end=" ")
                
            if n > 1:    
                r = r + columnas
            n = n + columnas
              
                               
        
        dot.render('tablero', view=True)       


    def datos_estudiante(nombre_estudiante, carnet, curso, carrera, semestre):
        print("\n")
        print("...................................................................")
        print(f"Nombre del estudiante: {nombre_estudiante}")
        print(f"Carnet: {carnet}")
        print(f"Curso: {curso}")
        print(f"Carrera: {carrera}")
        print(f"Semestre: {semestre}")
        print("...................................................................")
        print("\n") 


    


def main():
    
    nombre_estudiante = "Carlos Hugo Rios Mancilla"
    carnet = "9520488"
    curso = "Introducción a la Programación y Computación 2 sección 'A'"
    carrera = "ingenieria en Ciencias y Sistemas"
    semestre = "4to Semestre"
    
    while True:    
        print("\nMenú:")
        print("1. Crear tablero")        
        print("2. Datos del estudiante")
        print("3. Salida")
        
        opcion = input("Seleccione una opción: ")
        os.system('cls')        
        if opcion == "1":
            print("...................................................................")
            
            colum = int(input("Ingrese el ancho del tablero: "))
            filas = int(input("Ingrese el alto del tablero: "))            

            print("...................................................................")
            print("\n", end = "")

            tablero = Tablero()
            tablero.llenar(colum, filas)

            # tablero = Tablero()            
            # for i in range(0, alto):
            #     for j in range(0, ancho):                    
            #         tablero.iniciar(i, j)
            tablero.imprimir(colum)
            
            print("...................................................................")
            print("\n", end = "")
            menu = ""

            while menu != 'n':
                print(" - Azul (A)")
                print(" - Rojo (R)")
                print(" - Verde (V)")                
                print(" - Naranja (N)")
                print(" - Purpura (P)", end = "\n\n")                                       

                color = input("Ingrese el color que desea: ")
                filac = int(input("Ingrese la fila: ")) - 1 
                columc = int(input("Ingrese la columna: ")) - 1                 
                tablero.pintar(filac, columc, color)
                tablero.imprimir(colum)                
                menu = input("Desea continuar? (s/n)\n Imprimir (i): ")
                if menu == "n":
                    menu = "n" 
                elif menu == "i":
                    tablero.grafica(filas, colum)
                # os.system('cls')
            
            
        elif opcion == "2": 
            Tablero.datos_estudiante(nombre_estudiante, carnet, curso, carrera, semestre)           
      
        elif opcion == "3":                        
            break        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    

main()
