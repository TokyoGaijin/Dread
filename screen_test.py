import pygame
import colorswatch as cs


test_screen = (640, 480)
surface = pygame.display.set_mode(test_screen)
BG = cs.black["pygame"]

menu_screen = ["--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "-------------------------------------------------------------------------------A------------------------------------------------",
               "-----------------------------------------R------------------------------------A-AA----------------------------------------------",
               "-----------------------------------------RR---------------EEEEEEEE-----------AA---A-------DDDDDDDDDD----------------------------",
               "--------------------DDDDDDDD-------------RRRRRRRR-------EEE-----E-----------AA----AA------DD--------DDDDD-----------------------",
               "--------------------DD------DDDDD---------RR-----RR-----EE-----------------AA-------AA----DD-------------DDD--------------------",
               "--------------------DD------------DDD-----RR------RR----EE------E---------AA--------AA----DD---------------DD-------------------",
               "--------------------DD--------------DD----RRRRRRRR------EEEEEEEEE---------AAAAAAAAAAAA----DD---------------DD-------------------",
               "--------------------DD--------------DD----RR----RR------EE------E---------AA--------AA----DD---------------DD-------------------",
               "--------------------DD--------------DD----RR------RR----EE---------E-----AA---------AA----DD---------------DD-------------------",
               "--------------------DD--------------DD----RR------RR----EE--EEEEEEEEE----AA---------AA----DDDDDDDDDDD------DD-------------------",
               "--------------------DD----------DDDD-------RR-----RRR---EEEE-------------AA--------------------------DD----DD-------------------",
               "--------------------DD-------DDD----------RR------------EE---------------AA---------------------------DD---DD-------------------",
               "--------------------DD-----DD-----------RR-------------------------------AA----------------------------DD--DD-------------------",
               "--------------------DD---DD----------------------------------------------A-------------------------------DDDD-------------------",
               "--------------------DD--DD-----DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD------DD-------------------",
               "--------------------DD-DD-----DDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDD-----DD-------------------",
               "--------------------DDDD-------DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD---------------------------",
               "--------------------DD----------------------------------------------------------------------------------------------------------",
               "--------------------DD---------------D---D---D---D-------D---D-------DDDD----D----DDDD----D---D---------------------------------",
               "-------------------------------------D---DD--D----D-----D---D-D-----D--------D---D----D---DD--D---------------------------------",
               "-------------------------------------D---D-D-D-----D---D---D---D-----DDDD----D---D----D---D-D-D---------------------------------",
               "-------------------------------------D---D--DD------D-D---DDDDDDD--------D---D---D----D---D--DD---------------------------------",
               "-------------------------------------D---D---D-------D---D-------D---DDDD----D----DDDD----D---D---------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "-------------------------------------------------------AAA----------------------------------------------------------------------",
               "--------------------A----------------------------AAA-----A----------------------------------------------------------------------",
               "---------AAAAAA-----AAA----AAAAAA--AA-AA-AA-----A---A----AAAA--AA----A----------------------------------------------------------",
               "--------A----A-----A---A--A----A----AA--A--AA---AAAA-----A---A--A----A----------------------------------------------------------",
               "--------A----A-----A---A--A----A----A---A---A---A--------A---A---A---A----------------------------------------------------------",
               "---------AAAAAAA----AAA----AAAAAAA--A------AAA---AAAA---AAAAA-----AAAA----------------------------------------------------------",
               "-------------------A-------------------------------------------------A----------------------------------------------------------",
               "--------------------AAA----------------------------------------------A----------------------------------------------------------",
               "-----------------------A-----------------------------------------A--A-----------------------------------------------------------",
               "--------------------AAA------------------------------------------AAA------------------------------------------------------------",
               "------------------------------------M---M--M--M-----MM-----M---M----------------------------------M-----M-----------------------",
               "------------------------------------MM-MM-----M--M-M--M-----M-M---MM----M---M---MM----MMMM---MM---M--M--------------------------",
               "------------------------------------M-M-M--M--M-M--MMMM------M---M--M---MM-MM--M--M-----M---M--M--M-M---M-----------------------",
               "------------------------------------M---M--M--MMM--M---------M---M--M---M-M-M--M--M----M----M--M--MMM---M-----------------------",
               "------------------------------------M---M--M--M--M--MMM------M----MMMM--M---M---MMMM--MMMM---MMM--M--M--M-----------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------SSSSSSS----SSSSSS-----------SS---------------SSSSSS--SSSSSSSSS----------------------------",
               "------------------------------------SS-------SS--SS----SS--------SS-SS-----------SS--------SS-----------------------------------",
               "------------------------------------SS-----------SS------SS-----SS---SS--------SS----------SS-----------------------------------",
               "--------------------------------------SS---------SS------SS----SS-----SS-------SS----------SS-----------------------------------",
               "----PPPPP--PPP---PPPP---PPP---PPP-------SSSS-----SS----SS-----SS-------SS------SS----------SSSSSSS------------------------------",
               "-----P--PP-P--P--P-----P-----P---------------SS--SSSSSS------SSSSSSSSSSSSS-----SS----------SS-----------------------------------",
               "-----P---P-P-----PPP----PP----PP-------------SS--SS---------SS-----------SS----SS----------SS-----------------------------------",
               "-----P---P-P-----P--------P-----P----SS----SSS---SS--------SS-------------SS-----SS--------SS-----------------------------------",
               "-----PPPP--P-----PPPP--PPP---PPP-------SSSSS-----SS-------SS---------------SS------SSSSSS--SSSSSSSSS----------------------------",
               "-----P--------------------------------------------------------------------------------------------------------------------------",
               "-----P--------------------------------------------------------------------------------------------------------------------------",
               "----------------------------------------------------------------------P-------------P----------------------P--------------------",
               "----------------------------------------------------------------------P-------------P-------------------------------------------",
               "--------------------------------------------------------------------PPPPP---PPP-----P--------PPP----PPPPP--P--PP-PP-------------",
               "----------------------------------------------------------------------P----P---P----P-PPP---P---P--P---P---P---PP--P------------",
               "----------------------------------------------------------------------P----P---P----PP---P--PPPPP--P---P---P---P---P------------",
               "----------------------------------------------------------------------P-P--P---P----P----P--P------P---P---P---P---P------------",
               "-----------------------------------------------------------------------P----PPP-----PPPPP----PPP----PPP----P--PP----P-----------",
               "-------------------------------------------------------------------------------------------------------P------------------------",
               "---------------------------------------------------------------------------------------------------P---P------------------------",
               "----------------------------------------------------------------------------------------------------PPP-------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------",
               "--------------------------------------------------------------------------------------------------------------------------------"]


screen_display = []

x, y = 0, 0

class Pixel(object):
    def __init__(self, surface, posX, posY, color):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = color
        self.rect = pygame.Rect(self.posX, self.posY, 5, 5)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

        

for row in menu_screen:
    for col in row:
        if col == "D" or col == "P":
            screen_display.append(Pixel(surface, x, y, cs.death_red["pygame"]))
        if col == "R":
            screen_display.append(Pixel(surface, x, y, cs.elevenoclock["pygame"]))
        if col == "E":
            screen_display.append(Pixel(surface, x, y, cs.night_gray["pygame"]))
        if col == "A":
            screen_display.append(Pixel(surface, x, y, cs.shit["pygame"]))
        if col == "M":
            screen_display.append(Pixel(surface, x, y, cs.gray["pygame"]))
        if col == "S":
            screen_display.append(Pixel(surface, x, y, cs.golden_shower["pygame"]))
        x += 5
    y += 5
    x = 0


def drawscreen():
    for pixels in screen_display:
        pixels.draw()
    


inPlay = True
while inPlay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False

    drawscreen()
    pygame.display.update()
    surface.fill(BG)
