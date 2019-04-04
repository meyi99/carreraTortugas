'''
Created on 2 abr. 2019

@author: meyi
'''
import random
import turtle

class Circuito():
    '''
    Atributos
    '''
    corredores = []
    posicionY = (-30, -10, 10, 30)
    colorT = ("red", "yellow", "blue", "green")


    def __init__(self, width, height):
        '''
        Constructor
        '''
                
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__starline = - width / 2 + 20
        self.__finishline = width / 2 -20
        
        self.__runners()
        
    def __runners(self):
        '''
        Función que crea a los corredores
        '''           
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.shape("turtle")
            newTurtle.color(self.colorT[i])
            newTurtle.penup()
            newTurtle.setpos(self.__starline, self.posicionY[i])
            self.corredores.append(newTurtle)

    def carrera(self):
        '''
        Función que encargada para la parte de la carrera
        '''
        ganador = False
        
        while not ganador:
            for i in self.corredores:
                avance = random.randint(1, 6)
                i.fd(avance)
                
                if i.position()[0] >= self.__finishline:
                    ganador = True 
                    print("Ha ganado la tortuga de color {}".format(i.color()[0]))
                    break

if __name__ == "__main__":
    circuito = Circuito(640, 480)
    circuito.carrera()