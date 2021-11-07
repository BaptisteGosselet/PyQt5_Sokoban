#!/usr/bin/python3
import sys
import random
import logging
import threading
from pathlib import Path
sys.path.append("/export/etu/adrien.hannon/IHM/sokoban/model")
sys.path.append("/home/adrien/sokoban/model")
from model.model import model
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt, QSound
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist


class view(QMainWindow):
    
    def __init__(self):
        """
        Constructeur
        """
        super().__init__()
        self.chemins={"X" : "img/WallRound_Brown.png", "O" : "img/Ground_Concrete.png", "C" : "img/Crate_Brown.png", "JB" : "img/Character4.png", "JG" : "img/Character1.png", "JH" : "img/Character7.png", "JD" : "img/Character2.png", "R" : "img/Crate_Red.png", 1 : "img/EndPoint_Red.png"}
        self.setFixedSize(512,557)
        self.model = model(1)
        self.controller = None
        self.setWindowTitle("Sokoban")
        self.statusBar().showMessage("Nombre de mouvement : 0")

        self.nbCoup = 0
        self.niveauActuel = 1
        self.__window = Dessin() 
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.orientationPerso = "JB"

        self.caisseBille = QSound("sound/caisseBille.wav")
        self.mur = QSound("sound/mur.wav")
        self.pousseCaisse = QSound("sound/pousseCaisse.wav")
        self.victoire = QSound("sound/victoire.wav")
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(
            QDir.current().absoluteFilePath("sound/musique.wav"))))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.levelSound = QMediaPlayer()
        self.levelSound.setPlaylist(self.playlist)
        
        self.playMusic = True
        self.playEffect = True

        menuBar = self.menuBar()
        gameMenu = QMenu("Jeu", self)
        menuBar.addMenu(gameMenu)
        
        niv1 = QAction(self)
        niv1.setText("Niveau 1")
        gameMenu.addAction(niv1)
        niv1.triggered.connect(self.niveau1)
        
        niv2 = QAction(self)
        niv2.setText("Niveau 2")
        gameMenu.addAction(niv2)
        niv2.triggered.connect(self.niveau2)
        
        niv3 = QAction(self)
        niv3.setText("Niveau 3")
        gameMenu.addAction(niv3)
        niv3.triggered.connect(self.niveau3)
        
        niv4 = QAction(self)
        niv4.setText("Niveau 4")
        gameMenu.addAction(niv4)
        niv4.triggered.connect(self.niveau4)
        
        aleatoire = QAction(self)
        aleatoire.setText("Niveau Aléatoire")
        gameMenu.addAction(aleatoire)
        aleatoire.triggered.connect(self.aleatoire)

        restart = QAction(self)
        restart.setText("Restart")
        gameMenu.addAction(restart)
        restart.triggered.connect(self.restart)
        
        soundMenu = QMenu("Sound", self)
        menuBar.addMenu(soundMenu)

        cutMusic = QAction(self)
        cutMusic.setText("Activer/désactiver musique")
        soundMenu.addAction(cutMusic)
        cutMusic.triggered.connect(self.cutMusic)
        
        cutEffect = QAction(self)
        cutEffect.setText("Activer/désactiver les effets")
        soundMenu.addAction(cutEffect)
        cutEffect.triggered.connect(self.cutEffect)

        self.levelSound.play()
        self.show()
        
    def setModel(self, model) :
        """
        Setter model
        """
        self.model = model    
    
    def setController(self, controller):
        """
        Setter Controller
        """
        self.controller = controller
    
    def updateView(self):
        """
        Ask for updating the view.
        """
        self.update()  

    def updateStatus(self):
        """
        Mettre a jour le nb de coups
        """
        if (self.nbCoup == 0 or self.nbCoup == 1) :
            message = "Nombre de mouvement : " + str(self.nbCoup)
            self.statusBar().showMessage(message)
        else :
            message = "Nombre de mouvements : " + str(self.nbCoup)
            self.statusBar().showMessage(message)
 
    def messageFin(self) :
        """
        Afficher le message de fin
        """
        message = "Bravo, vous avez réussi le niveau en " + str(self.nbCoup) + " coups ! Vous pouvez selectionner un nouveau niveau."
        self.statusBar().showMessage(message)

    def niveau1(self):
        """
        Initialiser le niveau 1
        """
        self.nbCoup = 0 
        self.niveauActuel = 1
        self.model.changerLevel(1) 
        self.__window = Dessin()
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.updateStatus()
    
    def niveau2(self):
        """
        Initialiser le niveau 2
        """
        self.nbCoup = 0 
        self.niveauActuel = 2
        self.model.changerLevel(2) 
        self.__window = Dessin()
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.updateStatus()
    
    def niveau3(self):
        """
        Initialiser le niveau 3
        """
        self.nbCoup = 0 
        self.niveauActuel = 3
        self.model.changerLevel(3) 
        self.__window = Dessin()
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.updateStatus()
    
    def niveau4(self):
        """
        Initialiser le niveau 4
        """
        self.nbCoup = 0 
        self.niveauActuel = 4
        self.model.changerLevel(4)
        self.__window = Dessin()
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.updateStatus()
    
    def aleatoire(self):
        """
        Initialiser un niveau aléatoire
        """
        self.nbCoup = 0 
        choix = random.randint(1, 4)
        self.niveauActuel = choix
        self.model.changerLevel(choix) 
        self.__window = Dessin()
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.updateStatus()

    def restart(self):
        """
        Permet de redémmarer la partie
        """
        self.nbCoup = 0
        self.model.changerLevel(self.niveauActuel) 
        self.__window = Dessin()
        self.__window.setModel(self.model)
        self.setCentralWidget(self.__window)
        self.updateStatus()
        
    def cutMusic(self) :
        """
        Permet de couper la musique
        """
        if self.playMusic == True : 
            self.playMusic = False
            self.levelSound.stop()
        elif self.playMusic == False : 
            self.playMusic = True
            self.levelSound.play()

    def cutEffect(self):
        """
        Permet de couper les effets
        """
        if self.playEffect == True :    
            self.playEffect = False
        elif self.playEffect == False :    
            self.playEffect = True
        
    
    def playPousseCaisse(self) :
        """
        Permet de jouer le son d'une caisse qui se fait pousser
        """
        if self.playEffect == True :    
            self.pousseCaisse.play()
        
    def playCaisseBille(self) :
        """
        Permet de jouer le son d'une caisse sur une bille
        """
        if self.playEffect == True :    
            self.caisseBille.play()
        
    def playMur(self):
        """
        Permet de jouer le son d'un joueur contre un mur
        """
        if self.playEffect == True :    
            self.mur.play()
        
    def playVictoire(self) :
        """
        Permet de jouer le son d'une victoire
        """
        if self.playEffect == True :    
            self.victoire.play()

    def keyPressEvent(self, event):
        """
        Méthode qui récupère les entrées claviers et qui appelle movePlayer()
        avec les bons argument
        """
         
        if self.controller.endGame() == False :
            if event.key() == Qt.Key_Up: #fleche du haut
                self.controller.movePlayer(0)
                self.orientationPerso = "JH"
                self.nbCoup += 1 ;
            elif event.key() == Qt.Key_Down: #fleche du bas
                self.controller.movePlayer(2)
                self.orientationPerso = "JB"
                self.nbCoup += 1 ;
            elif event.key() == Qt.Key_Right: #fleche de droite
                self.controller.movePlayer(1)
                self.orientationPerso = "JD"
                self.nbCoup += 1 ;
            elif event.key() == Qt.Key_Left: #fleche de gauche
                self.controller.movePlayer(3)
                self.orientationPerso = "JG"
                self.nbCoup += 1 ;
            self.__window = Dessin()
            self.__window.setModel(self.model)
            self.setCentralWidget(self.__window)
            self.updateStatus()
        
        if self.controller.endGame() == True :
            self.playVictoire()
            self.messageFin()
        
    def getCase(self, i, j):
        matrix, points = self.model.getMatrix()
        k = matrix[j][i]
        if (k == "J") :
            k = "O"
        return self.chemins.get(k)


class Dessin(QWidget):
    

    def __init__(self):
        super().__init__()
        self.resize(512,512)
        self.move(0,0)
        self.model = None    
        self.chemins={"X" : "img/WallRound_Brown.png", "O" : "img/Ground_Concrete.png", "C" : "img/Crate_Brown.png", "JB" : "img/Character4.png", "JG" : "img/Character1.png", "JH" : "img/Character7.png", "JD" : "img/Character2.png", "R" : "img/Crate_Red.png", 1 : "img/EndPoint_Red.png"}

    def setModel(self, model):
        self.model = model

    def updateDessin(self):
        """
        Ask for updating the view.
        """
        self.update() 

    def getCase(self, i, j):
        """
        Permet de récupérer dans la bibliothèque les liens des images
        """
        
        matrix, points = self.model.getMatrix()
        k = matrix[j][i]
        if (k == "J") :
            k = "O"
        return self.chemins.get(k)

    def caisseVerte(self, lig, col):
        """
        Méthode qui prend en paramètre une ligne et une colonne et vérifie
        s'il se trouve sur cette case une caisse verte.
        @return boolean.
        """
        matrixJeu, matrixPoints = self.model.getMatrix()
        return (matrixJeu[lig][col] == "C" and matrixPoints[lig][col] == 1) 

    def paintEvent(self, event): 
        """
        Permet de dessiner le plateau
        """        
        matrix, points = self.model.getMatrix()
        painter = QPainter(self)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                img = QPixmap(self.chemins.get("O"))
                painter.drawPixmap(64*i, 64*j, img)
                if (self.caisseVerte(j, i) == False) :
                    k = self.getCase(i, j)
                    img = QPixmap(k)
                    painter.drawPixmap(64*i , 64*j, img)
                if (points[j][i] == 1 and self.caisseVerte(j, i) == False) :
                    img = QPixmap(self.chemins.get(1))
                    painter.drawPixmap(64*i+16, 64*j+16, img)
                if (matrix[j][i] == "J") :
                    k = self.chemins.get("JB")
                    img = QPixmap(k)
                    painter.drawPixmap(64*i+14 , 64*j+2, img)
                if (self.caisseVerte(j, i) == True):
                    img = QPixmap(self.chemins.get("R"))
                    painter.drawPixmap(64*i , 64*j, img)
                    
        
