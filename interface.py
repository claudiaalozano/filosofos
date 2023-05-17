from tkinter import *
from filosofos import *

root= Tk()
root.geometry("600x600")



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
    
    def stop(self):
        for f in self.filosofo:
            f.is_running = False

app = interfaz()
app.mainloop()



