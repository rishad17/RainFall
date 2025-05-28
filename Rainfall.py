from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


W_Width,W_Height = 800,600

#Rain
num_drops = 100
drop_positions = np.random.rand(num_drops,2)*2-1
rain_direction = 0
bg_color = [1.0,1.0,1.0]

def render_house():
    glLineWidth(3)

    # House walls - light brown
    glColor3f(0.8, 0.6, 0.4)
    glBegin(GL_POLYGON)
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.1)
    glVertex2f(-0.4, 0.1)
    glEnd()

    # Wall outline - black
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.1)
    glVertex2f(-0.4, 0.1)
    glEnd()

    # Roof - red
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.45, 0.1)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.45, 0.1)
    glEnd()

    # Roof outline - black
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.45, 0.1)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.45, 0.1)
    glEnd()

    # Door - dark brown
    glColor3f(0.4, 0.2, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.1)
    glVertex2f(-0.1, -0.1)
    glEnd()

    # Door outline - black
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.1)
    glVertex2f(-0.1, -0.1)
    glEnd()

    # Door knob - gold
    glColor3f(1.0, 0.84, 0.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(0.05, -0.3)
    glEnd()

    # Left window - light blue
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.3, -0.1)
    glVertex2f(-0.15, -0.1)
    glVertex2f(-0.15, 0.05)
    glVertex2f(-0.3, 0.05)
    glEnd()

    # Left window outline - black
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.3, -0.1)
    glVertex2f(-0.15, -0.1)
    glVertex2f(-0.15, 0.05)
    glVertex2f(-0.3, 0.05)
    glEnd()

    # Right window - light blue
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.15, -0.1)
    glVertex2f(0.3, -0.1)
    glVertex2f(0.3, 0.05)
    glVertex2f(0.15, 0.05)
    glEnd()

    # Right window outline - black
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.15, -0.1)
    glVertex2f(0.3, -0.1)
    glVertex2f(0.3, 0.05)
    glVertex2f(0.15, 0.05)
    glEnd()

def render_background():
    # Grass - darker green for wet look
    glColor3f(0.0, 0.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, -0.5)
    glVertex2f(-1.0, -0.5)
    glEnd()

    # Large rainwater puddle 1
    glColor3f(0.4, 0.6, 0.8)
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = 2 * np.pi * i / 100
        x = -0.3 + 0.25 * np.cos(angle)  # wider puddle
        y = -0.7 + 0.12 * np.sin(angle)
        glVertex2f(x, y)
    glEnd()

    # Large rainwater puddle 2
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = 2 * np.pi * i / 100
        x = 0.4 + 0.2 * np.cos(angle)
        y = -0.75 + 0.1 * np.sin(angle)
        glVertex2f(x, y)
    glEnd()

    # Optional: add small scattered puddles
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = 2 * np.pi * i / 100
        x = 0.0 + 0.15 * np.cos(angle)
        y = -0.65 + 0.07 * np.sin(angle)
        glVertex2f(x, y)
    glEnd()






def render_bent_rain():
    global drop_positions, rain_direction
    glColor3f(0.0, 0.5, 1.0)  # strong blue
    glLineWidth(2)  # increased from 1 → 2 for better visibility

    glBegin(GL_LINES)
    for i, pos in enumerate(drop_positions):
        bent_x = pos[0] + np.sin(rain_direction) * (1 - pos[1])
        length = np.random.uniform(0.05, 0.08)  # moderate length
        glVertex2f(bent_x, pos[1])
        glVertex2f(bent_x + np.sin(rain_direction) * 0.02, pos[1] - length)
    glEnd()

    # Fall speed
    drop_positions[:, 1] -= 0.025

    # Reset drops when they go below the screen
    reset_indices = drop_positions[:, 1] < -1
    drop_positions[reset_indices, 1] = 1
    drop_positions[reset_indices, 0] = np.random.uniform(-1, 1, np.sum(reset_indices))





def update_bg_color():
    glClearColor(bg_color[0],bg_color[1],bg_color[2],1.0)

def handle_keys(key, x, y):
    global bg_color
    if key == b'w':
        bg_color = [min(c+0.1,1.0) for c in bg_color]  # Lighten background
    elif key == b's':
        bg_color = [max(c-0.1,0.0) for c in bg_color]  # Darken background
    glutPostRedisplay()

def handle_special_keys(key, x, y):
    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction -= 0.1
    elif key == GLUT_KEY_RIGHT:
        rain_direction += 0.1
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    update_bg_color()
    render_background()
    render_house()
    render_bent_rain()
    glutSwapBuffers()

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1,1,-1,1)

def animate():
    glutPostRedisplay()

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"House and Rainfall")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(handle_keys)
glutSpecialFunc(handle_special_keys)
glutMainLoop()