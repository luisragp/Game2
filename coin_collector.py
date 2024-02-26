import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500

score = 0
game_over = False

#Actors
hog = Actor("hedgehog")
hog.pos = 100, 100

coin = Actor("coin")
coin.pos = 200,200

#Display the score
def draw():
    screen.fill("yellow")
    hog.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color = "red", topleft = (10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(score), topleft = (10,10), fontsize = 60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        hog.x = hog.x -2
    elif keyboard.right:
        hog.x = hog.x +2
    elif keyboard.up:
        hog.y = hog -2
    elif keyboard.down:
        hog.y = hog.y +2
    
    #If the hog touches the coin this variable will be True
    coin_collected = hog.colliderect(coin)

    #This will increase the score by ten
    if coin_collected:
        score = score + 10
        place_coin()


clock.schedule(time_up, 12)
place_coin()
pgzrun.go()