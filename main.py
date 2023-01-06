import pygame
from sys import exit


# ======================================================================================================================
# Additional functions
def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
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


# ======================================================================================================================
# Pygame init

displaySizeWidth = 1920
displaySizeHeight = 1080
angle = 120

pygame.init()
screen = pygame.display.set_mode((displaySizeWidth, displaySizeHeight))
pygame.display.set_caption('CarDashboard')
clock = pygame.time.Clock()

# ======================================================================================================================
# UI Init
clocksBackground = pygame.image.load('source/PNG/CloockBackground.png')
wskazowka = pygame.image.load('source/PNG/wskazowka.png')
wskazowka = pygame.transform.scale(wskazowka, (900,900))

pedal = pygame.Surface((200, 600))
pedal.fill('Red')
pedalRect = pedal.get_rect(topleft=(1600, 100))

# ======================================================================================================================
# Engine parameters

# ======================================================================================================================

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mousePos = pygame.mouse.get_pos()

    pos = (screen.get_width() / 2, screen.get_height() / 2)
    w, h = wskazowka.get_size()

    # draw all our elements
    w, h = clocksBackground.get_size()
    blitRotate(screen, clocksBackground, pos, (w / 2, h / 2), 0)
    w, h = wskazowka.get_size()
    blitRotate(screen, wskazowka, pos, (w / 2, h / 2), angle)

    screen.blit(pedal,pedalRect)
    if pedalRect.collidepoint(mousePos) and pygame.mouse.get_pressed(3)[0]:
        angle -= 1
    elif angle < 90:
        angle += 1
    # update everything
    pygame.display.update()
    clock.tick(60)
