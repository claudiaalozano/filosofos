import tkinter as tk
from filosofos import *
import math



class Interface(tk.Tk):
    def __init__(self, log_box, filosofo_label, filosofo_contador, fork_label, counter_lock, shared_label, contador_label, shared_contador, root):
        super().__init__()
        self.log_box = log_box
        self.filosofo_label = filosofo_label
        self.filosofo_contador = filosofo_contador
        self.fork_label = fork_label
        self.max_contador_comida= 5
        self.shared_contador = shared_contador
        self.terminar_de_comer = False
        self.counter_lock = counter_lock
        self.root = root
        self.title("Cena de filosofos")
        self.geometry("800x600")
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        x= 400
        y= 300
        angulo_inicial = -90
        angulo_incremento = 360/n

        self.filosofos = []

        for i in range(n):
            x_pos = x + 150 * math.cos(math.radians(angulo_inicial + angulo_incremento * i))

if __name__ == "__main__":
    interface = Interface()
    interface.mainloop()
