    # spojení všeho

"""
1) import
2) inicializace
3) knihovna barev
    - 2, 3, 5, 7
4) načtení obrázků
5) classa buttonů
    - init
    - create
    - pressed
6) classa hry
    - základní parametry
    - různá okna - jako funkce - a v nich loopy
        * menu
        * game
        * primes
        * game over <- is game over or endthistry
        * herní loop
    - exitování přes button "EXIT" a při quitnutí
    - play
        * init
        * jedno pevné pozadí
        * vytvoření tabulky
        * přidávání čísel
        * pohyb
        * spojení po/při pohybu
        * updatování skóre
        * game over?
        * True -> game over
+) fce na random světlé pozadí
7) spuštění hry
"""

import numpy as np
import pygame as pg
import random as r
import sys

pg.init()

barvicky_2 = {0: (255, 255, 255),
            2: (9, 246, 112),
            4: (18, 222, 147),
            8: (18, 222, 181),
            16: (18, 222, 222),
            32: (18, 181, 222),
            64: (18, 137, 222),
            128: (24, 83, 201),
            256: (35, 24, 201),
            512: (142, 24, 201),
            1024: (212, 72, 234),
            2048: (254, 47, 226),
            4096: (254, 47, 147),
            8192: (254, 47, 85),
            16384: (254, 1, 1),
            32768: (255, 35, 0),
            65536: (250, 62, 0)}

barvicky_3 = {0: (255, 255, 255),
              3: (112, 9, 246),
              9: (147, 18, 222),
              27: (181, 18, 222),
              81: (222, 18, 222),
              243: (222, 18, 181),
              729: (222, 18, 137),
              2187: (201, 24, 83),
              6561: (201, 35, 24),
              19683: (201, 142, 24),
              59049: (234, 212, 72),
              177147: (226, 254, 47),
              531441: (147, 254, 47),
              1594323: (85, 254, 47),
              4782969: (1, 254, 1,),
              14348907: (0, 255, 35),
              43046721: (0, 250, 62)}

barvicky_5 = {0: (255, 255, 255),
            5: (9, 112, 246),
            25: (18, 147, 222),
            125: (18, 181, 222),
            625: (18, 222, 222),
            3125: (18, 222, 181),
            15625: (18, 222, 137),
            78125: (24, 201, 83),
            390625: (35, 201, 24),
            1953125: (142, 201, 24),
            9765625: (212, 234, 72),
            48828125: (254, 226, 47),
            244140625: (254, 147, 47),
            1220703125: (254, 85, 47),
            6103515625: (254, 1, 1),
            30517578125: (255, 0, 35),
            152587890625: (250, 0, 62)}

barvicky_7 = {0: (255, 255, 255),
              7: (246, 112, 9),
              49: (222, 147, 18),
              343: (222, 181, 18),
              2401: (222, 222, 18),
              16807: (181, 222, 18),
              117649: (137, 222, 18),
              823543: (83, 201, 24),
              5764801: (24, 201, 35),
              40353607: (24, 201, 142),
              282475249: (72, 234, 212),
              1977326743: (47, 226, 254),
              13841287201: (47, 147, 255),
              96889010407: (47, 85, 254),
              678223072849: (1, 1, 254),
              4747561509943: (35, 0, 255),
              33232930569601: (62, 0, 250)}






class buttOn:
    def __init__(self, x, y, image):
        self.image = image
        self.pole = self.image.get_rect()
        self.pole.topleft = (x, y)
        self.clicked = False

    def make_button(self, screen):
        screen.blit(self.image, (self.pole.x, self.pole.y))

    def buTton_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        akce = False
        if self.pole.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                akce = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return akce



def gen_svetle_pozadi():
    rgb_souradnice = (r.randrange(140, 180), r.randrange(160, 210), r.randrange(210, 255))
    rgb_permutation = r.sample(rgb_souradnice, 3)
    return tuple(rgb_permutation)
    


class Game_p_Asterisk_asterisk_n:
    def __init__(self):
        self.num = 4

        self.hrana_ctverce = 121
        self.mezera = 5

        self.hrana_bloku = self.hrana_ctverce + 2 * self.mezera

        self.base = 2

        self.score = 0
        self.high_score = 0

        self.sirka_okna = self.num * self.hrana_bloku
        self.vyska_okna = self.sirka_okna + 120

        pg.init()

        self.okno = pg.display.set_mode((self.sirka_okna, self.vyska_okna))
        pg.display.set_caption("The p^11 Game")



        play_obr = pg.image.load("play_obr.png").convert_alpha()
        menu_obr = pg.image.load("menu_obr.png").convert_alpha()
        primes_obr = pg.image.load("primes_obr.png").convert_alpha()
        exit_obr = pg.image.load("exit_obr.png").convert_alpha()
        endthistry_obr = pg.image.load("endthistry_obr.png").convert_alpha()
        two_obr = pg.image.load("two_obr.png").convert_alpha()
        three_obr = pg.image.load("three_obr.png").convert_alpha()
        five_obr = pg.image.load("five_obr.png").convert_alpha()
        seven_obr = pg.image.load("seven_obr.png").convert_alpha()



        self.play_button = buttOn(197, 247, play_obr)
        self.primes_button = buttOn(184, 331, primes_obr)
        self.exit_button = buttOn(203, 415, exit_obr)

        self.menu_button = buttOn(190, 510, menu_obr)

        self.endthistry_button = buttOn(310, 582, endthistry_obr)

        self.two_button = buttOn(66, 199, two_obr)
        self.three_button = buttOn(171, 200, three_obr)
        self.five_button = buttOn(276, 200, five_obr)
        self.seven_button = buttOn(381, 200, seven_obr)




        self.font_big = pg.font.SysFont("Berlin Sans FB Demi", 50, True)
        self.font_small = pg.font.SysFont("Berlin Sans FB Demi", 25, True)
        self.font_tiny = pg.font.SysFont("Berlin Sans FB Demi", 17, False)


    def make_it_Start(self):
        self.menU()   


    def menU(self):
        pg.display.flip()
        self.okno.fill(gen_svetle_pozadi())

        self.play_button.make_button(self.okno)
        self.primes_button.make_button(self.okno)
        self.exit_button.make_button(self.okno)

        self.okno.blit(self.font_big.render("The p^11 Game", True, (0, 0, 0)), (114, 20))
        self.okno.blit(self.font_small.render("High Score:", True, (0, 0, 0)), (20, 600))
        self.okno.blit(self.font_small.render(f"{self.high_score}", True, (255, 255, 255)), (150, 600))

        self.okno.blit(self.font_small.render("Base:", True, (0, 0, 0)), (400, 600))
        self.okno.blit(self.font_small.render(f"{self.base}", True, (255, 255, 255)), (465, 600))

        pg.display.update()

        running_menu = True

        while running_menu:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running_menu = False
                    self.exit()


            if self.play_button.buTton_clicked():
                self.plaY()
                running_menu = False

            elif self.primes_button.buTton_clicked():
                self.priMes()
                running_menu = False


            elif self.exit_button.buTton_clicked():
                running_menu = False
                self.exit()

            pg.display.update()

                        
    def priMes(self):

        self.okno.fill(gen_svetle_pozadi())
        
        self.two_button.make_button(self.okno)
        if self.high_score < 244140620:
            seven = False
            if self.high_score < 531438:
                five = False
                if self.high_score < 4094:
                    three = False
                else:
                    three = True
                    self.three_button.make_button(self.okno)
            else:
                five = True
                self.five_button.make_button(self.okno)
                three = True
                self.three_button.make_button(self.okno)
        else:
            seven = True
            self.seven_button.make_button(self.okno)
            five = True
            self.five_button.make_button(self.okno)
            three = True
            self.three_button.make_button(self.okno)


        self.menu_button.make_button(self.okno)

        self.okno.blit(self.font_big.render("Choose the base", True, (0, 0, 0)), (90, 15))
        

        viceradkovy_text = "The higher the base, the faster your score will grow. To unlock\nnext,higher base, you will need to pass the score of 12th power\nof the previous base minus the value of the previous base. For\nexample to unlock base 3, you need to get over 4094 of score\npoints. The highest achievable base is 7."
        linky = viceradkovy_text.split("\n")
        y = 84
        for line in linky:
            self.okno.blit(self.font_tiny.render(line, True, (0, 0, 0)), (26, y))
            y += 17

        self.okno.blit(self.font_small.render("High Score:", True, (0, 0, 0)), (20, 600))
        self.okno.blit(self.font_small.render(f"{self.high_score}", True, (255, 255, 255)), (150, 600))

        self.okno.blit(self.font_small.render("Base:", True, (0, 0, 0)), (400, 600))
        self.okno.blit(self.font_small.render(f"{self.base}", True, (255, 255, 255)), (465, 600))

        pg.display.update()

        running_primes = True
        while running_primes:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running_primes = False
                    self.exit()


            if self.two_button.buTton_clicked():
                self.base = 2
                self.priMes()

            elif self.three_button.buTton_clicked() and three:
                self.base = 3
                self.priMes()

            elif self.five_button.buTton_clicked() and five:
                self.base = 5
                self.priMes()

            elif self.seven_button.buTton_clicked() and seven:
                self.base = 7
                self.priMes()

            elif self.menu_button.buTton_clicked():
                self.menU()

        pg.display.update()                        


    def exit(self):
        pg.quit()
        sys.exit()




    

    def plaY(self):
        self.herni_pole = np.zeros((self.num, self.num))
        self.Add_number()
        self.update_Score()

        self.barva_pozadi = gen_svetle_pozadi()
        self.okno.fill(self.barva_pozadi)
        

        self.endthistry_button.make_button(self.okno)

        self.okno.blit(self.font_big.render("Score:", True, (0, 0, 0)), (5, 515))
        self.okno.blit(self.font_big.render(f"{self.score}", True, (255, 255, 255)), (137, 515))
        self.okno.blit(self.font_tiny.render("Highscore:", True, (0, 0, 0)), (5, 600))
        self.okno.blit(self.font_tiny.render(f"{self.high_score}", True, (255, 255, 255)), (92, 600))

        pg.display.update()
        


        running_play = True
        while running_play:
            
            self.Make_a_board()
            pg.display.update()

            for event in pg.event.get():
                
                puvodni_tabulka = self.herni_pole.copy()

                if event.type == pg.QUIT:
                    running_play = False
                    
                elif event.type == pg.KEYDOWN:
                    

                    if event.key == pg.K_LEFT:
                        self.movE("L")

                    elif event.key == pg.K_RIGHT:
                        self.movE("R")

                    elif event.key == pg.K_UP:
                        self.movE("U")

                    elif event.key == pg.K_DOWN:
                        self.movE("D")

                    if self.is_game_oveR():
                        self.gAme_over()
                        running_play = False

                    if (self.herni_pole == puvodni_tabulka).all() == False:
                        self.Add_number()
                        self.update_Score()

                        pg.draw.rect(self.okno, self.barva_pozadi, pg.Rect(136, 514, 388, 58))
                        self.okno.blit(self.font_big.render(f"{self.score}", True, (255, 255, 255)), (137, 515))

                        pg.draw.rect(self.okno, self.barva_pozadi, pg.Rect(91, 599, 208, 25))
                        self.okno.blit(self.font_tiny.render(f"{self.high_score}", True, (255, 255, 255)), (92, 600))



            if self.endthistry_button.buTton_clicked():
                self.gAme_over()
                running_play = False





    def Make_a_board(self):


        for x in range(self.num):
            souradnice_x = x * self.hrana_bloku + self.mezera

            for y in range(self.num):
                souradnice_y = y * self.hrana_bloku + self.mezera

                hod_ctverce = int(self.herni_pole[y][x])

                if self.base == 2:
                    pg.draw.rect(self.okno,
                                 barvicky_2[hod_ctverce],
                                 pg.Rect(souradnice_x, souradnice_y, self.hrana_ctverce, self.hrana_ctverce))
                    
                elif self.base == 3:
                    pg.draw.rect(self.okno,
                                 barvicky_3[hod_ctverce],
                                 pg.Rect(souradnice_x, souradnice_y, self.hrana_ctverce, self.hrana_ctverce))
                    
                elif self.base == 5:
                    pg.draw.rect(self.okno,
                                 barvicky_5[hod_ctverce],
                                 pg.Rect(souradnice_x, souradnice_y, self.hrana_ctverce, self.hrana_ctverce))
                    
                else:
                    pg.draw.rect(self.okno,
                                 barvicky_7[hod_ctverce],
                                 pg.Rect(souradnice_x, souradnice_y, self.hrana_ctverce, self.hrana_ctverce))


                if hod_ctverce != 0:
                    delka_hod = len(str(hod_ctverce))
                    if delka_hod < 9:
                        m = 51 - delka_hod * 3
                    elif 8 < delka_hod and delka_hod < 13:
                        m = 24 - (24 - 9) * 2
                    else:
                        m = 17 - (delka_hod - 13)
                    
                    fnt = pg.font.SysFont("Berlin Sans FB Demi", m, True)
                    napis_co = fnt.render(f"{hod_ctverce}", True, (15, 15, 15))
                    napis_kam = napis_co.get_rect(center = (souradnice_x + self.hrana_bloku / 2 - 8, souradnice_y + self.hrana_bloku / 2))

                    self.okno.blit(source = napis_co, dest = napis_kam)


    def movE(self, direction):

        for souradnice in range(self.num):

            if direction in "LR":
                line = self.herni_pole[souradnice, :]
            else:
                line = self.herni_pole[:, souradnice]

            obracene = True
            line = line[::-1]

            if direction in "LU":
                obracene = False
                line = line[::-1]

            line = self.Kombine(line)

            line = line + (self.num - len(line)) * [0]

            if obracene:
                line = line[::-1]

            if direction in "LR":
                self.herni_pole[souradnice, :] = line
            else:
                self.herni_pole[:, souradnice] = line

    def Kombine(self, line):
        
        outcome = [0]

        line = [cislo for cislo in line if cislo != 0]

        for i in line:
            if i == outcome[len(outcome) - 1]:
                outcome[len(outcome) - 1] *= int(self.base)
                self.score += outcome[len(outcome) - 1]
                outcome.append(0)

            else:
                outcome.append(i)

        outcome = [cislo for cislo in outcome if cislo != 0]
        return outcome


    def Add_number(self):
        null_ctverce = list(zip(*np.where(self.herni_pole == 0)))

        for pozice in r.sample(null_ctverce, 1):
            self.herni_pole[pozice] = self.base

    def update_Score(self):
        self.score = 0

        for x in range(self.num):
            for y in range(self.num):
                self.score += int(self.herni_pole[y][x])


        if self.score >= self.high_score:
            a = self.score
            self.high_score = a

    def is_game_oveR(self):
        kopie_pole = self.herni_pole.copy()

        for direction in "LRUD":
            self.movE(direction)

            if (self.herni_pole == kopie_pole).all() == False:
                self.herni_pole = kopie_pole
                return False
            
        return True

    # Y
    def gAme_over(self):
        self.okno.fill(gen_svetle_pozadi())

        self.okno.blit(self.font_big.render("Game Over!", True, (0, 0, 0)), (130, 50))

        self.okno.blit(self.font_small.render("Your score:", True, (0, 0, 0)), (90, 200))
        self.okno.blit(self.font_small.render(f"{self.score}", True, (255, 255, 255)), (220, 200))

        self.okno.blit(self.font_small.render("Highscore:", True, (0, 0, 0)), (110, 250))
        self.okno.blit(self.font_small.render(f"{self.high_score}", True, (255, 255, 255)), (235, 250))

        if self.score >= self.high_score:
            self.okno.blit(self.font_small.render("New Record!", True, (0, 0, 0)), (190, 135))

        self.menu_button.make_button(self.okno)

        pg.display.update()


        running_game_over = True
        while running_game_over:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running_game_over = False


            if self.menu_button.buTton_clicked():
                self.score = 0
                self.menU()
                running_game_over = False




if __name__ == "__main__":
    game = Game_p_Asterisk_asterisk_n()
    game.make_it_Start()