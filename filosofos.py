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
    cenas_completadas=0

    def __init__(self, log_box, filosofo_labels, filosofo_contador, fork_labels, shared_contador, contador_lock, root):
        super().__init__()
        self.id = filosofo.count
        filosofo.count += 1
        filosofo.estado.append('PENSANDO')
        filosofo.tenedores.append(threading.Semaphore(0))
        
        self.log_box = log_box
        self.filosofo_labels = filosofo_labels
        self.filosofo_contador = filosofo_contador
        self.fork_labels = fork_labels
        self.max_cenas = 5
        self.shared_contador = shared_contador
        self.cenas_terminadas = False
        self.contador_lock = contador_lock
        self.root = root
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