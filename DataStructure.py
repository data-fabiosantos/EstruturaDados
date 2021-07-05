from console_logging.console import Console
console = Console()


class Battery:
    

    def __init__(self):
        console.log("start batteries ")
        self.__battery = []
        

    def push(self, value):
        console.log("push " + str(value))
        self.__battery.append(value)


    def pop(self):
        console.info("Pop")
        return self.__battery.pop()


    def show(self):
        console.success("Battery: {}".format(self.__battery))


class Filas:
    def __init__(self):
        console.log("Starting")
        self.__fila = []


    def insere(self, value):
        console.log("Inserindo " + str(value))
        self.__fila.append(value)


    def remove(self):
        console.log("POP DATA")
        return self.__fila.pop(0)


    def show(self):
        console.success(f'Queue: {self.__fila}')


class Node:
    def __init__(self, value, arquivo , next=None):
        self.__value = value
        self.arquivo = arquivo
        self.next = next

    @property
    def value(self):
        return self.__value

#ListaEncadeadaSimples

class simplelist:
    def __init__(self):
        self.__main_node = None

    def append(self, value,arquivo):
        if self.__main_node is None:
            self.__main_node = Node(value,arquivo)
            return

        next_node = self.__main_node
        while next_node.next is not None:
            next_node = next_node.next
        next_node.next = Node(value,arquivo)

    def remove(self, value):
        if self.__main_node is None:
            return

        left_node = None
        next_node = self.__main_node

        if next_node.value == value:
            self.__main_node = next_node.next

        while True:
            left_node = next_node
            next_node = next_node.next

            if next_node is None:
                break

            if next_node.value == value:
                left_node.next = next_node.next

    def show(self):
        values = []
        next_node = self.__main_node
        while next_node is not None:
            data = {
              "arquivo.txt":  next_node.arquivo,
              "frequencia": next_node.value
            }
            values.append(data)
            next_node = next_node.next
        list_ordenada = sorted(values, key=lambda k: k['frequencia']) 
            
            
        print("list_ordenada: {}".format(list_ordenada))

#Fim