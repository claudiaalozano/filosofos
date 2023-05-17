import tkinter as tk
from filosofos import *


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
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
            x_pos = x + 150 * tk.cos 

if __name__ == "__main__":
    interface = Interface()
    interface.mainloop()
