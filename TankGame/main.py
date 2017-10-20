import pygame
import time
import random
pygame.init()

fireSound = pygame.mixer.Sound('sounds/boom.wav')
#explosionSound = pygame.mixer.Sound('sounds/explosion.mp3')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-2)

display_height = 600
display_width = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Tanks')

icon = pygame.image.load('images/tank_icon.png')
pygame.display.set_icon(icon,)

white = (255,255,255)
white_smoke = (245,245,245)
light_cyan = (224,255,255)
alice_blue = (240,248,255)
floral_white = (255,250,240)
black = (0,0,0)
red = (220,20,60)
dark_red =	(139,0,0)
light_green = (144,238,144)
yellow = (255,255,0)
dark_yellow = (255,215,0)
green = (50,205,50)
dark_green = (0,100,0)
blue = (70,130,180)
light_blue = (173,216,230)

silver = (192,192,192)



# img_head = pygame.image.load('images/snakehead_small_up.png')
# img_body = pygame.image.load('images/snakebody_small.png')
# img_apple = pygame.image.load('images/apple_small.png')
# img_mouse = pygame.image.load('images/mouse_small.png')
# img_victory = pygame.image.load('images/snake_med.png')
# img_speedup = pygame.image.load('images/speedup.png')
# img_slowdown = pygame.image.load('images/slowdown.png')

clock = pygame.time.Clock()

tankWidth = 70
tankHeight = 50

turretWidth = 5
wheelWidth = 5

ground_height = 37

FPS = 15

fontSize = 30

xsmallfont = pygame.font.SysFont(None, 15)
smallfont = pygame.font.SysFont(None, 25)
medfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 80)


# def victory():
#
#     victory = True
#
#     while victory:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_c:
#                     victory = False
#                     gameLoop()
#                 elif event.key == pygame.K_q:
#                     pygame.quit()
#                     quit()
#
#         gameDisplay.fill(white)
#         message_to_screen("Congratulations! You win!", blue, -250, 'medium')
#         gameDisplay.blit(img_victory, [275, 100])
#         message_to_screen("Press 'C' to start a new game or 'Q' to quit.", black, 215, 'small')
#
#         pygame.display.update()
#         clock.tick(5)
def score(score):
    text = smallfont.render("Score: " + str(score),True, black)
    gameDisplay.blit(text,[10,10])

def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    elif size == 'xsmall':
        textSurface = xsmallfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = 'small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (buttonx + (buttonwidth/2), buttony + (buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg,color, y_displace=0, size = 'small'):
    textSurf, textRect = text_objects(msg, color, size)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text,[display_width/2 - msglen, display_height/2])
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def tank(x,y,turPos = 0):

    tur0 = pygame.image.load('images/tank_turret_0.png')
    tur1 = pygame.image.load('images/tank_turret_1.png')
    tur2 = pygame.image.load('images/tank_turret_2.png')
    tur3 = pygame.image.load('images/tank_turret_3.png')
    tur4 = pygame.image.load('images/tank_turret_4.png')
    tur5 = pygame.image.load('images/tank_turret_5.png')
    tur6 = pygame.image.load('images/tank_turret_6.png')
    tur7 = pygame.image.load('images/tank_turret_7.png')

    possibleTurrets = [tur0,tur1,tur2,tur3,tur4,tur5,tur6,tur7]

    gameDisplay.blit(possibleTurrets[turPos], [x-18, y-25])
    mainTank = pygame.image.load('images/tank_small.png')
    gameDisplay.blit(mainTank, [x,y])

    turretPoints = [(x - 27 ,y - 2),
                       (x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 15, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)]

    return turretPoints[turPos]

def enemyTank(x,y,enemyTurPos = 0):

    tur0 = pygame.image.load('images/enemy_tank_turret_0.png')
    tur1 = pygame.image.load('images/enemy_tank_turret_1.png')
    tur2 = pygame.image.load('images/enemy_tank_turret_2.png')
    tur3 = pygame.image.load('images/enemy_tank_turret_3.png')
    tur4 = pygame.image.load('images/enemy_tank_turret_4.png')
    tur5 = pygame.image.load('images/enemy_tank_turret_5.png')
    tur6 = pygame.image.load('images/enemy_tank_turret_6.png')
    tur7 = pygame.image.load('images/enemy_tank_turret_7.png')

    possibleEnemyTurrets = [tur0,tur1,tur2,tur3,tur4,tur5,tur6,tur7]

    gameDisplay.blit(possibleEnemyTurrets[enemyTurPos], [x-20, y-25])
    enemyTank = pygame.image.load('images/enemy_tank_small.png')
    gameDisplay.blit(enemyTank, [x,y])

    turretPoints = [(x - 27 ,y - 2),
                       (x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 15, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)]

    return turretPoints[enemyTurPos]

# def tank(x,y,turPos):
#     x = int(x)
#     y = int(y)
#
#     possibleTurrets = [(x - 27 ,y - 2),
#                        (x - 27, y - 2),
#                        (x - 26, y - 5),
#                        (x - 25, y - 8),
#                        (x - 23, y - 12),
#                        (x - 20, y - 14),
#                        (x - 18, y - 15),
#                        (x - 15, y - 17),
#                        (x - 13, y - 19),
#                        (x - 11, y - 21)]
#
#     pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))
#     pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))
#
#     pygame.draw.line(gameDisplay, black, (x, y), possibleTurrets[turPos],turretWidth)
#
#     pygame.draw.circle(gameDisplay, black, (x - 15, y + 20), wheelWidth)
#     pygame.draw.circle(gameDisplay, black, (x - 10, y + 20), wheelWidth)
#     pygame.draw.circle(gameDisplay, black, (x - 5, y + 20), wheelWidth)
#     pygame.draw.circle(gameDisplay, black, (x, y + 20), wheelWidth)
#     pygame.draw.circle(gameDisplay, black, (x + 5, y + 20), wheelWidth)
#     pygame.draw.circle(gameDisplay, black, (x + 10, y + 20), wheelWidth)
#     pygame.draw.circle(gameDisplay, black, (x + 15, y + 20), wheelWidth)
    # startX = 20
    #
    # for x in range(8):
    #     pygame.draw.circle(gameDisplay,black,(x-startX,y+20),wheelWidth)
    #     startX -=5
    #

def controls():
    gcont = True

    while gcont:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls", blue, -100, 'large')
        message_to_screen("Fire: Spacebar", black, -30, 'small')
        message_to_screen("Move Turret: Up/Down arrows", black, 10, 'small')
        message_to_screen("Move Tank: Left/Right arrows", black, 50, 'small')
        # message_to_screen("Press 'C' to play or 'Q' to quit.", black, 180, 'small')
        message_to_screen("Press: 'P' to pause.", black, 90, 'small')
        message_to_screen("© 2017 Mark Wesolowski", black, 280, 'xsmall')

        button('Play', 150, 500, 100, 50, light_green, green, action='play')
        button('Main Menu', 350, 500, 100, 50, yellow, dark_yellow, action='menu')
        button('Quit', 550, 500, 100, 50, red, dark_red, action='quit')

        pygame.display.update()
        clock.tick(15)


def button(text,x,y,width, height, inactive_color, active_color,text_color = black, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            elif action == 'controls':
                controls()
            elif action == 'play':
                gameLoop()
            elif action == 'menu':
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text,black,x,y,width,height)


def pause():

    paused = True

    message_to_screen("Paused", black, -100, 'large')
    message_to_screen("Press 'C' to continue, 'R' to restart, or 'Q' to quit.", black, 25, 'small')
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c or event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    gameLoop()
        # gameDisplay.fill(silver)


        clock.tick(100)

def barrier(xlocation, randomHeight, randomWidth):
    pygame.draw.rect(gameDisplay,blue,[xlocation,display_height-randomHeight,randomWidth,randomHeight])


def clouds(x,y, size = 50):

        startPoint = x,y

        colorChoices = [white, white_smoke, light_cyan, alice_blue, floral_white]

        for i in range(1, 16):
            size = random.randint(20, 70)
            xOffset = random.randint(-40, 40)
            yOffset = random.randint(-30, 30)

            pygame.draw.circle(gameDisplay,colorChoices[random.randrange(0,4)],(x+ xOffset, y+ yOffset),random.randrange(20,70))

            pygame.display.update()
            clock.tick(100)


def explosion(x,y, size = 50):

    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

        startPoint = x,y

        colorChoices = [red, dark_red, yellow, dark_yellow]

        magnitude = 1

        while magnitude < size:
            exploding_bit_x = int(x + random.randrange(-1 * magnitude, magnitude))
            exploding_bit_y = int(y + random.randrange(-1 * magnitude, magnitude))

            pygame.draw.circle(gameDisplay,colorChoices[random.randrange(0,4)], (exploding_bit_x, exploding_bit_y),random.randrange(1,5))
            magnitude +=1

            pygame.display.update()
            clock.tick(100)

        explode = False

def fireShell(xy,tankx,tanky,turPos, gun_power, xlocation, randomWidth, randomHeight, enemyTankX, enemyTankY):
    pygame.mixer.Sound.play(fireSound)
    damage = 0
    fire = True

    startingShell = list(xy)

    # print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

        # print(startingShell[0], startingShell[1])
        startingShell[0] = int(startingShell[0])
        startingShell[1] = int(startingShell[1])

        # print((startingShell[0]+16, startingShell[1]+6))

        pygame.draw.circle(gameDisplay, dark_red, (startingShell[0] + 16, startingShell[1] + 6), 5)
        startingShell[0] -= (12 - turPos)*2
        startingShell[1] += int((((startingShell[0] + 16-xy[0]) * 0.015/(gun_power/50)) **2) - (turPos+turPos/(12-turPos)))

        if startingShell[1]  > display_height - ground_height:
            hit_x = int((startingShell[0] + 16) * display_height) / (startingShell[1] + 6)
            hit_y = int(display_height - ground_height)
            if enemyTankX +15 > hit_x > enemyTankX -15:
                print("Hit Target")
                damage = 25
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = (startingShell[0] + 16) <= xlocation + randomWidth
        check_x_2 = (startingShell[0] + 16) >= xlocation

        check_y_1 = (startingShell[1] + 6) <= display_height
        check_y_2 = (startingShell[1] + 6) >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int(((startingShell[0] + 16)))
            hit_y = int((startingShell[1] + 6))
            explosion(hit_x,hit_y)
            fire = False

        pygame.display.update()
        clock.tick(120)
    return damage

def enemyFireShell(xy,tankx,tanky,enemyTurPos, gun_power, xlocation, randomWidth, randomHeight, ptankX, ptankY):
    pygame.mixer.Sound.play(fireSound)
    damage = 0

    currentPower = 1
    power_found = False

    while not power_found:
        currentPower +=1

        if currentPower > 100:
            power_found = True
            print(currentPower)

#****Begin AI Calculation
            fire = True

            startingShell = list(xy)

            # print("FIRE!",xy)

            while fire:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pause()

                startingShell[0] = int(startingShell[0])
                startingShell[1] = int(startingShell[1])

                # pygame.draw.circle(gameDisplay, dark_red, (startingShell[0] + 75, startingShell[1] + 6), 5)
                startingShell[0] += (12 - enemyTurPos) * 2
                startingShell[1] += int((((startingShell[0] + 75 - xy[0]) * 0.015 / (currentPower / 50)) ** 2) - (

                enemyTurPos + enemyTurPos / (12 - enemyTurPos)))

                if startingShell[1] > display_height - ground_height:
                    hit_x = int((startingShell[0] + 75) * display_height) / (startingShell[1] + 6)
                    hit_y = int(display_height - ground_height)
                    # explosion(hit_x, hit_y)
                    if ptankX + 15 > hit_x > ptankX -15:
                        print('Target Acquired')
                        power_found = True


                    fire = False

                check_x_1 = (startingShell[0] + 75) <= xlocation + randomWidth
                check_x_2 = (startingShell[0] + 75) >= xlocation

                check_y_1 = (startingShell[1] + 6) <= display_height
                check_y_2 = (startingShell[1] + 6) >= display_height - randomHeight

                if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                    hit_x = int(((startingShell[0] + 75)))
                    hit_y = int((startingShell[1] + 6))
                    explosion(hit_x, hit_y)
                    fire = False
#****End AI Calculation



    fire = True

    startingShell = list(xy)

    # print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

        # print(startingShell[0], startingShell[1])


        startingShell[0] = int(startingShell[0])
        startingShell[1] = int(startingShell[1])



        # print((startingShell[0]+16, startingShell[1]+6))

        pygame.draw.circle(gameDisplay, dark_red, (startingShell[0]+75, startingShell[1] + 6), 5)
        startingShell[0] += (12 - enemyTurPos) * 2

        gun_power = random.randrange(int(currentPower*0.90), int(currentPower*1.10))

        startingShell[1] += int((((startingShell[0]+75-xy[0]) * 0.015/(gun_power/50)) **2) - (enemyTurPos+enemyTurPos/(12-enemyTurPos)))


        if startingShell[1]  > display_height - ground_height:
            hit_x = int((startingShell[0]+75) * display_height) / (startingShell[1] + 6)
            hit_y = int(display_height - ground_height)
            if ptankX +15 > hit_x > ptankX -15:
                print("Hit Target")
                damage = 25
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = (startingShell[0]+75) <= xlocation + randomWidth
        check_x_2 = (startingShell[0]+75) >= xlocation

        check_y_1 = (startingShell[1] + 6) <= display_height
        check_y_2 = (startingShell[1] + 6) >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int(((startingShell[0]+75)))
            hit_y = int((startingShell[1] + 6))
            explosion(hit_x,hit_y)
            fire = False

        pygame.display.update()
        clock.tick(120)

    return damage

def power(player_level,cpu_level):
    text = smallfont.render("Player Power: " + str(player_level) + "%", True, black )
    gameDisplay.blit(text,[display_width * 0.65, 10])

    text = smallfont.render("CPU Power: " + str(cpu_level) + "%", True, black )
    gameDisplay.blit(text,[display_width * 0.1, 10])




def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                # pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    gameLoop()

        gameDisplay.fill(alice_blue)
        message_to_screen("Welcome to Tanks!", blue, -100, 'large')
        message_to_screen("The objective is to shoot and destroy", black, -30, 'small')
        message_to_screen("the enemy tank, before they destroy you.", black, 10, 'small')
        message_to_screen("The more enemies you destroy, the harder they get.", black, 50, 'small')
        # message_to_screen("Press 'C' to play or 'Q' to quit.", black, 180, 'small')
        # message_to_screen("Press 'P' or hit the Spacebar to pause.", black, 220, 'small')
        message_to_screen("© 2017 Mark Wesolowski", black, 280, 'xsmall')


        button('Play', 150, 500, 100, 50, light_green, green, action = 'play')
        button('Controls', 350, 500, 100, 50, yellow, dark_yellow, action = 'controls')
        button('Quit',550, 500, 100, 50, red, dark_red, action = 'quit')

        pygame.display.update()
        clock.tick(15)

def game_over():

    game_over = True

    while game_over:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()


        gameDisplay.fill(alice_blue)
        message_to_screen("Game Over!", dark_red, -100, 'large')
        message_to_screen("You died", black, -30, 'small')
        # message_to_screen("Press 'C' to play or 'Q' to quit.", black, 180, 'small')
        # message_to_screen("Press 'P' or hit the Spacebar to pause.", black, 220, 'small')
        message_to_screen("© 2017 Mark Wesolowski", black, 280, 'xsmall')


        button('Replay', 150, 500, 100, 50, light_green, green, action = 'play')
        button('Controls', 350, 500, 100, 50, yellow, dark_yellow, action = 'controls')
        button('Quit',550, 500, 100, 50, red, dark_red, action = 'quit')

        pygame.display.update()
        clock.tick(15)



def you_win():

    you_win = True

    while you_win:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()


        gameDisplay.fill(alice_blue)
        message_to_screen("You won!", blue, -100, 'large')
        message_to_screen("Congratulations!", black, -30, 'small')
        # message_to_screen("Press 'C' to play or 'Q' to quit.", black, 180, 'small')
        # message_to_screen("Press 'P' or hit the Spacebar to pause.", black, 220, 'small')
        message_to_screen("© 2017 Mark Wesolowski", black, 280, 'xsmall')


        button('Replay', 150, 500, 100, 50, light_green, green, action = 'play')
        button('Controls', 350, 500, 100, 50, yellow, dark_yellow, action = 'controls')
        button('Quit',550, 500, 100, 50, red, dark_red, action = 'quit')

        pygame.display.update()
        clock.tick(15)

def health_bars(player_health,enemy_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color,(display_width * 0.65, 30, player_health,25))
    pygame.draw.rect(gameDisplay, enemy_health_color,(display_width * 0.1, 30, enemy_health,25))

def gameLoop():

    gameExit = False
    gameOver = False
    FPS = 15

    player_health = 100
    enemy_health = 100

    player_health_change = 0
    enemy_health_change = 0

    mainTankX = int(display_width * 0.9)
    mainTankY = int(display_height * 0.9)

    enemyTankX = int(display_width * 0.1)
    enemyTankY = int(display_height * 0.9)

    tankMove = 0
    enemyTankMove = 0

    minTur = 0
    maxTur = 7

    currentTurPos = 0
    enemyTurPos = 7

    changeTur = 0
    changeEnemyTur = 0

    fire_power = 50
    enemy_fire_power = 50

    power_change = 0
    enemy_power_change = 0

    xlocation =(display_width/2)+ random.randint(-0.1*display_width,0.1*display_width)
    randomHeight = random.randrange(display_height*0.1, display_height*0.4)
    randomWidth = 50


    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over", red, -50, size='large')
            message_to_screen("Press 'C' to Continue, or 'Q' to Quit", blue, 50, size='medium')
            pygame.display.update()

        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    changeTur = 1
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1
                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, randomWidth, randomHeight, enemyTankX, enemyTankY)
                    enemy_health -= 0

                    possibleMovement = ['f','r']
                    moveIndex = random.randrange(0,2)

                    for x in range(random.randrange(0,10)):

                        if display_width * 0.3 > enemyTankX > display_width * 0.03:
                            if possibleMovement[moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == "r":
                                enemyTankX -= 5


                            gameDisplay.fill(alice_blue)
                            health_bars(player_health, enemy_health)

                            gun = tank(mainTankX, mainTankY, currentTurPos)
                            enemyGun = enemyTank(enemyTankX, enemyTankY, enemyTurPos)

                            fire_power += power_change
                            enemy_fire_power += enemy_power_change

                            power(fire_power, enemy_fire_power)

                            barrier(xlocation, randomHeight, randomWidth)
                            gameDisplay.fill(dark_green,
                                             rect=[0, display_height - ground_height, display_width, ground_height])
                            pygame.display.update()

                            clock.tick(FPS)

                    damage = enemyFireShell(enemyGun, enemyTankX, enemyTankY, enemyTurPos, enemy_fire_power, xlocation, randomWidth, randomHeight, mainTankX, mainTankY)
                    player_health -= damage
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_w:
                    enemy_power_change = 1
                elif event.key == pygame.K_s:
                    enemy_power_change = -1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    tankMove = 0
                elif event.key == pygame.K_RIGHT:
                    tankMove = 0
                elif event.key == pygame.K_UP:
                    changeTur = 0
                elif event.key == pygame.K_DOWN:
                    changeTur = 0
                elif event.key == pygame.K_a:
                    power_change = 0
                elif event.key == pygame.K_d:
                    power_change = 0
                elif event.key == pygame.K_w:
                    enemy_power_change = 0
                elif event.key == pygame.K_s:
                    enemy_power_change = 0



        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > maxTur:
            currentTurPos = maxTur
        elif currentTurPos < minTur:
            currentTurPos = minTur

        if currentTurPos < 4:
            if mainTankX -15 < xlocation + randomWidth:
                mainTankX +=5
        elif currentTurPos == 4:
            if mainTankX < xlocation + randomWidth:
                mainTankX +=5
        elif currentTurPos == 5:
            if mainTankX < xlocation + randomWidth:
                mainTankX +=5
        elif currentTurPos == 6:
            if mainTankX < xlocation + randomWidth:
                mainTankX +=5
        elif currentTurPos == 7:
            if mainTankX < xlocation + randomWidth:
                mainTankX +=5




        if mainTankX >= display_width-(tankWidth/2) or mainTankX -(tankWidth /2)< 0:
            tankMove = 0

        gameDisplay.fill(alice_blue)
        health_bars(player_health,enemy_health)

        gun = tank(mainTankX, mainTankY, currentTurPos)
        enemyGun = enemyTank(enemyTankX, enemyTankY, enemyTurPos)

        fire_power += power_change

        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1

        enemy_fire_power += enemy_power_change

        power(fire_power, enemy_fire_power)

        barrier(xlocation, randomHeight, randomWidth)
        gameDisplay.fill(dark_green,rect=[0,display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        clock.tick(FPS)

        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            you_win()


    pygame.quit()
    quit()

game_intro()
gameLoop()
