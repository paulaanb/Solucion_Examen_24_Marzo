class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def añadirAnterior(self, posanterior):
        posanterior.anterior=self.anterior
        posanterior.siguiente = self
        if(self.anterior!=None):
            self.anterior.siguiente=posanterior
        self.anterior = posanterior
        return posanterior

    def añadirSiguiente(self, possiguiente):
        possiguiente.siguiente=self.siguiente
        possiguiente.anterior = self
        if(self.siguiente!=None):
            self.siguiente.anterior=possiguiente
        self.siguiente = possiguiente
        return possiguiente

    def eliminar(self):
        if(self.anterior!=None):
            self.anterior.siguiente=self.siguiente
        if(self.siguiente!=None):
            self.siguiente.anterior=self.anterior

    def nodoant(self):
        return self.anterior

    def nodosig(self):
        return self.siguiente

    def getvalue(self):
        return self.valor

    def primero(self):
        copia=self
        while copia.anterior!= None:
            copia=copia.anterior
        return copia

    def ultimo(self):
        copia=self
        while copia.siguiente!= None:
            copia=copia.siguiente
        return copia
#Imprimir desde cualquier nodo hasta el final
    def imprimir(self):
        copia=self
        while copia!=None:
            print(copia.getvalue())
            copia=copia.siguiente
#Imprimir todo desde el principio
    def imprimirdesdeprincipio(self):
        copia=self.primero()
        while copia!=None:
            print(copia.getvalue())
            copia=copia.siguiente

    def imprimirdesdefinal(self):
        copia=self.ultimo()
        while copia!=None:
            print(copia.getvalue())
            copia=copia.anterior

if __name__ == '__main__':
    elemento=Nodo(30)
    elemento=elemento.añadirSiguiente(Nodo(50))
    elemento=elemento.añadirSiguiente(Nodo(32))
    print("Imprimir con tres nodos")
    elemento.primero().imprimir()
    nodoborrar=elemento
    elemento=elemento.añadirSiguiente(Nodo(88))
    elemento=elemento.añadirAnterior(Nodo(54))
    print("Imprimir añadiendo detrás de un nodo")
    elemento.primero().imprimir()
    elemento=nodoborrar.añadirSiguiente(Nodo(1))
    nodoborrar.eliminar()
    print("Lista desde el principio")
    elemento.imprimirdesdeprincipio()
    print("Lista al revés")
    elemento.imprimirdesdefinal()