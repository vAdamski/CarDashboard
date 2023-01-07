import time

import pygame
import asyncio
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


def dispalyPosition(positionInPrecent=(0, 0)) -> tuple:
    return screen.get_width() * positionInPrecent[0] / 100, screen.get_height() * positionInPrecent[1] / 100


# ======================================================================================================================
# Pygame init
debug = True
displaySizeWidth = 1920
displaySizeHeight = 1080
angle_speed = 32
angle_rpm = -5

pygame.init()
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
startStopButton = pygame.image.load('source/PNG/StartStopButton.png')
startStopButton = pygame.transform.scale(startStopButton, (300, 300))
startStopButtonRect = startStopButton.get_rect(topleft = (1550, 50))

clocksBackground = pygame.image.load('source/PNG/clocks.png')
clocksBackground = pygame.transform.scale(clocksBackground, (1920, 1080))
pointer_rpm = pygame.image.load('source/PNG/arrow.png')
pointer_rpm = pygame.transform.scale(pointer_rpm, (300, 300))

pointer_speed = pygame.image.load('source/PNG/arrow.png')
pointer_speed = pygame.transform.scale(pointer_speed, (500, 500))

gasPedal = pygame.Surface((200, 600))
gasPedal.fill('Red')
gasPedalRect = gasPedal.get_rect(topleft=(1600, 400))

breakPedal = pygame.Surface((200, 400))
breakPedal.fill('Red')
breakPedalRect = gasPedal.get_rect(topleft=(1350, 600))

# ======================================================================================================================
# Engine parameters
speedMin = 32
speedMax = -210
rpmMin = -5
rpmMax = -230
kph = 0
gear = 1
isRunning = False
isStarting = False
startingStageSpeed = 0
startingStageRpm = 0
isTurningOff = False

# Icons
iconsState = (False, False, False, False, False, False, False, False, False)
# iconsState = turnOnAllIcons()
# ======================================================================================================================

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mousePos = pygame.mouse.get_pos()

    # Draw all our elements
    # Background
    # screen.blit(bg, (0,0))

    # Wskazowka i zegar
    screen.blit(clocksBackground, (0,0))
    blitRotate(screen, pointer_rpm, (576,561), angle_speed)
    blitRotate(screen, pointer_speed, (997, 558), angle_rpm)

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

    screen.blit(gasPedal, gasPedalRect)
    screen.blit(breakPedal, breakPedalRect)

    screen.blit(startStopButton, startStopButtonRect)

    # Logika aplikacji
    # Engine start/stop
    if isRunning:
        if not isTurningOff:
            # Tu kod dla działającego silnika

            if gasPedalRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0]:
                # Zwerownaie rpm jesli pedal nie jest nacisniety
                angle_rpm -= 10
                if angle_rpm < rpmMax:
                    angle_rpm = rpmMax
            elif angle_rpm < -25:
                angle_rpm += 2

            # Dalszy kod działajacego silnika


            # Turning off procedure
            # Przycisk stop start -> Tutaj jest wyłaczanie auta -> trzeba dodac zerownaie kph
            if startStopButtonRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0] and not isTurningOff:
                isTurningOff = True
                time.sleep(0.2)
        else:
            # Wyłaczanie auta
            if angle_speed <= 120:
                angle_speed += 10
                if angle_speed >= speedMin:
                    angle_speed = speedMin
                    isRunning = False
                    isTurningOff = False
                    iconsState = turnOffAllIcons()

    else:
        if startStopButtonRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0] and not isStarting:
            isStarting = True
        # Starting procedure
        # TODO: Take it to another function
        if isStarting:
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



    # update everything
    if debug:
        print(f'isRunning = {isRunning}')
        print(f'isStarting = {isStarting}')
        print(f'angleSpeed = {angle_speed}')
        print(f'angle_rpm = {angle_rpm}')

    pygame.display.update()
    clock.tick(60)
