class Nodo:
    def __init__(self,dato):
        self.elemento = dato
        self.next = None
#lista
class Lista:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    def print(self):
        temp = self.head
        cadena = ''
        while(temp is not None):
            print(temp.elemento)
            cadena += str(temp.elemento) + ' '
            temp = temp.next
        return cadena
    def append(self,dato):
        nodo = Nodo(dato)
        if self.length == 0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo
        self.length += 1
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head 
        pre = self.head
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return str(temp.elemento)
