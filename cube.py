import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import randrange


def faces(num_faces: str, face: str, translate: list, rotate: list, color_1="white", color_2="blue", color_3="white", color_line="black"):
    """Create the face base on color"""

    facesbuff = (
        (1, -1, -1),
        (1, 1, -1),
        (1, 1, 1),
        (1, -1, 1),  # One face stop len 4
        (-1, -1, 1),
        (-1, 1, 1),  # Two faces stop len 6
        (-1, 1, -1)
    )

    facesbordbuff = (
        (0, 1),
        (0, 3),
        (2, 3),
        (2, 1),  # One face stop len 4
        (2, 5),
        (3, 4),
        (5, 4),  # Two faces stop len 7 = 6 +1
        (5, 6),
        (6, 1)  # three faces stop len 10
    )

    insidefaces = (
        (0, 3, 2, 1),
        (2, 3, 4, 5),
        (1, 2, 5, 6)
    )

    numface = {"one": 4, "two": 7, "three": 10, "ONE": 0, "TWO": 1, "THREE": 2}
    numarea = {"one": 4, "two": 6, "three": 7}
    pair_colors = {"white": (1, 1, 1), "blue": (0, 0, 1), "red": (1, 0.2, 0.3), "orange": (1, 0.5, 0.1),
                   "green": (0, 1, 0), "yellow": (1, 1, 0), "black": (0, 0, 0)}

    glTranslated(translate[0], translate[1], translate[2])
    glRotated(rotate[0], rotate[1], rotate[2], rotate[3])

    glBegin(GL_QUADS)
    if face == "ONE":
        for vertex in insidefaces[numface.get(face)]:
            glColor3fv(pair_colors.get(color_1))
            glVertex3fv(facesbuff[vertex])
    elif face == "TWO":
        for vertex in insidefaces[numface.get("ONE")]:
            glColor3fv(pair_colors.get(color_1))
            glVertex3fv(facesbuff[vertex])
        for vertex in insidefaces[numface.get(face)]:
            glColor3fv(pair_colors.get(color_2))
            glVertex3fv(facesbuff[vertex])
    elif face == "THREE":
        for vertex in insidefaces[numface.get("ONE")]:
            glColor3fv(pair_colors.get(color_1))
            glVertex3fv(facesbuff[vertex])
        for vertex in insidefaces[numface.get("TWO")]:
            glColor3fv(pair_colors.get(color_2))
            glVertex3fv(facesbuff[vertex])
        for vertex in insidefaces[numface.get(face)]:
            glColor3fv(pair_colors.get(color_3))
            glVertex3fv(facesbuff[vertex])
    glEnd()

    glBegin(GL_LINES)
    count = 0
    for line in facesbordbuff:
        if count < numface.get(num_faces):
            for point in line:
                glColor3fv(pair_colors.get(color_line))
                glVertex3fv(facesbuff[point])
            count += 1
        else:
            break
    glEnd()

    # glTranslated(-(translate[0]), -(translate[1]), -(translate[2]))
    glRotated(-rotate[0], (rotate[1]), (rotate[2]), (rotate[3]))


def faccie_pos(num_faces: str, face: str, translate: list, rotate: list, color_1="white", color_2="blue", color_3="white", color_line="black"):
    """Adjust pos of faces on the screen"""

    faces(num_faces, face, translate, rotate, color_1, color_2, color_3, color_line)
    glTranslated(-translate[0], -translate[1], -translate[2])


def f_layer(layer: list):
    """Create the first layer"""

    faccie_pos("three", "THREE", [0, 3, 0], [90, 0, -1, 0], layer[0][0], layer[0][1], layer[0][2])

    faccie_pos("two", "TWO", [2, 3, 0], [90, 0, 0, 1], layer[1][0], layer[1][1])

    faccie_pos("three", "THREE", [4, 3, 0], [0, 0, 0, 0], layer[2][0], layer[2][1], layer[2][2])

    faccie_pos("two", "TWO", [4, 3, -2], [90, -1, 0, 0], layer[3][0], layer[3][1])

    faccie_pos("three", "THREE", [4, 3, -4], [90, -1, 0, 0], layer[4][0], layer[4][1], layer[4][2])

    faccie_pos("two", "TWO", [2, 3, -4], [180, 1, 1, 0], layer[5][0], layer[5][1])

    faccie_pos("three", "THREE", [0, 3, -4], [180, 0, -1, 0], layer[6][0], layer[6][1], layer[6][2])

    faccie_pos("two", "TWO", [0, 3, -2], [180, 0, 1, 1], layer[7][0], layer[7][1])

    faccie_pos("one", "ONE", [2, 3, -2], [180, 1, 1, 0], layer[8][0])


def s_layer(layer: list):
    """Create the second layer"""

    faccie_pos("two", "TWO", [0, 1, 0], [90, 0, -1, 0], layer[0][0], layer[0][1])

    faccie_pos("one", "ONE", [2, 1, 2], [90, 0, 1, 0], layer[1][0])

    faccie_pos("two", "TWO", [4, 1, 0], [180, 1, 0, 1], layer[2][0], layer[2][1])

    faccie_pos("one", "ONE", [4, 1, -2], [0, 0, 0, 0], layer[3][0])

    faccie_pos("two", "TWO", [4, 1, -4], [90, 0, 1, 0], layer[4][0], layer[4][1])

    faccie_pos("one", "ONE", [2, 1, -4], [90, 0, 1, 0], layer[5][0])

    faccie_pos("two", "TWO", [0, 1, -4], [180, 1, 0, -1], layer[6][0], layer[6][1])

    faccie_pos("one", "ONE", [-2, 1, -2], [0, 0, 0, 0], layer[7][0])


def t_layer(layer: list):
    """Create the third layer"""

    faccie_pos("three", "THREE", [0, -1, 0], [180, 0, 0, 1], layer[0][0], layer[0][1], layer[0][2])

    faccie_pos("two", "TWO", [2, -1, 0], [90, 0, 0, -1], layer[1][0], layer[1][1])

    faccie_pos("three", "THREE", [4, -1, 0], [90, 0, 0, -1], layer[2][0], layer[2][1], layer[2][2])

    faccie_pos("two", "TWO", [4, -1, -2], [90, 1, 0, 0], layer[3][0], layer[3][1])

    faccie_pos("three", "THREE", [4, -1, -4], [180, -100, -1, 0], layer[4][0], layer[4][1], layer[4][2])

    faccie_pos("two", "TWO", [2, -1, -4], [180, -100, 100, -1], layer[5][0], layer[5][1])

    faccie_pos("three", "THREE", [0, -1, -4], [180, -1, 1, 0], layer[6][0], layer[6][1], layer[6][2])

    faccie_pos("two", "TWO", [0, -1, -2], [180, 0, -100, 100], layer[7][0], layer[7][1])

    faccie_pos("one", "ONE", [2, -3, -2], [90, 0, -1, 100], layer[8][0])


def u_first_animation(m, cube: list):
    """U' animation"""

    if type(m) == list:
        k = 0
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        while k < 90:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            s_layer(cube[9:17])
            t_layer(cube[17:])
            # Move first layer
            glPushMatrix()
            glTranslated(2, 0, -2)
            glRotated(k, 0, 1, 0)
            glTranslated(-2, 0, 2)
            f_layer(cube[:9])
            glPopMatrix()
            drawText(50, 120, f"Shuffling cube for {m[2]}/{m[1]} cycles", m[0])
            k += 20
            pygame.display.flip()
    else:
        while m < 90:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            s_layer(cube[9:17])
            t_layer(cube[17:])
            # Move first layer
            glPushMatrix()
            glTranslated(2, 0, -2)
            glRotated(m, 0, 1, 0)
            glTranslated(-2, 0, 2)
            f_layer(cube[:9])
            glPopMatrix()
            m += 7
            pygame.display.flip()


def u_animation(m: int, cube: list):
    """U animation"""

    while m < 90:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        s_layer(cube[9:17])
        t_layer(cube[17:])
        # Move first layer
        glPushMatrix()
        glTranslated(2, 0, -2)
        glRotated(m, 0, -1, 0)
        glTranslated(-2, 0, 2)
        f_layer(cube[:9])
        glPopMatrix()
        m += 7
        pygame.display.flip()


def m_animation(m: int, cube: list):
    """M animation"""

    z_animation(m, cube)
    cube = z_move(cube)

    while m < 90:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        f_layer(cube[:9])
        t_layer(cube[17:])
        # Move first layer
        glPushMatrix()
        glTranslated(2, 0, -2)
        glRotated(m, 0, -1, 0)
        glTranslated(-2, 0, 2)
        s_layer(cube[9:17])
        glPopMatrix()
        m += 7
        pygame.display.flip()


def m_first_animation(m: int, cube: list):
    """M' animation"""

    z_animation(m, cube)
    cube = z_move(cube)

    while m < 90:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        f_layer(cube[:9])
        t_layer(cube[17:])
        # Move first layer
        glPushMatrix()
        glTranslated(2, 0, -2)
        glRotated(m, 0, 1, 0)
        glTranslated(-2, 0, 2)
        s_layer(cube[9:17])
        glPopMatrix()
        m += 7
        pygame.display.flip()


def x_first_animation(m: int, cube: list):
    """X' animation"""

    while m < 90:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Move first layer
        glPushMatrix()
        glTranslated(-2, 0, -2)
        glRotated(m, 1, 0, 0)
        glTranslated(2, 0, 2)
        f_layer(cube[:9])
        s_layer(cube[9:17])
        t_layer(cube[17:])
        glPopMatrix()
        m += 7
        pygame.display.flip()


def z_animation(m, cube: list):
    """Z animation"""

    if type(m) == list:
        k = 0
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        while k < 90:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            # Move first layer
            glPushMatrix()
            glTranslated(2, 0, 2)
            glRotated(k, 0, 0, -1)
            glTranslated(-2, 0, -2)
            f_layer(cube[:9])
            s_layer(cube[9:17])
            t_layer(cube[17:])
            glPopMatrix()
            drawText(50, 120, f"Shuffling cube for {m[2]}/{m[1]} cycles", m[0])
            k += 20
            pygame.display.flip()
    else:

        while m < 90:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            # Move first layer
            glPushMatrix()
            glTranslated(2, 0, 2)
            glRotated(m, 0, 0, -1)
            glTranslated(-2, 0, -2)
            f_layer(cube[:9])
            s_layer(cube[9:17])
            t_layer(cube[17:])
            glPopMatrix()
            m += 7
            pygame.display.flip()


def shuffle_animation(cycle: int, m: int, cube: list, font):
    """Shuffle the cube"""

    k = 1
    while k < cycle:
        u_first_animation([font, cycle, k], cube)
        cube = u_first_move(cube)
        z_animation([font, cycle, k], cube)
        cube = z_move(cube)
        k += 1


def sexy_animation(m: int, cube: list):
    """Do the Sexy Move"""

    z_animation(m, cube)
    cube = z_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    u_first_animation(m, cube)
    cube = u_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    u_animation(m, cube)
    cube = u_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    u_first_animation(m, cube)
    cube = u_first_move(cube)
    z_animation(m, cube)
    cube = z_move(cube)
    u_first_animation(m, cube)
    cube = u_first_move(cube)


def u_first_move(cube: list):
    """Take the cube, do a movement and give it back with update position"""

    temp_cube = list()
    temp_pos = list()
    count = 0
    for face in cube:
        if len(face) == 2 and 0 <= count < 9:
            temp_cube.append([face[1], face[0]])
        elif count == 2:
            temp_cube.append([face[1], face[2], face[0]])
        elif count == 4:
            temp_cube.append([face[2], face[0], face[1]])
        else:
            temp_cube.append(face)

        count += 1

    # Change 3 faces
    temp_0 = temp_cube[0]
    temp_cube[0] = temp_cube[6]
    temp_2 = temp_cube[2]
    temp_cube[2] = temp_0
    temp_4 = temp_cube[4]
    temp_cube[4] = temp_2
    temp_cube[6] = temp_4

    # Change 2 faces
    temp_1 = temp_cube[1]
    temp_cube[1] = temp_cube[7]
    temp_3 = temp_cube[3]
    temp_cube[3] = temp_1
    temp_5 = temp_cube[5]
    temp_cube[5] = temp_3
    temp_cube[7] = temp_5

    return temp_cube


def u_move(cube: list):
    """Take the cube, do a movement and give it back with update position"""

    temp_cube = list()
    temp_pos = list()
    count = 0
    for face in cube:
        if len(face) == 2 and 0 <= count < 9:
            temp_cube.append([face[1], face[0]])
        elif count == 2:
            temp_cube.append([face[0], face[1], face[2]])
        elif count == 4:
            temp_cube.append([face[2], face[0], face[1]])
        elif count == 6:
            temp_cube.append([face[1], face[2], face[0]])
        else:
            temp_cube.append(face)
        count += 1

    # Change 3 faces
    temp_6 = temp_cube[6]
    temp_cube[6] = temp_cube[0]
    temp_4 = temp_cube[4]
    temp_cube[4] = temp_6
    temp_2 = temp_cube[2]
    temp_cube[2] = temp_4
    temp_cube[0] = temp_2

    # Change 2 faces
    temp_7 = temp_cube[7]
    temp_cube[7] = temp_cube[1]
    temp_5 = temp_cube[5]
    temp_cube[5] = temp_7
    temp_3 = temp_cube[3]
    temp_cube[3] = temp_5
    temp_cube[1] = temp_3

    return temp_cube


def m_move(cube: list):
    """Take the cube, do a movement and give it back with update position"""

    temp_cube = list()
    temp_pos = list()
    count = 0
    for face in cube:
        if count in (1, 5, 18, 22):
            temp_cube.append([face[1], face[0]])
        else:
            temp_cube.append(face)
        count += 1

    temp_1 = temp_cube[1]
    temp_cube[1] = temp_cube[5]
    temp_8 = temp_cube[8]
    temp_cube[8] = temp_cube[14]
    temp_cube[5] = temp_cube[22]
    temp_cube[14] = temp_cube[25]
    temp_cube[22] = temp_cube[18]
    temp_cube[25] = temp_cube[10]
    temp_cube[18] = temp_1
    temp_cube[10] = temp_8

    temp_cube = z_move(temp_cube)

    return temp_cube


def m_first_move(cube: list):
    """Take the cube, do a movement and give it back with update position"""

    temp_cube = list()
    temp_pos = list()
    count = 0
    for face in cube:
        if count in (1, 5, 18, 22):
            temp_cube.append([face[1], face[0]])
        else:
            temp_cube.append(face)
        count += 1

    # Change central faces
    temp_5 = temp_cube[5]
    temp_cube[5] = temp_cube[1]
    temp_14 = temp_cube[14]
    temp_cube[14] = temp_cube[8]
    temp_22 = temp_cube[22]
    temp_cube[22] = temp_5
    temp_25 = temp_cube[25]
    temp_cube[25] = temp_14
    temp_18 = temp_cube[18]
    temp_cube[18] = temp_22
    temp_10 = temp_cube[10]
    temp_cube[10] = temp_25
    temp_cube[1] = temp_18
    temp_cube[8] = temp_10

    temp_cube = z_move(temp_cube)

    return temp_cube


def x_first_move(cube):
    """Take the cube and rotate it, so place on top the face to move"""

    temp_cube = list()
    temp_pos = list()
    count = 0
    for face in cube:
        if len(face) == 2:
            temp_cube.append([face[1], face[0]])
        elif count in (0, 17, 2):
            temp_cube.append([face[1], face[2], face[0]])
        elif count in (6, 23, 19):
            temp_cube.append([face[2], face[0], face[1]])
        else:
            temp_cube.append(face)
        count += 1

    # Central line
    temp_10 = temp_cube[10]
    temp_cube[10] = temp_cube[8]
    temp_cube[8] = temp_cube[14]
    temp_cube[14] = temp_cube[25]
    temp_cube[25] = temp_10

    temp_18 = temp_cube[18]
    temp_cube[18] = temp_cube[1]
    temp_cube[1] = temp_cube[5]
    temp_cube[5] = temp_cube[22]
    temp_cube[22] = temp_18

    # Edge
    temp_19 = temp_cube[19]
    temp_cube[19] = temp_cube[2]
    temp_cube[2] = temp_cube[4]
    temp_cube[4] = temp_cube[21]
    temp_cube[21] = temp_19

    temp_11 = temp_cube[11]
    temp_cube[11] = temp_cube[3]
    temp_cube[3] = temp_cube[13]
    temp_cube[13] = temp_cube[20]
    temp_cube[20] = temp_11

    temp_17 = temp_cube[17]
    temp_cube[17] = temp_cube[0]
    temp_cube[0] = temp_cube[6]
    temp_cube[6] = temp_cube[23]
    temp_cube[23] = temp_17

    temp_9 = temp_cube[9]
    temp_cube[9] = temp_cube[7]
    temp_cube[7] = temp_cube[15]
    temp_cube[15] = temp_cube[24]
    temp_cube[24] = temp_9


    return temp_cube


def z_move(cube: list):
    """Take the cube and rotate it, so place on top the face to move"""

    temp_cube = list()
    temp_pos = list()
    count = 0
    for face in cube:
        if len(face) == 2:
            temp_cube.append([face[1], face[0]])
        elif count == 17:
            temp_cube.append([face[1], face[2], face[0]])
        elif count == 0:
            temp_cube.append([face[2], face[0], face[1]])
        elif count == 4:
            temp_cube.append([face[1], face[2], face[0]])
        elif count == 6:
            temp_cube.append([face[2], face[0], face[1]])
        else:
            temp_cube.append(face)
        count += 1

    # Central Single
    temp_12 = temp_cube[12]
    temp_cube[12] = temp_cube[8]
    temp_cube[8] = temp_cube[16]
    temp_cube[16] = temp_cube[25]
    temp_cube[25] = temp_12

    # Central edges
    temp_20 = temp_cube[20]
    temp_cube[20] = temp_cube[3]
    temp_cube[3] = temp_cube[7]
    temp_cube[7] = temp_cube[24]
    temp_cube[24] = temp_20

    # Right edges

    temp_21 = temp_cube[21]
    temp_cube[21] = temp_cube[4]
    temp_cube[4] = temp_cube[6]
    temp_cube[6] = temp_cube[23]
    temp_cube[23] = temp_21

    # Right central

    temp_13 = temp_cube[13]
    temp_cube[13] = temp_cube[5]
    temp_cube[5] = temp_cube[15]
    temp_cube[15] = temp_cube[22]
    temp_cube[22] = temp_13

    # Left edges

    temp_19 = temp_cube[19]
    temp_cube[19] = temp_cube[2]
    temp_cube[2] = temp_cube[0]
    temp_cube[0] = temp_cube[17]
    temp_cube[17] = temp_19

    # Left central

    temp_11 = temp_cube[11]
    temp_cube[11] = temp_cube[1]
    temp_cube[1] = temp_cube[9]
    temp_cube[9] = temp_cube[18]
    temp_cube[18] = temp_11

    return temp_cube


def sexy_move(cube: list):
    """Do sexy move"""

    cube = z_move(cube)
    cube = z_move(cube)
    cube = z_move(cube)
    cube = u_move(cube)
    cube = z_move(cube)
    cube = u_move(cube)
    cube = z_move(cube)
    cube = z_move(cube)
    cube = z_move(cube)
    cube = u_first_move(cube)
    cube = z_move(cube)
    cube = u_first_move(cube)

    return cube


def shuffle(cycle, cube: list):
    """Take the cube and move the faces to messy the all cube"""

    k = 1
    while k < cycle:
        cube = u_first_move(cube)
        cube = z_move(cube)
        k += 1

    return cube


def drawText(x: int, y: int, text: str, font):
    """Print on the screen how many times is shuffling the cube"""
    
    textSurface = font.render(text, True, (255, 255, 66, 255)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


def main():
    """Main code"""

    # Manual definition of layers
    first_layer = [["orange", "blue", "white"], ["white", "orange"], ["green", "orange", "white"],
                   ["green", "white"], ["green", "white", "red"], ["white", "red"], ["blue", "red", "white"],
                   ["blue", "white"], ["white"]]

    second_layer = [["orange", "blue"], ["orange"], ["orange", "green"], ["green"], ["red", "green"],
                    ["red"],
                    ["red", "blue"], ["blue"]]

    third_layer = [["blue", "orange", "yellow"], ["yellow", "orange"], ["yellow", "orange", "green"],
                   ["green", "yellow"], ["green", "red", "yellow"], ["yellow", "red"], ["yellow", "red", "blue"],
                   ["blue", "yellow"], ["yellow"]]

    # Build the cube base on previous layers
    rubik_cube = list()
    for layer in (first_layer, second_layer, third_layer):
        lay = layer
        for face in lay:
            rubik_cube.append(face)


    # Initialize pygame gui
    pygame.init()
    pygame.font.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    icon = pygame.image.load('rubik.png')
    pygame.display.set_icon(icon)
    font = pygame.font.SysFont('lucinda console', 64)
    pygame.display.set_caption("Rubik Cube")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-1.0, 1.0, -25)  # Camera view
    glRotatef(45, 1, 1, 1)  # Prospective view


    # No overlapping
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # Extra variables
    u_first_key = False
    u_key = False
    m_key = False
    m_first_key = False
    z_key = False
    x_first_key = False
    shuffle_key = False
    sexy_key = False
    cycle = 0
    m = 1
    prev_pos_x = 0
    prev_pos_y = 0

    # Show the cube on screen
    while True:

        # Check for pressed keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:  # Change camera view
                    glRotatef(20, 0, -1, 0)
                if event.key == pygame.K_f:  # Change camera view
                    glRotatef(20, 0, 1, 0)
                if event.key == pygame.K_s:  # Change camera view
                    glRotatef(10, 0, 2, 1)
                if event.key == pygame.K_d:  # Change camera view
                    glRotatef(90, 1, 0, 0)
                if event.key == pygame.K_ESCAPE:  # Exit
                    exit()

                # U' Move
                if event.key == pygame.K_o:
                    u_first_animation(m, rubik_cube)
                    u_first_key = True

                # U Move
                if event.key == pygame.K_p:
                    u_animation(m, rubik_cube)
                    u_key = True

                # M Move
                if event.key == pygame.K_v:
                    m_animation(m, rubik_cube)
                    m_key = True

                # M' Move
                if event.key == pygame.K_c:
                    x_first_animation(m, rubik_cube)
                    m_first_key = True

                # Z Move
                if event.key == pygame.K_t:
                    z_animation(m, rubik_cube)
                    z_key = True

                # X' Move
                if event.key == pygame.K_w:
                    x_first_animation(m, rubik_cube)
                    x_first_key = True

                # Sexy Move
                if event.key == pygame.K_s:
                    sexy_animation(m, rubik_cube)
                    sexy_key = True

                # Shuffle Move
                if event.key == pygame.K_a:
                    cycle = randrange(5, 100)
                    shuffle_animation(cycle, m, rubik_cube, font)
                    shuffle_key = True

        # Mouse Camera
        for event in pygame.mouse.get_pressed(3):
            if event:
                if abs(prev_pos_x - pygame.mouse.get_pos()[0]) == 0:
                    glRotatef(20, 1, 0, 0)  # Camera view
                elif abs(prev_pos_y - pygame.mouse.get_pos()[1]) == 0:
                    glRotatef(20, 0, 1, 0)  # Camera view
                elif abs(prev_pos_y - pygame.mouse.get_pos()[1]) > 1 and abs(prev_pos_x - pygame.mouse.get_pos()[0]) > 1:
                    glRotatef(20, 1, 1, 0)  # Camera view
            prev_pos_x = pygame.mouse.get_pos()[0]
            prev_pos_y = pygame.mouse.get_pos()[1]


        # Clear view
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if u_first_key:
            rubik_cube = u_first_move(rubik_cube)
            u_first_key = False
        elif u_key:
            rubik_cube = u_move(rubik_cube)
            u_key = False
        elif m_key:
            rubik_cube = m_move(rubik_cube)
            m_key = False
        elif m_first_key:
            rubik_cube = m_first_move(rubik_cube)
            m_first_key = False
        elif x_first_key:
            rubik_cube = x_first_move(rubik_cube)
            x_first_key = False
        elif z_key:
            rubik_cube = z_move(rubik_cube)
            z_key = False
        elif shuffle_key:
            rubik_cube = shuffle(cycle, rubik_cube)
            shuffle_key = False
        elif sexy_key:
            rubik_cube = sexy_move(rubik_cube)
            sexy_key = False

        # Show updated layer
        f_layer(rubik_cube[:9])
        s_layer(rubik_cube[9:17])
        t_layer(rubik_cube[17:])

        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == '__main__':
    main()
