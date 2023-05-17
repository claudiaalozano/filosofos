#programa cena de filosofos
import threading
import time
import random
import tkinter as tk

n= 5
tiempo_total=3

class filosofo(threading.Thread):
    mutex=threading.Lock()
    estado = []
    tenedores = []
    count=0

    def __init__(self, canvas, x, y):
        super().__init__()
        self.id = filosofo.count
        filosofo.count += 1
        filosofo.estado.append('PENSANDO')
        filosofo.tenedores.append(threading.Semaphore(0))
        self.canvas = canvas
        self.x = x
        self.y = y
        self.circle = self.canvas.create_oval(self.x-25, self.y-25, self.x+25, self.y+25, fill="white", outline="black")
        self.label = self.canvas.create_text(self.x, self.y, text="Filosofo {}".format(self.id))
        print("Filosofo {} pensando".format(self.id))

    def __del__(self):
        print("Filosofo {} se para de la mesa".format(self.id))

    def pensar(self):
        time.sleep(random.randint(0,5))
    
    def derecha(self,i):
        return (i-1)%n
    
    def izquierda(self,i):
        return (i+1)%n
    
    def verificar(self,i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i] = 'COMIENDO'
            filosofo.tenedores[i].release()

    def tomar_tenedores(self):
        filosofo.mutex.acquire()
        filosofo.estado[self.id] = 'HAMBRIENTO'
        self.verificar(self.id)
        filosofo.mutex.release()
        filosofo.tenedores[self.id].acquire()
    
    def soltar(self):
        filosofo.mutex.acquire()
        filosofo.estado[self.id] = 'PENSANDO'
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.mutex.release()

    def comer(self):
        print("Filosofo {} comiendo".format(self.id))
        time.sleep(random.randint(0,5))
        print("Filosofo {} termino de comer".format(self.id))

    def run(self):
        for i in range(tiempo_total):
            self.pensar()
            self.tomar_tenedores()
            self.comer()
            self.soltar()