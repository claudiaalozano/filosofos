from tkinter import *
from filosofos import *

root= Tk()
root.geometry("600x600")

tittle = Label(root, text="Cena de los filosofos", font=("Arial", 20)).place(x=150, y=10)
tittle.config(font=17)
tittle.pack(pady=2)

class interfaz(root.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cena de los filosofos")
        self.geometry("600x600")
        self.id = []
        self.forks = [threading.Lock() for n in range(5)]

        for i in range(5):
            self.id.append(i)
            self.id[i] = filosofo()
            self.id[i].start()
        
        start_button = root.Button(self, text="Start", command=self.start.filosofo())
        start_button.pack()

        stop_button = root.Button(self, text="Stop", command=self.stop.filosofo())
        stop_button.pack()

        self.filosofo=[]

    def start(self):
        for i in range(5):
            f= filosofo(f"Filosofo {i}", self.forks[i], self.forks[(i+1)%5])
            f.start()
            self.filosofo.append(f)


