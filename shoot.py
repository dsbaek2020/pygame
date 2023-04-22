#만든사람: 김민진
#만든날: 2023. 04. 22(토)

import pgzrun
import random


print('hello')

my_Point=0

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text(":)" + str(my_Point), ( 500,5), color="red" )
    
def place_apple():
    apple.x = random.randint(5, 595)
    apple.y = random.randint(5,395)
    
def on_mouse_down(pos):
   global my_Point
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()    
        my_Point = my_Point + 2
        
    else:
        print("you missed")
        quit()




place_apple()

pgzrun.go()
