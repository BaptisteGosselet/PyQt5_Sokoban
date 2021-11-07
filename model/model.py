#!/usr/bin/python3

class model:

    def __init__(self, choix):
        """
        Constructeur
        """
        self.view = None
        self.controller = None

        self.level, self.points = self.generateLevel(choix)

    def generateLevel(self,choix):
        """
        Méthode qui génère le niveau.
        @return 2 matrices, une avec le niveau, l'autre avec les points où il faut placer les caisses.

        "X" = Mur ; "O" = Chemin ; "C" = Caisse ; "J" = Joueur
         0  = vide ; 1  = point où il faut placer une caisse
        """
        if choix==1:
            return [
                       ["X","X","X","X","X","X","X","X"],
                       ["X","X","O","O","O","X","X","X"],
                       ["X","O","O","X","O","C","J","X"],
                       ["X","O","O","X","O","X","O","X"],
                       ["X","O","C","O","O","C","O","X"],
                       ["X","O","O","O","O","X","X","X"],
                       ["X","X","O","C","O","O","O","X"],
                       ["X","X","X","X","X","X","X","X"]
                   ],[
                       [0,0,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,1,0,0,0,1,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,1,0],
                       [0,0,0,0,0,0,0,0]
                   ]
        elif choix==2:
            return [
                       ["X","X","X","O","O","O","X","X"],
                       ["X","O","J","O","C","O","X","X"],
                       ["X","X","X","O","C","O","X","X"],
                       ["X","O","X","X","C","O","X","X"],
                       ["X","O","X","O","O","O","X","X"],
                       ["X","C","O","C","O","C","O","X"],
                       ["X","O","O","O","O","O","O","X"],
                       ["X","X","X","X","X","X","X","X"]
                   ],[
                       [0,0,0,0,0,0,0,0],
                       [0,1,0,0,0,0,0,0],
                       [0,0,0,0,0,1,0,0],
                       [0,1,0,0,0,0,0,0],
                       [0,0,0,0,1,0,0,0],
                       [0,0,0,0,0,0,1,0],
                       [0,0,0,0,1,0,0,0],
                       [0,0,0,0,0,0,0,0]
                   ]
        elif choix==3:
            return [
                       ["X","X","X","X","X","O","X","O"],
                       ["X","X","O","X","X","O","O","O"],
                       ["O","O","C","O","C","O","X","X"],
                       ["X","X","O","C","O","O","X","O"],
                       ["O","J","O","C","O","O","O","O"],
                       ["O","O","X","O","O","O","O","O"],
                       ["O","C","O","O","O","X","O","X"],
                       ["O","O","X","X","X","X","X","X"]
                   ],[
                       [0,0,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0,0],
                       [1,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1],
                       [0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0]
                   ]
        elif choix==4:
            return [
                       ["X","X","X","X","X","X","X","X"],
                       ["X","O","X","O","O","O","X","X"],
                       ["X","O","O","C","O","O","X","X"],
                       ["X","O","X","C","C","O","O","X"],
                       ["X","O","O","C","J","X","X","X"],
                       ["X","O","O","O","C","X","X","X"],
                       ["X","X","O","O","O","O","X","X"],
                       ["X","X","O","O","X","X","X","X"]
                   ],[
                       [0,0,0,0,0,0,0,0],
                       [0,1,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,1,1,1,0],
                       [0,1,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                   ]
        
    def changerLevel(self, choix):
        """
        Permet de changer le niveau
        """
        self.level, self.points = self.generateLevel(choix)

    def getMatrix(self):
        """
        @return les 2 matrices
        """
        return self.level.copy(), self.points.copy()
    
    def getLevel(self):
        """
        @return la matrice du niveau
        """
        return self.level.copy()
    
    def setMatrix(self, matrix):
        """
        setter qui met à jour le niveau
        """
        self.level = matrix
        self.view.update()

    def setView(self, view):
        """
        setter de la vue
        """
        self.view = view
        self.view.update()

    def setModel(self, choix) :
        """
        Méthode qui change de niveau
        """
        self.level, self.points = model.generateLevel(self, choix)

        
