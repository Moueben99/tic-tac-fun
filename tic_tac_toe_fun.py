import tkinter
from random import randrange
from math import log

possibilites = [7, 56, 73, 84, 146, 273, 292, 448] #Possibilités de victoire
fourchettes = [[68, 16, 427, 2], [12, 16, 67, 1], [10, 16, 69, 1], [68, 16, 10, 1], [20, 64, 291, 1]] #Possibilités de fourchettes

class Application(tkinter.Tk):
    """Application principale"""
    def __init__(self, boss = None):
        tkinter.Tk.__init__(self)
        #Definition du premier joueur
        self.joueura = 'on'
        #Initialisation gérée par la méthode 'Recommencer'
        self.l1 = tkinter.Label(self, text='Score : \n Vous 0 -  Ordi 0')
        self.l1.pack(pady = 1)
        #Definition du Canvas principal
        self.can1 = tkinter.Canvas(self, width = 300, height = 300, bg = 'white')
        self.can1.pack(padx = 5, pady = 5)
        self.ai = Intel_Art(boss = self)
        self.ai_enabled = 'on'
        self.recommencer()
        self.can1.bind("<Button-1>", self.analyser_pos_click)#Cliquer hors de la zone de jeu I.E. Bouton quitter n'activera pas le jeu
        self.bind("<Escape>", self.quitter)
        self.b1 = tkinter.Button(self, text='Réinitialiser', command=self.recommencer2)#Changement du libelle du bouton
        self.b1.pack(side = 'left', padx = 5)
        self.b2 = tkinter.Button(self, text='Quitter', command=self.destroy)
        self.b2.pack(side = 'right', padx = 5)
        self.pos = [0] * 10
        self.ja_score = 0
        self.jb_score = 0

    def tracer_plateau(self):
        """Trace du plateau"""
        self.can1.create_line(105, 10, 105, 290, width=10)
        self.can1.create_line(205, 10, 205, 290, width=10)
        self.can1.create_line(10, 105, 290, 105, width=10)
        self.can1.create_line(10, 205, 290, 205, width=10)

    
        
        
        
        
class Intel_Art(Application):
    """Definition de l'intelligence artificelle"""
    def __init__(self, boss):
        self.boss = boss
        
   
   
   
   
   
   
   
        
if __name__ == '__main__':
    fen = Application()
    fen.mainloop()
