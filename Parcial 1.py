import os
os.system('cls')

class personaje():
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, daño):
        self.vida = self.vida - daño
        if(self.vida>0):
            print(f"vida actual {self.vida}")
        else:
            print(f"se murio (vida={self.vida})")

    def mover(self, direccion):
        print(f"se movio hacia {direccion} {self.velocidad} posiciones")

class soldado(personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.__ataque= ataque
    
    def atacar(self):
        return self.__ataque

class campesino(personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.__cosecha = cosecha
    
    def getcosecha(self):
        return self.__cosecha 
    
    def setcosecha(self, cosecha):
        self.__cosecha = self.__cosecha + cosecha
    
    cosecha = property(getcosecha, setcosecha)

pedro=campesino(45, 20, 5, 0)
juan = campesino(35, 20, 4, 0)
mati= soldado(100, 10, 7, 30)
agustin = soldado(80, 10, 8, 20)

def accionesCampesino(nombre):
    while True:
        print("1= mostrar cosechado")
        print("2= cosechar")
        print("3= moverse")
        print("0= salir")
        y=int(input())
        if (y==1):
            print(f"cosecho={nombre.cosecha}")
        elif(y==2):
            print("ingresar cantidad= ", end="")
            nombre.cosecha = int(input())
        elif(y==3):
            print("ingresar direccion= ", end="")
            x = input()
            nombre.mover(x)
        elif(y==0):
            break

def accionesSoldado(nombre, soldado2):
    while True:
        print("1= atacar")
        print("2= moverse")
        print("0= salir")
        y=int(input())
        if (y==1):
            print("¿a quien ataca?")
            print(f"1=el otro soldado")
            print("2=pedro")
            print("3=juan")
            z=int(input())
            if(z==1):
                soldado2.recibir_ataque(nombre.atacar())
            elif(z==2):
                pedro.recibir_ataque(nombre.atacar())
            elif(z==3):
                juan.recibir_ataque(nombre.atacar())
        elif(y==2):
            print("ingresar direccion= ", end="")
            x = input()
            nombre.mover(x)
        elif(y==0):
            break


while True:
    print("selecciones personaje")
    print("1= pedro")
    print("2= juan")
    print("3= mati")
    print("4= agustin")
    x = int(input())
    if(x==1):
        print("seleccionaste a pedro")
        accionesCampesino(pedro)
    elif(x==2):
        print("seleccionaste a juan")
        accionesCampesino(juan)
    elif(x==3):
        print("seleccionaste a mati")
        accionesSoldado(mati, agustin)
    elif(x==4):
        print("seleccionaste a agustin") 
        accionesSoldado(agustin, mati)  
    else:
        print("valor incorrecto") 
    
    



    
    
    

    

        