
class Animal():
    def __init__(self,name):
        self.name=name

class Mamifero(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

class Oviparo(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

class Gato(Mamifero):
    def __init__(self,name):
        Mamifero.__init__(self,name)

class Ornitorrinco(Mamifero,Oviparo):
    def __init__(self,name):
        Mamifero.__init__(self,name)
        Oviparo.__init__(self,name)

class Pato(Oviparo):
    def __init__(self,name):
        Oviparo.__init__(self,name)
