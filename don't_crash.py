import pygame
import random

pygame.init()
gamedisplay = pygame.display.set_mode((800,600))
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Don't Crash")
clock = pygame.time.Clock()

explode_sound = pygame.mixer.Sound("crash.wav")
launch_sound = pygame.mixer.Sound("launch.wav")
ring_sound = pygame.mixer.Sound("ring.wav")
pygame.mixer.music.load("The Easy Winners.mp3")
roadimg = pygame.image.load("road.jpg")
beachimg = pygame.image.load("beach.png")
mycarimg = pygame.image.load("yellow_car.png")
explodeimg = pygame.image.load("explode.png")
busimg = pygame.image.load("bus.png")
bluecarimg = pygame.image.load("blue_car.png")
policecarimg = pygame.image.load("police_car.png")
redcarimg = pygame.image.load("red_car.png")
introimg = pygame.image.load("intro.jpg")
rocketimg = pygame.image.load("rocket.png")
rocketicon = pygame.image.load("rocketicon.png")
missileimg = pygame.image.load("missile.png")


#**********color**********
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
brightred = (255,0,0)
green = (0,200,0)
brightgreen = (0,255,0)
blue = (0,0,200)
brightblue = (0,0,255)
yellow = (200,200,0)
brightyellow = (255,255,0)
purple = (200,0,200)
brightpurple = (255,0,255)

#**********functions********
def quitgame():
    pygame.quit()
    quit()

def road1(x,y):
    gamedisplay.blit(roadimg,(x,y))
def road2(x,y):
    gamedisplay.blit(roadimg,(x,y))
def road3(x,y):
    gamedisplay.blit(roadimg,(x,y))
def beach1(x,y):
    gamedisplay.blit(beachimg,(x,y))
def beach2(x,y):
    gamedisplay.blit(beachimg,(x,y))
def beach3(x,y):
    gamedisplay.blit(beachimg,(x,y))

def Label(msg,x,y,size,color):
    font = pygame.font.SysFont("comicsansms",size)
    text = font.render(msg,True,color)
    gamedisplay.blit(text,(x,y))

def Button(msg,x,y,width,height,i_color,a_color,command=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gamedisplay,a_color,(x,y,width,height))
        if click[0] == 1 and command != None:
            command()
    else:
        pygame.draw.rect(gamedisplay,i_color,(x,y,width,height))
    buttontext = pygame.font.SysFont("comicsansms",20)
    buttonmsg = buttontext.render(msg,True,black)
    buttonmsgrect = buttonmsg.get_rect()
    buttonmsgrect.center = ((x+width/2),(y+height/2))
    gamedisplay.blit(buttonmsg,buttonmsgrect)


def explode(x,y):
    x -= 50
    y -= 50
    gamedisplay.blit(explodeimg,(x,y))
    pygame.mixer.Sound.play(explode_sound)

def crash(x,y):
    pygame.mixer.music.stop()
    explode(x,y)
    Label("You Crashed!",100,200,100,yellow)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Button("Try Again",200,400,100,50,green,brightgreen,gameloop)
        Button("Exit",500,400,100,50,red,brightred,quitgame)

        pygame.display.update()
        clock.tick(15)

def scorelabel(score):
    Label("Score: "+str(score),5,5,30,blue)

def unpause():
    pygame.mixer.music.unpause()
    global paused
    paused = False

def pause():
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        Label("Paused",250,150,100,blue)
        Button("Continue",200,400,100,50,green,brightgreen,unpause)
        Button("Exit",500,400,100,50,red,brightred,quitgame)
        Button("Restart", 680, 500, 100, 50, yellow, brightyellow, gameloop)
        Button("Intro",20,500,100,50,purple,brightpurple,intro)
        pygame.display.update()
        clock.tick(15)


def rocket(x,y):
    gamedisplay.blit(rocketimg,(x,y))
def missile(x,y):
    gamedisplay.blit(missileimg,(x,y))
def missilelabel(shots):
    gamedisplay.blit(rocketicon,(600,470))
    Label("X "+str(shots),730,500,30,purple)


#************cars*************
def mycar(x,y):
    gamedisplay.blit(mycarimg,(x,y))
def bus(x,y):
    gamedisplay.blit(busimg,(x,y))
def bluecar(x,y):
    gamedisplay.blit(bluecarimg,(x,y))
def policecar(x,y):
    gamedisplay.blit(policecarimg,(x,y))
def redcar(x,y):
    gamedisplay.blit(redcarimg,(x,y))



#*********Main_game***********
def intro():
    gamedisplay.blit(introimg, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Label("Welcome",250,80,70,blue)
        Label("to",370,170,50,yellow)
        Label("Don't Crash",130,210,100,red)
        Label("Press p to pause",300,470,27,purple)
        Label("Press SPACE to Launch",270,510,27,purple)
        Button("Start",200,400,100,50,green,brightgreen,gameloop)
        Button("Exit",500,400,100,50,blue,brightblue,quitgame)
        pygame.display.update()


def gameloop():
    pygame.mixer.music.play(-1)
    global paused
    speed = 0
    score = 0
    shots = 0
    change_x = 0
    myx = 370

    road1y = -225
    road2y = -225-825
    road3y = -225-825-825
    road_speed = 15

    beach1y = -1422+600
    beach2y = -1422*2 + 600
    beach3y = -1422*3 + 600

    busx = random.randrange(100,700-72)
    busy = -210
    bus_speed = -2

    bluecarx = random.randrange(100,700-67)
    bluecary = -160
    bluecar_speed = 0

    policecarx= random.randrange(100,700-83)
    policecary = -170
    policecar_speed = -4

    redcarx = random.randrange(100,700-69)
    redcary = -170
    redcar_speed = -6

    rocketx = random.randrange(100,700-75)
    rockety = -50
    rocket_speed = 3

    missilex = -500
    missiley = 600
    missile_speed = -7

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -5
                if event.key == pygame.K_RIGHT:
                    change_x = 5
                if event.key == pygame.K_p:
                    paused = True
                    pause()
                if event.key == pygame.K_SPACE:
                    if shots > 0:
                        pygame.mixer.Sound.play(launch_sound)
                        shots -= 1
                        missilex = myx+10
                        missiley = 460
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_x = 0
        #*******Beach*******
        if beach1y > 600:
            beach1y = -1422
        if beach2y > 600:
            beach2y = -1422
        if beach3y > 600:
            beach3y = -1422
        beach1y += road_speed + speed
        beach2y += road_speed + speed
        beach3y += road_speed + speed
        beach1(0,beach1y)
        beach2(0,beach2y)
        beach3(0,beach3y)

        #********Road********
        if road1y > 600:
            road1y = -825
        if road2y > 600:
            road2y = -825
        if road3y > 600:
            road3y = -825
        road1y += road_speed + speed
        road2y += road_speed + speed
        road3y += road_speed + speed
        road1(100, road1y)
        road2(100,road2y)
        road3(100,road3y)
        #*********************

        scorelabel(score)
        missilelabel(shots)

        myx += change_x
        mycar(myx,460)

        bus(busx,busy)
        busy += bus_speed + speed
        if busy > 600:
            busy = -2000
            busx = random.randrange(100,700-72)
            score += 1
        if bluecarx < busx < bluecarx + 67 or bluecarx < busx+72 <bluecarx + 67 or bluecarx < busx+36 <bluecarx + 67:
            busx = random.randrange(100,700-72)
        if policecarx < busx < policecarx + 83 or policecarx < busx+72 < policecarx + 83 or policecarx <  busx+36 < policecarx + 83:
            busx = random.randrange(100, 700 - 72)
        if redcarx < busx < redcarx + 69 or redcarx < busx+72 < redcarx + 69 or redcarx < busx+36 < redcarx + 69:
            busx = random.randrange(100, 700 - 72)

        bluecar(bluecarx,bluecary)
        bluecary += bluecar_speed + speed
        if bluecary > 600:
            bluecary = -1000
            bluecarx = random.randrange(100,700-67)
            score += 1
        if busx < bluecarx < busx+72 or busx < bluecarx + 67 < busx+72 or busx < bluecarx+33.5 < busx + 72:
            bluecarx = random.randrange(100,700-67)
        if policecarx < bluecarx < policecarx + 83 or policecarx < bluecarx+67 < policecarx + 83 or policecarx < bluecarx+33.5 < policecarx + 83:
            bluecarx = random.randrange(100,700-67)
        if redcarx < bluecarx < redcarx + 69 or redcarx < bluecarx+67 < redcarx + 69 or redcarx < bluecarx+33.5 < redcarx + 69:
            bluecarx = random.randrange(100, 700 - 67)

        policecar(policecarx,policecary)
        policecary += policecar_speed + speed
        if policecary > 600:
            policecary = -3000
            policecarx = random.randrange(100,700-83)
            score += 1
        if busx < policecarx < busx + 72 or busx < policecarx+83 < busx + 72 or busx < policecarx+83/2 < busx + 72:
            policecarx = random.randrange(100, 700 - 83)
        if bluecarx < policecarx < bluecarx + 67 or bluecarx < policecarx+83 < bluecarx + 67 or bluecarx < policecarx+83/2 < bluecarx + 67:
            policecarx = random.randrange(100, 700 - 83)
        if redcarx < policecarx < redcarx + 69 or redcarx < policecarx+83 < redcarx + 69 or redcarx < policecarx+83/2 < redcarx + 69:
            policecarx = random.randrange(100, 700 - 83)

        redcar(redcarx,redcary)
        redcary += redcar_speed + speed
        if redcary > 600:
            redcary = -2000
            redcarx = random.randrange(100, 700 - 69)
            score += 1
        if busx < redcarx < busx + 72 or busx < redcarx+69 < busx + 72 or busx < redcarx+69/2 < busx + 72:
            redcarx = random.randrange(100, 700 - 69)
        if bluecarx < redcarx < bluecarx + 67 or bluecarx < redcarx+69 < bluecarx + 67 or bluecarx < redcarx+69/2 < bluecarx + 67:
            redcarx = random.randrange(100, 700 - 69)
        if policecarx < redcarx < policecarx + 83 or policecarx <  redcarx+69 < policecarx + 83 or policecarx < redcarx+69/2 < policecarx + 83:
            redcarx = random.randrange(100, 700 - 69)

        #**************rocket_and_missile*************
        rocket(rocketx,rockety)
        rockety += rocket_speed
        if rockety > 600:
            rockety = -1000
            rocketx = random.randrange(100,700-75)
        if rockety+50 > 460:
            if rocketx < myx < rocketx+75 or rocketx < myx+62 < rocketx+75 or rocketx < myx+31 < rocketx+75:
                rockety = -1000
                rocketx = random.randrange(100,700-75)
                shots += 1
                pygame.mixer.Sound.play(ring_sound)

        missile(missilex,missiley)
        missiley += missile_speed
        if missiley+130 < 0:
            missiley = 600
            missilex = -500
        if busy+210 > missiley:
            if busx+10 < missilex < busx+72-10 or busx+10 < missilex+44 < busx+72-10 or busx+10 < missilex+22 < busx+72-10:
                explode(missilex+22,missiley)
                missilex = -500
                missiley = 600
                busx = -1000
                busy = 1000
        if bluecary+150-30 > missiley:
            if bluecarx+15 < missilex < bluecarx+67-15 or bluecarx+15 < missilex+44 < bluecarx+67-15 or bluecarx+15 < missilex+22 < bluecarx+67-15:
                explode(missilex + 22, missiley)
                missilex = -500
                missiley = 600
                bluecarx = -2000
                bluecary = 1000
        if policecary+165-20 > missiley:
            if policecarx+20 < missilex < policecarx+83-20 or policecarx+20 < missilex+44 < policecarx+83-20 or policecarx+20 < missilex+22 < policecarx+83-20:
                explode(missilex + 22, missiley)
                missilex = -500
                missiley = 600
                policecarx = -3000
                policecary = 1000
                score += 1
        if redcary+130 > missiley:
            if redcarx+5 < missilex < redcarx+69-5 or redcarx+5 < missilex+44 < redcarx+69-5 or redcarx+5 < missilex+22 < redcarx+69-5:
                explode(missilex + 22, missiley)
                missilex = -500
                missiley = 600
                redcarx = -4000
                redcary = 1000

        #************crashes*************
        if myx < 100 or myx+62 > 700:
            crash(myx+31,460)
        if busy+210 > 460:
            if busx+10 < myx < busx+72-10 or busx+10 < myx+62 < busx+72-10 or busx+10 < myx+31 < busx+72-10:
                crash(myx+31,460)
        if bluecary+150-30 > 460:
            if bluecarx+15 < myx < bluecarx+67-15 or bluecarx+15 < myx+62 < bluecarx+67-15 or bluecarx+15 < myx+31 < bluecarx+67-15:
                crash(myx+31,460)
        if policecary+165-20 > 460:
            if policecarx+20 < myx < policecarx+83-20 or policecarx+20 < myx+62 < policecarx+83-20 or policecarx+20 < myx+31 < policecarx+83-20:
                crash(myx+31,460)
        if redcary+130 > 460:
            if redcarx+5 < myx < redcarx+69-5 or redcarx+5 < myx+62 < redcarx+69-5 or redcarx+5 < myx+31 < redcarx+69-5:
                crash(myx+31,460)

        if speed < 15:
            speed += 0.005

        pygame.display.update()
        clock.tick(60)

intro()
gameloop()
quitgame()

