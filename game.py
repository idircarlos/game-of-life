#!/usr/bin/python3
from os import write
import tkinter as tk
import time
from tkinter.constants import TRUE, X
GROW_FACTOR = 10
ROWS = int(input("Rows: "))
COLUMNS = int(input("Columns: "))
HEIGHT = ROWS*GROW_FACTOR
WIDTH  = COLUMNS*GROW_FACTOR
alives = []
deaths = []
grid = [[0 for x in range(int((HEIGHT/GROW_FACTOR)))] for y in range(int((WIDTH/GROW_FACTOR)))]
f = open("grid.txt", "w",encoding='utf8')

def writeble_line():
    i = 0
    while i < COLUMNS - 1:
        f.write("│   ")
        i = i + 1
    f.write("│   │\n")

def first_line():
    i = 0
    f.write("┌───")
    while i < COLUMNS - 1:
        f.write("┬───")
        i = i + 1
    f.write("┐\n")
    i = 0
    writeble_line()


def last_line():
    i = 0
    f.write("└───")
    while i < COLUMNS - 1:
        f.write("┴───")
        i = i + 1
    f.write("┘\n")
    i = 0

def write_board():  
    i = 1
    j = 1
    first_line()
    while i < ROWS:
        j = 1
        f.write("├───")
        while j < COLUMNS - 1:
            f.write("┼───")
            j = j + 1
        f.write("┼───┤\n")
        writeble_line()
        i = i + 1
    last_line()
    f.close()

def revive(x,y):
    grid[x][y] = 1
    alives.append([x,y])

def kill(x,y):
    grid[x][y] = 0
    deaths.append([x,y])

def read_file():
    f = open("grid.txt", "r",encoding='utf8')
    n_line = 0
    cont_spaces = 0
    just_checked = False
    x = 0
    y = 0
    lines = f.readlines()
    del lines[0::2]
    for line in lines:
        y = 0
        cont_spaces = 0
        for c in line:
            if c == ' ':
                if cont_spaces == 1:
                    y = y + 1
                    cont_spaces = cont_spaces + 1
                elif cont_spaces == 2 or just_checked == True:
                    cont_spaces = 0
                    just_checked = False
                else:
                    cont_spaces = cont_spaces + 1
            elif c == 'x' or c == 'X':
                revive(y,x)
                y = y + 1
                cont_spaces = 0
                just_checked = True
        x = x + 1
    

write_board()
print("Check the grid.txt file and replace the spaces ' ' by 'x'")
input("Press enter when you are ready. Make sure to save the changes in the file")
read_file()


OFF_SET = 18
TOTAL_SQUARES = (HEIGHT*WIDTH)/GROW_FACTOR
TURN_TIME = 0.001



window = tk.Tk()
window.title("ventana")
window.geometry(str(HEIGHT) + "x" + str(WIDTH))
canvas = tk.Canvas(window, bg="black", height=HEIGHT, width=WIDTH)




def print_lines():
    i = 0
    while i < HEIGHT:
        canvas.create_line(i,0,i,HEIGHT,fill='white')
        canvas.create_line(0,i,WIDTH,i,fill='white')
        i = i + GROW_FACTOR

def active_cell():
    print('pulsado')

def print_all():
    for alive in alives:
        canvas.create_rectangle(alive[0]*GROW_FACTOR,alive[1]*GROW_FACTOR,alive[0]*GROW_FACTOR + GROW_FACTOR,alive[1]*GROW_FACTOR + GROW_FACTOR,fill='white')
    for death in deaths:
        canvas.create_rectangle(death[0]*GROW_FACTOR,death[1]*GROW_FACTOR,death[0]*GROW_FACTOR + GROW_FACTOR,death[1]*GROW_FACTOR + GROW_FACTOR,fill='black')
    alives.clear()
    deaths.clear()
    

def check_top_left(x,y):
    if grid[x-1][y-1] == 1:

        return True
    else: 
        return False

def check_top_middle(x,y):
    if grid[x][y-1] == 1:

        return True
    else: 
        return False

def check_top_right(x,y):
    
    if grid[x+1][y-1] == 1:

        return True
    else: 
        return False

def check_left(x,y):
    if grid[x-1][y] == 1:

        return True
    else: 
        return False

def check_right(x,y):
    if grid[x+1][y] == 1:

        return True
    else: 
        return False

def check_bot_left(x,y):
    if grid[x-1][y+1] == 1:

        return True
    else: 
        return False

def check_bot_middle(x,y):
    if grid[x][y+1] == 1:

        return True
    else: 
        return False

def check_bot_right(x,y):
    if grid[x+1][y+1] == 1:
        return True
    else: 
        return False

def upgrade_step():
    cont = 0
    x = 1
    y = 1
    point = []
    reviving_points = []
    dying_points = []
    while x < HEIGHT/GROW_FACTOR - 1:
        y = 1
        while y < WIDTH/GROW_FACTOR - 1:
            if grid[x][y] == 0:
                if check_top_left(x,y) == True:
                    cont = cont + 1
                if check_top_middle(x,y) == True:
                    cont = cont + 1
                if check_top_right(x,y) == True:
                    cont = cont + 1
                if check_left(x,y) == True:
                    cont = cont + 1
                if check_right(x,y) == True:
                    cont = cont + 1
                if check_bot_left(x,y) == True:
                    cont = cont + 1
                if check_bot_middle(x,y) == True:
                    cont = cont + 1
                if check_bot_right(x,y) == True:
                    cont = cont + 1
                if cont == 3:
                    reviving_points.append([x,y])
                cont = 0

            elif grid[x][y] == 1:
                if check_top_left(x,y) == True:
                    cont = cont + 1
                if check_top_middle(x,y) == True:
                    cont = cont + 1
                if check_top_right(x,y) == True:
                    cont = cont + 1
                if check_left(x,y) == True:
                    cont = cont + 1
                if check_right(x,y) == True:
                    cont = cont + 1
                if check_bot_left(x,y) == True:
                    cont = cont + 1
                if check_bot_middle(x,y) == True:
                    cont = cont + 1
                if check_bot_right(x,y) == True:
                    cont = cont + 1
                if cont != 2 and cont != 3:
                    dying_points.append([x,y])
                cont = 0
            y = y + 1
        x = x + 1

    i = 0
    for punto in reviving_points:
        grid[punto[0]][punto[1]] = 1
        alives.append(punto)
        i = i + 2

    for punto in dying_points:
        grid[punto[0]][punto[1]] = 0
        deaths.append(punto)
        i = i + 2
    #print(alives)
    #print(deaths)
    reviving_points.clear()
    dying_points.clear()
        
canvas.pack()
while True:
    #print_lines()
    print_all()
    
    window.update_idletasks()
    window.update()

    time.sleep(TURN_TIME)
    upgrade_step()
    

