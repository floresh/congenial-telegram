from Tkinter import *
import pylab as pl
import math
start_x = -140
start_y = -120
width = 500
height = 500
zoom =100

class coordinate(object):
    '''coordinate([x,y])
    class for information of a coordinate point'''
    def __init__(self,x,y):
        self.color = color(z_function(complex((x/zoom)+(start_x/zoom),(y/zoom)+(start_y/zoom))))
        self.x = x
        self.y = y
    def __str__(self):
        return str(complex(self.x,self.y))

def z_function(z,c=complex(-.4,-.6),max_steps=10,escaping_num=100000):
    
    num_steps = 0
    while abs(z) < escaping_num:
        try:
            z = z**3 - z**2 + c
        except ZeroDivisionError:
            return -1
        num_steps += 1
        if num_steps > max_steps:
            return -1
        
    return num_steps

def color(num_steps):
    if num_steps==-1:return 'black'
    if num_steps==0:return '#540EAD' ##5712AF
    if num_steps==1:return '#402F56'
    if num_steps==2:return '#170034'
    if num_steps==3:return '#FB000D'		
    if num_steps==4:return '#7D3F42'
    if num_steps==5:return '#4B0004'
    if num_steps==6:return '#04859D'
    if num_steps==7:return '#28484F'
    if num_steps==8:return '#00282F'
    if num_steps==9:return '#5610AF'
    if num_steps==10:return '#0776AD'


def graph():
    root = Tk()

    frame = Frame(root, width=width, height=height)
    frame.pack()

    canvas = Canvas(frame,width=width,height=height)
    canvas.pack()

    res = int(raw_input("resolution: "))
    c_list = []
    
    for x in range(width):
        c_list.append([])
        
        for y in range(height):
            c_list[x].append([float(x*res),float(y*res)])
            c = coordinate(c_list[x][y][0],c_list[x][y][1])
            canvas.create_rectangle(c.x,c.y,c.x+res,c.y+res,fill=c.color,outline=c.color)
            canvas.update()
        
    root.mainloop()

graph()