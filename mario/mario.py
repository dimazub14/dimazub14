from tkinter import *
import random

WIDTH = 900
HEIGHT = 300

PAD_W = 10
PAD_H = 100
#МЯЧ
BALL_RADIUS = 40
BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0


root = Tk()
root.title("Пінг-понг:)")

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#008B8B")
c.pack()

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill = "white")#ліва
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill = "white")#права
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT,fill="white")#центр
#мяч
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
          HEIGHT/2-BALL_RADIUS/2,
          WIDTH/2+BALL_RADIUS/2,
          HEIGHT/2+BALL_RADIUS/2, fill="#ff4500")
#ракетка
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="#DA70D6")
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH - PAD_W/2, PAD_H, width=PAD_W, fill="#DA70D6")
PAD_SPEED = 20
LEFT_PAD_SPEED =0
RIGHT_PAD_SPEED =0
BALL_SPRRD_UP = 1.00
BALL_MAX_SPEED = 30
BALL_X_SPEED =20
BALL_Y_SPEED = 20
right_line_distance = WIDTH - PAD_W
def bounce (action):
    global BALL_X_SPEED, BALL_Y_SPEED
    if action == 'strike':
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= - BALL_SPRRD_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
            BALL_Y_SPEED = -BALL_Y_SPEED




def move_ball():
   ball_left, ball_top, ball_right,ball_bot= c.coords(BALL)
   ball_canter = (ball_top + ball_bot)/2
   if ball_right + BALL_X_SPEED < right_line_distance and ball_left + BALL_X_SPEED > PAD_W:
       c.move(BALL, BALL_X_SPEED,BALL_Y_SPEED)
   elif ball_right== right_line_distance or ball_left == PAD_W:
       if ball_right > WIDTH / 2:


def move_pads():
        PADS = {LEFT_PAD:LEFT_PAD_SPEED,
                RIGHT_PAD:RIGHT_PAD_SPEED}
        for pad in PADS:
            c.move(pad, 0, PADS [pad])
            if c.coords(pad)[1] < 0:
                c.move(pad, 0, -c.coords (pad)[1])
            elif c.coords(pad)[3]>HEIGHT:
                c.move(pad , 0, HEIGHT - c.coords(pad)[3])



def main():
    move_ball()
    move_pads()
    root.after(30, main)

    c.focus_set()
def moveent_handler(event):
        global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
        if event.keysym == 'w':
            LEFT_PAD_SPEED = - PAD_SPEED
        elif event.keysym == 's':
            LEFT_PAD_SPEED =PAD_SPEED
        elif event.keysym == "Up":
            RIGHT_PAD_SPEED = -PAD_SPEED
        elif event.keysym == "Down":
            RIGHT_PAD_SPEED = PAD_SPEED
            c.bind("<KeyPrees>", moveent_handler)

def stop_pad(event):
            global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
            if event.keysym in 'ws':
                RIGHT_PAD_SPEED = 0
                if event.keysym in ('Up', 'Down'):
                    RIGHT_PAD_SPEED = 0
c.bind("<KeyRelease>",stop_pad)

main()

root.mainloop()
