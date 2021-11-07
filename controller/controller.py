#!/usr/bin/python3

import random
import PyQt5
import logging
import threading
import time
from model.model import model


class controller:

    QUIT=5
    LEFT=3
    RIGHT=1
    DOWN=2
    UP=0
    
    def __init__(self):
        """
        Constructeur
        """
        self.__model = None
        self.__view = None
        self.__finished=False

    def setModel(self, model):
        """
        Setter model
        """
        self.model = model
        
    def setView(self, view):
        """
        Setter veiw
        """
        self.view = view
    
    def movePlayer(self, direction):
        """
        Méthode qui déplace le joueur.
        """

        plateau, points = self.model.getMatrix()

        #Trouver les coordonnées du joueur
        xPlayer = 0
        yPlayer = 0
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if plateau[i][j] == "J":
                    xPlayer = i
                    yPlayer = j
                    break

        #Case cible du joueur
        xCible = xPlayer
        yCible = yPlayer
        xMoveBox = xPlayer
        yMoveBox = yPlayer
        if direction == 0: #Haut
            xCible += -1
            xMoveBox += -2
        elif direction == 1: #Droite
            yCible += 1
            yMoveBox += 2
        elif direction == 2: #Bas
            xCible += 1
            xMoveBox += 2
        elif direction == 3: #Gauche
            yCible += -1
            yMoveBox += -2


        #Faire le déplacement
        if direction in [0,1,2,3]:
            if self.passagePossible(xPlayer, yPlayer, xCible, yCible): 
                if plateau[xCible][yCible] == "C": 
                    if self.passagePossible(xCible, yCible, xMoveBox, yMoveBox): 
                        self.moveBox(xCible, yCible, xMoveBox, yMoveBox) 
                        self.view.playPousseCaisse()
                        plateau[xPlayer][yPlayer] = "O"
                        plateau[xCible][yCible] = "J"
                        if (plateau[xMoveBox][yMoveBox] == "C" and points[xMoveBox][yMoveBox] == 1) :
                            self.view.playCaisseBille()
                    else :
                        self.view.playMur()
                else:
                    plateau[xPlayer][yPlayer] = "O"
                    plateau[xCible][yCible] = "J"
            else :
                self.view.playMur()
        
        self.model.setMatrix(plateau)
        
    
    def moveBox(self, xCaisse, yCaisse, xCible, yCible):
        """
        Méthode qui déplace une caisse.
        """
        
        level = self.model.getLevel()
        
        if self.passagePossible(xCaisse, yCaisse, xCible, yCible):
            level[xCible][yCible] = "C"
            level[xCaisse][yCaisse] = "O"   
            
        self.model.setMatrix(self)
        
            
    def passagePossible(self,ligneCase1, colonneCase1, ligneCase2, colonneCase2):
        """
        Si le joueur ou une caisse peut se déplacer sur la case cible
        @return boolean.
        """            
        matrixJeu, matrixPoint = self.model.getMatrix()

        if ligneCase2 <= len(matrixJeu)-1 and ligneCase2 >= 0 and colonneCase2 <= len(matrixJeu)-1 and colonneCase2 >= 0:
            if matrixJeu[ligneCase1][colonneCase1] == "J":        
                if matrixJeu[ligneCase2][colonneCase2] == "O" or matrixJeu[ligneCase2][colonneCase2] == "C":
                    return True
            elif matrixJeu[ligneCase1][colonneCase1] == "C":
                if matrixJeu[ligneCase2][colonneCase2] == "O":
                    return True
            
        return False
        
    def endGame(self):
        """
        Méthode qui vérifie si les caisses sont sur les points.
        @return boolean.
        """
        
        level, points = self.model.getMatrix()
        
        endGame = True
        for i in range(len(points)):
            for j in range(len(points[i])):
                if points[i][j] == 1 and level[i][j] != "C": #Si on trouve une caisse qui ne superpose pas un emplacement
                    endGame = False
                    break
        return endGame
                      
