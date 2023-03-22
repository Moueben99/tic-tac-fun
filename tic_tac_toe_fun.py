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
        self.can1.create_line(105, 10, 105, 290, width=10, fill='yellow')
        self.can1.create_line(205, 10, 205, 290, width=10, fill='yellow')
        self.can1.create_line(10, 105, 290, 105, width=10, fill='yellow')
        self.can1.create_line(10, 205, 290, 205, width=10, fill='yellow')

    def recommencer(self):
        """Réinitialise la partie"""
        self.winner = None  #Initialisation du gagnant
        self.ai.reset()
        self.joueura = 'on'
        self.joueurb = 'off'
        self.title("""Tic Tac Fun !""")
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

        i = 0
        if self.winner == None:
            if event.x > 0 and event.x < 100:
                if event.y > 0 and event.y < 100:
                    i = 1
                    self.xtrace = 55
                    self.ytrace = 55
                if event.y > 100 and event.y < 200:
                    i = 4
                    self.xtrace = 55
                    self.ytrace = 155
                if event.y > 200 and event.y < 300:
                    i = 7
                    self.xtrace = 55
                    self.ytrace = 255
            elif event.x > 100 and event.x < 200:
                if event.y > 0 and event.y < 100:
                    i = 2
                    self.xtrace = 155
                    self.ytrace = 55
                if event.y > 100 and event.y < 200:
                    i = 5
                    self.xtrace = 155
                    self.ytrace = 155
                if event.y > 200 and event.y < 300:
                    i = 8
                    self.xtrace = 155
                    self.ytrace = 255
            elif event.x > 200 and event.x < 300:
                if event.y > 0 and event.y < 100:
                    i = 3
                    self.xtrace = 255
                    self.ytrace = 55
                if event.y > 100 and event.y < 200:
                    i = 6
                    self.xtrace = 255
                    self.ytrace = 155
                if event.y > 200 and event.y < 300:
                    i = 9
                    self.xtrace = 255
                    self.ytrace = 255
            if self.joueura == 'on' and self.posNULL & 2 ** (i - 1):
                self.posA = self.posA + 2 ** (i - 1)
                self.posNULL -= 2 ** (i - 1)
                self.tracer_croix(self.xtrace, self.ytrace)
                if self.ai_enabled != 'on':
                    self.joueura = 'off'
                    self.joueurb = 'on'
                if self.ai_enabled == 'on':
                    self.verif_gagner()
                    if self.winner != None:
                        return 1
                    self.ai.ai_analyser()
                    return 1
            elif (self.joueurb == 'on' and self.posNULL & 2 ** (i - 1) and self.ai_enabled != 'on'):
                if self.ai_enabled != 1:
                    self.posB += 2 ** (i - 1)
                    self.posNULL -= 2 ** (i - 1)
                    self.tracer_rond(self.xtrace, self.ytrace)
                    self.joueura = 'on'
                    self.joueurb = 'off'
            else:
                print("Coup impossible")
                return 1
            self.verif_gagner()
        else:
            self.recommencer()

    def verif_gagner(self):
        """Vérifie que le joueur a gagné"""
        self.winner = None
        #Definition des 8 possibilites de gagner et tracer d'une grand ligne si gagner
        for ver in possibilites:
            if self.posA & ver == ver:
                self.winner, pos = 'A', ver
            elif self.posB & ver == ver:
                self.winner, pos = 'B', ver
        if self.posNULL == 0:
            self.winner = 'Nul'
        if self.winner != None and self.winner != 'Nul':
            self.tracer_ligne(pos)

        if self.winner != None:
            if self.winner == 'A':
                self.title('Joueur A Win !!')
                self.score('a')
            elif self.winner == 'B':
                self.title('Joueur B Win !!')
                self.score('b')
            elif self.winner == 'Nul':
                self.title('Match Nul')

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
        for iteration in range(4):  #Il faut tourner 4 fois pour revenir au plateau initial
            posB, posA, posNULL, loc = self.rotate(posB), self.rotate(posA), self.rotate(posNULL), self.rotate(loc)
            for a, b, null, dest in fourchettes:
                if (posA & a) == a and (posB & b) == b and (posNULL & null) == null and not trouve:
                    loc = dest
                    trouve = True
        loc = int(log(loc, 2)) + 1  #Ramène la valeur de la case à son index
        if not trouve:  #Prendre la première case vide s'il n'y a pas de fourchette
            while not ((2 ** (loc - 1)) & posNULL):
                loc += 1
        self.tracer(loc)

    def ai_analyser(self):
        #Analyse si IA peut gagner au prochain coup
        #Joueur B est toujours l'IA
        #Changement du moteur de vérifications.
        trouve = False
        if not self.premierTour:
            for i in range(0, 10):
                for position in possibilites:
                    #Si la case permet de gagner, la case est inoccupée ET l'IA n'a pas encore joué
                    if (
                            self.boss.posB | 2 ** i) & position == position and not self.boss.posA & 2 ** i and not self.boss.posB & 2 ** i and not trouve:
                        self.tracer(i + 1)
                        trouve = True
            for i in range(0, 10):
                #Vérifie si l'adversaire peut gagner
                for position in possibilites:
                    #Si la case permettrait à l'adversaire de gagner, la case est inoccupée et l'IA n'a pas encore joué
                    if (
                            self.boss.posA | 2 ** i) & position == position and not self.boss.posB & 2 ** i and not self.boss.posA & 2 ** i and not trouve:
                        self.tracer(i + 1)
                        trouve = True
            #S'il ne peut pas gagner ou si bloquer on fait
            if not trouve:
                self.trouverFourchette()
        else:
            #Au premier tour, deux possibilités valides: le centre ou le cas échéant, un coin.
            if self.boss.posA & 16:
                self.tracer(1)
            else:
                self.tracer(5)
            self.premierTour = False

            #Finalement, vérifier si il y a victoire
        self.boss.verif_gagner()

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

    def rotate(self, entree):
        sortie = 0
        for i in range(9):
            if entree & 2 ** i:
                sortie += 2 ** ((i + 1) * 3 % 10 - 1)
        return sortie


if __name__ == '__main__':
    fen = Application()
    fen.mainloop()
