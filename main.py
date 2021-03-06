import pygame
from math import pi, cos, sin, sqrt, hypot
import pygame.gfxdraw
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (171, 183, 183)

size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)


    def hex_corner(center, size_, i):
        angle_deg = 60 * i
        angle_rad = pi / 180 * angle_deg
        return center.x + size_ * cos(angle_rad), center.y + size_ * sin(angle_rad)

    hex_center = Point(300, 300)
    corner1 = hex_corner(hex_center, 50, 1)
    corner2 = hex_corner(hex_center, 50, 2)
    corner3 = hex_corner(hex_center, 50, 3)
    corner4 = hex_corner(hex_center, 50, 4)
    corner5 = hex_corner(hex_center, 50, 5)
    corner6 = hex_corner(hex_center, 50, 6)

    hex_size = hypot(hex_center.x - corner1[0], hex_center.y - corner1[1])
    hex_width = 2 * hex_size
    hex_height = sqrt(3) * hex_size
    adjust_x = hex_width * 3 / 4
    adjust_y = hex_height

    hex_center2 = Point(adjust_x + 300, adjust_y + 300)

    corner7 = hex_corner(hex_center2, 50, 1)
    corner8 = hex_corner(hex_center2, 50, 2)
    corner9 = hex_corner(hex_center2, 50, 3)
    corner10 = hex_corner(hex_center2, 50, 4)
    corner11 = hex_corner(hex_center2, 50, 5)
    corner12 = hex_corner(hex_center2, 50, 6)

    pygame.gfxdraw.filled_polygon(screen, (corner1, corner2, corner3, corner4, corner5, corner6), GREY)
    pygame.gfxdraw.filled_polygon(screen, (corner7, corner8, corner9, corner10, corner11, corner12), GREY)

    pygame.display.flip()

pygame.quit()
