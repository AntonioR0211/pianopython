import turtle as tl
import keyboard
from playsound import playsound
import pygame

my_window = tl.Screen()
my_window.bgcolor("Black")
draw = tl.Turtle()
my_window.bgpic("images.gif")
pygame.init()
a1 = pygame.mixer.Sound("a1.wav")
b1 = pygame.mixer.Sound("b1.wav")
c1 = pygame.mixer.Sound("c1.wav")
d1 = pygame.mixer.Sound("d1.wav")
e1 = pygame.mixer.Sound("e1.wav")
f1 = pygame.mixer.Sound("f1.wav")
g1 = pygame.mixer.Sound("g1.wav")

draw.hideturtle()  
draw.color("white")
draw.pensize(12)

i = 0

while i == 0:
    if keyboard.is_pressed("a"):
        i += 1
        pygame.mixer.Sound.play(a1)

    if keyboard.is_pressed("b"):
        pygame.mixer.Sound.play(b1)
        
    if keyboard.is_pressed("c"):
        pygame.mixer.Sound.play(c1)
        
    if keyboard.is_pressed("d"):
        pygame.mixer.Sound.play(d1)
        
    if keyboard.is_pressed("e"):
        pygame.mixer.Sound.play(e1)
        
    if keyboard.is_pressed("f"):
        pygame.mixer.Sound.play(f1)
        
    if keyboard.is_pressed("g"):
        pygame.mixer.Sound.play(g1)

i = 0

my_window.mainloop()
