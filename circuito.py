'''
Created on 2 abr. 2019

@author: meyi
'''

import turtle
from reportlab.lib.colors import yellow
# from pexpect.screen import screen
# from prompt_toolkit.layout.screen import Screen
# from distutils.core import setup

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
#         self.width = width
#         self.height = height        
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

if __name__ == "__main__":
    circuito = Circuito(640, 480)
    
input()
























