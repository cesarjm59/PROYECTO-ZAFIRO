import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)

        self.mapa_seleccionado = '1'
        self.menu_seleccion_mapa()
        self.new_game()

    def menu_seleccion_mapa(self):
        pg.mouse.set_visible(True) 
        seleccionando = True

        fuente_titulo = pg.font.SysFont('Impact', 56)
        fuente_opciones = pg.font.SysFont('Impact', 22)
        fuente_detalles = pg.font.SysFont('Arial', 12, bold=True)
        
        try:
            imagen_fondo = pg.image.load('resources/textures/hola.png').convert()
            imagen_fondo = pg.transform.scale(imagen_fondo, RES) 
        except pg.error:
            imagen_fondo = pg.Surface(RES)
            imagen_fondo.fill((20, 10, 10)) 

        ancho_panel = 440
        alto_panel = 80
        x_pos = 90  
        
        rect_btn1 = pg.Rect(x_pos, HEIGHT // 2 - 90, ancho_panel, alto_panel)
        rect_btn2 = pg.Rect(x_pos, HEIGHT // 2 + 10, ancho_panel, alto_panel)
        rect_btn3 = pg.Rect(x_pos, HEIGHT // 2 + 110, ancho_panel, alto_panel)

        while seleccionando:
            self.clock.tick(60)

            self.screen.blit(imagen_fondo, (0, 0))
            pos_mouse = pg.mouse.get_pos()
            
            txt_titulo_sombra = fuente_titulo.render("SELECCIONA MISIÓN", True, (5, 5, 5))
            txt_titulo = fuente_titulo.render("SELECCIONA MISIÓN", True, (240, 35, 35))
            self.screen.blit(txt_titulo_sombra, (x_pos + 3, HEIGHT // 5 - 37))
            self.screen.blit(txt_titulo, (x_pos, HEIGHT // 4 - 40))

            pg.draw.line(self.screen, (150, 30, 30), (x_pos - 15, HEIGHT // 5), (x_pos - 15, HEIGHT // 2 + 180), 3)

            if rect_btn1.collidepoint(pos_mouse):
                color_fondo1 = (130, 15, 15, 170) 
                color_borde1 = (255, 100, 100)      
                color_texto1 = (255, 255, 255)
            else:
                color_fondo1 = (12, 12, 12, 215)  
                color_borde1 = (140, 35, 35)       
                color_texto1 = (210, 170, 170)

            if rect_btn2.collidepoint(pos_mouse):
                color_fondo2 = (130, 15, 15, 170)
                color_borde2 = (255, 100, 100)
                color_texto2 = (255, 255, 255)
            else:
                color_fondo2 = (12, 12, 12, 215)
                color_borde2 = (140, 35, 35)
                color_texto2 = (210, 170, 170)
            if rect_btn3.collidepoint(pos_mouse):
                color_fondo3 = (130, 15, 15, 170)
                color_borde3 = (255, 100, 100)
                color_texto3 = (255, 255, 255)
            else:
                color_fondo3 = (12, 12, 12, 215)
                color_borde3 = (140, 35, 35)
                color_texto3 = (210, 170, 170)
            lista_botones = [
                (rect_btn1, color_fondo1, color_borde1), 
                (rect_btn2, color_fondo2, color_borde2),
                (rect_btn3, color_fondo3, color_borde3) 
            ]    
            for rect, color_f, color_b in [(rect_btn1, color_fondo1, color_borde1), (rect_btn2, color_fondo2, color_borde2), (rect_btn3, color_fondo3, color_borde3)]:
                superficie_btn = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
                superficie_btn.fill(color_f)
                pg.draw.rect(superficie_btn, color_b, (0, 0, rect.width, rect.height), 2, border_radius=4)
                self.screen.blit(superficie_btn, (rect.x, rect.y))

            txt_m1_tit = fuente_opciones.render("UAC NUCLEAR INFRASTRUCTURE", True, color_texto1)
            txt_m1_det = fuente_detalles.render("RISK LEVEL: NOMINAL  ||  LOCATION: EARTH", True, (140, 135, 135))
            self.screen.blit(txt_m1_tit, (rect_btn1.x + 25, rect_btn1.y + 12))
            self.screen.blit(txt_m1_det, (rect_btn1.x + 27, rect_btn1.y + 48))

            txt_m2_tit = fuente_opciones.render("THE CHAOTIC LABYRINTHS", True, color_texto2)
            txt_m2_det = fuente_detalles.render("RISK LEVEL: EXTREME  ||  LOCATION: HELL", True, (140, 135, 135))
            self.screen.blit(txt_m2_tit, (rect_btn2.x + 25, rect_btn2.y + 12))
            self.screen.blit(txt_m2_det, (rect_btn2.x + 27, rect_btn2.y + 48))

            txt_m3_tit = fuente_opciones.render("PHOBOS ANOMALY STATION", True, color_texto3)
            txt_m3_det = fuente_detalles.render("RISK LEVEL: NIGHTMARE  ||  LOCATION: MOON", True, (140, 135, 135))
            self.screen.blit(txt_m3_tit, (rect_btn3.x + 25, rect_btn3.y + 12))
            self.screen.blit(txt_m3_det, (rect_btn3.x + 27, rect_btn3.y + 48))

            pg.display.flip()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        if rect_btn1.collidepoint(event.pos):
                            self.mapa_seleccionado = '1'
                            seleccionando = False 
                        elif rect_btn2.collidepoint(event.pos):
                            self.mapa_seleccionado = '2'
                            seleccionando = False
                        elif rect_btn3.collidepoint(event.pos):
                            self.mapa_seleccionado = '3'
                            seleccionando = False         
        pg.mouse.set_visible(False)

    def new_game(self):
        self.map = Map(self, seleccion_mapa=self.mapa_seleccionado)
        self.player = Player(self)

        if self.mapa_seleccionado == '1':
            self.player.x, self.player.y = 1.5, 5.0
        elif self.mapa_seleccionado == '2':
            self.player.x, self.player.y = 1.5, 1.5
        elif self.mapa_seleccionado == '3':
            self.player.x, self.player.y = 1.5, 1.5

        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)

        self.pathfinding.get_path.cache_clear()
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()      
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
if __name__ == '__main__':
    game = Game()
    game.run()