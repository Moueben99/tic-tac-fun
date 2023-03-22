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

    def recommencer(self):
        """Réinitialise la partie"""
        self.winner = None  #Initialisation du gagnant
        self.ai.reset()
        self.joueura = 'on'
        self.joueurb = 'off'
        self.title(""".TicTac!'s Fun""")
        self.can1.delete(tkinter.ALL)
        self.tracer_plateau()
        self.pos = [0] * 10
        self.posA = 0
        self.posB = 0
        self.posNULL = 511
        self.winner = None

    def recommencer2(self):
        """Réinitialise le score"""
        self.recommencer()
        self.score('r')

    def quitter(self, event):
        """Quitte le jeu"""
        self.destroy()

    def tracer_croix(self, x, y):
        """Trace une croix dans le Canvas principal"""
        self.can1.create_line(x - 35, y - 35, x + 35, y + 35, width=5, fill='blue')
        self.can1.create_line(x - 35, y + 35, x + 35, y - 35, width=5, fill='blue')

    def tracer_rond(self, x, y):
        """Trace un rond dans la Canvas principal"""
        self.can1.create_oval(x - 35, y - 35, x + 35, y + 35, outline='red', width=5)

    def tracer_ligne(self, position):
        if position == 7:
            self.can1.create_line(10, 55, 290, 55, width=10, fill='green')
        elif position == 56:
            self.can1.create_line(10, 155, 290, 155, width=10, fill='green')
        elif position == 448:
            self.can1.create_line(10, 255, 290, 255, width=10, fill='green')
        elif position == 73:
            self.can1.create_line(55, 10, 55, 290, width=10, fill='green')
        elif position == 146:
            self.can1.create_line(155, 10, 155, 290, width=10, fill='green')
        elif position == 292:
            self.can1.create_line(255, 10, 255, 290, width=10, fill='green')
        elif position == 273:
            self.can1.create_line(10, 10, 290, 290, width=10, fill='green')
        elif position == 84:
            self.can1.create_line(10, 290, 290, 10, width=10, fill='green')

    def analyser_pos_click(self, event):
        """Analyse la case sélectionnée par le joueur"""
        # Detection de la position de la souris dans le Canvas en fonction des cases
        # 1 | 2 | 3
        # - + - + -
        # 4 | 5 | 6
        # - + - + -
        # 7 | 8 | 9.

        # Valeurs de chacune des cases:
        # 1 | 2 | 4
        # - + - + -
        # 8 | 16|32
        # - + - + -
        # 64|128|256



    def verif_gagner(self):
        """Vérifie que le joueur a gagné"""
        self.winner = None

    def score(self, joueur):
        if joueur == 'a':
            self.ja_score = self.ja_score + 1
        elif joueur == 'b':
            self.jb_score = self.jb_score + 1
        elif joueur == 'r':
            self.jb_score = 0
            self.ja_score = 0
        self.l1.configure(text='Score : \n Vous ' + str(self.ja_score) + ' -  Ordi ' + str(self.jb_score))


class Intel_Art(Application):
    """Definition de l'intelligence artificelle"""
    def __init__(self, boss):
        self.boss = boss

    def reset(self):
        self.premierTour = True

    def trouverFourchette(self):
        posB = self.boss.posB
        posA = self.boss.posA
        posNULL = self.boss.posNULL
        loc = 1
        trouve = False

    def ai_analyser(self):
        # Analyse si IA peut gagner au prochain coup
        # Joueur B est toujours l'IA
        # Changement du moteur de vérifications.
        trouve = False

    def tracer(self, case):
        if case == 1:
            self.boss.tracer_rond(55, 55)
        elif case == 2:
            self.boss.tracer_rond(155, 55)
        elif case == 3:
            self.boss.tracer_rond(255, 55)
        elif case == 4:
            self.boss.tracer_rond(55, 155)
        elif case == 5:
            self.boss.tracer_rond(155, 155)
        elif case == 6:
            self.boss.tracer_rond(255, 155)
        elif case == 7:
            self.boss.tracer_rond(55, 255)
        elif case == 8:
            self.boss.tracer_rond(155, 255)
        elif case == 9:
            self.boss.tracer_rond(255, 255)
        self.boss.posB += 2 ** (case - 1)
        self.boss.posNULL -= 2 ** (case - 1)

        

   
   
   
   
   
   
        
if __name__ == '__main__':
    fen = Application()
    fen.mainloop()
