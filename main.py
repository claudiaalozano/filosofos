from filosofos import *
def main():
    lista=[]
    for i in range(n):
        lista.append(filosofo())

    for f in lista:
        f.start()

    for f in lista:
        f.join()
        