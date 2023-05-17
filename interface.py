from tkinter import *
from filosofos import *

root= Tk()
root.geometry("600x600")

#crea una interfaz para mostrar a los filosofos
class Filosofo:
    def __init__(self):
        super().__init__()
        self.id = filosofo.count
        filosofo.count += 1
        filosofo.estado.append('PENSANDO')
        filosofo.tenedores.append(threading.Semaphore(0))
        print("Filosofo {} pensando".format(self.id))
        self.label = Label(root, text="Filosofo {} pensando".format(self.id))
        self.label.pack()
    def comer(self):
        print("Filosofo {} comiendo".format(self.id))
        time.sleep(random.randint(0,5))
        print("Filosofo {} termino de comer".format(self.id))
        self.label.config(text="Filosofo {} comiendo".format(self.id))
        time.sleep(random.randint(0,5))
        self.label.config(text="Filosofo {} termino de comer".format(self.id))
    def __del__(self):
        print("Filosofo {} se para de la mesa".format(self.id))
        self.label.config(text="Filosofo {} se para de la mesa".format(self.id))