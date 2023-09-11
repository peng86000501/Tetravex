#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import tkinter
import random
#import tkmessagebox
 
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的颜色为白色
from tkinter import *

def ifthrow():
    global throwback
    if boxindex == 0:
        if (boxes[3].up == -1 or boxes[3].up == squares[mess[moveindex]].down) and \
            (boxes[1].left == -1 or boxes[1].left == squares[mess[moveindex]].right):
            throwback = False
        else:
            throwback = True
                
    elif boxindex == 1:
        if (boxes[0].right == -1 or boxes[0].right == squares[mess[moveindex]].left) and \
            (boxes[4].up == -1 or boxes[4].up == squares[mess[moveindex]].down) and \
            (boxes[2].left == -1 or boxes[2].left == squares[mess[moveindex]].right) :
            throwback = False
        else:
            throwback = True

    elif boxindex == 2:
        if (boxes[1].right == -1 or boxes[1].right == squares[mess[moveindex]].left) and \
            (boxes[5].up == -1 or boxes[5].up == squares[mess[moveindex]].down):
            throwback = False
        else:
            throwback = True

    elif boxindex == 3:
        if (boxes[0].down == -1 or boxes[0].down == squares[mess[moveindex]].up) and \
            (boxes[4].left == -1 or boxes[4].left == squares[mess[moveindex]].right) and \
            (boxes[6].up == -1 or boxes[6].up == squares[mess[moveindex]].down):
            throwback = False
        else:
            throwback = True
    
    elif boxindex == 4:
        if (boxes[1].down == -1 or boxes[1].down == squares[mess[moveindex]].up) and \
            (boxes[3].right == -1 or boxes[3].right == squares[mess[moveindex]].left) and \
            (boxes[5].left == -1 or boxes[5].left == squares[mess[moveindex]].right) and \
            (boxes[7].up == -1 or boxes[7].up == squares[mess[moveindex]].down):
            throwback = False
        else:
            throwback = True
    
    elif boxindex == 5:
        if (boxes[2].down == -1 or boxes[2].down == squares[mess[moveindex]].up) and \
            (boxes[4].right == -1 or boxes[4].right == squares[mess[moveindex]].left) and \
            (boxes[8].up == -1 or boxes[8].up == squares[mess[moveindex]].down):
            throwback = False
        else:
            throwback = True

    elif boxindex == 6:
        if (boxes[3].down == -1 or boxes[3].down == squares[mess[moveindex]].up) and \
            (boxes[7].left == -1 or boxes[7].left == squares[mess[moveindex]].right):
            throwback = False
        else:
            throwback = True
    
    elif boxindex == 7:
        if (boxes[4].down == -1 or boxes[4].down == squares[mess[moveindex]].up) and \
            (boxes[6].right == -1 or boxes[6].right == squares[mess[moveindex]].left) and \
            (boxes[8].left == -1 or boxes[8].left == squares[mess[moveindex]].right):
            throwback = False
        else:
            throwback = True
    
    elif boxindex == 8:
        print("boxindex == 8 condition",(boxes[5].down == -1 or boxes[5].down == squares[mess[moveindex]].up), (boxes[7].left == -1 or boxes[7].left == squares[mess[moveindex]].right))
        if (boxes[5].down == -1 or boxes[5].down == squares[mess[moveindex]].up) and \
            (boxes[7].right == -1 or boxes[7].right == squares[mess[moveindex]].left):
            print("throw = False")
            throwback = False
        else:
            print("throw = True")
            throwback = True

    if throwback == False:
        boxes[boxindex].up = squares[mess[moveindex]].up
        boxes[boxindex].left = squares[mess[moveindex]].left
        boxes[boxindex].right = squares[mess[moveindex]].right
        boxes[boxindex].down = squares[mess[moveindex]].down
    return throwback

def ifthrow2():
    conditions = {
        0: (boxes[2].up == -1 or boxes[2].up == squares[mess[moveindex]].down,
            boxes[1].left == -1 or boxes[1].left == squares[mess[moveindex]].right),
        1: (boxes[0].right == -1 or boxes[0].right == squares[mess[moveindex]].left,
            boxes[3].up == -1 or boxes[3].up == squares[mess[moveindex]].down),
        2: (boxes[0].down == -1 or boxes[0].down == squares[mess[moveindex]].up,
            boxes[3].left == -1 or boxes[3].left == squares[mess[moveindex]].right),
        3: (boxes[1].down == -1 or boxes[1].down == squares[mess[moveindex]].up,
            boxes[2].right == -1 or boxes[2].right == squares[mess[moveindex]].left)
    }
    
    if conditions[boxindex][0] and conditions[boxindex][1]:
        '''
        for i in range(4):
            boxes[i].up = squares[mess[moveindex]].up
            boxes[i].left = squares[mess[moveindex]].left
            boxes[i].right = squares[mess[moveindex]].right
            boxes[i].down = squares[mess[moveindex]].down
        '''
        boxes[boxindex].up = squares[mess[moveindex]].up
        boxes[boxindex].left = squares[mess[moveindex]].left
        boxes[boxindex].right = squares[mess[moveindex]].right
        boxes[boxindex].down = squares[mess[moveindex]].down
        throwback = False
    else:
        throwback = True
    
    return throwback

def ifthrow3():
    throwback = False
    box_indices = [0, 1, 2, 3] # 存储四个方块的索引
    
    for i in box_indices: # 遍历每个方块
        if i == 0: # 如果是第一个方块
            # 判断是否满足条件
            condition = (boxes[2].up == -1 or boxes[2].up == squares[mess[moveindex]].down) and \
                (boxes[1].left == -1 or boxes[1].left == squares[mess[moveindex]].right)
        elif i == 1: # 如果是第二个方块
            # 判断是否满足条件
            condition = (boxes[0].right == -1 or boxes[0].right == squares[mess[moveindex]].left) and \
                (boxes[3].up == -1 or boxes[3].up == squares[mess[moveindex]].down)
        elif i == 2: # 如果是第三个方块
            # 判断是否满足条件
            condition = (boxes[0].down == -1 or boxes[0].down == squares[mess[moveindex]].up) and \
                (boxes[3].left == -1 or boxes[3].left == squares[mess[moveindex]].right)
        elif i == 3: # 如果是第四个方块
            # 判断是否满足条件
            condition = (boxes[1].down == -1 or boxes[1].down == squares[mess[moveindex]].up) and \
                (boxes[2].right == -1 or boxes[2].right == squares[mess[moveindex]].left)
        if condition: # 如果条件成立
            throwback = False # 不需要扔回去
        else: # 如果条件不成立
            throwback = True # 需要扔回去

        if throwback == False:
            boxes[boxindex].up = squares[mess[moveindex]].up
            boxes[boxindex].left = squares[mess[moveindex]].left
            boxes[boxindex].right = squares[mess[moveindex]].right
            boxes[boxindex].down = squares[mess[moveindex]].down
    return throwback # 返回结果

def mouse_key(event):
    print("clicked at", event.x, event.y)
    '''
    if(clicked):
        clicked = False
    else:
        clicked =  True
    '''
    global move
    #clicked = not clicked
    global moveindex
    global boxindex
    global throwback
    global win
    global txwin
    global move
    global mess
    global place_seq
    moveindex = -1
    boxindex = -1
    throwback = False
    place = False
    squares_num = 9
    print("moveindex  mess[moveindex] mess[i] -----yrp",moveindex, mess[moveindex], mess[0])
    print("mess", mess)

    for i in range(0, 9):
        print("i x y",i,squares[mess[i]].x,squares[mess[i]].y)
        if(event.x > squares[mess[i]].x and event.x - squares[mess[i]].x < 100 and event.y > squares[mess[i]].y and event.y - squares[mess[i]].y < 100):
            moveindex = i
            print("moveindex", moveindex)
            break

    for i in range(0,squares_num):
        if(event.x > box_x[i] and event.x - box_x[i] < 100 and event.y > box_y[i] and event.y - box_y[i] < 100):
            boxindex = i
            print("boxindex", boxindex)
            break

    if moveindex == -1:
        move = False

    if boxindex == -1:
        place = False

    if moveindex != -1:
        move = not move

    if boxindex != -1 and moveindex != -1:
        place = True
        ifthrowback = ifthrow()
        #ifthrowback = ifthrow2()
        #ifthrowback = ifthrow3()
        
        if ifthrowback:
            squares[mess[moveindex]].move(origin_x[moveindex] + 10 - squares[mess[moveindex]].x, origin_y[moveindex] + 10 - squares[mess[moveindex]].y)
        else:
            squares[mess[moveindex]].move(box_x[boxindex] + 15 - squares[mess[moveindex]].x, box_y[boxindex] + 13 - squares[mess[moveindex]].y)
            place_seq[boxindex] = moveindex

        print("boxindex move", boxindex, move)
        if move == True:
            print("move == True boxindex move", boxindex, move)
            place_seq[boxindex] = -1
            boxes[boxindex].up = -1
            boxes[boxindex].left = -1
            boxes[boxindex].right = -1
            boxes[boxindex].down = -1

    print("moveindex boxindex move place", moveindex, boxindex, move, place)
    print("judgewin")
    if win == True:
        #exit()
        print("judgewin delete txwin")
        cv.delete(txwin)
        win = False
        for i in range(9):
            squares[i].delete()
            place_seq[i] = -1
        
        start()
    judgewin()

def on_mouse_move(event):
    global last_x, last_y
    #global moveindex
    dx = event.x - last_x
    dy = event.y - last_y
    if (move):
        '''
        cv.move(r1, dx, dy)
        cv.move(tr1, dx, dy)
        cv.move(tx1, dx, dy)
        cv.move(tr2, dx, dy)
        cv.move(tx2, dx, dy)
        cv.move(tr3, dx, dy)
        cv.move(tx3, dx, dy)
        cv.move(tr4, dx, dy)
        cv.move(tx4, dx, dy)
        '''

        '''
        cv.move(s1.r1, dx, dy)
        cv.move(s1.trup, dx, dy)
        cv.move(s1.txup, dx, dy)
        cv.move(s1.trleft, dx, dy)
        cv.move(s1.txleft, dx, dy)
        cv.move(s1.trright, dx, dy)
        cv.move(s1.txright, dx, dy)
        cv.move(s1.trdown, dx, dy)
        cv.move(s1.txdown, dx, dy)
        cv.move(s1.l1, dx, dy)
        cv.move(s1.l2, dx, dy)
        '''

        squares[mess[moveindex]].move(dx,dy)
    last_x, last_y = event.x, event.y
    #print("last x and y",last_x, last_y)
    print("moveindex  mess[moveindex]",moveindex,mess[moveindex])
    print("mess", mess)

def printsquare(squ):
    #print(str(squ))
    print(" ",squ.up)
    print(squ.left, " ",squ.right)
    #print(s1.right)
    print(" ",squ.down)
    return

def printsquares():
    for i in range(0,3):
        print("------------")
        #print("get_index(i, 0)",get_index(i, 0))
        #print("get_index(i, 1)",get_index(i, 1))
        print(" ",boxes[i*3+0].up, " | ", boxes[i*3+1].up, " | ", boxes[i*3+2].up)
        print(boxes[i*3+0].left, "", boxes[i*3+0].right, "|", boxes[i*3+1].left, "",boxes[i*3+1].right, "|", boxes[i*3+2].left, "",boxes[i*3+2].right)
        print(" ",boxes[i*3+0].down," | ", boxes[i*3+1].down," | ", boxes[i*3+2].down)
    print("------------")
    return

def judgewin():
    global txwin
    print("judgewin conditions", boxes[0].right == boxes[1].left and boxes[0].down == boxes[3].up,\
       boxes[2].left == boxes[1].right and boxes[2].down == boxes[5].up,\
       boxes[4].left == boxes[3].right and boxes[4].right == boxes[5].left and boxes[4].down == boxes[7].up,\
       boxes[5].down == boxes[8].up,\
       boxes[6].up == boxes[3].down and boxes[6].right == boxes[7].left,\
       boxes[7].up == boxes[4].down and boxes[7].right == boxes[8].left,\
       "full = ",
       check_place_seq_full())
    if boxes[0].right == boxes[1].left and boxes[0].down == boxes[3].up and\
       boxes[2].left == boxes[1].right and boxes[2].down == boxes[5].up and\
       boxes[4].left == boxes[3].right and boxes[4].right == boxes[5].left and boxes[4].down == boxes[7].up and\
       boxes[5].down == boxes[8].up and\
       boxes[6].up == boxes[3].down and boxes[6].right == boxes[7].left and\
       boxes[7].up == boxes[4].down and boxes[7].right == boxes[8].left and\
       check_place_seq_full():
        print("win")
        txwin = cv.create_text(200, 190, text= "     You Win!\nClick to Start again",fill="black",font=('Helvetica 15 bold'))
        global win
        win = True
        for i in range(9):
            boxes[i].up = -1
            boxes[i].left = -1
            boxes[i].right = -1
            boxes[i].down = -1

            squares[i].x = 10
            squares[i].y = 10

def start():
    global last_x, last_y, move, place, throwback, win, moveindex, boxindex, mess, sequence
    
    last_x = 0
    last_y = 0
    move = False
    place = False
    throwback = False
    win = False
    moveindex = -1
    boxindex = -1
    global mess, sequence
    mess=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
    sequence = [0,1,2,3,4,5,6,7,8]

    s1.up = random.randint(0,9)
    s1.left = random.randint(0,9)
    s1.right = random.randint(0,9)
    s1.down = random.randint(0,9)

    s2.up = random.randint(0,9)
    s2.left=s1.right
    s2.right = random.randint(0,9)
    s2.down = random.randint(0,9)

    s3.up = random.randint(0,9)
    s3.left = s2.right
    s3.right = random.randint(0,9)
    s3.down = random.randint(0,9)

    s4.up = s1.down
    s4.left= random.randint(0,9)
    s4.right = random.randint(0,9)
    s4.down = random.randint(0,9)

    s5.up = s2.down
    s5.left= s4.right
    s5.right = random.randint(0,9)
    s5.down = random.randint(0,9)

    s6.up = s3.down
    s6.left= s5.right
    s6.right = random.randint(0,9)
    s6.down = random.randint(0,9)

    s7.up = s4.down
    s7.left= random.randint(0,9)
    s7.right = random.randint(0,9)
    s7.down = random.randint(0,9)

    s8.up = s5.down
    s8.left= s7.right
    s8.right = random.randint(0,9)
    s8.down = random.randint(0,9)

    s9.up = s6.down
    s9.left= s8.right
    s9.right = random.randint(0,9)
    s9.down = random.randint(0,9)


    print("mess", mess)

    '''
    for i in range(0,9):
        mess[i] = i
        squares[i].draw()
        squares[i].move(origin_x[i], origin_y[i])
    '''
    #'''
    for j in range(0,9):
        i=random.randint(0,8-j)
        print("j ", j, "sequence[i]",sequence[i], "i", i , "mess[i]", mess[i])
        mess[j] = sequence[i]
        del sequence[i]
        print("j sequence i mess[i]",j, sequence,i,mess[i])
        print("mess",mess)
    #'''
    for i in range(0,9):
        squares[mess[i]].draw()
        squares[mess[i]].move(origin_x[i], origin_y[i])
'''
    s1.draw()
    #s1.move(115,0)

    s2.draw()
    #s2.move(0,0)

    s3.draw()
    #s3.move(0,110)

    s4.draw()
    #s4.move(115,110)
'''

def check_place_seq_full():
    full = True
    print("full at first", full, "place_seq",place_seq)
    for i in range(0, 9):
        if place_seq[i] == -1:
            full = False
            print("i full False", i)
            break
    print("full at last", full)
    return full



class square:
    def __init__(self):
        self.up = -1
        self.left = -1
        self.right = -1
        self.down = -1
        self.x=10
        self.y=10

    def draw(self):
        global colors
        self.r1 = cv.create_rectangle(10,10,110,110)
        
        tex1 = str(self.left)
        randomcolor = colors[self.left]
        self.trleft = cv.create_polygon(10, 10, 60, 60, 10, 110, 10, 10, fill=randomcolor)
        self.txleft = cv.create_text(30, 60, text= tex1,fill="black",font=('Helvetica 15 bold'))
        
        tex1 = str(self.up)
        randomcolor = colors[self.up]
        self.trup = cv.create_polygon(10, 10, 60, 60, 110, 10, 10, 10, fill=randomcolor)
        self.txup = cv.create_text(60, 30, text= tex1,fill="black",font=('Helvetica 15 bold'))

        tex1 = str(self.right)
        randomcolor = colors[self.right]
        self.trright = cv.create_polygon(110, 10, 60, 60, 110, 110, 110, 10, fill=randomcolor)
        self.txright = cv.create_text(90, 60, text= tex1,fill="black",font=('Helvetica 15 bold'))

        tex1 = str(self.down)
        randomcolor = colors[self.down]
        self.trdown = cv.create_polygon(10, 110, 60, 60, 110, 110, 10, 110, fill=randomcolor)
        self.txdown = cv.create_text(60, 90, text= tex1,fill="black",font=('Helvetica 15 bold'))

        self.l1 = cv.create_line(10, 10, 110, 110)
        self.l2 = cv.create_line(110, 10, 10, 110)

    def move(self, x, y):
        cv.move(self.r1, x, y)
        cv.move(self.trup, x, y)
        cv.move(self.txup, x, y)
        cv.move(self.trleft, x, y)
        cv.move(self.txleft, x, y)
        cv.move(self.trright, x, y)
        cv.move(self.txright, x, y)
        cv.move(self.trdown, x, y)
        cv.move(self.txdown, x, y)
        cv.move(self.l1, x, y)
        cv.move(self.l2, x, y)
        self.x = self.x+x
        self.y = self.y+y
        print("self x and y",self.x, self.y)
        printsquares()

    def delete(self):
        cv.delete(self.r1)
        cv.delete(self.trleft)
        cv.delete(self.txleft)
        cv.delete(self.trup)
        cv.delete(self.txup)
        cv.delete(self.trright)
        cv.delete(self.txright)
        cv.delete(self.trdown)
        cv.delete(self.txdown)
        cv.delete(self.l1)
        cv.delete(self.l2)

last_x = 0
last_y = 0
move = False
place = False
throwback = False
win = False
moveindex = -1
boxindex = -1
mess = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
#mess = [0,1,2,3,4,5,6,7,8]
sequence = [0,1,2,3,4,5,6,7,8]
place_seq = [-1,-1,-1,-1,-1,-1,-1,-1,-1]

colors = ["springgreen", "yellow", "blue", "red", "green", "gray", "brown", "pink", "orange", "purple"]
origin_x = [0, 115, 230, 0, 115, 230, 0, 115, 230]
origin_y = [0, 0, 0, 110, 110, 110, 220, 220, 220]
box_x = [0, 110, 220, 0, 110, 220, 0, 110, 220]
box_y = [350, 350, 350, 460, 460, 460, 570, 570, 570]

root = Tk()
root.title('Tetravex 四邻')
root.geometry("360x720")
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white', width = 360, height = 720)
#cv.geometry("600x600")
# 创建一个矩形，坐标为(10,10,110,110)

r0 = cv.create_rectangle(10,350,350,690)
cv.create_line(120, 350, 120, 690)
cv.create_line(230, 350, 230, 690)
cv.create_line(10, 470, 350, 470)
cv.create_line(10, 575, 350, 575)


#r1 = cv.create_rectangle(10,10,110,110)

#tr1 = cv.create_polygon(120, 10, 220, 10, 120, 120, 120, 10, fill="PaleTurquoise")
'''
tr1 = cv.create_polygon(10, 10, 60, 60, 10, 110, 10, 10, fill="springgreen")
tx1 = cv.create_text(30, 60, text= "6",fill="black",font=('Helvetica 15 bold'))
tr2 = cv.create_polygon(10, 10, 60, 60, 110, 10, 10, 10, fill="yellow")
tx2 = cv.create_text(60, 30, text= "2",fill="black",font=('Helvetica 15 bold'))
tr3 = cv.create_polygon(110, 10, 60, 60, 110, 110, 110, 10, fill="blue")
tx3 = cv.create_text(90, 60, text= "3",fill="black",font=('Helvetica 15 bold'))
tr4 = cv.create_polygon(10, 110, 60, 60, 110, 110, 10, 110, fill="red")
tx4 = cv.create_text(60, 90, text= "4",fill="black",font=('Helvetica 15 bold'))
'''
#frame = Frame(root, width=100, height=100)
#frame.focus_set()
#frame.bind("<Button-1>", mouse_key)
#frame.pack()

cv.focus_set()
cv.bind("<Button-1>", mouse_key)
#cv.bind("<B1-Motion>", on_left_button_move)#left down drag
cv.bind("<Motion>", on_mouse_move)
cv.pack()


s1 = square()
s2 = square()
s3 = square()
s4 = square()
s5 = square()
s6 = square()
s7 = square()
s8 = square()
s9 = square()

squares = [s1, s2, s3, s4,s5, s6, s7, s8, s9]

b1 = square()
b2 = square()
b3 = square()
b4 = square()
b5 = square()
b6 = square()
b7 = square()
b8 = square()
b9 = square()

boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

start()


root.mainloop()
# 为明显起见，将背景色设置为白色，用以区别 root
#top.mainloop()
