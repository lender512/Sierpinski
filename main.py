import sys, pygame, random
pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

size = width, height = 900, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

screen.fill(black)

mouse_pressed = False
base_point = False
start = False

origin_dots = []
new_dots = []
radius = 1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        start = True

    if not start and not base_point:
        if pygame.mouse.get_pressed(3) == (1, 0, 0) and not mouse_pressed:
            mouse_pos = pygame.mouse.get_pos()
            origin_dots.append(mouse_pos)
            point = pygame.draw.circle(screen, pygame.Color(255, 0, 0), mouse_pos, radius)
            mouse_pressed = True

        if pygame.mouse.get_pressed(3) == (0, 0, 0):
            mouse_pressed = False

    elif start and not base_point:
            if pygame.mouse.get_pressed(3) == (1, 0, 0):
                mouse_pos = pygame.mouse.get_pos()
                new_dots.append(mouse_pos)
                point = pygame.draw.circle(screen, pygame.Color(0, 255, 0), mouse_pos, radius)
                base_point = True

    elif start and base_point:
        base_dot1 = origin_dots[random.randint(0, len(origin_dots)-1)]
        base_dot2 = new_dots[random.randint(0, len(new_dots)-1)]

        new_dot_x = (base_dot2[0] + base_dot1[0]) / 2
        new_dot_y = (base_dot2[1] + base_dot1[1]) / 2

        pygame.draw.circle(screen, pygame.Color(255, 0, 0), (new_dot_x, new_dot_y), radius)
        new_dots.append((new_dot_x, new_dot_y))

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            start = False

    pygame.display.flip()
    fpsClock.tick(FPS)
