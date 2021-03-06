""" 
This code will create a list with random pairs of socks and after a shuffle the system will 
sort them automatically V0.6
"""
import random #IMPORT random to generate the random list of socks
import pygame #IMPORT PYGAME for the grapchical version of the code.
import os     #IMPORT os so we can get the images from other folders
import time   #IMPORT time so the buttons can run only once and not several times
#Initialize pygame
pygame.init()
clock = pygame.time.Clock()
#size of the screen
size = 1200, 650
#colors RGB
color_bred = (255,0,0)
color_bgreen = (0,255,0)
color_green=(0,100,0)
color_red=(100,0,0) 
color_white=(255,255,255)
color_grey=(211,211,211)
#available list of socks 
socks = [
    'blue','orange','yellow',
    'red', 'green', 'striped_orange',
    'white','black','striped_blue',
]
#random picked socks and their pairs the drawer
picked = []
pairs = []
GUI_drawer = []
#list for pairs
GUI_blue_list =[]
GUI_orange_list =[]
GUI_yellow_list = []
GUI_red_list = []
GUI_green_list = []
GUI_striped_orange_list = []
GUI_white_list = []
GUI_black_list = []
GUI_striped_blue_list = []
#for GUI purposes define socks     SOON TO CHANGE FOR PNG FILES WITHOUT BG
icon = pygame.image.load(os.path.join('images/socks.png'))
blue_sock = pygame.image.load(os.path.join('images/blue.png'))
orange_sock = pygame.image.load(os.path.join('images/orange.png'))
yellow_sock = pygame.image.load(os.path.join('images/yellow.png'))
red_sock = pygame.image.load(os.path.join('images/red.png'))
green_sock = pygame.image.load(os.path.join('images/green.png'))
white_sock = pygame.image.load(os.path.join('images/white.png'))
black_sock = pygame.image.load(os.path.join('images/black.png'))
striped_blue_sock = pygame.image.load(os.path.join('images/striped_blue.png'))
striped_orange_sock = pygame.image.load(os.path.join('images/striped_orange.png'))
#Start the screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SOCK SORTING")
pygame.display.set_icon(icon)
amount_of_socks = random.randint(2,len(socks)) #random amount of socks (minimum 2 pairs and a max length of socks)
#Text sizes and fonts
small_text = pygame.font.Font('freesansbold.ttf',20)
large_text = pygame.font.Font('freesansbold.ttf',115)
#switch case to python
def blue():
    screen.blit(blue_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_blue_list.append(blue_sock)
    if GUI_blue_list not in GUI_drawer:
        GUI_drawer.append(GUI_blue_list)

def orange():
    screen.blit(orange_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_orange_list.append(orange_sock)
    if GUI_orange_list not in GUI_drawer:
        GUI_drawer.append(GUI_orange_list)
    
def yellow():
    screen.blit(yellow_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_yellow_list.append(yellow_sock)
    if GUI_yellow_list not in GUI_drawer:
        GUI_drawer.append(GUI_yellow_list)
    
def red():
    screen.blit(red_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_red_list.append(red_sock)
    if GUI_red_list not in GUI_drawer:
        GUI_drawer.append(GUI_red_list)
    
def black():
    screen.blit(black_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_black_list.append(black_sock)
    if GUI_black_list not in GUI_drawer:
        GUI_drawer.append(GUI_black_list)
    
def white():
    screen.blit(white_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_white_list.append(white_sock)
    if GUI_white_list not in GUI_drawer:
        GUI_drawer.append(GUI_white_list)    
    
def striped_blue():
    screen.blit(striped_blue_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_striped_blue_list.append(striped_blue_sock)
    if GUI_striped_blue_list not in GUI_drawer:
        GUI_drawer.append(GUI_striped_blue_list)
    
def striped_orange():
    screen.blit(striped_orange_sock, (random.randint(0,800),random.randint(0,462)))
    GUI_striped_orange_list.append(striped_orange_sock)
    if GUI_striped_orange_list not in GUI_drawer:
        GUI_drawer.append(GUI_striped_orange_list)
    
def green():
    screen.blit(green_sock, (random.randint(0,800),random.randint(0,462)))#462 ensures that the socks are inside the screen
    GUI_green_list.append(green_sock)
    if GUI_green_list not in GUI_drawer:
       GUI_drawer.append(GUI_green_list)

#generates text for buttons
def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Dictionary to pull socks randomly
def pull(sock_list):
    sock_dict = {
        'blue':blue,
        'orange':orange,
        'yellow':yellow,
        'red':red,
        'black':black,
        'white':white,
        'striped_orange':striped_orange,
        'striped_blue':striped_blue,
        'green':green
    }
    function = sock_dict.get(sock_list, lambda:"invalid")
    running = False
    function()

#function that sorts the socks and displays them with their pair
#this will change as they only are randomly placed on screen need to come up with a way to get it in order
def sort(x,y):
    for element in range(len(GUI_drawer)):
        x_c=random.randint(0,800)
        y_c=random.randint(0,462)
        screen.blit(GUI_drawer[element][0],(x_c,y_c))
        screen.blit(GUI_drawer[element][1],(x_c+x,y_c+y))

#button function so you can add more buttons
def button(x,y,w,h,ic,ac,msg,status = None):
    mouse = pygame.mouse.get_pos()                      #gets mouse position
    click = pygame.mouse.get_pressed()                  #gets if mouse is clicking
    if ((w+x > mouse[0] >x) and (y+h >mouse[1]>y)):     #if mouse pointer is inside the "button"
        pygame.draw.rect(screen,ac,(x,y,w,h))           #highlight the button to see selection
        if(click[0] == 1 and status != None):           #if left click and is from a button
            if status == "pull":                        #if is the right button
                t0 = time.time()
                for x in range(amount_of_socks):
                    number = random.randint(0,8)
                    if socks[number] not in picked:
                        picked.append(socks[number])
                time.sleep(1)                           #timer to get one click only
                screen.fill(color_grey)
                pygame.display.update()
                pairs = picked
                for element in range(len(picked)):
                    pull(picked[element])
                    pull(pairs[element])
                print(time.time()-t0)
            elif(status == "sort"):
                t0 = time.time()
                time.sleep(1)
                screen.fill(color_grey)
                sort(0,70)
                print(time.time()-t0)
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    textsurf, textrect = text_objects(msg, small_text, color_grey)
    textrect.center= ((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)
    pygame.display.update()
    clock.tick(60)

#Run the introduction of the GUI
def intro():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        #for loop to select from random amount of socks random socks
        screen.fill(color_grey)
        textsurf, textrect = text_objects("Sorting socks", large_text,color_green)
        textrect.center= (460,300)
        screen.blit(textsurf,textrect)
        pygame.display.update()
        clock.tick(60)
        loop()
def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        button(1000,100,100,50,color_green,color_bgreen,"random","pull")
        button(1000,400,100,50,color_red,color_bred,"pair","sort")
        pygame.display.update()
        clock.tick(60)
intro()
loop()    
pygame.quit()
quit()