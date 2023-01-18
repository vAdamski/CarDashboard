import random
import pygame
import time
from sys import exit


# ======================================================================================================================
# Additional functions
def turnOnAllIcons():
    return (True, True, True, True, True, True, True, True, True)
def turnOffAllIcons():
    return (False, False, False, False, False, False, False, False, False)

def blitRotate(surf, image, pos, angle=0):
    w, h = image.get_size()

    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - w/2, pos[1] - h/2))
    #fix image_rect center of image

    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
    # pygame.draw.rect(surf, (255, 0, 0), (rotated_image_rect.topleft, rotated_image.get_size()), 2)

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def dispalyPosition(positionInPrecent=(0, 0)) -> tuple:
    return screen.get_width() * positionInPrecent[0] / 100, screen.get_height() * positionInPrecent[1] / 100

def drawError(iconsState: tuple) -> tuple:
    tupelAsList = list(iconsState)
    rand = bool(random.getrandbits(1))
    x = len(tupelAsList)
    value = random.randint(0, x-1)
    tupelAsList[value] = rand
    return  tuple(tupelAsList)


# ======================================================================================================================
# Pygame init
debug = False
displaySizeWidth = 1920
displaySizeHeight = 1080
angle_speed = 32
angle_rpm = -5

pygame.mixer.init()
screen = pygame.display.set_mode((displaySizeWidth, displaySizeHeight))
pygame.display.set_caption('CarDashboard')

clock = pygame.time.Clock()

# ======================================================================================================================
# UI Init
# bg = pygame.image.load('source/bg.jpg')

abs = pygame.image.load('source/PNG/ABS.png')
abs = pygame.transform.scale(abs, (40, 40))
checkEngine = pygame.image.load('source/PNG/Check_engine.png')
checkEngine = pygame.transform.scale(checkEngine, (40, 40))
esp = pygame.image.load('source/PNG/Esp.png')
lights = pygame.image.load('source/PNG/Lights.png')
lights = pygame.transform.scale(lights, (40, 40))
oil = pygame.image.load('source/PNG/Oil.png')
oil = pygame.transform.scale(oil, (40, 40))
reserve = pygame.image.load('source/PNG/Reserve.png')
reserve = pygame.transform.scale(reserve, (40, 40))
temp = pygame.image.load('source/PNG/Temp.png')
temp = pygame.transform.scale(temp, (40, 40))
traction = pygame.image.load('source/PNG/Traction.png')
traction = pygame.transform.scale(traction, (40, 40))
warning = pygame.image.load('source/PNG/Warning.png')
warning = pygame.transform.scale(warning, (40, 40))
kierunkowskaz_prawy = pygame.image.load('source/PNG/kierunek.png')
kierunkowskaz_prawy = pygame.transform.scale(kierunkowskaz_prawy, (200, 200))
kierunkowskaz_lewy = pygame.image.load('source/PNG/kierunek.png')
kierunkowskaz_lewy = pygame.transform.scale(kierunkowskaz_lewy, (200, 200))
startStopButton = pygame.image.load('source/PNG/StartStopButton.png')
startStopButton = pygame.transform.scale(startStopButton, (300, 300))
startStopButtonRect = startStopButton.get_rect(topleft = (1550, 50))

clocksBackground = pygame.image.load('source/PNG/clocks.png')
clocksBackground = pygame.transform.scale(clocksBackground, (1920, 1080))
pointer_rpm = pygame.image.load('source/PNG/arrow.png')
pointer_rpm = pygame.transform.scale(pointer_rpm, (500, 500))

pointer_speed = pygame.image.load('source/PNG/arrow.png')
pointer_speed = pygame.transform.scale(pointer_speed, (300, 300))

gasPedal = pygame.image.load('source/PNG/accelerator.png')
gasPedal = pygame.transform.scale(gasPedal, (200, 600))
gasPedalRect = gasPedal.get_rect(topleft=(1700, 400))

# Ikonki paliwa
paliwo1 = pygame.image.load('source/PNG/line1_1.png')
paliwo1 = pygame.transform.scale(paliwo1, (30, 40))
paliwo2 = pygame.image.load('source/PNG/line1_2.png')
paliwo2 = pygame.transform.scale(paliwo2, (30, 40))
paliwo3 = pygame.image.load('source/PNG/line1_2.png')
paliwo3 = pygame.transform.scale(paliwo3, (30, 40))
paliwo4 = pygame.image.load('source/PNG/line1_2.png')
paliwo4 = pygame.transform.scale(paliwo4, (30, 40))
paliwo5 = pygame.image.load('source/PNG/line1_2.png')
paliwo5 = pygame.transform.scale(paliwo5, (30, 40))
paliwo6 = pygame.image.load('source/PNG/line1_3.png')
paliwo6 = pygame.transform.scale(paliwo6, (30, 40))




# Sound init
kierunek_sound = pygame.mixer.Sound("source/SOUND/kierunek_sound.mp3")
klakson = pygame.mixer.Sound("source/SOUND/Cutlass80HornMediu PE867510_preview.mp3")
startSilnika = pygame.mixer.Sound("source/SOUND/StartSilnika.mp3")
stopSilnika = pygame.mixer.Sound("source/SOUND/StopSilnika.mp3")
pracaSilnika = pygame.mixer.Sound("source/SOUND/PracaSilnika.mp3")

# ======================================================================================================================
# Engine parameters
speedMin = 32
speedMax = -210
rpmMin = -5
rpmMax = -230
fuelLvl = 6
counter = 0
counterFuel = 150
isRunning = False
isRunningSoundFlag = False
isStarting = False
isStartingSoundFlag = False
startingStageSpeed = 0
startingStageRpm = 0
isTurningOff = False
isTurningOffSoundFlag = False
kierunek_prawy = False
kierunek_prawy_pokaz = False
kierunek_lewy = False
kierunek_lewy_pokaz = False
kirunkowskaz_iterator = 0
kirunkowskaz_iterator_max = 15
kierunek_sound_flag = False

# Icons
iconsState = (False, False, False, False, False, False, False, False, False)
# iconsState = turnOnAllIcons()
# ======================================================================================================================

# make a second window using pyglet library


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Obsluga klawiatury
        if event.type == pygame.KEYDOWN:
            # Kierunkowskazy
            # Lewy
            if event.key == pygame.K_LEFT:
                if debug == True:
                    print("Key K_LEFT has been pressed")
                kierunek_lewy = not kierunek_lewy
                if kierunek_prawy:
                    kierunek_prawy = not kierunek_prawy

            # Prawy
            if event.key == pygame.K_RIGHT:
                if debug == True:
                    print("Key K_RIGHT has been pressed")
                kierunek_prawy = not kierunek_prawy
                if kierunek_lewy:
                    kierunek_lewy = not kierunek_lewy

            # Klakson
            if event.key == pygame.K_SPACE:
                klakson.play()

            # Losowanie bledow
            if event.key == pygame.K_RETURN and isRunning:
                iconsState = drawError(iconsState)

    mousePos = pygame.mouse.get_pos()

    # Draw all our elements

    # Wskazowka i zegar
    screen.blit(clocksBackground, (0,0))
    blitRotate(screen, pointer_speed, (581,565), angle_speed)
    blitRotate(screen, pointer_rpm, (980, 558), angle_rpm)

    # Ikonki
    if iconsState[0]:
        screen.blit(abs, (1254, 371))
    if iconsState[1]:
        screen.blit(checkEngine, (1302, 353))
    # if iconsState[2]:
        # screen.blit(esp, (1025,200))
    if iconsState[3]:
        screen.blit(lights, (1450, 371))
    if iconsState[4]:
        screen.blit(oil, (1302, 393))
    if iconsState[5]:
        screen.blit(reserve, (1402, 356))
    if iconsState[6]:
        screen.blit(temp, (1402, 390))
    if iconsState[7]:
        screen.blit(traction,  (1350, 371))
    # if iconsState[8]:
    #     screen.blit(warning, (990,800))
    if kierunek_prawy_pokaz and kierunek_prawy:
        blitRotate(screen, kierunkowskaz_prawy, (1200, 310), 180)
    if kierunek_lewy_pokaz and kierunek_lewy:
        blitRotate(screen, kierunkowskaz_lewy, (740, 310), 0)

    # Paliwo wykres
    if fuelLvl == 0:
        pass
    if fuelLvl == 1:
        screen.blit(paliwo1, (570, 790))
    if fuelLvl == 2:
        screen.blit(paliwo1, (570, 790))
        screen.blit(paliwo2, (598, 791))
    if fuelLvl == 3:
        screen.blit(paliwo1, (570, 790))
        screen.blit(paliwo2, (598, 791))
        screen.blit(paliwo3, (626, 791))
    if fuelLvl == 4:
        screen.blit(paliwo1, (570, 790))
        screen.blit(paliwo2, (598, 791))
        screen.blit(paliwo3, (626, 791))
        screen.blit(paliwo4, (654, 791))
    if fuelLvl == 5:
        screen.blit(paliwo1, (570, 790))
        screen.blit(paliwo2, (598, 791))
        screen.blit(paliwo3, (626, 791))
        screen.blit(paliwo4, (654, 791))
        screen.blit(paliwo5, (682, 791))
    if fuelLvl == 6:
        screen.blit(paliwo1, (570, 790))
        screen.blit(paliwo2, (598, 791))
        screen.blit(paliwo3, (626, 791))
        screen.blit(paliwo4, (654, 791))
        screen.blit(paliwo5, (682, 791))
        screen.blit(paliwo6, (710, 791))

    screen.blit(gasPedal, gasPedalRect)

    screen.blit(startStopButton, startStopButtonRect)

    # Logika aplikacji
    # Engine start/stop
    if isRunning:
        isStartingSoundFlag = False
        if not isTurningOff:
            # Tu kod dla działającego silnika
            if gasPedalRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0]:
                # Zwerownaie rpm jesli pedal nie jest nacisniety
                angle_rpm -= 10
                angle_speed -= 10
                if angle_rpm < rpmMax:
                    angle_rpm = rpmMax
                if angle_speed < speedMax:
                    angle_speed = speedMax

            if angle_rpm < -25:
                angle_rpm += 2
            if angle_speed <= speedMin:
                angle_speed += 1

            # Dalszy kod działajacego silnika

            # Dzwiek dzialajacego silnika
            if isRunningSoundFlag == False:
                pracaSilnika.play(loops=-1)
                isRunningSoundFlag = True

            # Obnizenie poziomu paliwa o 1 co x tickow
            counter += 1
            if counter == counterFuel:
                fuelLvl -= 1
                counter = 0


            # Obsluga kierukowskazow
            kirunkowskaz_iterator += 1
            if kirunkowskaz_iterator == kirunkowskaz_iterator_max:
                kierunek_lewy_pokaz = not kierunek_lewy_pokaz
                kierunek_prawy_pokaz = not kierunek_prawy_pokaz
                kirunkowskaz_iterator = 0

            if not kierunek_lewy and not kierunek_prawy:
                kierunek_sound_flag = False
                kierunek_sound.stop()
            if (kierunek_prawy or kierunek_lewy) and not kierunek_sound_flag:
                kierunek_sound.play(loops=-1)
                kierunek_sound_flag = True


            # Turning off procedure
            # Przycisk stop start -> Tutaj jest wyłaczanie auta
            if ((startStopButtonRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0]) and not isTurningOff) or (fuelLvl == 0 and not isTurningOff):
                isTurningOff = True
                time.sleep(0.2)
        else:
            # Wyłaczanie auta
            if angle_speed <= 120:
                angle_speed += 10
                if angle_speed >= speedMin:
                    angle_speed = speedMin

            angle_rpm = rpmMin
            angle_speed = speedMin
            isRunning = False
            isRunningSoundFlag = False
            pracaSilnika.stop()
            isTurningOff = False
            iconsState = turnOffAllIcons()
            if isTurningOffSoundFlag == False:
                stopSilnika.play()
                isTurningOffSoundFlag = True

    else:
        isTurningOffSoundFlag = False
        if startStopButtonRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0] and not isStarting:
            isStarting = True
        # Starting procedure
        if isStarting:
            if isStartingSoundFlag == False:
                startSilnika.play()
                isStartingSoundFlag = True

            # Odpal wszystkie ikonki
            iconsState = turnOnAllIcons()
            # Tutaj mamy zwiększanie wskazowek kph do max poziomu
            if angle_speed >= speedMax and startingStageSpeed == 0:
                angle_speed -= 9.68
                if angle_speed <= speedMax:
                    startingStageSpeed = 1

            # Gdy osiagnie max poziom zmniejsz je do poziomu 0kph
            elif angle_speed <= 32 and startingStageSpeed == 1:
                angle_speed += 9.68
                if angle_speed >= 32:
                    startingStageSpeed = 2

            # Tutaj mamy zwiększanie wskazowek rpm do max poziomu
            if angle_rpm >= rpmMax and startingStageRpm == 0:
                angle_rpm -= 9.4
                if angle_rpm <= rpmMax:
                    startingStageRpm = 1

            # Gdy osiagnie max poziom zmniejsz je do poziomu 1000rpm
            elif angle_rpm <= -25 and startingStageRpm == 1:
                angle_rpm += 9.4
                if angle_rpm >= -25:
                    startingStageRpm = 2

            # Jesli oba zegary sprawdzily sie uruchom silnik i i wylacz procedure startu
            if startingStageSpeed == 2 and startingStageRpm == 2 and isStarting and not isRunning:
                startingStageRpm = 0
                startingStageSpeed = 0
                # wyłacz prodedure startu i wlacz silnik
                isStarting = False
                isRunning = True
                # wylacz ikonki
                iconsState = turnOffAllIcons()
                # Zresetuj flage dziwieku staru silnika
                isTurningOffSoundFlag = False

    # update everything
    if debug:
        print(f'isRunning = {isRunning}')
        print(f'isStarting = {isStarting}')
        print(f'angleSpeed = {angle_speed}')
        print(f'angle_rpm = {angle_rpm}')

    pygame.display.update()
    clock.tick(60)
