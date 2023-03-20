# -*- coding: utf-8 -*-
"""
v2 -> Color changed button
V3= everything (textbox, label, buttons) define at initialization
v4= more organized and easy button creation with class

Got help from 
ChatGPT
https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python

Created on Thu Feb  9 15:13:53 2023

https://www.rapidtables.com/web/color/RGB_Color.html
@author: kec994
pip install pygame==2.1.2
"""

# Imports
import sys
import pygame
#from time import sleep


#%%
#%% Set Color class
class colors():
    
    Black = (0,0,0)
    White = (255,255,255) 
    Red = (255,0,0)
    Green = (0,255,0)
    Blue = (0,0,255)
    
    Violet = (150, 75, 194)
    Yellow = (255, 255, 0)
    Cyan = (0, 255, 255)
    Magenta = (255,0,255)
    
    Orange_dark = (255,140,0)
    Coral = (255,127,80)
    
    Silver = (192,192,192)
    Gray = (128,128,128) 
    Maroon = (128,0,0) 
    Olive = (128,128,0)
    Green_dark = (0,128,0)
    Purple = (128,0,128)
    Teal = (0,128,128)
    Navy = (0,0,128)
    Mint_cream = (245,255,250)
    Ivory = (255,255,240)
    Wheat = (245,222,179)
    Indigo = (75,0,130)
    Gold = 	(255,215,0)
    
    Magenta_dark = (139,0,139)
    Saddle_brown = (139,69,19)
    Slate_gray = (112,128,144)
    Indian_red = (205,92,92)
#%%
#%%
#%%
#%%
# Configuration
def create_pygame(fps = 60, width= 640, height = 480, font_det=('Arial', 40), caption='pygame', icon=None):
    pygame.init()
    pygame.display.set_caption(caption)
    
    if icon!=None:
        pygame_icon = pygame.image.load(icon)
        pygame.display.set_icon(pygame_icon)
    
    fpsClock = pygame.time.Clock()
    font = pygame.font.SysFont(font_det[0],font_det[1])
    
    objects = []
    screen = pygame.display.set_mode((width, height))
    
    return screen, font, fpsClock, fps, objects




#%%
#%%
#%%
#%%
class TextBox:
    def __init__(self, x, y, width, height, text='', font_size=32, font_=None, max_c=5, screen=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(font_, font_size)
        self.color = (0, 0, 0)
        self.text = text
        self.active = False
        self.screen=screen
        self.max_c=max_c

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"Text entered: {self.text}")
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self):
        # Render the text.
        txt_surface = self.font.render(self.text, True, self.color)
        # Resize the box if the text is too long.
        width = max(self.max_c, txt_surface.get_width()+10)
        self.rect.w = width
        # Blit the text.
        self.screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)

#%%
#%%
#%%
#%%
class Button:
    def __init__(self, x, y, width, height, text, font_size=20, font_=None, text_color=colors.White,
                 button_colors=(colors.Magenta_dark,colors.Coral, colors.Navy),
                 action=None, screen=None):
        #self.x = x
        #self.y = y
        #self.width = width
        #self.height = height
        #self.text = text
        self.action = action
        self.screen=screen
        
        font = pygame.font.Font(font_, font_size)
    
        self.onePress = False
        self.alreadyPressed = False
        self.fillColors = button_colors
        self.buttonSurface = pygame.Surface((width, height))
        self.buttonRect = pygame.Rect(x, y, width, height)
        self.buttonSurf = font.render(text, True, text_color)
        

    def draw(self, mousePos, mouse_pressed): # pygame.mouse.get_pos(),pygame.mouse.get_pressed(num_buttons=3)[0]           
        #mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors[0])
        if self.buttonRect.collidepoint(mousePos):
            
            self.buttonSurface.fill(self.fillColors[1])
            #if pygame.mouse.get_pressed(num_buttons=3)[0]:
            if mouse_pressed:
                self.buttonSurface.fill(self.fillColors[2])
                if self.onePress and self.action:
                    self.action()
                elif not self.alreadyPressed:
                    self.action()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)
            
#%%
def print_text(text):
    print(text)
    
#%%
#%%
#%%
#%%
class Label:
    def __init__(self, x, y, text, font=None, text_color=colors.White, size=20, screen=None):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.text_color = text_color
        self.size=size
        self.screen=screen

    def draw(self):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.center = (self.x, self.y)

        self.screen.blit(text, text_rect)
#%%
#%%
#%%
class create_func:
    def __init__(self,func,**kargs):
        self.kargs=kargs
        self.func=func
    def d_func(self,*args2,**kargs2):
        self.kargs.update(kargs2)
        self.args2=args2
        return self.func(*self.args2,**self.kargs)
        
#%% Quit Pygame
def quit_pygame(s=None):
    pygame.quit()
    sys.exit()

#%%
#%%
#%%
if __name__=='__main__':
    
    screen, font, fpsClock, fps, objects = create_pygame()
    
    
    def_bt=create_func(Button,font_size=20, font_=None, text_color=colors.White,
                 button_colors=(colors.Magenta_dark,colors.Coral, colors.Navy),
                 screen=screen)
    def_tb=create_func(TextBox,screen=screen)
    
    def_lb=create_func(Label,text_color=colors.Green_dark,screen=screen)
    
    
    
    # Create two text boxes.
    text_box1 = def_tb.d_func(50, 50, 140, 40, text='Text box 1',max_c=60)
    text_box2 = def_tb.d_func(200, 200, 140, 40, text='Text box 2',max_c=5)
    
    # Buttons
    #red_button = def_bt.d_func(100,100,100,50,"Red",lambda: print_text("Red button was clicked!"))
    red_button = def_bt.d_func(100,100,100,50,"Red",action=lambda: print_text('Red button was clicked!'))
    green_button = def_bt.d_func(200,100,100,50,"Green",action=lambda: print_text('Green button was clicked!'))
    exit_button = def_bt.d_func(0,350,100,50,"Exit",action=lambda: quit_pygame())
    
    
    
    # Label
    label_0 = def_lb.d_func(200, 300, text='Lanel 0')
    label_1 = def_lb.d_func(200, 320, text= 'Lanel 1')
    
    running = True
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            # Text box -----------------------------------
            text_box1.handle_event(event)
            text_box2.handle_event(event)
            
    

        # Fill the screen with white.
        screen.fill((255, 255, 255))

        # Draw the text boxes. -----------------------------------
        text_box1.draw()
        text_box2.draw()
        #print(text_box1.text)
        #print(text_box2.text)
        
        # Buttons -----------------------------------
        mousePos, mouse_pressed = pygame.mouse.get_pos(),pygame.mouse.get_pressed(num_buttons=3)[0]           
        red_button.draw(mousePos, mouse_pressed)
        green_button.draw(mousePos, mouse_pressed)
        exit_button.draw(mousePos, mouse_pressed)
        
        # Label -----------------------------------
        label_0.draw()
        label_1.draw()     
        #print(label_0.text)
        #print(label_1.text)

        pygame.display.update()
        

    pygame.quit()
    
    


