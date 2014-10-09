#created by FF on 19/04/2014
# template for "Stopwatch: The Game"
import simplegui
# define global variables
running = False
increment = 0
HEIGHT = 300
WIDTH = 200
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
   '''format given tents of 
   a second to a A:BC.D format'''
   global tents
   tents = t % 10
   BC = t // 10
   mins = BC // 60
   secs = BC % 60
   if secs < 10:
        secs = "0" + str (secs) 
   return str (mins) + ":" + str (secs) + "." + str(tents)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global running
    running = True
    timer.start()

def Stop():
    global running
    timer.stop()
    if running == False:
        print "You must start the stopwatch first."
    else:
        running = False
        is_mached()

def Reset():
    timer.stop()
    global increment, x, y
    increment, x, y = 0, 0, 0
    
def is_mached():
    global x, y
    if tents == 0:
        x += 1
        y += 1
    else:
        y += 1

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global increment
    increment += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(increment), (HEIGHT / 2.3, WIDTH / 2), 24, "Red")
    canvas.draw_text(str (x) + "/" + str (y), (HEIGHT / 1.3, WIDTH / 8), 24, "Green")
   
# create frame
frame = simplegui.create_frame("Stopwatch the Game", HEIGHT, WIDTH)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.add_button('Start', Start, 100)
frame.add_button('Stop', Stop, 100)
frame.add_button('Reset', Reset, 100)

# start frame
frame.start()
# Please remember to review the grading rubric