# filosofos
Mi dirección de Github: https://github.com/claudiaalozano/filosofos.git

En este proyecto he realizado un código para la cena de los filósofos.
El código empleado es:
```
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

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
    
    def update_filosofo_labels(self):
        for i in range(n):
            filosofo_state = filosofo.estado[i]
            filosofo_status = "comiendo" if filosofo_state == "COMIENDO" else "pensando"
            filosofo_texto="Filosofo {}: {} ({}), contador: {}".format(i, filosofo_state, filosofo_status, self.filosofo_contador[i])
            self.filosofo_labels[i].configure(text=filosofo_texto)
    def update_fork_labels(self):
        for i in range (n):
            fork_state = "USANDO" if filosofo.estado[i] == "COMIENDO" else "LIBRE"
            fork_text = "Tenedor {}: {}".format(i, fork_state)
            self.fork_labels[i].configure(text=fork_text)

    def pensar(self):
        time.sleep(random.randint(0,5))
    
    def derecha(self,i):
        return (i-1)%n
    
    def izquierda(self,i):
        return (i+1)%n
    
    def verificar(self,i):
        if self.filosofo_contador[self.id] >= self.max_cenas and not self.cenas_terminadas and filosofo.estado=="HAMBRIENTO" and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i] = 'COMIENDO'
            filosofo.tenedores[i].release()
            with self.contador_lock:
                self.filosofo_contador[self.id] += 1
            self.update_filosofo_labels()
        elif self.filosofo_contador[self.id] >= self.max_cenas and not self.cenas_terminadas and self.shared_contador< n:
            self.log("Filosofo{} ha alcanzado el número máximo de cenas. Esperando a los demás...".format(self.id))
            self.cenas_terminadas = True
            
            

    def tomar_tenedores(self):
        if self.filosofo_contador[self.id]< self.max_cenas :

            
            filosofo.mutex.acquire()
            filosofo.estado[self.id] = 'HAMBRIENTO'
            self.update_filosofo_labels()
            self.update_fork_labels()
            self.verificar(self.id)
            filosofo.mutex.release()
            filosofo.tenedores[self.id].acquire()
    
    def soltar(self):
        if self.filosofo_contador[self.id] < self.max_cenas:
            filosofo.mutex.acquire()
            filosofo.estado[self.id] = 'PENSANDO'
            self.update_filosofo_labels()
            self.update_fork_labels()
            self.verificar(self.izquierda(self.id))
            self.verificar(self.derecha(self.id))
            filosofo.mutex.release()

    def comer(self):
        if self.filosofo_contador[self.id] < self.max_cenas:
            self.log_box.insert(tk.END, "Filosofo {} comiendo".format(self.id))
            time.sleep(random.randint(0,5))
            self.log_box.insert(tk.END, "Filosofo {} termino de comer".format(self.id))

    def run(self):

        while self.shared_contador < n:
            self.pensar()
            if not self.cenas_terminadas:
                self.tomar_tenedores()
            self.comer()
            if not self.cenas_terminadas:
                self.soltar()
            if self.filosofo_contador[self.id] >= self.max_cenas and not self.cenas_terminadas:
                self.cenas_terminadas = True
                with self.contador_lock:
                    self.shared_contador += 1
        
        if self.shared_contador == n:
            self.root.quit()

def main():
    root = tk.Tk()
    root.title("Cena de Filosofos")

    log_box = tk.Text(root)
    log_box.pack()

    filosofo_labels = []
    filosofo_contador = []
    fork_labels = []
    for i in range(n):
        filosofo_label= tk.Label(root, text="Filosofo {}: PENSANDO (esperando), contador: 0".format(i))
        filosofo_label.pack()
        filosofo_labels.append(filosofo_label)
        filosofo_contador.append(0)
        fork_label = tk.Label(root, text="Tenedor {}: LIBRE".format(i))
        fork_label.pack()
        fork_labels.append(fork_label)
    
    shared_contador = 0
    contador_lock = threading.Lock()

    filosofos = []
    for i in range(n):
        f=filosofo(log_box, filosofo_labels, filosofo_contador, fork_labels, shared_contador, contador_lock, root)
        filosofos.append(f)
        f.start()
    
    def update_log_box():
        for f in filosofos:
            f.join()

        root.destroy()

    threading.Thread(target=update_log_box).start()
    root.mainloop()
    
```
