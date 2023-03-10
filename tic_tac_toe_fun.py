import Tkinter
from random import randrange
from math import log

possibilites = [7, 56, 73, 84, 146, 273, 292, 448] #Possibilités de victoire
fourchettes = [[68, 16, 427, 2], [12, 16, 67, 1], [10, 16, 69, 1], [68, 16, 10, 1], [20, 64, 291, 1]] #Possibilités de fourchettes

class Application(Tkinter.Tk):
    """Application principale"""
    def __init__(self, boss = None):
        Tkinter.Tk.__init__(self)
        #Definition du premier joueur
        self.joueura = 'on'
        #Initialisation gérée par la méthode 'Recommencer'
        self.l1 = Tkinter.Label(self, text='Score : \n Vous 0 -  Ordi 0')
        self.l1.pack(pady = 1)
        #Definition du Canvas principal
        self.can1 = Tkinter.Canvas(self, width = 300, height = 300, bg = 'white')
        self.can1.pack(padx = 5, pady = 5)
        self.ai = Intel_Art(boss = self)
        self.ai_enabled = 'on'
        self.recommencer()
        self.can1.bind("<Button-1>", self.analyser_pos_click)#Cliquer hors de la zone de jeu I.E. Bouton quitter n'activera pas le jeu
        self.bind("<Escape>", self.quitter)
        self.b1 = Tkinter.Button(self, text='Réinitialiser', command=self.recommencer2)#Changement du libelle du bouton pour un terme moins ambigu
        self.b1.pack(side = 'left', padx = 5)
        self.b2 = Tkinter.Button(self, text='Quitter', command=self.destroy)
        self.b2.pack(side = 'right', padx = 5)
        self.pos = [0] * 10
        self.ja_score = 0
        self.jb_score = 0
        
        
        
        
class Intel_Art(Application):
    """Definition de l'intelligence artificelle"""
    def __init__(self, boss):
        self.boss = boss
        
   
   
   
   
   
   
   
        
if __name__ == '__main__':
    fen = Application()
    fen.mainloop()
